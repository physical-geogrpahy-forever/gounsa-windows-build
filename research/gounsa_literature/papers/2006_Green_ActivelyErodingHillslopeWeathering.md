# 서지정보
Green, E. G., Dietrich, W. E., & Banfield, J. F. (2006). Quantification of chemical weathering rates across an actively eroding hillslope. *Earth and Planetary Science Letters, 242*(1-2), 155-169. DOI: 10.1016/j.epsl.2005.11.039.

# 이 논문을 찾은 이유
사면 위치와 physical erosion이 chemical weathering flux를 얼마나 바꾸는지 정량화한 고전 field mass-balance 자료를 확인하기 위해 검토했다.

# 연구 유형
- field geochemical mass balance
- cosmogenic-nuclide-constrained timescale analysis

# 공간 구조
- soil-mantled eroding hillslope
- ridge to downslope positions
- soil + saprolite

# 적용 환경
- granodiorite hillslope
- southern New South Wales, Australia

# 핵심 과정
- soil chemical weathering
- saprolite weathering
- physical erosion
- solute export
- hillslope position
- residence time

# 식생 입력
explicit vegetation state 없음.

따라서 식생 process source가 아니라 hillslope weathering/erosion constraint로 사용한다.

# 핵심 결과
solution mass loss가 total hillslope mass loss의 약:
```
35-55%
```
를 차지했다.

Chemical weathering rates and degrees vary across the actively eroding hillslope.

핵심은:
```
physical erosion / residence time
<-> chemical weathering
```
을 분리할 수 없다는 점이다.

# 고운사에 직접 사용할 수 있는 부분
식생이 erosion을 바꾸면 chemical weathering도 간접적으로 변한다.

따라서:
```
vegetation
 -> SWEHR / q_hill
 -> soil residence time / fresh-mineral supply
 -> W_chem
```
경로를 feedback architecture에 포함할 근거다.

# 새로운 coupling이 필요한 부분
고운사 event-scale erosion에서 annual soil residence/fresh-mineral exposure state를 chemistry에 넘기는 것은 새로운 coupling.

# 한계
- vegetation explicit 없음
- granodiorite
- site-specific mass balance
- direct process model 아님

# 최종 판정
- **채택: physical erosion-chemical weathering hillslope feedback constraint**
- coefficient source 아님

# 참고 링크 / DOI
https://doi.org/10.1016/j.epsl.2005.11.039
