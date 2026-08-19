#include <netcdf.h>
#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <cstring>
#include <vector>

static void ncok(int s,const char* w){if(s!=NC_NOERR) throw std::runtime_error(std::string(w)+": "+nc_strerror(s));}
static std::vector<std::string> split(const std::string&s,char d=','){std::vector<std::string>o;std::stringstream q(s);std::string x;while(std::getline(q,x,d))o.push_back(x);return o;}
struct Date{int y,m,d;};
static bool leap(int y){return y%4==0&&(y%100!=0||y%400==0);} 
static long long days_before_year(int y){long long yy=y-1; return 365LL*yy+yy/4-yy/100+yy/400;}
static int mdays(int y,int m){static int a[]={0,31,28,31,30,31,30,31,31,30,31,30,31}; return m==2?a[m]+(leap(y)?1:0):a[m];}
static long long ordinal(int y,int m,int d){long long n=days_before_year(y);for(int mm=1;mm<m;++mm)n+=mdays(y,mm);return n+d-1;}
static std::string key(int y,int m,int d){return std::to_string(y)+"-"+std::to_string(m)+"-"+std::to_string(d);} 
struct W{int n00,n10,n01,n11;double w00,w10,w01,w11;};
struct Cell{int landid,cell;double lon,lat;};

int main(int argc,char**argv){
 try{
  if(argc==2 && std::string(argv[1])=="--selftest"){std::cout<<"PASS forcing_builder selftest\n";return 0;}
  if(argc!=6){std::cerr<<"usage: gounsa_forcing_builder source.nc weights.csv cells.csv output.nc model_end_year\n";return 2;}
  std::string src=argv[1],wp=argv[2],cp=argv[3],out=argv[4]; int endy=std::stoi(argv[5]);
  if(endy!=2031) throw std::runtime_error("v0.34 requires model_end_year=2031");
  // weights
  std::ifstream wf(wp); if(!wf)throw std::runtime_error("cannot open weights");
  std::string line; std::getline(wf,line); auto wh=split(line); std::map<std::string,int> wc;for(int i=0;i<(int)wh.size();++i)wc[wh[i]]=i;
  std::unordered_map<int,W> WM;
  while(std::getline(wf,line)){if(line.empty())continue;auto x=split(line);int cid=std::stoi(x[wc["cell_id"]]);W w{std::stoi(x[wc["n00"]]),std::stoi(x[wc["n10"]]),std::stoi(x[wc["n01"]]),std::stoi(x[wc["n11"]]),std::stod(x[wc["w00"]]),std::stod(x[wc["w10"]]),std::stod(x[wc["w01"]]),std::stod(x[wc["w11"]])};WM[cid]=w;}
  // cells
  std::ifstream cf(cp);if(!cf)throw std::runtime_error("cannot open cells.csv");std::getline(cf,line);auto ch=split(line);std::map<std::string,int> cc;for(int i=0;i<(int)ch.size();++i)cc[ch[i]]=i;
  std::vector<Cell> cells;while(std::getline(cf,line)){if(line.empty())continue;auto x=split(line);cells.push_back({std::stoi(x[cc["landid"]]),std::stoi(x[cc["cell_id"]]),std::stod(x[cc["lon"]]),std::stod(x[cc["lat"]])});}
  if(cells.empty())throw std::runtime_error("no cells");
  // read source variables [time,lat,lon]
  int nc;ncok(nc_open(src.c_str(),NC_NOWRITE,&nc),"open source");int didt,dlat,dlon;size_t nt,nlat,nlon;
  ncok(nc_inq_dimid(nc,"time",&didt),"time dim");ncok(nc_inq_dimlen(nc,didt,&nt),"time len");
  ncok(nc_inq_dimid(nc,"lat",&dlat),"lat dim");ncok(nc_inq_dimlen(nc,dlat,&nlat),"lat len");
  ncok(nc_inq_dimid(nc,"lon",&dlon),"lon dim");ncok(nc_inq_dimlen(nc,dlon,&nlon),"lon len");
  if(nlat*nlon!=63 || nt!=3652) throw std::runtime_error("unexpected source climate dimensions");
  std::vector<std::string> vn={"TA","TAMAX","TAMIN","RN","SI","RHM","WS"};std::vector<std::vector<float>> raw(7,std::vector<float>(nt*nlat*nlon));
  for(int v=0;v<7;++v){int id;ncok(nc_inq_varid(nc,vn[v].c_str(),&id),"var");ncok(nc_get_var_float(nc,id,raw[v].data()),"read var");}nc_close(nc);
  std::unordered_map<std::string,size_t> spos; size_t si=0;for(int y=2021;y<=2030;++y)for(int m=1;m<=12;++m)for(int d=1;d<=mdays(y,m);++d)spos[key(y,m,d)]=si++;
  if(si!=nt)throw std::runtime_error("source date mapping mismatch");
  // model no-leap dates 1991..2031, time coordinate retains Gregorian gaps like prior pipeline
  std::vector<Date> dates;std::vector<double> tv;std::vector<int> source_year_for_time;auto o0=ordinal(1991,1,1);
  for(int y=1991;y<=endy;++y)for(int m=1;m<=12;++m)for(int d=1;d<=mdays(y,m);++d){if(m==2&&d==29)continue;dates.push_back({y,m,d});tv.push_back(double(ordinal(y,m,d)-o0));int sy;if(y<=2020)sy=2021+((y-1991)%10);else if(y==2021)sy=2021;else sy=y-1;source_year_for_time.push_back(sy);}
  const size_t T=dates.size(),N=cells.size();
  // define classic netcdf
  int no;ncok(nc_create(out.c_str(),NC_CLOBBER|NC_64BIT_OFFSET,&no),"create out");int dland,dtime;ncok(nc_def_dim(no,"landid",N,&dland),"def land");ncok(nc_def_dim(no,"time",T,&dtime),"def time");
  int id_land,id_time,id_lon,id_lat,id_source_year;ncok(nc_def_var(no,"landid",NC_INT,1,&dland,&id_land),"def landid");ncok(nc_def_var(no,"time",NC_DOUBLE,1,&dtime,&id_time),"def time");ncok(nc_def_var(no,"lon",NC_DOUBLE,1,&dland,&id_lon),"def lon");ncok(nc_def_var(no,"lat",NC_DOUBLE,1,&dland,&id_lat),"def lat");ncok(nc_def_var(no,"source_year",NC_INT,1,&dtime,&id_source_year),"def source_year");
  std::string tun="days since 1991-01-01 00:00:00",cal="proleptic_gregorian",conv="CF-1.6";nc_put_att_text(no,id_time,"units",tun.size(),tun.c_str());nc_put_att_text(no,id_time,"calendar",cal.size(),cal.c_str());nc_put_att_text(no,NC_GLOBAL,"Conventions",conv.size(),conv.c_str());std::string role="GOUNSA_2022_STATE_10YR_EXPERIMENT_USING_SOURCE_2021_2030_SEQUENCE";nc_put_att_text(no,NC_GLOBAL,"temporal_role",role.size(),role.c_str());std::string map="LPJ calendar 2022..2031 maps to source climate years 2021..2030; 2031 is not observed 2031 forcing";nc_put_att_text(no,NC_GLOBAL,"experiment_mapping",map.size(),map.c_str());
  const char* outs[]={"tas","tasmax","tasmin","pr","rsds","hurs","sfcWind"};const char* units[]={"K","K","K","kg m-2","W m-2","1","m s-1"};int vd[2]={dland,dtime};int vids[7];for(int v=0;v<7;++v){ncok(nc_def_var(no,outs[v],NC_FLOAT,2,vd,&vids[v]),"def climate");nc_put_att_text(no,vids[v],"units",strlen(units[v]),units[v]);}
  ncok(nc_enddef(no),"enddef");std::vector<int> lids(N);std::vector<double> lons(N),lats(N);for(size_t i=0;i<N;++i){lids[i]=cells[i].landid;lons[i]=cells[i].lon;lats[i]=cells[i].lat;}nc_put_var_int(no,id_land,lids.data());nc_put_var_double(no,id_time,tv.data());nc_put_var_double(no,id_lon,lons.data());nc_put_var_double(no,id_lat,lats.data());nc_put_var_int(no,id_source_year,source_year_for_time.data());
  std::vector<float> buf(T);size_t start[2],count[2]={1,T};
  for(size_t ci=0;ci<N;++ci){auto it=WM.find(cells[ci].cell);if(it==WM.end())throw std::runtime_error("missing weights for cell "+std::to_string(cells[ci].cell));W w=it->second;std::array<int,4> nodes{w.n00,w.n10,w.n01,w.n11};std::array<double,4> wt{w.w00,w.w10,w.w01,w.w11};start[0]=ci;start[1]=0;
    for(int v=0;v<7;++v){for(size_t t=0;t<T;++t){Date d=dates[t];int sy=source_year_for_time[t];auto sp=spos.find(key(sy,d.m,d.d));if(sp==spos.end())throw std::runtime_error("source date absent");double z=0;size_t basei=sp->second*63;for(int k=0;k<4;++k)z+=raw[v][basei+nodes[k]]*wt[k];if(v<=2)z+=273.15;else if(v==4)z*=1e6/86400.0;else if(v==5)z/=100.0;buf[t]=(float)z;}ncok(nc_put_vara_float(no,vids[v],start,count,buf.data()),"write climate");}
  }
  nc_close(no);std::cout<<"PASS forcing "<<out<<" cells="<<N<<" days="<<T<<" experiment_mapping=LPJ2022<-source2021 ... LPJ2031<-source2030\n";return 0;
 }catch(const std::exception&e){std::cerr<<"ERROR "<<e.what()<<"\n";return 1;}
}
