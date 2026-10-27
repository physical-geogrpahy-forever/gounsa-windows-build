// Isolated SEIMS dev formula probe, NOT a complete native model build.
// Inspected upstream: seims/src/seims_main/modules/erosion/KinWavSed_OL/KinWavSed_OL.cpp
// Exact arithmetic structure of GetTransportCapacity preserved with switchable mm->m.
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
double capacity(double v_m_s, double h_mm, double slope, double K,
                double eco1, double eco2, bool convert, double& q) {
    q = v_m_s * (convert ? h_mm/1000.0 : h_mm) * 60.0;
    const double S0=std::sin(std::atan(std::max(0.001,slope)));
    const double threshold=0.046;
    double Ctrans=0.0;
    if(q>0) {
        if(q<threshold) Ctrans=eco1*K*S0*std::sqrt(q);
        else Ctrans=eco2*K*S0*std::pow(q,2);
        Ctrans/=q;
    }
    return Ctrans;
}
int main() {
    double q_orig,q_si;
    double co=capacity(0.1,5,0.2,0.3,1,1,false,q_orig);
    double cs=capacity(0.1,5,0.2,0.3,1,1,true,q_si);
    assert(std::abs(q_orig/q_si-1000.)<1e-8);
    std::cout<<std::setprecision(12)
             <<"ISOLATED_FORMULA_NOT_FULL_SEIMS_BINARY\n"
             <<"q_raw="<<q_orig<<" q_si="<<q_si<<" ratio="<<q_orig/q_si<<"\n"
             <<"branch_raw="<<(q_orig<.046?"LOW":"HIGH")<<" branch_si="<<(q_si<.046?"LOW":"HIGH")<<"\n"
             <<"TC_raw="<<co<<" TC_si="<<cs<<" ratio="<<co/cs<<"\n";
}
