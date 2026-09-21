# 서지정보
Bower, J. A., Ross, D. S., Bailey, S. W., Pennino, A. M., Jercinovic, M. J., McGuire, K. J., Strahm, B. D., & Schreiber, M. E. (2023). Development of a lateral topographic weathering gradient in temperate forested podzols. *Geoderma, 439*, 116677. DOI: 10.1016/j.geoderma.2023.116677.

# 이 논문을 찾은 이유
산림사면에서 lateral hydrologic flow가 실제 mineral weathering intensity를 얼마나 크게 바꾸는지 정량 field evidence를 찾기 위해 검토했다.

# 연구 유형
- forested hillslope toposequence
- mineral mass-transfer analysis
- electron microscopy / microprobe mineral depletion

# 공간 구조
- closely spaced forested podzols
- lateral eluvial zones
- lateral illuvial zones
- vertically developed podzols
- local gradient in depth to bedrock and lateral water flow

# 적용 환경
- White Mountains, New Hampshire
- humid temperate forest
- postglacial podzols

# 핵심 과정
- lateral subsurface water flow
- podzolization
- plagioclase weathering
- Na/Al depletion
- short-range topographic weathering gradients

# 식생 입력
forested ecosystem background이며 dynamic vegetation model은 없다.

즉 vegetation type effect보다 forest soil + topographic hydrology weathering evidence로 사용한다.

# 핵심 결과
Lateral-flow-affected podzols had substantially stronger mineral depletion.

Median Na loss:
- lateral eluvial: 약 74%
- lateral illuvial: 약 56%
- vertical podzol: 약 40%

Microprobe-estimated plagioclase loss:
- lateral eluvial: 약 74%
- lateral illuvial: 약 39%
- vertical: 약 23%

즉:
```
lateral hillslope flushing
 -> much stronger mineral depletion
```
가 가능하다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요하다.

```
vertical 1D pedogenesis only
```
는 산지 forest soil weathering을 충분히 설명하지 못할 수 있다.

고운사에서는:
```
upslope water delivery
lateral flushing
depth-to-bedrock
```
를 W_chem spatial state에 포함할 강한 근거.

# 새로운 coupling이 필요한 부분
Landlab/BioRT/PFLOTRAN flow field에서:
- lateral throughflow
- accumulated upslope water flux
를 WITCH/PROFILE cell chemistry에 전달하는 것은 NEW COUPLING이다.

# 한계
- podzol/glacial parent material
- no dynamic vegetation
- long-term weathering extent
- sandstone-specific 아님

# 최종 판정
- **핵심 채택: forest hillslope lateral-flow chemical-weathering gradient**
- local vertical column weathering 한계의 직접 evidence
- spatial hydrology 우선순위 강화

# 참고 링크 / DOI
https://doi.org/10.1016/j.geoderma.2023.116677
