# 서지정보
Wang, F., Ouyang, C., An, H., Chen, X., Zhou, S., & Xu, Q. (2025). A flash flood numerical modeling and forecasting tool in mountainous small catchments based on a 2-D hydrodynamic model. *Earth and Space Science, 12*(7), e2024EA004076. https://doi.org/10.1029/2024EA004076. Original first published July 3, 2025.

# 이 논문을 찾은 이유
LISEM 외 다른 원본 **mountain steep hillslope + LAI canopy interception + genuine free X/Y 2D runoff** published application with verifiable open CUDA source and cm computational precedent, checking whether **soil erosion** is simultaneously native.

# 연구 유형 및 공간
Peer reviewed numerical hydro model BRIF (Baseflow-Rainfall-Interception-Flood), GPU accelerated **local inertia approximation** to SWEs, so 2D local inertial hydraulics not identical to *complete* SWE momentum. Forest/crop/grass canopy interception parameterized by landuse crown density and LAI. Paper numerical V-shaped 2D test uses **1m cell**, Cutou mountainous watershed (22km²) storm experiment uses **2.5m cell (6.32 million cells)**, alternative 5m (~1.6 million cells), separate Heishuigou basin experiment uses **8m cell**. These are real computational grid dimensions not LiDAR sample pixel. Cutou uses 0.3m UAV terrain but aggregation: **not 0.3m native simulation**. No 5–10cm computational mesh published.

# 적용 환경
Cutou catchment Wenchuan Sichuan mountainous channel mean gradient 0.181, gully/flash floods including 2021–2022 heavy rain events with 18–24h modeled; land-use forest/shrub/grass/crop and soil depth. LAI input available at **500m** from published Table 5, canopy values are typical land-cover parameter classes, not fine UAV crown LAI for individual patches.

# 핵심 과정
Rainfall, dynamic canopy interception on forest and grasses, soil infiltration, baseflow, 2D local inertia surface routing with variable Courant dt, GPU+CPU speedup and stream discharge validation. **NO coupled soil particle detachment/splash/transport/deposition field in paper**; floods modeled with water only. 2.5m domain is too large for 5–10cm physical micro-rills.

# 식생 입력
Publisher Table1 forest crown density 0.8 LAI10, shrub 0.5/LAI8, cropland0.1/LAI4, grass0.05/LAI2 (phenological and local site values in original model case, not universal constants). These are input/reference values, not measured Gounsa species parameters. DOI paper discusses interception affecting early runoff, no leafdrip kinetic detachment.

# 핵심식 및 실제 CUDA configuration
Official source https://github.com/chinafl/HFDM-GPU, README calls it HFDM high-performance flood dynamic model, CUDA/C++; repo `test/wind_cuda.cu` blob SHA `4c4d756f3aba141cb03f3ae451d792ba5fd5f500`, L~930–1080 sets class-specific V_LAI, V_Cover, `V_Smax` and `V_K`:
- `V_Smax=0.1713*V_LAI` for a forest class, in units of water storage based on model's definitions;
- `V_Smax=0.59*pow(V_LAI,0.88)` for another broadleaf/grass parameter class;
- `V_K=1-exp(-V_Cover*V_LAI)` attenuation; 
- `test/windmath_cuda.cuh` line86 declares CUDA `Diff_interception(... V_Smax,V_K,...)` and other CUDA flow/infiltration kernel prototypes.
- 2D flux output source `test/main.cu` / `test/wind_cuda.cu`, registered global water and interception classes.

# PUBLIC CODE LIMIT (critical)
Repo tree exact `test/`: `case`, `dem.cu`, `dem.cuh`, `main.cu`, `structfile.cuh`, `wind_cuda.cu`, `wind_cuda.cuh`, **`windmath_cuda.cuh` declaration only; NO `windmath_cuda.cu` function implementation in the public repository tree**. `hfdm` file root is binary (GitHub text access UnicodeDecodeError). Source prototype presence is **not fully editable complete solver** nor a successful rebuild. No original particle erosion/sediment/bedupdate code in inspected source tree. Paper Data Availability says part of core code, NOT entire source (Zenodo DOI10.5281/zenodo.15613301). Do not claim full open executable from public test files.

# 파라미터와 단위
Cutou cell Δx=2.5m, Ncell=6.32 million, rainfall-event duration18–24h; rainfall input WRF forecast 1km, DEM from UAV0.3m and Gaofen7 1m; LAI observed input resolution 500m. Published 18h run ~1.9h Tesla V100 or 2.9h DCU. V-shape benchmark1m grid. No actual 0.05/0.1m case. Internally variable CFL dt, exact smallest Δt depends on run.

# 원논문의 구현범위
Native 2D water and vegetation canopy interception plus infiltration and baseflow in steep mountain local inertial hydrodynamics. Published scientifically valid physical storm-water model, NOT native hillslope soil detachment/deposition solver.

# 고운사 활용
Strong near-forest canopy+2D hydrology paper reference with **exact native fine computational grid documented** and source evidence. But to meet storm erosion would require manual extra sediment solver/new coupling and violate single original user requirement.

# 한계 및 최종판정
**보조 수문연구 / Gounsa single native model 탈락**. Canopy+2D local inertial+steep mountains PASS; native 5cm FAIL (min1m generic /2.5m forest); native sediment erosion/dep FAIL; fully editable open CUDA source FAIL (missing required implementation).

# sources
https://doi.org/10.1029/2024EA004076
https://github.com/chinafl/HFDM-GPU
https://doi.org/10.5281/zenodo.15613301
