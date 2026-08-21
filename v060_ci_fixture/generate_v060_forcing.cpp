#include <netcdf.h>
#include <cmath>
#include <cstring>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

static void ck(int s,const char* w){ if(s!=NC_NOERR) throw std::runtime_error(std::string(w)+": "+nc_strerror(s)); }
static bool leap(int y){ return y%4==0 && (y%100!=0 || y%400==0); }
static int mdays(int y,int m){ static int d[]={0,31,28,31,30,31,30,31,31,30,31,30,31}; return d[m] + (m==2 && leap(y)); }
static long long days_before_year(int y){ long long yy=y-1; return 365LL*yy + yy/4 - yy/100 + yy/400; }
static long long ordinal(int y,int m,int d){ long long n=days_before_year(y); for(int mm=1;mm<m;++mm)n+=mdays(y,mm); return n+d-1; }
static void textatt(int ncid,int var,const char* name,const std::string& v){ ck(nc_put_att_text(ncid,var,name,v.size(),v.c_str()),name); }

static int make_input(const std::string& out){
    const int y0=1991,y1=2031; const long long o0=ordinal(y0,1,1);
    std::vector<double> time; std::vector<int> doy;
    for(int y=y0;y<=y1;++y){ int nd=0; for(int m=1;m<=12;++m) for(int d=1;d<=mdays(y,m);++d){ if(m==2&&d==29) continue; ++nd; time.push_back(double(ordinal(y,m,d)-o0)); doy.push_back(nd); } }
    const size_t T=time.size(), N=2;
    int nc; ck(nc_create(out.c_str(),NC_CLOBBER|NC_64BIT_OFFSET,&nc),"create input");
    int dland,dtime; ck(nc_def_dim(nc,"landid",N,&dland),"landid dim"); ck(nc_def_dim(nc,"time",T,&dtime),"time dim");
    int vland,vtime,vlon,vlat; ck(nc_def_var(nc,"landid",NC_INT,1,&dland,&vland),"landid"); ck(nc_def_var(nc,"time",NC_DOUBLE,1,&dtime,&vtime),"time"); ck(nc_def_var(nc,"lon",NC_DOUBLE,1,&dland,&vlon),"lon"); ck(nc_def_var(nc,"lat",NC_DOUBLE,1,&dland,&vlat),"lat");
    textatt(nc,vtime,"units","days since 1991-01-01 00:00:00"); textatt(nc,vtime,"calendar","proleptic_gregorian");
    textatt(nc,vlon,"units","degrees_east"); textatt(nc,vlon,"standard_name","longitude"); textatt(nc,vlat,"units","degrees_north"); textatt(nc,vlat,"standard_name","latitude"); textatt(nc,NC_GLOBAL,"Conventions","CF-1.6");
    const char* names[]={"tas","tasmax","tasmin","pr","rsds","hurs","sfcWind"};
    const char* units[]={"K","K","K","kg m-2","W m-2","1","m s-1"};
    const char* stdn[]={"air_temperature","air_temperature","air_temperature","precipitation_amount","surface_downwelling_shortwave_flux_in_air","relative_humidity","wind_speed"};
    int dims[2]={dland,dtime}, vids[7];
    for(int i=0;i<7;++i){ ck(nc_def_var(nc,names[i],NC_FLOAT,2,dims,&vids[i]),"def climate"); textatt(nc,vids[i],"units",units[i]); textatt(nc,vids[i],"standard_name",stdn[i]); textatt(nc,vids[i],"coordinates","lon lat"); }
    ck(nc_enddef(nc),"enddef");
    int lids[2]={0,1}; double lons[2]={128.75805903,128.75839373}, lats[2]={36.46499298,36.46499365};
    ck(nc_put_var_int(nc,vland,lids),"put land"); ck(nc_put_var_double(nc,vtime,time.data()),"put time"); ck(nc_put_var_double(nc,vlon,lons),"put lon"); ck(nc_put_var_double(nc,vlat,lats),"put lat");
    std::vector<float> buf(T); const double pi=3.14159265358979323846;
    size_t start[2], count[2]={1,T};
    for(size_t c=0;c<N;++c){ start[0]=c; start[1]=0; double off=(c==0?0.0:0.8);
      for(int v=0;v<7;++v){ for(size_t t=0;t<T;++t){ double ang=2*pi*(double(doy[t])-172.0)/365.0; double x=0;
        if(v==0) x=273.15 + 7.0 + off + 12.0*std::cos(ang);
        else if(v==1) x=273.15 + 12.0 + off + 12.0*std::cos(ang);
        else if(v==2) x=273.15 + 2.0 + off + 12.0*std::cos(ang);
        else if(v==3) x=1.5 + 1.0*(1.0+std::cos(ang));
        else if(v==4) x=145.0 + 90.0*std::cos(ang);
        else if(v==5) x=0.60;
        else if(v==6) x=3.0 + 0.2*c;
        buf[t]=(float)x;
      } ck(nc_put_vara_float(nc,vids[v],start,count,buf.data()),"write climate"); }
    }
    ck(nc_close(nc),"close input"); std::cout<<"PASS input forcing days="<<T<<"\n"; return 0;
}

static int make_percell(const std::string& out){
    const size_t T=3,N=2; int nc; ck(nc_create(out.c_str(),NC_CLOBBER|NC_64BIT_OFFSET,&nc),"create percell");
    int dt,dl; ck(nc_def_dim(nc,"time",T,&dt),"time dim"); ck(nc_def_dim(nc,"landid",N,&dl),"land dim");
    int vl,vy,vd; ck(nc_def_var(nc,"landid",NC_INT,1,&dl,&vl),"landid"); ck(nc_def_var(nc,"calendar_year",NC_INT,1,&dt,&vy),"year"); ck(nc_def_var(nc,"day_of_year",NC_INT,1,&dt,&vd),"doy");
    const char* names[]={"temp_c","prec_mm_day","insol_native","relhum_frac","wind_m_s","tmin_c","tmax_c","dtr_c","co2_ppm","dNH4dep","dNO3dep"};
    const char* units[]={"degC","mm day-1","W m-2","1","m s-1","degC","degC","degC","ppm","kgN m-2 day-1","kgN m-2 day-1"};
    int dims[2]={dt,dl}, vv[11]; for(int i=0;i<11;++i){ ck(nc_def_var(nc,names[i],NC_DOUBLE,2,dims,&vv[i]),"def var"); textatt(nc,vv[i],"units",units[i]); }
    ck(nc_enddef(nc),"enddef"); int ids[2]={42,9001}, years[3]={2023,2023,2023}, days[3]={1,2,3}; ck(nc_put_var_int(nc,vl,ids),"ids"); ck(nc_put_var_int(nc,vy,years),"years"); ck(nc_put_var_int(nc,vd,days),"days");
    double a[3][2];
    for(int v=0;v<11;++v){ for(int t=0;t<3;++t) for(int c=0;c<2;++c){ double x=0;
      if(v==0) x=(c==0?20:10)+t; else if(v==1) x=(c==0?2:1)+2*t; else if(v==2) x=150; else if(v==3) x=.5; else if(v==4) x=(c==0?10:5); else if(v==5) x=(c==0?15:5)+t; else if(v==6) x=(c==0?25:15)+t; else if(v==7) x=10; else if(v==8) x=420; else x=0; a[t][c]=x; }
      ck(nc_put_var_double(nc,vv[v],&a[0][0]),"put percell"); }
    ck(nc_close(nc),"close percell"); std::cout<<"PASS percell forcing\n"; return 0;
}

int main(int argc,char** argv){ try{ if(argc!=3){ std::cerr<<"usage: generator input|percell out.nc\n"; return 2;} std::string m=argv[1]; if(m=="input") return make_input(argv[2]); if(m=="percell") return make_percell(argv[2]); throw std::runtime_error("bad mode"); } catch(const std::exception& e){ std::cerr<<"ERROR "<<e.what()<<"\n"; return 1;} }
