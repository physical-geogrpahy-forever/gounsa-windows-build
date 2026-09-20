# 서지정보
Stott, D. E., Alberts, E. E., & Weltz, M. A. (1995). *Residue Decomposition and Management*. In D. C. Flanagan & M. A. Nearing (Eds.), USDA-Water Erosion Prediction Project: Hillslope Profile and Watershed Model Documentation. NSERL Report No. 10, Chapter 9.

# 이 문서를 찾은 이유
산불 후 litter/dead-root/residue pool을 erosion resistance와 연결할 때 WEPP가 어떤 residue pools를 분리하는지 확인하기 위해 검토했다.

# 연구 유형
- official technical model documentation

# 핵심 과정
- residue decomposition
- standing/flat/buried residue
- dead roots
- management effects
- surface coarse fragments handled separately in WEPP system

# 식생 입력
- standing residue
- flat residue
- buried residue
- dead root biomass

# 핵심 식
Detailed decomposition/management equations are in Chapter 9.

# 파라미터와 단위
Original WEPP units.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS litter/dead-root output을 하나의 cover로 축약하지 않고 separate pools로 유지해야 한다는 strong precedent.

# 새로운 coupling이 필요한 부분
LPJ-GUESS litter carbon -> WEPP residue mass/pool definitions is **new coupling** unless calibrated conversion is documented.

# 한계
agricultural management heritage; forest postfire mapping requires care.

# 최종 판정
**core residue-pool source.**
