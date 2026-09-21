# 결정: 균근(mycorrhiza) production 제외

날짜: 2026-09-21

## 결정

고운사 현재 production 및 sensitivity architecture에서 균근 관련 상태와 coupling을 제외한다.

제외:
```
mycorrhizal_type
AM / EcM / mixed state
fungal hyphal weathering
fungal oxalate allocation
PFT -> mycorrhizal functional type mapping
mycorrhizal weathering multiplier
```

관련 문헌은 삭제하지 않고 archive/reference only로 보존한다.

## 이유

현재 고운사 production의 식생-풍화 경로는 균근 없이도 다음 published process pathways로 구성 가능하다.

```
LPJ-GUESS
├─ root depth/distribution
├─ root water uptake
├─ root respiration / belowground CO2
├─ litter / SOM
├─ nutrient uptake / return
├─ soil temperature
└─ hydrology / drainage
       |
       v
chemical-weathering engine
```

따라서 모델 복잡도를 불필요하게 늘리는 균근 functional-type mapping은 현재 범위에서 제외한다.

## 유지하는 vegetation-weathering pathways

- root respiration -> soil/fracture CO2
- root/litter-derived DOC 또는 organic-ligand sensitivity
- root depth/distribution -> water and solute transport
- nutrient uptake/return -> solution chemistry
- litter/SOM decomposition -> soil chemistry
- vegetation-controlled hydrology
- erosion suppression -> fresh-mineral supply limitation

주의:
root/litter organic-ligand pathway를 유지한다고 해서 fungal/mycorrhizal source term을 포함하는 것은 아니다.

## 관련 논문 판정

다음 문헌은 archive/reference only:
- Bonneville et al. 2011
- Quirk et al. 2012
- Schmalenberger et al. 2015
- Rombouts et al. 2026
- Taylor et al. 2011의 mycorrhizal-specific mechanism

Taylor et al. 2012는 DGVM -> process-based weathering이라는 상위 구조만 참고한다. mycorrhizal functional type 항은 고운사에 사용하지 않는다.

Banwart et al. 2009는 soil CO2, DOC, pH, hydrology, mineral kinetics 구조만 사용하며 mycorrhizal-specific interpretation은 사용하지 않는다.

## production rule

금지:
```
LPJ-GUESS PFT
 -> AM/EcM
 -> W_chem
```

금지:
```
W_chem *= f_mycorrhiza
```

현재 production chemical-weathering input에는 균근 변수가 없다.

## 우선순위

균근을 제외한 뒤 다음을 우선한다.

1. LPJ-GUESS layer-wise root state
2. root respiration / soil CO2
3. hydrology / residence time
4. litter/SOM and DOC sensitivity
5. nutrient uptake/return
6. sandstone mineralogy/cement
7. reactive surface area
8. WITCH/PROFILE vs BioRT engine selection
