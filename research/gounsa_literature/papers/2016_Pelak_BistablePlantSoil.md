# 서지정보
Pelak, N. F., Parolari, A. J., & Porporato, A. (2016). Bistable plant-soil dynamics and biogenic controls on the soil production function. *Earth Surface Processes and Landforms, 41*(8), 1011-1017. DOI: 10.1002/esp.3878.

# 이 논문을 찾은 이유
plant biomass가 soil production function에 직접 들어가는 published numerical model이 실제로 있는지 확인하고, 고운사의 식생-sensitive sandstone soil-production sensitivity에 사용할 수 있는지 재검토했다.

# 연구 유형
- minimal coupled numerical/theoretical model
- two-state plant-soil dynamics
- bistability analysis

# 공간 구조
- local soil-depth / plant-biomass dynamical system
- explicit 2D hillslope routing model은 아님

# 적용 환경
- generic hillslope plant-soil system
- erosion-dominated environments
- land degradation / vegetation-removal scenarios

# 핵심 과정
- plant biomass growth
- plant-driven soil production
- vegetation-mediated erosion inhibition
- soil-depth dynamics
- positive plant-soil feedback
- bistability / degraded vs sustainable state

# 식생 입력
- plant biomass density `b` [kg m^-2]
- vegetation growth rate
- vegetation turnover

PFT/root-organ-specific model은 아니다.

# 핵심 식

원 논문의 abstract는 두 coupled nonlinear differential equations로 plant-soil feedback을 구성한다고 명시한다.

Schaller & Ehlers (2022) supplement가 Pelak et al. 2016의 soil-production law를 다음과 같이 재현한다.

```
P(h,b)
=
[P0 + Pv b(h)] exp(-ks h)
```

where:
- `P0`: abiotic soil production rate in absence of vegetation and soil [mm yr^-1]
- `Pv`: sensitivity of soil production to vegetation [mm^3 yr^-1 kg^-1 in the Schaller unit reconstruction]
- `ks`: shielding/decoupling rate with soil depth [m^-1]
- `h`: soil depth [m]

Vegetation equilibrium response to soil depth:

```
b(h)
=
(r/m)[1-exp(-kg h)]
```

where:
- `r`: vegetation growth rate [yr^-1]
- `m`: turnover coefficient [m^2 yr^-1 kg^-1]
- `kg`: vegetation growth response to soil depth [m^-1]

Important:
the above equation/units were independently checked through the Schaller & Ehlers 2022 supplement, which explicitly notes unit adjustments in its cross-model comparison. Before direct implementation, Pelak Table I/original typeset equations must still be checked against the final parameter units.

# 모델 거동
Because:
- biomass is low at very small `h`
- biomass increases with soil depth
- deep soil shields bedrock from surface/biotic weathering

the coupled model can generate:

```
P(h)
= humped
```

without simply imposing a fixed humped curve.

The paper shows sufficiently strong positive plant-soil feedback can produce soil-depth bistability.

# 원 논문의 구현 범위
이 논문은:
- plant-driven soil production
- vegetation erosion inhibition
을 minimal local system으로 탐색한다.

It is not:
- a sandstone-specific process model
- a root-fracture mechanics model
- a reactive-transport chemical-weathering model
- a distributed hillslope model

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 published structural precedent:

```
vegetation quantity
 -> soil production potential
```

을 explicit equation으로 둔다는 점.

Rossi et al. 2026:
- forest structure
- bedrock exposure
- humped soil production

Schaller & Ehlers 2022:
- observed soil-production variation most closely resembles soil-depth + biomass models

와 함께 고려하면 vegetation-sensitive soil-production sensitivity를 별도 시험할 강한 근거가 된다.

# 새로운 coupling이 필요한 부분
고운사에서는 다음이 모두 새 coupling이다.

```
LPJ-GUESS PFT/root state
 -> Pelak biomass state
```

```
Pelak generic production
 -> sandstone-specific P_sand
```

특히:
- AGB를 쓸지
- FineRootC를 쓸지
- root-zone biomass를 쓸지
원 논문만으로 정할 수 없다.

# 한계
- minimal model
- spatial hillslope position 없음
- process identity가 lumped soil production
- physical, chemical, root-mechanical weathering을 분리하지 않음
- generic plant biomass
- long-term equilibrium/bistability focus
- sandstone calibration 없음

# 최종 판정
- **채택: explicit vegetation-sensitive soil-production model의 핵심 이론 선례**
- 고운사 기본 production law로 직접 사용하지 않음
- **vegetation-sensitive Mode C / sensitivity candidate**로 승격
- coefficient direct transfer 금지
- current Mode A/B를 대체하지 않음

# 참고 링크 / DOI
https://doi.org/10.1002/esp.3878

# 재검증 메모
- Original abstract/model existence: Pelak et al. 2016 / Calhoun CZO archive.
- Equation reconstruction: Schaller & Ehlers 2022 supplement, DOI 10.5194/esurf-10-131-2022-supplement.
