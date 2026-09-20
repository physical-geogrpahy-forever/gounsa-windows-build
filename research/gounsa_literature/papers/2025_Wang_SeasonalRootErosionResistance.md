# 서지정보
Wang, J., Yang, Y., Wang, B., & Liu, G. (2025). Seasonal variations in soil erosion resistance under tap and fibrous root systems grasslands on the Chinese Loess Plateau. *Geoderma, 458*, 117350.

# 이 논문을 찾은 이유
LPJ-GUESS의 계절적 root dynamics를 erosion parameter time series로 연결할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- 현장/실험

# 공간 구조
- grassland plots

# 적용 환경
- Loess Plateau grassland

# 핵심 과정
- rill erodibility
- critical shear stress

# 식생 입력
- tap vs fibrous root systems
- RMD
- RLD
- RSAD

# 핵심 식
이 채팅 정리에는 tap-root grassland `K_r`가 fibrous-root보다 약 2.83배 높고, `K_r`가 root traits 증가에 따라 감소한다고 기록됨.

# 파라미터와 단위
`K_r`, `tau_c`, RMD, RLD, RSAD.

# 원 논문의 구현 범위
한 growing season 동안 root traits와 erosion resistance의 계절변화를 추적.

# 고운사에 직접 사용할 수 있는 부분
PFT/root phenology에 따라 erosion parameter가 시간변화해야 한다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS seasonal FineRootC와 root architecture로 `K_r(t)`, `tau_c(t)`를 계산하면 새로운 coupling.

# 한계
수치 지형모델 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2025.117350
