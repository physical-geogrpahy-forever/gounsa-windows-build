# Stoebke et al. 2026 - LPJ-GUESS spatially-explicit canopy

## Bibliography

Stoebke, J. E., Wårlind, D., Olin, S., Eckes-Shephard, A., Brzeziecki, B., Peltoniemi, M., & Pugh, T. A. M. (2026). Representing canopy structure dynamics within the LPJ-GUESS dynamic global vegetation model (revision 13221). *Geoscientific Model Development, 19*, 3595-3615. https://doi.org/10.5194/gmd-19-3595-2026

## Why searched

고운사에서 개체목 모델의 계산부담을 피하면서도 상층 수관공극, 하층식생, 재생과 천이를 표준 LPJ-GUESS보다 더 명시적으로 표현할 수 있는지 확인하기 위해 검토했다.

## Study type

LPJ-GUESS canopy-demography model development and evaluation.

## Spatial structure

논문은 표준 LPJ, LPD, PPA, SEC canopy schemes를 비교한다. SEC에서는 각 tree cohort의 aggregated crown area centroid에 patch 내부 고정 위치를 부여한다. tree mortality이 발생하면 그 위치의 canopy gap이 지속되며 새 cohort가 밝은 지점에 정착할 수 있다.

중요한 한계는 SEC의 위치가 실제 지도상의 GIS x-y 좌표가 아니라 patch 내부의 1-D circular coordinate라는 점이다.

## Applied environment

Boreal, temperate, tropical forest sites를 포함한 다지역 stand simulations. 특정 고운사 산불사면 검증은 아니다.

## Core processes

- cohort age/size structure
- horizontal canopy heterogeneity within a patch
- persistent canopy gaps
- cohort crown area and height
- light competition
- herbaceous understory light environment
- gap-dependent establishment
- self-thinning and mortality
- post-disturbance/regrowth stand dynamics

## Vegetation inputs

Standard LPJ-GUESS PFT/cohort vegetation with tree height, bole height, crown area, LAI and establishment/light parameters.

SEC에서는 forest floor의 위치별 light condition에 따라 herbaceous understory leaf area가 동적으로 조정되고 새 PFT cohort establishment가 달라진다.

## Key formulation

SEC의 핵심은 cohort crown centroid를 patch 내부 공간에 지속적으로 두어 개체 사망이나 harvest로 생긴 gap을 다음 해에도 보존한다는 것이다.

이 방식은 standard LPJ-GUESS의 horizontally uniform leaf-area assumption과 다르며, fully spatial individual-based model보다는 단순하다.

## Parameters and units relevant to Gounsa

- cohort height and bole height: tree geometry
- crown area: area
- LAI/fPAR: canopy light interception
- forest-floor PAR: J m-2 d-1 in establishment calculations
- tree density and DBH: stand structure diagnostics

## What can be used for Gounsa

1. 개체목 모델보다 단순한 cohort 기반 구조를 유지하면서 canopy gap을 지속적으로 표현할 수 있다.
2. 하층 초본과 재생층의 빛 제한을 standard LPJ-GUESS보다 현실적으로 다룬다.
3. 산불 후 수관 공극과 천이 회복을 연구하는 고운사 목적에 직접적으로 유리하다.
4. cohort별 crown area, height, density가 tree throw와 canopy-interception coupling의 입력 후보가 된다.

## Required new coupling

SEC 내부 위치를 실제 geomorphology cell과 동일시하지 않는다.

고운사에서는 다음 계층이 새로운 coupling이다.

```text
GIS vegetation unit / hillslope element
 -> LPJ-GUESS stand/patch
 -> SEC internal cohort positions
```

또한 SEC branch와 LPJ-GUESS-RE soil hydrology를 결합하는 것은 논문 자체에 제시된 단일 released model이 아니므로 branch merge/new coupling으로 기록한다.

## Limitations

- explicit x-y individual positions가 아니다.
- cohort 내부 individual끼리 shading interaction을 하지 않는다.
- solar angle을 직접 공간적으로 추적하지 않는다.
- SEC는 standard scheme보다 계산비용이 크게 증가한다.
- hydrology와 geomorphology를 해결하는 모듈은 아니다.

## Final decision

**ACCEPTED AS THE PREFERRED CANOPY/UNDERSTORY BRANCH FOR GOUNSA, SUBJECT TO MERGE FEASIBILITY WITH RE SOIL HYDROLOGY.**

고운사에서 필요한 `개체목보다 단순하지만 하층식생과 gap succession을 명시하는 cohort model`이라는 요구에 현재 가장 잘 맞는 LPJ-GUESS 내부 선택지다.
