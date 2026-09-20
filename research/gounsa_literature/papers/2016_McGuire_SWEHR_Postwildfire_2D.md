# 서지정보
McGuire, L. A., Kean, J. W., Staley, D. M., Rengers, F. K., & Wasklewicz, T. A. (2016). *Constraining the relative importance of raindrop- and flow-driven sediment transport mechanisms in postwildfire environments and implications for recovery time scales*. Journal of Geophysical Research: Earth Surface, 121(11), 2211-2237. DOI: 10.1002/2016JF003867.

# 이 논문을 찾은 이유
고운사처럼 steep postfire mountain hillslope에서 genuine 2D runoff와 Hairsine-Rose rainfall/flow erosion을 함께 계산하고, rill network가 실제로 발달하는 published model을 확인하기 위해 검토했다.

# 연구 유형
- process-based numerical erosion model
- high-resolution postwildfire field-model integration
- synthetic-hillslope sensitivity experiments

# 공간 구조
- 2D depth-averaged surface flow
- local orthogonal Cartesian coordinates aligned with topographic surface
- spatially distributed sediment transport
- high-resolution topography
- dynamic erosion/deposition and rill development

# 적용 환경
- San Gabriel Mountains, California
- 2009 Station Fire
- steep recently burned mountain basin
- approximately 0.01 km2 monitored headwater basin

# 핵심 과정
- rainfall interception
- infiltration
- 2D overland flow
- raindrop detachment/redetachment
- flow-driven entrainment/reentrainment
- size-selective sediment
- deposited-layer shielding
- deposition
- bedload extension
- rill formation/evolution
- postfire recovery sensitivity

# 식생 입력
Vegetation is represented mainly by:
- vegetation cover fraction C_v
- canopy throughfall coefficient T_c
- canopy storage/drainage parameters

Postfire recovery is not dynamically simulated.
Instead, C_v and saturated hydraulic conductivity k_s are varied as proxies for recovery.

No root biomass/RLD direct input.

# 핵심 식
The sediment model uses Hairsine-Rose.

For each sediment class k it tracks:
- suspended concentration c_k
- deposited sediment mass m_k
- original-soil detachment
- deposited-layer redetachment
- flow entrainment/reentrainment
- deposition

Rainfall shielding by vegetation is represented with:
```
((1 - C_v) + T_c C_v)
```

A deposited layer progressively shields original soil.

Flow-driven entrainment uses excess stream power and can form rills without predefining a fixed rill mask.

# 파라미터와 단위
Key variables:
- C_v: vegetation cover fraction [-]
- T_c: throughfall coefficient [-]
- k_s: saturated hydraulic conductivity [mm h^-1]
- n: Manning coefficient [s m^-1/3]
- deposited mass needed for complete shielding [kg m^-2]
- rainfall detachability coefficients
- stream-power entrainment fraction F
- particle sizes

# 원 논문의 구현 범위
The model was calibrated against TLS-derived topographic change from real postfire storms.

Major verified findings:
- long-duration/modest-intensity storm: >60% of hillslope erosion could be associated with raindrop-driven processes
- short/high-intensity storm: flow-driven erosion becomes relatively more important
- rills form when flow-driven detachment is active
- rills become deeper/more extensive when rainfall- and flow-driven detachment act together
- erosion recovery timescale depends differently on vegetation recovery and infiltration recovery depending on the dominant erosion process

# 고운사에 직접 사용할 수 있는 부분
This is one of the closest process engines to Gounsa:
```
steep postfire mountain
+ 2D flow
+ rainfall detachment
+ flow entrainment
+ deposited loose layer
+ multi-size sediment
+ emergent rills
+ field topographic-change calibration
```

It is especially important because it does **not** require a fixed rill mask.

# 새로운 coupling이 필요한 부분
Replacing cover-based vegetation effects with:
- LPJ-GUESS FineRootC/RMD/RLD
- exposed litter mass/geometry
- incorporated litter mass/LSAD
is **새로운 coupling**.

# 한계
- vegetation protection remains cover-based
- no dynamic root biomass/root mechanics
- vegetation/soil recovery explored through parameter sweeps rather than an ecosystem model
- event-scale model, not 100-year continuous simulation by itself

# 최종 판정
- **top-tier Gounsa water-erosion engine candidate**
- much stronger than previously recorded
- must be compared directly with Kim 2013 Hairsine-Rose, Iber+ 2024, Ouyang 2023 and SERGHEI-SE
- root/litter quantitative coupling remains unresolved

# 참고 링크 / DOI
https://doi.org/10.1002/2016JF003867
