# 결정 내용
현재 고운사 100년 이내 모델에서 우선 정리하는 지형과정은 다음 세 축이다.

1. 유수침식
2. 사면확산 및 biogenic hillslope transport
3. 풍화 및 soil/regolith production

# 유수침식
Saco식 biomass-erodibility 선례는 유지하되 최종 생산모델은 total biomass 하나보다 PFT별 root traits와 hydraulics를 사용하는 방향을 우선한다.

후보 구조:
FineRootC_i -> RMD_i, RLD_i, RSAD_i, SRL_i
그 뒤 Dc, Kr, tau_c를 hydraulics와 soil structure의 함수로 계산.

# 사면확산
COPLAS의 LeafC -> total D 구조는 채택하지 않는다.

작업구조:
q_hill = q_creep + q_rootgrowth + q_treethrow

산불 후에는 CWD sediment storage/connectivity 효과를 별도 상태로 둔다.

# 풍화
작업구조:
W_total = W_hydroclimatic + W_deep_root_chemical + W_woody_mechanical

root-access depth는 AB thickness와 동일시하지 않고 C/Cr까지 허용한다.

# 근거 논문
- Gabet et al. 2003
- Gabet & Mudd 2010
- Doane et al. 2021/2023/2024
- Adams et al. 2023
- REWTCrunch 2022
- Pawlik et al. 2023/2024
- Osorio-Leon et al. 2025
- Billings et al. 2025
- Bemis et al. 2026

# 주의
위 세 과정의 합성구조는 하나의 기존 published model이 아니라 **고운사 새로운 coupling**이다.
