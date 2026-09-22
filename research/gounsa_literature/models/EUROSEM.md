# EUROSEM lineage

## 고운사에서 검토한 이유
매립 석력과 surface armour가 infiltration, runoff, splash, rill/interrill erosion에 미치는 효과를 하나의 published erosion model에서 명시적으로 처리하는지 확인하기 위해 검토했다.

## 핵심 문헌
- Morgan et al. 1998, EUROSEM key paper
- Morgan et al. 1998, EUROSEM documentation and user guide
- Khaleghpanah et al. 2017, stony steep lands validation
- Jomaa et al. 2012, rock-fragment hydrology/erosion modeling comparison

## 공간 구조
- distributed event model
- cascading plane/channel elements
- interrill/rill explicit
- genuine 2D SWE 아님

## rock-fragment state
EUROSEM은 세 변수를 명시적으로 분리한다.

### ROC
`ROC` = soil volume 중 rock-fragment fraction.

기존 KINEROS infiltration formulation을 따라:
```
B_roc = B (1 - ROC)
```
으로 soil water-storage/saturation-deficit term을 조정한다.

### PAVE
`PAVE` = soil surface의 non-erodible/rock-fragment cover fraction.

raindrop detachment:
```
DET_pav = DET (1 - PAVE)
```

### ISTONE
surface position/sealing condition에 따라 PAVE가 saturated hydraulic conductivity를 증가 또는 감소시키도록 선택한다.

infiltration-reducing condition:
```
K_s,roc = K_s (1 - PAVE)
```

infiltration-enhancing condition:
```
K_s,roc = K_s (1 + PAVE)
```

중요: `embedded`라는 단어만으로 ISTONE 부호를 정하지 않는다.
- surface seal에 partially embedded된 fragments는 infiltration을 낮출 수 있음.
- high structural porosity/macroporosity 조건의 fully embedded/resting fragments는 infiltration을 높일 수 있음.
따라서 현장 surface seal/porosity 상태가 필요하다.

## 고운사에서 직접 쓸 수 있는 부분
- ROC, PAVE, ISTONE의 정의
- surface armour의 splash shielding
- stoniness와 infiltration/runoff를 같은 erosion model 안에서 연결한 published precedent
- steep stony hillslope 적용 선례

## 고운사에서 그대로 쓰기 어려운 부분
- full EUROSEM은 genuine 2D가 아님.
- rock-fragment state가 event 중 dynamic size-class armour로 진화하지 않음.
- high-volume embedded stone의 full unsaturated hydraulic conductivity curve에는 현대 GEM model이 더 적합함.

## 최종 판정
**부분 채택.**
- surface PAVE/shielding과 surface seal-position logic의 published source
- full production erosion engine으로는 사용하지 않음
- 고운사의 high embedded stoniness hydraulic property는 GEM/Naseri 계열을 우선

## 관련 파일
- ../papers/1998_Morgan_EUROSEM.md
- ../papers/2017_Khaleghpanah_EUROSEM_StonySteepLands.md
- ../papers/2012_Jomaa_RockFragmentHydrologyErosionModel.md
