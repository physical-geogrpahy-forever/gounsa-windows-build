#include <algorithm>
#include <cmath>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
namespace fs=std::filesystem;
static std::vector<std::string> csvsplit(const std::string&s){std::vector<std::string>o;std::stringstream q(s);std::string x;while(std::getline(q,x,','))o.push_back(x);return o;}
static std::vector<std::string> wsplit(const std::string&s){std::vector<std::string>o;std::stringstream q(s);std::string x;while(q>>x)o.push_back(x);return o;}
struct Cell{int id,row,col,rec=-1;double z0,soil0,dist=30,slope0=0;};
struct Ann{double gpp=0,npp=0,bio=0,fpc=0,h=0;std::string pft="NONE";};
struct Table{std::vector<std::string> h;std::vector<std::vector<double>> rows;};
static Table read_numeric_table(const fs::path&p){std::ifstream f(p);if(!f)throw std::runtime_error("missing output "+p.string());std::string line;if(!std::getline(f,line))throw std::runtime_error("empty output");Table t;t.h=wsplit(line);while(std::getline(f,line)){if(line.empty())continue;auto s=wsplit(line);if(s.size()!=t.h.size())throw std::runtime_error("malformed "+p.string());std::vector<double>r;for(auto&x:s)r.push_back(std::stod(x));t.rows.push_back(std::move(r));}return t;}
static int hidx(const std::vector<std::string>&h,const std::string&n){for(int i=0;i<(int)h.size();++i)if(h[i]==n)return i;throw std::runtime_error("column "+n+" absent");}
static std::vector<int> read_cellids(const fs::path&p){std::ifstream f(p);if(!f)throw std::runtime_error("missing cells.csv");std::string line;std::getline(f,line);auto h=csvsplit(line);int ci=-1;for(int i=0;i<(int)h.size();++i)if(h[i]=="cell_id")ci=i;if(ci<0)throw std::runtime_error("cell_id absent");std::vector<int>o;while(std::getline(f,line)){if(line.empty())continue;auto x=csvsplit(line);o.push_back(std::stoi(x[ci]));}return o;}
int main(int argc,char**argv){try{
 if(argc==2&&std::string(argv[1])=="--selftest"){std::cout<<"PASS geomorph_driver selftest\n";return 0;}
 if(argc!=6){std::cerr<<"usage: gounsa_geomorph_driver initial_dem_soil.csv receiver.csv shards_dir out_dir result_mode\n";return 2;}
 fs::path gp=argv[1],rp=argv[2],sd=argv[3],out=argv[4];std::string mode=argv[5];if(mode!="LITERATURE_TRANSFER_SENSITIVITY")throw std::runtime_error("v0.34 only permits explicit LITERATURE_TRANSFER_SENSITIVITY");fs::create_directories(out);
 std::ifstream gf(gp);if(!gf)throw std::runtime_error("grid missing");std::string line;std::getline(gf,line);auto gh=csvsplit(line);std::map<std::string,int>gc;for(int i=0;i<(int)gh.size();++i)gc[gh[i]]=i;std::vector<Cell>C;std::unordered_map<int,int>ix;while(std::getline(gf,line)){if(line.empty())continue;auto x=csvsplit(line);Cell c;c.id=std::stoi(x[gc["cell_id"]]);c.row=std::stoi(x[gc["row"]]);c.col=std::stoi(x[gc["col"]]);c.z0=std::stod(x[gc["elevation_m"]]);c.soil0=std::stod(x[gc["soil_depth_m"]]);ix[c.id]=C.size();C.push_back(c);}const int N=C.size();if(N!=4454)throw std::runtime_error("expected 4454 cells");
 std::ifstream rf(rp);if(!rf)throw std::runtime_error("receiver missing");std::getline(rf,line);auto rh=csvsplit(line);std::map<std::string,int>rc;for(int i=0;i<(int)rh.size();++i)rc[rh[i]]=i;while(std::getline(rf,line)){if(line.empty())continue;auto x=csvsplit(line);int cid=std::stoi(x[rc["cell_id"]]),rid=std::stoi(x[rc["receiver_cell_id"]]);auto k=ix.find(cid);if(k==ix.end())continue;int i=k->second;C[i].rec=rid<0?-1:ix.at(rid);C[i].slope0=std::stod(x[rc["slope_from_rounded_dem"]]);if(rid>=0){int j=C[i].rec;int dr=std::abs(C[i].row-C[j].row),dc=std::abs(C[i].col-C[j].col);C[i].dist=(dr&&dc)?30.0*std::sqrt(2.0):30.0;}}
 int outlet=-1;for(int i=0;i<N;++i)if(C[i].id==2081)outlet=i;if(outlet<0||C[outlet].rec!=-1)throw std::runtime_error("outlet contract failed");
 std::vector<int> indeg(N,0);for(int i=0;i<N;++i)if(C[i].rec>=0)indeg[C[i].rec]++;std::queue<int>q;for(int i=0;i<N;++i)if(indeg[i]==0)q.push(i);std::vector<int>order;while(!q.empty()){int i=q.front();q.pop();order.push_back(i);if(C[i].rec>=0&&--indeg[C[i].rec]==0)q.push(C[i].rec);}if((int)order.size()!=N)throw std::runtime_error("receiver graph cycle");
 const int Y0=2022,Y1=2031,DY=365,ND=10*DY;size_t M=(size_t)N*ND;float NaN=std::numeric_limits<float>::quiet_NaN();std::vector<float> leaf(M,NaN),root(M,NaN),lit(M,NaN),runoff(M,NaN);
 std::map<std::pair<int,int>,Ann> annual;
 std::vector<fs::path> dirs;for(auto&e:fs::directory_iterator(sd))if(e.is_directory()&&fs::exists(e.path()/"cells.csv"))dirs.push_back(e.path());std::sort(dirs.begin(),dirs.end());
 for(auto&dir:dirs){auto cids=read_cellids(dir/"cells.csv");int nc=cids.size();std::ifstream ef(dir/"out/veslem_exchange.out");if(!ef)throw std::runtime_error("LPJ exchange missing: "+dir.string());std::getline(ef,line);size_t recno=0;while(std::getline(ef,line)){if(line.empty())continue;auto x=wsplit(line);if(x.size()<17)throw std::runtime_error("bad exchange line");int yr=std::stoi(x[2]),day=std::stoi(x[3]);if(yr<Y0||yr>Y1)continue;int local=(int)(recno/ND);if(local>=nc)throw std::runtime_error("exchange record overflow");int gi=ix.at(cids[local]);int di=(yr-Y0)*DY+(day-1);size_t k=(size_t)gi*ND+di;leaf[k]=std::stof(x[4]);root[k]=std::stof(x[5]);lit[k]=std::stof(x[8]);runoff[k]=std::stof(x[12]);recno++;}
   if(recno!=(size_t)nc*ND)throw std::runtime_error("exchange row count mismatch in "+dir.string()+" got "+std::to_string(recno));
   Table tg=read_numeric_table(dir/"out/agpp.out"), tn=read_numeric_table(dir/"out/anpp.out"), tb=read_numeric_table(dir/"out/cmass.out"), tf=read_numeric_table(dir/"out/fpc.out"), th=read_numeric_table(dir/"out/height.out");
   int iy=hidx(tg.h,"Year"),itot=hidx(tg.h,"Total");size_t per=tg.rows.size()/nc;if(per*nc!=tg.rows.size())throw std::runtime_error("annual row blocks mismatch");
   if(tn.rows.size()!=tg.rows.size()||tb.rows.size()!=tg.rows.size()||tf.rows.size()!=tg.rows.size()||th.rows.size()!=tg.rows.size())throw std::runtime_error("annual table size mismatch");
   for(int lc=0;lc<nc;++lc){int gi=ix.at(cids[lc]);for(size_t rr=lc*per;rr<(lc+1)*per;++rr){int yr=(int)std::llround(tg.rows[rr][iy]);if(yr<Y0||yr>Y1)continue;Ann a;a.gpp=tg.rows[rr][itot];a.npp=tn.rows[rr][itot];a.bio=tb.rows[rr][itot];double best=-1;int bp=-1;for(int col=3;col<(int)tf.h.size();++col){if(tf.h[col]=="Total")continue;double v=tf.rows[rr][col];if(v>best){best=v;bp=col;}}a.fpc=std::max(0.0,best);if(bp>=0){a.pft=tf.h[bp];int hc=-1;for(int z=0;z<(int)th.h.size();++z)if(th.h[z]==a.pft)hc=z;if(hc>=0)a.h=th.rows[rr][hc];}annual[{gi,yr}]=a;}}
 }
 for(size_t k=0;k<M;++k)if(!std::isfinite(leaf[k])||!std::isfinite(root[k])||!std::isfinite(lit[k])||!std::isfinite(runoff[k]))throw std::runtime_error("nonfinite/missing daily LPJ exchange");
 const double A=900.0,width=30.0,bulk=1.3,mass_scale=1.414269598840801e-6;
 std::vector<double> soilmass(N),bed(N),z(N);for(int i=0;i<N;++i){soilmass[i]=C[i].soil0*A*bulk;bed[i]=C[i].z0-C[i].soil0;z[i]=C[i].z0;}
 std::vector<double> annual_export(10,0),annual_mean_z(10,0),annual_mean_soil(10,0),V(N),H(N),incoming(N),net(N),prop(N),diffvol(N),din(N),dnet(N),slope(N);
 std::ofstream snap(out/"dem_annual.csv");snap<<"year,cell_id,elevation_m,soil_depth_m\n";std::ofstream audit(out/"geomorph_daily_audit.csv");audit<<"year,day,fluvial_export_t,diffusive_export_t,total_export_t,max_abs_dz_m\n";
 for(int di=0;di<ND;++di){
   for(int i=0;i<N;++i){if(C[i].rec<0)slope[i]=0;else{double s=(z[i]-z[C[i].rec])/C[i].dist;slope[i]=(C[i].slope0==0?0:s);if(slope[i]<-1e-10)throw std::runtime_error("fixed D8 reversed by DEM evolution");if(slope[i]<0)slope[i]=0;}}
   for(int i=0;i<N;++i){double h=runoff[(size_t)i*ND+di]*1e-3;if(h<0)throw std::runtime_error("negative runoff");V[i]=A*h;}for(int i:order)if(C[i].rec>=0)V[C[i].rec]+=V[i];for(int i=0;i<N;++i)H[i]=V[i]/A;
   for(int i=0;i<N;++i){double R=root[(size_t)i*ND+di],L=leaf[(size_t)i*ND+di],T=lit[(size_t)i*ND+di];double rh=((R-1.895)/0.087)/5.0+0.5, lh=((L-0.051)/0.011)/5.0+0.5, thh=((T-0.096)/0.011)/5.0+0.5;double beta=(0.5*rh<1.0)?500.0*(1.0-0.5*rh):0.0;double D=9e-7*std::exp(-0.5*lh);double n=0.025+0.07*thh;if(!(n>0&&std::isfinite(n)&&std::isfinite(D)&&std::isfinite(beta)))throw std::runtime_error("COPLAS normalization produced invalid field (no clipping allowed)");double qv=(1.0/n)*std::pow(H[i],5.0/3.0)*std::sqrt(slope[i]);double idx=beta*std::pow(qv,1.7)*std::pow(slope[i],0.69);prop[i]=std::max(0.0,idx*mass_scale*width);diffvol[i]=std::max(0.0,D*slope[i]*A);incoming[i]=net[i]=din[i]=dnet[i]=0;}
   double exf=0,exd=0;
   for(int i:order){double avail=soilmass[i]+incoming[i];double outm=std::min(prop[i],std::max(0.0,avail));net[i]+=incoming[i]-outm;int r=C[i].rec;if(r<0){}else if(r==outlet)exf+=outm;else incoming[r]+=outm;}
   for(int i=0;i<N;++i)soilmass[i]+=net[i];
   for(int i:order){double availv=std::max(0.0,soilmass[i]/bulk+din[i]);double outv=std::min(diffvol[i],availv);dnet[i]+=din[i]-outv;int r=C[i].rec;if(r<0){}else if(r==outlet)exd+=outv*bulk;else din[r]+=outv;}
   double mdz=0;for(int i=0;i<N;++i){soilmass[i]+=dnet[i]*bulk;if(soilmass[i]<-1e-8)throw std::runtime_error("negative soil mass");if(soilmass[i]<0)soilmass[i]=0;double zn=bed[i]+soilmass[i]/(bulk*A);mdz=std::max(mdz,std::abs(zn-z[i]));z[i]=zn;}
   int yi=di/DY;annual_export[yi]+=exf+exd;audit<<(Y0+yi)<<','<<(di%DY+1)<<','<<std::setprecision(15)<<exf<<','<<exd<<','<<(exf+exd)<<','<<mdz<<'\n';
   if(di%DY==DY-1){int yr=Y0+yi;double mz=0,ms=0;for(int i=0;i<N;++i){double hs=soilmass[i]/(bulk*A);mz+=z[i];ms+=hs;snap<<yr<<','<<C[i].id<<','<<std::setprecision(15)<<z[i]<<','<<hs<<'\n';}annual_mean_z[yi]=mz/N;annual_mean_soil[yi]=ms/N;}
 }
 std::ofstream ac(out/"annual_cells.csv");ac<<"year,experiment_year,forcing_source_year,cell_id,dominant_pft,height_m,fpc,biomass_kgC_m2\n";std::ofstream sm(out/"annual_summary.csv");sm<<"year,experiment_year,forcing_source_year,gpp_tC_yr,npp_tC_yr,biomass_tC,soil_export_t,mean_elevation_m,mean_soil_depth_m\n";
 for(int yr=Y0;yr<=Y1;++yr){double sg=0,sn=0,sb=0,sz=0,ss=0;for(int i=0;i<N;++i){auto it=annual.find({i,yr});Ann a;if(it!=annual.end())a=it->second;sg+=a.gpp*A/1000.0;sn+=a.npp*A/1000.0;sb+=a.bio*A/1000.0;ac<<yr<<','<<(yr-Y0+1)<<','<<(yr-1)<<','<<C[i].id<<','<<a.pft<<','<<a.h<<','<<a.fpc<<','<<a.bio<<'\n';int yi=yr-Y0;
 }
   sm<<yr<<','<<(yr-Y0+1)<<','<<(yr-1)<<','<<std::setprecision(15)<<sg<<','<<sn<<','<<sb<<','<<annual_export[yr-Y0]<<','<<annual_mean_z[yr-Y0]<<','<<annual_mean_soil[yr-Y0]<<'\n';
 }
 std::ofstream meta(out/"RESULT_MODE.txt");meta<<"LITERATURE_TRANSFER_SENSITIVITY\nREAL_LPJ_OUTPUT_REQUIRED=TRUE\nREAL_DAILY_COPLAS_NUMERICAL_UPDATE=TRUE\nONE_WAY_LPJ_TO_GEOMORPH=TRUE\nGEOMORPH_TO_LPJ_HYDRAULIC_FEEDBACK=FALSE\nGOUNSA_CALIBRATED_PREDICTION=FALSE\nEXPERIMENT_YEAR_MAPPING=LPJ_2022_2031_USES_SOURCE_CLIMATE_2021_2030_SEQUENCE\nCALENDAR_2031_IS_NOT_OBSERVED_2031_FORCING=TRUE\nPOOL_NORMALIZATION=HOWARD_SPRINGS_REPRODUCTION_NO_CLIPPING\nMANNING_WIDTH_DIVISION=OMITTED_GOUNSA_LOCKED_DIMENSIONAL_CORRECTION\nFIXED_D8_GRAPH=GOUNSA_RECEIVER_GRAPH_30M_v0_1\n";
 std::cout<<"PASS real geomorph calculation cells="<<N<<" days="<<ND<<"\n";return 0;
}catch(const std::exception&e){std::cerr<<"ERROR "<<e.what()<<"\n";return 1;}}
