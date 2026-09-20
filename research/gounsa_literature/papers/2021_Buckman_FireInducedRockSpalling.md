# 서지정보
Buckman, S., Morris, R. H., & Bourman, R. P. (2021). Fire-induced rock spalling as a mechanism of weathering responsible for flared slope and inselberg development. *Nature Communications, 12*, 2150. https://doi.org/10.1038/s41467-021-22451-2

# 이 논문을 찾은 이유
산불 중 새롭게 생성되는 박리암편의 두께, 면적, 질량과 장기적인 지형학적 의미를 정량적으로 확인하기 위해 검토했다.

# 연구 유형
- 현장조사
- 사진측량
- 장기 침식률 추정
- 개념모델

# 공간 구조
- 호주 여러 암석노두, 인셀베르크, 암괴, 절벽
- 2019–2020 Black Summer 산불 이후 현장 포함
- 수치 격자모델은 아님

# 적용 환경
- 화강암
- 사암
- 현무암
- 건조지역과 온대 산불환경

# 핵심 과정
- fire-induced rock spalling
- thermal expansion
- rock flaking
- sediment production
- 인셀베르크 기부의 측방침식

# 식생 입력
- 식생은 fuel load와 fire severity를 조절하는 배경인자
- biomass 기반 지형식은 아님

# 핵심 식
장기 fire-spalling erosion rate:
```text
E = W × A / t
```
- E: fire-spalling erosion rate, mm yr^-1
- W: 한 화재에서 생성되는 평균 spall 두께, mm
- A: 박리되는 노출암석 면적비율, 0–1
- t: 평균 fire recurrence interval, yr

sediment production:
```text
S_FS = P × H × E
```
- P: 인셀베르크 둘레, m
- H: 화재영향을 받는 flared slope 높이, m
- E: m yr^-1로 변환한 침식률

Cobargo 두 지점의 현장 측정에서는 16.89와 33.55 kg m^-2가 관찰되었고, 평균 박리두께로 환산하면 약 0.63–1.25 cm 수준이었다. Moonbi의 강한 사례에서는 한 화재로 여러 박리층이 생겨 총 5–20 cm 수준의 박리가 관찰되었다.

# 파라미터와 단위
- W: mm
- A: 무차원 면적비율
- t: yr
- E: mm yr^-1
- rock density: kg m^-3
- spall mass: kg 또는 kg m^-2

# 원 논문의 구현 범위
화재 재현주기와 한 번의 화재에서 발생하는 박리두께와 면적비율을 이용해 장기 측방침식률과 신규 퇴적물 생산을 추정한다.

# 고운사에 직접 사용할 수 있는 부분
한 번의 산불사건에서 spall mass를 생성하는 event-scale mass balance의 근거가 된다.

고운사 제안식:
```text
Delta M_sp = rho_r A_exposed d_sp f_sp
```
이 식은 Buckman의 두께 × 면적 개념을 사건단위 질량보존식으로 재구성한 새로운 coupling이며 원 논문에 그대로 존재하지 않는다.

# 새로운 coupling이 필요한 부분
- 노출암석면적 A_exposed를 고운사 격자에서 계산
- C/Cr 또는 R에서 빠진 질량을 M_spall로 이동
- spall 이동과 armour 효과를 별도로 계산

# 한계
- 원식 E = W A / t는 장기 평균식이므로 2025년 단일 사건의 직접 생산식으로 그대로 사용하면 안 됨
- 암질별, 화재강도별 W와 A 변동이 큼
- spall 이동과 토양유출 효과를 직접 계산하지 않음

# 최종 판정
- fire spall 생성과 장기 지형학적 중요성의 핵심 근거로 채택
- 단일 사건에서는 질량보존형 새로운 coupling으로 변환

# 참고 링크 / DOI
https://doi.org/10.1038/s41467-021-22451-2
