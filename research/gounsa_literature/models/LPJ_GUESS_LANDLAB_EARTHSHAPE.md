# LPJ-GUESS + Landlab / EarthShape coupling lineage

업데이트: 2026-09-23

## 왜 중요한가
고운사 모델은 식생이 지형을 바꾸고, 바뀐 지형과 토심이 다시 식생에 영향을 주는 양방향 vegetation-geomorph coupling을 요구한다.

EarthShape 계열은 LPJ-GUESS와 Landlab을 실제로 연결한 공개 코드가 존재하므로, 현재까지 확인된 가장 직접적인 LPJ-GUESS ↔ landscape-evolution software precedent 중 하나다.

공개 저장소:
- `toddehlers/lpj_guess_earthshape`
- `toddehlers/lpj_landlab_coupling`

---

# 1. Published origin
Werner et al. (2018)은 LPJ-GUESS에 subpixel landform mode를 추가했다.

목적:
```text
coarse climate / LPJ grid
 -> high-resolution DEM-derived landforms
 -> landform-specific vegetation dynamics
 -> future Landlab coupling
```

논문에서 계획한 two-way architecture:
```text
LPJ-GUESS
 -> vegetation cover + surface hydrology
 -> Landlab

Landlab
 -> updated topography + landform area + soil depth
 -> LPJ-GUESS
```

2018 논문 자체는 full coupling을 아직 구현하지 않았지만, 후속 공개 코드에는 실제 wrapper가 존재한다.

---

# 2. Open coupling code
`toddehlers/lpj_landlab_coupling`의 `DynVeg_LpjGuess`는 LPJ-GUESS를 Landlab Component처럼 감싼다.

공개 coupled example:
`landlab/test_simulation_coupled/runfile_space.py`

Landlab 구성:
- RasterModelGrid
- FlowRouter, D8
- SPACE
- ExponentialWeatherer
- DepthDependentDiffuser
- landform classifier

Landlab state:
- `topographic__elevation`
- `bedrock__elevation`
- `soil__depth`
- `vegetation__density`
- drainage area / slope / erosion rates

---

# 3. LPJ -> Landlab feedback is operational
`create_input_for_landlab.py`:

LPJ LAI를 Beer-Lambert 방식으로 FPC로 변환:
```text
FPC = (1 - exp(-0.5 * LAI)) * 100
```

그리고 최종 식생 cover를:
```text
grid.at_node['vegetation__density']
```
에 기록한다.

Landlab driver에서 이 vegetation state는 다음 지형과정에 들어간다.

## fluvial erodibility
식생량에 따라 sediment/bedrock erodibility를 조절.

## hillslope diffusivity
식생에 따라 linear diffusivity를 조절.

따라서:
```text
LPJ vegetation
 -> Landlab erosion / diffusion
```
은 공개 코드에서 실제로 작동한다.

주의:
고운사에서는 cover/FPC만으로 erosion resistance를 표현하지 않고 root biomass, litter, live/dead roots 등으로 교체해야 한다.

---

# 4. Landlab -> LPJ input bridge
`create_input_for_lpjguess.py`는 Landlab 결과에서 다음을 읽는다.
- elevation
- steepest slope
- aspect
- aspect-corrected slope
- landform ID
- soil depth

그리고 이를 LPJ-GUESS landform/site NetCDF input으로 재구성한다.

즉 Python coupling layer 자체에는:
```text
Landlab terrain / soil state
 -> LPJ input
```
경로가 이미 있다.

하지만 LPJ EarthShape source audit에서 중요한 제한이 발견됐다.

---

# 5. LPJ EarthShape soil-depth implementation
`guess_4.0.1/framework/guess.h`의 `Landform` struct:
- `elevation`
- `slope`
- `aspect`
- `soildepth`
- `soildepth_lower_mod`
- `has_deepwater`

`Site`에도 `soildepth`가 존재한다.

따라서 software data model은 soil depth를 받을 준비가 되어 있다.

그러나 `modules/landform.cpp`에서 continuous soil-depth NetCDF input은 주석 처리되어 있다.

예:
```text
// nc_soildepth = ...
// site.soildepth = nc_soildepth->get_value()
```

즉 inspected snapshot에서는 Landlab이 출력한 arbitrary soil depth를 LPJ가 그대로 읽지는 않는다.

---

# 6. 실제로 작동하는 soil-depth effect
대신 landform slope-position class에 따라 `soildepth_lower_mod`를 설정한다.

LPJ 기본 토층:
```text
upper = 0.5 m
lower = 1.0 m
```

EarthShape modifiers:
```text
ridge      lower * 0.25 -> total 약 0.75 m
upslope    lower * 0.33 -> total 약 0.83 m
midslope   lower * 0.50 -> total 1.00 m
flat       lower * 1.00 -> total 1.50 m
downslope  lower * 1.25 -> total 1.75 m
valley     lower * 1.50 -> total 2.00 m
```

`sp_modifysoildepth`가 활성화되면:
```text
awc[lower] *= soildepth_lower_mod
```
가 canopy/water uptake calculation에서 적용된다.

SOM/N leaching calculation에도 같은 depth modifier가 사용된다.

따라서:
```text
landform position
 -> effective soil depth / AWC
 -> plant water limitation
```
은 실제 작동하는 기능이다.

---

# 7. Root limitation
EarthShape branch의 plant water uptake는 여전히 PFT-prescribed `rootdist[]`를 사용한다.

즉 soil depth가 얕아져도:
- eroded root biomass를 실제 제거하지 않음
- root carbon pool을 토층별로 보존하지 않음
- soil truncation 후 root exposure를 계산하지 않음
- deposition 후 burial를 계산하지 않음

따라서 고운사의 핵심 추가 coupling은:
```text
new soil geometry
 -> truncate roots below/within eroded volume
 -> remove/export root C/N
 -> recompute surviving vertical root fractions
 -> update water uptake
```
이다.

---

# 8. Time/space scale of public coupled example
`inputFile.py`:
- 21 x 21 nodes
- dx = 100 m
- dt = 100 years
- total runtime = 1,000,000 years

따라서 이 coupling은 landscape-evolution timescale을 목적으로 한다.

고운사 요구:
```text
storm hydrology / geomorph: hourly or event
vegetation physiology: daily
long-term demography: annual or native schedule
```
와 시간구조가 다르다.

즉 code architecture는 재사용 가능하지만 timestep design은 새로 해야 한다.

---

# 9. High-value precedent for Gounsa
EarthShape는 다음을 이미 보여준다.

1. LPJ-GUESS를 external geomorph model wrapper에서 반복 실행할 수 있음
2. restart/state-dump 기반 segmented execution 가능
3. LPJ vegetation output을 Landlab field로 직접 변환 가능
4. landscape model의 elevation/slope/aspect/soil depth를 LPJ input dataset으로 다시 생성 가능
5. landform-specific effective soil depth가 LPJ water balance에 실제 feedback 가능

따라서 고운사에서 `LPJ-GUESS + geomorph`는 처음부터 새 software architecture를 만드는 것이 아니다.

---

# 10. What cannot be copied directly
고운사 최종모델에 그대로 쓰지 않는 요소:
- D8 FlowRouter를 genuine 2D erosion으로 간주하지 않음
- FPC/cover 하나로 erosion resistance를 계산하지 않음
- 100-year coupling interval 사용하지 않음
- slope-class-only soil depth 사용하지 않음
- static PFT rootdist만 사용하지 않음

---

# 11. Relationship to modern LPJ branches
EarthShape source is LPJ-GUESS 4.0.1 era.
Modern required branch functions:

```text
SEC/PPA 2026
 -> spatial cohort canopy / persistent gaps

PF-LPJG 2026
 -> hourly ParFlow + daily soil-state exchange

LPJ-GUESS-RE 2025
 -> flexible multilayer soil / Richards / bedrock

EarthShape/Landlab
 -> open vegetation-landscape coupling architecture
```

A single published branch combining these does not exist.

Gounsa integration is therefore a **new coupling/code merge**.

---

# 12. Recommended use in Gounsa design
EarthShape should not replace SEC/PF-LPJG.
Its role is software architecture precedent.

Recommended architecture:
```text
LPJ-GUESS SEC/PPA
  tree cohorts + gaps + shrub/herb competition
        |
        | daily vegetation state exchange
        v
Gounsa coupling layer
        |
        +--> external hydrology / geomorph
        |      hourly/event
        |      DEM and soil-depth update
        |
        +<-- soil moisture / soil geometry / root-loss event
```

Borrow from EarthShape:
- segmented LPJ execution / restart pattern
- GIS/landform input generation
- vegetation-output to geomorph-field translation

Replace EarthShape cover interface with:
- fine-root biomass
- live/dead root biomass
- litter
- LAI/interception
- PFT/cohort biomass

---

# 13. Current verdict
**핵심 coupling precedent / LPJ-GUESS 계열 평가를 크게 강화.**

EarthShape/Landlab 발견 이후 LPJ-GUESS의 가장 큰 약점이었던 “실제 geomorph model coupling 경험이 있는가?”에 대한 답은 YES이다.

그러나 현재 공개 code snapshot은:
- very long timestep
- cover-based geomorphic vegetation effect
- continuous dynamic soil-depth input partly unfinished
- root truncation absent

따라서 final production implementation은 modern SEC/PF-style LPJ를 기반으로 EarthShape coupling design을 이식하는 방식이 더 적합하다.

# 핵심 문헌
- Werner et al. (2018), Earth Surface Dynamics 6:829–858. DOI 10.5194/esurf-6-829-2018.
- Schmid et al. (2018), Earth Surface Dynamics 6:859–881. DOI 10.5194/esurf-6-859-2018.
- later EarthShape LPJ-GUESS/Landlab coupled presentations and source repositories.
