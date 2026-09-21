# Gounsa soil-weathering non-mycorrhizal handoff

날짜: 2026-09-21 10:20 KST
브랜치: `gounsa-water-erosion-deep-review-2026-09-21`

## 사용자 범위 수정

```
균근(mycorrhiza) 제외
```

현재 production 및 sensitivity에서 제외:

```
mycorrhizal_type
AM / EcM
fungal hyphal weathering
fungal oxalate allocation
PFT -> mycorrhiza mapping
mycorrhizal weathering multiplier
```

관련 문헌은 archive/reference only.

Authoritative:
`decisions/2026-09-21_MYCORRHIZA_EXCLUSION.md`

---

## 이번 추가 문헌검토 핵심

### newly reviewed non-mycorrhizal papers

- `papers/1994_Drever_LandPlants_SilicateWeathering.md`
- `papers/2010_Maher_FluidResidence_Weathering.md`
- `papers/2013_Calvaruso_PineRoots_ApatiteDissolution.md`
- `papers/2025_Chibesa_RootExudates_SiliconSolubilisation.md`
- `papers/2020_Tune_Bedrock_CO2_ForestCarbon.md`
- `papers/2023_Tune_DeepRoot_PetrogenicCarbonWeathering.md`

Earlier third-pass additions retained:
- Lawrence 2014
- Perez-Fodich 2019
- BioRT-Flux-PIHM 2022
- Wen 2022
- BioRT-HBV 2024
- Gatz-Miller 2022/2023
- Garcia-Arredondo 2023
- Potysz & Bartz 2024
- Yu & Hunt 2018

Mycorrhizal papers remain archive only:
- Bonneville 2011
- Quirk 2012
- Schmalenberger 2015
- Rombouts 2026
- Taylor 2011 mycorrhizal mechanism

---

## corrected Osorio-Leon 2025 lithology

원 site:
```
primarily argillite
+ sandstone interbeds
```

따라서 direct Gounsa sandstone coefficient source가 아니다.

Process use only:
```
deep-root-associated respiration
 -> bedrock-zone CO2
 -> carbonic-acid weathering
```

---

## current authoritative non-mycorrhizal chemical-weathering structure

```
LPJ-GUESS
├─ PFT / NPP
├─ FineRootC(z)
├─ root fraction by layer
├─ root access depth
├─ root water uptake by layer
├─ root / belowground respiration
├─ litter / SOM
├─ nutrient uptake / return
├─ soil temperature
└─ soil water / runoff / drainage
       |
       v
vegetation-hydrology interface
       |
       v
WITCH / PROFILE
or BioRT spatial alternative
       |
       ├─ pCO2 / pH
       ├─ mineral dissolution / precipitation
       ├─ reaction affinity / saturation
       ├─ residence time
       ├─ secondary-mineral state
       ├─ W_chem
       └─ nutrient release
              |
              v
       LPJ-GUESS-CNP
       [new return coupling]
```

Optional sensitivity only:
```
non-mycorrhizal root-derived DOC / organic ligand
```

---

## literature implications

### Drever 1994
```
vegetation effect
!= universal positive multiplier
```

pH effect, ligand effect, physical-soil effect, erosion/fresh-mineral supply can have different signs.

### Maher 2010
weathering rate can be strongly controlled by:
```
fluid residence time
flow rate
saturation state
```

Hence runoff-only forcing is insufficient for full production weathering.

### Calvaruso 2013
Scots pine root-only treatment increased apatite element release strongly relative to abiotic control.

Thus:
```
living roots
 -> proton / organic-acid source
 -> mineral dissolution
```
does not require mycorrhiza as a conceptual pathway.

### Chibesa 2025
root-exudate compounds show:
```
compound-specific
x mineral-specific
x soil-specific
```
weathering response.

Therefore exudate source is optional sensitivity, not fixed multiplier.

### Tune 2020/2023
deep-root-associated recently fixed carbon drives substantial CO2 production below soil.

Thus:
```
root access depth
>
mobile-soil depth
```
must remain possible.

---

## current process hierarchy

### core
- root/deep respiration -> CO2
- root vertical distribution
- root water uptake
- soil/subsurface hydrology
- water residence time
- soil temperature
- nutrient uptake/return
- litter/SOM chemistry
- mineralogy / cement
- reactive surface
- secondary minerals

### optional sensitivity
- root-derived DOC / organic ligands
- REWTCrunch-style exudation

### excluded
- all mycorrhizal states/processes
- arbitrary biomass/NPP weathering multiplier
- arbitrary root-exudate multiplier

---

## soil production boundary

unchanged:

```
W_chem
!=
P_sand(H)
```

`P_sand(H)` remains:
- Mode A exponential
- Mode B shallow finite-depth hump sensitivity

Chemical-weathering-to-front-advance bridge:
- Yu & Hunt 2018
- Braun 2016

remains future sensitivity only.

---

## new authoritative decision

`decisions/2026-09-21_SOIL_WEATHERING_FOURTH_PASS_NON_MYCORRHIZAL.md`

---

## next work

1. LPJ-GUESS source/output audit for root respiration
2. layer-wise root water uptake availability
3. drainage and water-balance outputs
4. calculation of water residence time
5. WITCH/PROFILE vs BioRT source/code practicality
6. Gounsa sandstone petrography/mineral assemblage
7. reactive surface area
8. optional non-mycorrhizal root-exudate source
9. nutrient-return mass balance
