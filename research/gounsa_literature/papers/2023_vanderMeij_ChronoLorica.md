# 서지정보
van der Meij, W. M., Temme, A. J. A. M., Binnie, S. A., & Reimann, T. (2023). ChronoLorica: Introduction of a soil–landscape evolution model combined with geochronometers. *Geochronology, 5*, 241–261. https://doi.org/10.5194/gchron-5-241-2023

# 이 논문을 찾은 이유
Lorica 계열에서 수직 토양입도와 토양층 이력이 어떻게 장기적으로 추적되는지 확인하고, 고운사 coarse fraction과 profile tracer 구조의 선례를 검토하기 위해 읽었다.

# 연구 유형
- 수치모델
- soil-landscape evolution
- geochronometer coupling

# 공간 구조
- Lorica 기반 다층 토양프로파일
- landscape evolution과 particle history 추적

# 적용 환경
- 장기 토양과 지형발달
- 이상화된 토양경관 및 지질연대 추적

# 핵심 과정
- soil mixing
- erosion
- deposition
- particle transport
- particle age
- radionuclide inventory

# 식생 입력
- 고운사에서 필요한 PFT/cohort 식생동태는 핵심이 아님

# 핵심 식
이 세션에서 exact 식 전체는 구현수준으로 복구하지 않았다. 중요한 점은 Lorica 계열의 토양입자와 층 상태를 보존하면서 입자의 이동과 퇴적 이력을 tracer처럼 추적할 수 있다는 것이다.

# 파라미터와 단위
- gravel, sand, silt, clay 등 입도 상태
- particle ages
- radionuclide inventories
- layer thickness
세부 단위와 계산식은 원문 재검증 필요.

# 원 논문의 구현 범위
Lorica soil-landscape evolution model에 geochronological tracer를 결합해 입자의 이동과 혼합, 퇴적 이력을 추적한다.

# 고운사에 직접 사용할 수 있는 부분
고운사에서 fire spall과 기존 coarse fragment를 같은 돌로 취급하지 않고 provenance 또는 tracer state를 부여할 수 있다는 구조적 선례.

# 새로운 coupling이 필요한 부분
```text
coarse fragment provenance = prefire / exposed C-Cr / fire-spall
```
처럼 출처를 구분하는 것은 ChronoLorica를 참고한 고운사 새로운 coupling이다.

# 한계
- fire spall 전용 모델이 아님
- 고운사 산불 후 단기과정과 시간척도가 다름
- 전체 Lorica transport engine을 이식하면 기존 모델과 중복 가능

# 최종 판정
- provenance/tracer 구조의 보조근거로 채택
- 전체 모델 이식은 미채택

# 참고 링크 / DOI
https://doi.org/10.5194/gchron-5-241-2023
