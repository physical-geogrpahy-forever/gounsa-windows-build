# 서지정보
Foster, G. R., Flanagan, D. C., Nearing, M. A., Lane, L. J., Risse, L. M., & Finkner, S. C. (1995). *Hillslope Erosion Component*. In D. C. Flanagan & M. A. Nearing (Eds.), USDA-Water Erosion Prediction Project: Hillslope Profile and Watershed Model Documentation. NSERL Report No. 10, Chapter 11.

# 이 문서를 찾은 이유
interrill/rill sediment continuity and Foster-style shear-excess equations를 공식 원문에서 확인하기 위해 검토했다.

# 연구 유형
- official technical model documentation

# 공간 구조
- 1D hillslope profile
- rill/interrill conceptual separation

# 핵심 과정
Sediment continuity:
```
dG/dx = D_f + D_i
```

Rill detachment capacity:
```
D_c = K_r (τ_f - τ_c)
```

Net rill detachment:
```
D_f = D_c (1 - G/T_c)
```

Interrill:
```
D_i = K_i,adj I_e σ_ir SDR_RR F_nozzle (R_s/w)
```

# 파라미터와 단위
Original Chapter 11 definitions and units must be used.

# 고운사에 직접 사용할 수 있는 부분
- distinct interrill/rill physics
- mathematical bridge to Wu 2020
- flow-driven shear-excess structure comparable to Iber+ Kd

# 새로운 coupling이 필요한 부분
Embedding these equations/parameters in a 2D solver outside WEPP is **new coupling** unless directly inherited in that published model.

# 한계
WEPP hillslope routing is not genuine 2D.

# 최종 판정
**core erosion-equation technical source.**
