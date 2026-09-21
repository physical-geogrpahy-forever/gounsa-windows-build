# 서지정보
Goddéris, Y., François, L. M., Probst, A., Schott, J., Moncoulon, D., Labat, D., & Viville, D. (2006). Modelling weathering processes at the catchment scale: The WITCH numerical model. *Geochimica et Cosmochimica Acta, 70*(5), 1128-1147. DOI: 10.1016/j.gca.2005.11.018.

# 이 논문을 찾은 이유
B-WITCH 이전에 forest biosphere와 WITCH가 어떤 방식으로 결합되었는지, 고운사에 필요한 식생-화학풍화 process chain이 실제 numerical model로 존재하는지 확인하기 위해 검토했다.

# 연구 유형
- 수치모델
- catchment-scale reactive weathering model
- forest water/carbon model coupling

# 공간 구조
- layered soil horizons + underlying bedrock
- catchment-scale weathering and stream chemistry
- root zone에서 bedrock 방향의 수직 풍화대

# 적용 환경
- Strengbach granitic forest watershed
- Vosges Mountains, France
- 산림 유역

# 핵심 과정
- primary mineral dissolution
- secondary mineral precipitation
- aqueous speciation
- soil/bedrock chemical weathering
- seasonal water and carbon forcing
- vegetation uptake/release of elements
- soil CO2 control by biospheric productivity

# 식생 입력
- forest ecosystem water and carbon cycle
- biospheric productivity
- soil CO2
- vegetation elemental uptake
- vegetation elemental release

# 핵심 식
WITCH는 laboratory-derived kinetic laws와 thermodynamic state를 이용해 mineral dissolution/precipitation을 계산한다.

식생 coupling 핵심은:

```
forest productivity
 -> soil CO2
 -> mineral dissolution chemistry

vegetation growth / turnover
 -> element uptake / release
 -> soil solution chemistry
 -> weathering
```

원 논문은 WITCH를 ASPECTS forest ecosystem model과 coupling하여 seasonal forcing을 제공한다.

# 파라미터와 단위
- mineral-specific dissolution rate constants
- thermodynamic affinity terms
- soil solution chemistry
- soil CO2
- hydrologic flux
- vegetation uptake/release fluxes

구체 mineral parameter는 고운사 sandstone mineralogy에 맞춰 다시 구성해야 한다.

# 원 논문의 구현 범위
- soil horizons와 underlying bedrock의 chemical weathering
- seasonal simulations
- forest ecosystem forcing
- soil solution 및 catchment stream major solute concentration 검증

# 고운사에 직접 사용할 수 있는 부분
- forest productivity가 soil CO2와 element cycling을 통해 chemical weathering을 조절하는 명시적 process architecture
- root zone부터 bedrock까지 reaction zone을 모델링하는 구조
- 100년 산불 후 vegetation recovery를 화학풍화에 연결할 수 있는 이론적 기반

# 새로운 coupling이 필요한 부분
LPJ-GUESS가 ASPECTS를 대체하면 새로운 coupling이다.

```
LPJ-GUESS
 -> soil/root respiration proxy
 -> soil CO2
 -> WITCH
```

고운사 sandstone-specific mineral assemblage와 반응표도 별도 구축이 필요하다.

# 한계
- 원 application은 granite
- soil production thickness 자체는 직접 계산하지 않음
- detailed reactive transport parameter burden가 큼

# 최종 판정
- **채택: B-WITCH/WITCH 화학풍화 계보의 핵심 기반**
- 고운사 production에서는 식생이 chemical weathering에 실제로 작용하는 근거로 사용한다.

# 참고 링크 / DOI
https://doi.org/10.1016/j.gca.2005.11.018
