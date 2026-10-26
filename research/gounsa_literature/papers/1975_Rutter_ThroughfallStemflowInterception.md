# 서지정보
Rutter, A. J., Morton, A. J., & Robins, P. C. (1975). A predictive model of rainfall interception in forests. II. Generalization of the model and comparison with observations in some coniferous and hardwood stands. *Journal of Applied Ecology, 12*, 367–380. https://doi.org/10.2307/2401739

# 이 논문을 찾은 이유
고운사 참나무 맹아와 억새 연구에 핵심인 Rutter 계열의 수간유하우 별도 계산이 실제 출판된 원 모형에 있는지, 이것이 SWEHR 2016 원논문과 공개 C에도 전달됐는지 구분.

# 연구 유형
수관 강우분배 수지모형 확장과 야외 관측 대조. [A: 영국생태학회 공식 출판정보 및 초록 직접 확인]

# 공간 구조
수관/줄기 저류 0D 또는 임분 수지. Per-stem spatial 2D runoff routing not published here.

# 적용 환경
Pinus nigra, Pseudotsuga menziesii, Picea abies, Carpinus betulus, old Quercus robur coppice and artificially defoliated Quercus robur plot.

# 핵심 과정
**Throughfall and stemflow separately modeled**, evaporation from trunks and leaf-on/leafless differences. Calculated interception losses averaged within 10% of observed mean for most stands over 8–18 months; old Q. robur coppice mean monthly interception underestimated by 20%, artificially defoliated coppice by 32%.

# 식생 입력
Crown canopy and trunk storage, free throughfall, stemflow allocation, stand structure and leaf state.

# 핵심식
Generalized canopy + trunk reservoirs mass budget; exact full-text trunk equations not transcribed from inaccessible body, do not invent symbols.

# 파라미터와 단위
Rain/stemflow/throughfall depth per event or month, storage mm, time scale; note long-term errors in coppice types.

# 원 논문의 구현 범위
Time-varying canopy/trunk storage with separate SF and TF. No erosion entrainment/redeposition and no spatial stem locations.

# 고운사에 직접 사용할 수 있는 부분
Rutter original family *does* distinguish stemflow, relevant to isolated oak stools versus dense grass tussocks. However McGuire (2016) simplified Eq24–26 only document generic canopy storage C and drainage D; independent trunk store and spatial SF NOT confirmed in current SWEHR C.

# 새로운 coupling
Stem/tussock count, morphology and location + reservoir SF allocation mapped to 2D water source, and separate direct-throughfall/drop KE.

# 한계
Rutter model empirical validation on mature coppice and defoliation had poorer fit; high intensity 1-hour burned Quercus shoots and M.sinensis are unlike old Q. robur stand. Field parameterization required.

# 최종 판정
Rutter 1975 species-relevant original structure, but not an already built spatial erosion component.

# 참고 링크
https://www.britishecologicalsociety.org/applied-ecology-resources/document/19751918683/
