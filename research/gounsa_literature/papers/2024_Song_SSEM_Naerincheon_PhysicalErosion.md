# Song et al. (2024) SSEM 내린천 산림유역

## 정확한 서지
Song, M. G., Kim, Y. H., Choi, C. U., Nguyen, V. L., & Yeon, M. H. (2024). Spatial analysis of soil erosion and deposition using physics-based distributed model. *Korean Journal of Agricultural Science, 51*(3), 375–389. https://doi.org/10.7744/kjoas.510312

## 검색 이유
한국 산림 급경사, 강우사상, 침식과 퇴적을 비교한 국내 연구로서 완전 공개 원본 2D 산림 LAI 침식모델인지 검토.

## 방법론 / 대상
강원도 인제 내린천 상류유역, 유역 약 829km², 산림 면적 90% 이상. DEM **250m** 격자로 2020년 3개 강우사상을 재현. 8개 AWS 공간강우 Thiessen; 관측하천 수위에서 유량 변환, 유량-유사량 관계 곡선 `Qss=0.268 Q^1.6081`을 통해 대조 유사량을 산정. 사건별 보정을 별도로 수행함으로써 독립적인 매개변수 전이 검증의 증거는 제한됨.

## 공간구조
분포형 **kinematic wave** `∂h/∂t + ∂q/∂x = r(x,t)` governing equation, flow direction + flow accumulation maps. This is directional 1D advection within a raster, **not true 2D Saint-Venant shallow-water equations**.

## Erosion equations
Two separate components in published SSEM:
`E_N=DF+DR`,
`DR = k KE exp(-b h_s)` (raindrop detachment), `KE=a*r` direct rain factor.
`DF=α(TC/1000-C)h_s` flow detachment / deposition depending transport capacity.
Sediment continuity `∂(h_s C_s)/∂t+∂(q_s C_s)/∂x - E_N=0`. `TC` from Yang(1972) unit-stream-power transport capacity with d50. No native **canopy interception, LAI, throughfall, leaf-drip kinetic energy** represented in the original equations shown. Flow depth, k and soil b parameters external.

## Observations / precision
3 storm runoff NSE 0.43, 0.68, 0.70; sediment NSE 0.63, 0.71, 0.62 against **rating-curve-derived** load, sediment peak ratios 0.55,0.54,0.78 (peak systematically underpredicted). Model internally calibrated each event. Site morphologic field validation of predicted per-cell net erosion 0.45,0.37,0.181cm maxima **not reported as observed true rill/TLS comparisons**.

## Source availability and native validation
Paper full-text freely accessible. Full model original calculation source, build targets and matching regression tests **NOT VERIFIED publicly**; article licensing is NOT source code license. No native run performed in this investigation.

## Suitability verdict
**REJECT native single Gounsa engine**: fails genuine 2D, native quantitative canopy storage/throughfall and original source verification. Valuable mountain forest storm erosion **regional reference only**, not a counterexample to all-native required model being unavailable.

## Reference
https://www.kjoas.org/articles/xml/P91L/
