# 2026-09-22 embedded-stone model-selection handoff

## 사용자 요구
- 고운사에는 매립 석력이 많다.
- 가장 중요한 것은 어떤 **기존 published model**을 가져오는가이다.
- 자의적인 새로운 경험식과 fitted factor를 만들지 않는다.

## 이번 세션 핵심 결정
### embedded rock-fragment hydrology
- 기본: Naseri et al. 2020 General Effective Medium (GEM)
- water retention: Naseri et al. 2023 published WRC/HCC framework
- 보조검증: Ma & Shao 2008 dual-porosity model

### surface stone / seal
- EUROSEM의 ROC/PAVE/ISTONE 원식 사용 가능
- 단, embedded라는 이유만으로 infiltration 감소 부호를 부여하지 않는다.
- surface seal/macroporosity/stone position과 원 모델 조건이 일치할 때만 적용.

### genuine 2D erosion
- Iber+ 2024를 production erosion-engine 우선후보로 유지
- 2D SWE, rainfall/flow detachment, multiclass sediment, loose-layer shielding, size-specific transport, Exner를 기존 구현 그대로 활용

## 자의성 방지 규칙
금지:
- custom armour factor
- custom stoniness-infiltration multiplier
- 임의 biomass-erodibility 계수
- fragment size threshold를 현장자료 없이 임의 지정

허용:
- published equations 그대로 사용
- 동일 물리량을 모델 간 전달
- site parameters는 측정값 또는 published calibration range 사용

## 모델 chain
```
embedded RF geometry/content
 -> GEM/Naseri
 -> K(h), theta(h), Ksat
 -> Iber+ hydrology/2D erosion
 -> multiclass sediment redistribution
```

surface seal/stone condition이 실제로 해당될 때만 EUROSEM PAVE/ISTONE을 적용.

## 단일 모델 trade-off
- EUROSEM alone: stoniness+hydrology+erosion 한 모델, 그러나 genuine 2D와 dynamic multiclass armour 부족
- Iber+ alone: 2D+multiclass 강함, embedded high-stoniness hydraulic property physics 부족
- 모든 기존 requirements 유지 시 GEM/Naseri -> Iber+ modular chain이 가장 비자의적

## 새로 저장한 파일
Papers:
- 1998_Morgan_EUROSEM.md
- 2017_Khaleghpanah_EUROSEM_StonySteepLands.md
- 2008_Ma_Shao_StonySoilDualPorosity.md
- 2020_Naseri_GEM_StonySoilHydraulicConductivity.md
- 2023_Naseri_RockFragments_WaterRetentionConductivity.md

Models:
- EUROSEM.md
- Stony_Soil_Hydraulics_GEM.md
- Rock_Fragment_Armour.md 갱신

Decision:
- 2026-09-22_STONY_SOIL_MODEL_SELECTION.md

MASTER 및 INDEX 갱신.

## 다음 검증
1. GEM output을 Iber+ Green-Ampt/Horton input으로 넘기는 published conversion이 있는지 확인
2. conversion이 없다면 Ksat/porosity/suction을 독립적으로 published soil-hydraulic model에서 산정할 방법 탐색
3. Iber+ loose layer가 fire-spall cobble/gravel classes까지 원 설계상 허용하는지 source/model-paper 수준 확인
4. sandstone fragment 자체의 K(h), theta(h) 자료 확인
5. fire severity -> spall mass/size distribution 정량모델 조사
