# 서지정보
Liu, J.-X., Li, P.-P., Liu, G.-B., & Flanagan, D. C. (2020). Quantifying the effects of plant litter in the topsoil on the soil detachment process by overland flow in typical grasslands of the Loess Plateau, China. *Hydrological Processes, 34*(9), 2076-2087.

# 이 논문을 찾은 이유
litter biomass 자체와 litter-soil contact geometry가 detachment parameter를 어떻게 바꾸는지 검토했다.

# 연구 유형
- 실험

# 공간 구조
- plot/flume

# 적용 환경
- grassland

# 핵심 과정
- soil detachment
- rill erodibility
- critical shear

# 식생 입력
- litter mass
- litter surface area density
- litter-soil contact area

# 핵심 식
이 채팅 정리에는 litter가 `D_c`, `K_r`, critical shear를 바꾸며 LSAD가 `K_r`를 잘 설명한다고 기록됨.

# 파라미터와 단위
litter input 0.1-1.3 kg m^-2, LSAD 등.

# 원 논문의 구현 범위
litter가 topsoil detachment를 줄이는 실험적 효과를 정량화.

# 고운사에 직접 사용할 수 있는 부분
SurfaceLitC를 단순 Manning n 이외에 erodibility/critical shear에 연결할 parameterization evidence.

# 새로운 coupling이 필요한 부분
SurfaceLitC -> litter mass/area -> LSAD -> erosion parameters는 새로운 coupling.

# 한계
수치 지형모델이 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1002/hyp.13713
