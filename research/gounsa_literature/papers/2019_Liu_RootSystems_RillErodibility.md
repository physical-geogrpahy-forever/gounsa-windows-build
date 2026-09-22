# 서지정보
Liu, J., Zhang, X., & Zhou, Z. (2019). Quantifying effects of root systems of planted and natural vegetation on rill detachment and erodibility of a loessial soil. *Soil & Tillage Research, 195*, 104420. https://doi.org/10.1016/j.still.2019.104420

# 이 논문을 찾은 이유
여러 root metrics 중 고운사 LPJ-GUESS와 erosion-resistance coupling에 어떤 root trait가 가장 적합한지 확인하기 위해 검토했다.

# 연구 유형
- flume experiment
- planted and natural vegetation comparison

# 공간 구조
- concentrated-flow/rill scale

# 적용 환경
- loessial soil
- vegetation restoration chronosequence

# 핵심 과정
- rill detachment
- rill erodibility K_r
- critical shear tau_c
- root metrics

# 식생 입력
- RMD
- RLD
- fine-root metrics
- vegetation type

# 핵심 결과
- root length density가 rill detachability/erodibility를 설명하는 가장 좋은 root predictor
- K_r는 RLD 증가에 따라 exponential decline
- tau_c와 root parameter의 관계는 문헌 및 본 연구에서 일관성이 낮음
- vegetation type별 root-network complexity 때문에 동일 root metric의 효과계수가 달라질 수 있음

# 고운사에 직접 사용할 수 있는 부분
- LPJ FineRootC 하나보다 RLD conversion이 필요한 근거
- root effect를 K_d/K_r에 두고 tau_s는 독립 측정하는 구조
- woody/herbaceous PFT에 동일 root coefficient를 강제하지 않을 근거

# 한계
loess soil이며 고운사 산림토양에 수치계수 직접 이식 불가.

# 최종 판정
- **FineRootC -> RLD -> K_d를 검토할 핵심 계보**
- generic coefficient 직접 이식은 금지

# 참고 링크 / DOI
https://doi.org/10.1016/j.still.2019.104420
