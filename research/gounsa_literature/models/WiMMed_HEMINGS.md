# WiMMed / HEMINGS lineage

## 핵심 문헌
- Millares et al. (2019), Environmental Modelling & Software 111, 61-71
- Millares, Herrero & Bermúdez (2020), *Long-term modeling of soil loss and fluvial transport processes in a mountainous semi-arid basin, southern Spain*, River Flow 2020
- HEMINGS 2026 model description discussed in this chat; exact formal paper metadata remains to be consolidated

## 고운사에서 검토한 이유
actual mountain-basin distributed erosion model that separates raindrop, rill, gully and channel/headcut processes.

## 공간구조
- distributed raster hydrology
- local routing / D8 lineage
- not genuine 2D shallow-water field

## 적용환경
- Mediterranean mountainous semi-arid basin
- high-mountain catchments
- long-term reservoir sedimentation calibration/validation

## processes
- raindrop erosion
- rill erosion
- gully erosion
- headcut migration
- fluvial transport
- hydrological connectivity

## vegetation
Plant residue/cover is part of rill-density/erosion parameterization.
The current chat did **not** verify a dynamic root biomass/RLD state directly calculated inside the model.

Earlier handoff language suggesting WiMMed root biomass was stronger than what later verification supported. Current strict judgement is therefore:
- mountain application: strong
- rill/interrill/gully distinction: strong
- genuine 2D: no
- quantitative dynamic root state: not confirmed

## 고운사에 쓸 수 있는 부분
- mountain/basin process architecture
- gully/headcut processes
- long-term erosion/sediment-transport validation precedent

## 새로운 coupling
LPJ-GUESS quantitative vegetation state -> WiMMed/HEMINGS erodibility is **new coupling** unless a direct published equation is independently verified.

## 최종 판정
**산지 적용 보조 lineage.**
Not the final strict 2D quantitative-vegetation solution.
