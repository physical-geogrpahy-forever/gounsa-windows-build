# Milly(1993) 정상 저장 문제의 몬테카를로 검증. Guswa(2008) 식 12(인쇄본)와 부록 A2 꼴 중 어느 쪽이 맞는지 가린다.
# 가정: 푸아송 강우, 지수 깊이, 즉시 침투, 일정한 Tpot, 용량 S 초과분은 유출.
import numpy as np
rng=np.random.default_rng(7)
def mc(S,alpha,lam,Tpot,N=400000):
    # 연속시간 정확 모의: 푸아송 강우(lam), 깊이 지수(alpha), 즉시 침투, 저장 S, 소모율 Tpot(저장>0일 때), 초과는 유출
    dt=rng.exponential(1/lam,N); h=rng.exponential(alpha,N)
    s=S*0.5; tot=0.0; T=0.0
    for d,hh in zip(dt,h):
        use=min(s,Tpot*d)        # 이 사이 증산량
        tot+=use; T+=d
        s=min(S,s-use+hh)        # 다음 강우
    return tot/T
def num(S,alpha,lam,Tpot):
    W=alpha*lam/Tpot
    if abs(1-W)<1e-9:
        g=S/alpha; return Tpot*g/(1+g)
    B=S*(1-W)/alpha
    return Tpot*W*(np.exp(B)-1)/(np.exp(B)-W)
def den(S,alpha,lam,Tpot):
    W=alpha*lam/Tpot
    if abs(1-W)<1e-12: return float('nan')
    B=S/(alpha*(1-W))
    return Tpot*W*(np.exp(B)-1)/(np.exp(B)-W)
print("S(mm) alpha lam Tpot  W | MC  분자형(구현)  분모형(인쇄본)")
for S,alpha,lam,Tpot in [(20,15,0.167,4),(60,15,0.167,4),(100,15,0.167,5.7),(30,10,0.3,4),(30,10,0.3,2.5),(40,12,0.25,3.0),(15,20,0.2,4),(30,12,0.25,3.0),(10,12,0.25,3.0)]:
    W=alpha*lam/Tpot
    print(f"{S:4} {alpha:4} {lam:5} {Tpot:4}  {W:5.2f} | {mc(S,alpha,lam,Tpot):6.3f}  {num(S,alpha,lam,Tpot):6.3f}  {den(S,alpha,lam,Tpot):6.3f}")
