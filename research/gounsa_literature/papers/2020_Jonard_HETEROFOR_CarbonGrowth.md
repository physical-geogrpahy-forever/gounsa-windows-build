# 서지정보
Jonard, M., André, F., de Coligny, F., de Wergifosse, L., Beudez, N., Davi, H., Ligot, G., Ponette, Q., Vincke, C., & others. (2020). HETEROFOR 1.0: a spatially explicit model for exploring the response of structurally complex forests to uncertain future conditions – Part 1: Carbon fluxes and tree dimensional growth. Geoscientific Model Development, 13, 905-935. DOI: 10.5194/gmd-13-905-2020

# 이 논문을 찾은 이유
LiDAR 기반 고운사 식생-지형 결합을 위해 개별목 좌표, 정량 root biomass, litter flux, 수관경쟁을 동시에 가진 온대림 모델인지 검토했다.

# 연구 유형
- 수치모델
- 공간명시적 개체목 process-based forest model

# 공간 구조
- 각 성목의 x, y, z 좌표를 명시적으로 입력
- 개체목별 수관 크기와 4방향 수관반경
- ray-tracing 기반 수관 광경쟁
- stand 규모 공간명시적 모델

# 적용 환경
- 온대 혼효림
- 유럽 활엽수림
- 후속 계보에서 북미 온대림과 침엽수 포함

# 핵심 과정
- 광합성
- 호흡
- 탄소배분
- 개체목 생장
- 경쟁
- fine-root production and turnover
- structural-root production and mortality
- leaf/fine-root litter
- tree mortality

# 식생 입력
- individual tree location
- DBH/girth
- total height
- crown base
- crown extension height
- crown radius in four directions
- leaf biomass
- fine-root biomass
- structural/coarse-root biomass
- fruit production

# 핵심 식
Fine-root biomass:
```
b_fine_root = b_leaf * r_fine_root_leaf
```
여기서 비율은 영양상태에 따라 변화한다.

Fine-root and leaf litter:
```
s_leaf_or_fine_root
= b_leaf_or_fine_root
  * turnover_rate
  * (1 - retranslocation_fraction)
```

Structural-root mortality도 별도 turnover로 계산한다.

# 파라미터와 단위
- biomass: kg C per tree
- litter flux: kg C yr-1
- fine-root turnover: yr-1
- tree dimensions updated yearly
- photosynthesis/water processes use finer time steps

# 원 논문의 구현 범위
개체목별 탄소획득, 기관별 배분, 수관 및 수목 크기 변화, fine/coarse root와 litter flux를 모의한다.

# 고운사에 직접 사용할 수 있는 부분
- LiDAR에서 추출한 개체목 좌표와 수관구조를 직접 초기화 가능
- 살아있는 fine-root biomass
- 구조근 biomass
- fine-root turnover와 dead-root/litter input
- 산불 후 surviving trees의 회복과 경쟁
- 100년 온대림 천이의 생리적 기반

# 새로운 coupling이 필요한 부분
- fire severity -> tissue mortality and initial postfire state
- fine-root biomass -> horizontal RLD/RSAD map
- structural root biomass -> root architecture/root reinforcement
- geomorphic soil-depth update -> HETEROFOR horizon geometry

# 한계
fine-root 총량은 leaf biomass와 영양상태 기반 비율로 산정한다. 수평 root architecture가 개별 뿌리로 명시되지는 않는다. 구조근 크기 등급 출력은 원 1.0에서는 모델 기능에 되먹임되지 않는다.

# 최종 판정
- 채택 후보
- LiDAR 기반 주 식생엔진의 핵심 근거

# 참고 링크 / DOI
https://doi.org/10.5194/gmd-13-905-2020
