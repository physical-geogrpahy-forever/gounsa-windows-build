# 서지정보
Li, X., Niu, J., & Xie, B. (2014). *The Effect of Leaf Litter Cover on Surface Runoff and Soil Erosion in Northern China*. PLOS ONE, 9(9), e107789. DOI: 10.1371/journal.pone.0107789.

# 이 논문을 찾은 이유
forest-floor surface litter를 cover fraction이 아니라 areal litter mass [kg m^-2] 자체로 조절한 실험에서 runoff와 sediment response를 정량화할 수 있는지 확인하기 위해 검토했다.

# 연구 유형
- field-plot rainfall simulation experiment
- numerical erosion model 아님

# 공간 구조
- 1 x 1 m hillslope subplots

# 적용 환경
- Northern China
- Quercus variabilis broadleaf litter
- Pinus tabulaeformis needle litter

# 핵심 과정
- rainfall interception
- surface runoff
- sediment yield
- raindrop shielding
- surface roughness / sediment deposition

# 식생 입력
Areal litter mass was explicitly manipulated:
- 0
- 0.3
- 0.5
- 0.8
- 1.0 kg m^-2

# 핵심 식
The paper reports direct empirical relationships between litter mass and sediment yield / sediment concentration rather than a process-model erodibility equation.

At 1 kg m^-2, total sediment yield decreased from about 13.77 kg on bare soil to about 0.75 kg for Quercus litter and 0.92 kg for Pinus litter.

The largest marginal reduction occurred when litter increased from 0 to 0.3 kg m^-2.

# 파라미터와 단위
- areal litter mass: kg m^-2
- rainfall intensity: multiple imposed intensities
- runoff volume
- sediment yield / sediment concentration

# 원 논문의 구현 범위
Directly tests surface-exposed litter mass and litter type under rainfall.

# 고운사에 직접 사용할 수 있는 부분
Strong evidence that exposed litter amount can be retained as a quantitative state variable rather than being represented only by vegetation cover.

It also shows a nonlinear/saturating response of sediment reduction to litter mass.

# 새로운 coupling이 필요한 부분
Using litter mass to modify 2D model rainfall detachability, shear resistance, or roughness is a **new coupling** because the paper does not provide a complete numerical erosion law for those parameters.

# 한계
- experiment, not a numerical model
- litter mass is still partly effective because it creates surface cover and roughness
- direct transfer to Gounsa forest-floor species is not justified

# 최종 판정
- **채택: exposed-surface litter mass evidence**
- not sufficient alone for final process equation

# 참고 링크 / DOI
https://doi.org/10.1371/journal.pone.0107789
