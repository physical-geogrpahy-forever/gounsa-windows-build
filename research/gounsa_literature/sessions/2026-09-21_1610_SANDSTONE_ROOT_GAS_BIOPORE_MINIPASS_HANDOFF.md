# Gounsa sandstone root-gas / biopore mini-pass handoff

날짜: 2026-09-21
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 이번 소묶음의 목적

전송 시간 초과를 피하기 위해 논문 4편만 검토하고 즉시 archive에 반영했다.

질문:

    sandstone forest hillslope에서 vegetation은
    chemical weathering / soil production / subsurface hydrology에
    어떤 서로 다른 경로로 들어가는가?

## 새로 검토한 논문

1. `papers/2019_Hodges_Sandstone_SoilGas_RootRespiration.md`
2. `papers/2016_Shouse_Phillips_Tree_SoilDeepening_ParentMaterial.md`
3. `papers/2018_Pawlik_Kasprzak_TreeRoot_ERT_Regolith.md`
4. `papers/2019_Turkington_Shouse_Sandstone_Tree_Bedrock_Denudation.md`

## 핵심 새 결론

### 1. respiration source와 gas state를 분리

    root respiration
      -> R_CO2(z)
      -> porosity / gas diffusion / saturation
      -> pCO2(z), pO2(z)
      -> weathering

Hodges 2019에서 sandstone watershed는 동일 깊이 기준 높은 pCO2와 낮은 pO2를 보였고, deeper root respiration과 macroporosity가 중요한 해석으로 제시됐다.

### 2. tree-induced local soil deepening은 존재하지만 rate는 아님

Shouse & Phillips 2016:

    root-rock contact
      -> local deeper soil/regolith

flat-bedded sedimentary setting에서도 나타남.

그러나 stump-adjacent depth contrast를 `P_sand`로 변환하지 않는다.

### 3. postfire에도 inherited root-channel structure가 남을 수 있음

Pawlik & Kasprzak 2018:

    tree roots
      -> root channels / moisture migration / regolith heterogeneity

그리고 tree mortality/cutting 후 수십 년에도 subsurface signature가 남을 수 있음.

따라서:

    live vegetation(t)
    !=
    inherited root-created connectivity(t)

로 본다.

decay law는 미확정이며 임의 생성하지 않는다.

### 4. vegetation은 surface protection과 bedrock bioerosion을 동시에 만들 수 있음

Turkington & Shouse 2019:

    roots -> surface stabilization

동시에:

    root grooves / joint opening -> sandstone bedrock denudation

따라서 single vegetation multiplier 금지를 더 강화한다.

## 모델/결정 파일 갱신

- `models/Hillslope_Vegetation_Weathering.md`
- `decisions/2026-09-21_HILLSLOPE_VEGETATION_WEATHERING.md`

## 이번에 하지 않은 것

- `INDEX.md` 전체 재생성
- `MASTER.md` 대규모 재작성
- arbitrary root-channel decay coefficient 생성
- ERT resistivity를 permeability로 직접 환산
- stump soil-depth contrast를 annual soil-production rate로 환산

## 다음 소묶음 우선순위

다음 3-4편은 아래 가운데 하나로 좁혀서 진행한다.

1. root-channel / biopore persistence의 disturbance 이후 시간변화
2. sandstone forest에서 pCO2 또는 deep respiration과 실제 mineral weathering flux를 함께 측정한 연구
3. fracture-accessible roots가 soil-production 또는 weathering-front migration을 정량화한 산림사면 연구

INDEX는 여러 소묶음이 쌓인 뒤 한 번만 actual tree 기준으로 재생성한다.