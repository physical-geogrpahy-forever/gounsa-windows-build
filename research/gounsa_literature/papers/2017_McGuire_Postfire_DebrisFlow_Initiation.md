# 서지정보
McGuire, L. A., Rengers, F. K., Kean, J. W., & Staley, D. M. (2017). *Debris flow initiation by runoff in a recently burned basin: Is grain-by-grain sediment bulking or en masse failure to blame?* Geophysical Research Letters, 44(14), 7310-7319. DOI: 10.1002/2017GL074243.

# 이 논문을 찾은 이유
McGuire 2016 postfire 2D erosion framework가 catchment-scale sediment redistribution과 debris-flow initiation까지 어떤 process consequences를 만들어내는지 확인하기 위해 검토했다.

# 연구 유형
- numerical model + high-resolution hydrologic/geomorphic field data
- postfire debris-flow process test

# 공간 구조
- recently burned drainage basin
- distributed hillslope-channel sediment routing

# 적용 환경
- recently burned California basin
- high-intensity rainfall
- postfire runoff-generated debris flow

# 핵심 과정
- hillslope sediment erosion
- channel redeposition
- sediment-dam formation
- en masse failure
- runoff-generated debris-flow initiation

# 식생 입력
This paper is not a vegetation-coupling study; it inherits the postfire model framework rather than adding quantitative root/litter states.

# 핵심 식
The paper tests two conceptual mechanisms:
1. grain-by-grain sediment bulking
2. en masse failure of sediment deposits/dams

Model results supported large hillslope sediment volumes being redeposited in channels and subsequent mass failure of those deposits.

# 파라미터와 단위
Model-specific sediment/hydrologic variables are inherited from the postfire modeling framework. Exact equations were not re-audited here because this paper is being retained for the sediment-storage/failure consequence rather than as the primary erosion formulation.

# 원 논문의 구현 범위
Connects postfire hillslope erosion and channel sediment storage to runoff-generated debris-flow initiation.

# 고운사에 직접 사용할 수 있는 부분
Shows that a 2D postfire erosion engine with strong sediment supply should retain deposition/storage because redeposited material can become a later geomorphic source.

# 새로운 coupling이 필요한 부분
Any LPJ-GUESS or 100-year vegetation recovery coupling is outside this paper.

# 한계
- debris-flow focus
- no quantitative vegetation/root state
- not the primary candidate for ordinary hillslope erosion

# 최종 판정
- **보조근거**
- retain for downstream consequence of postfire erosion/deposition, not as the core water-erosion model

# 참고 링크 / DOI
https://doi.org/10.1002/2017GL074243
