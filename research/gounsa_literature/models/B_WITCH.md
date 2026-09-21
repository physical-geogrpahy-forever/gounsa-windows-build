# B-WITCH / WITCH vegetation-weathering lineage

## 목적
고운사에서 식생이 chemical weathering에 실제로 들어가는 published process coupling을 정리한다.

## 핵심 계보
- Goddéris et al. 2006: WITCH + ASPECTS forest water/carbon model
- Roelandt et al. 2010: B-WITCH = LPJ-DGVM + WITCH
- ForSAFE/PROFILE: 독립적인 forest ecosystem-weathering 비교계보
- REWTCrunch: explicit root-exudation reactive-transport 고해상도 비교계보

## B-WITCH 구조

```
LPJ-DGVM
├─ PFT / fractional cover
├─ NPP
├─ vegetation / litter / soil C
├─ evapotranspiration
├─ soil water
├─ runoff / drainage
├─ belowground respiration
└─ biomass element uptake / return
        |
        v
B-interface
        |
        v
WITCH
├─ soil / saprolite water flux
├─ soil CO2 / pCO2
├─ primary mineral dissolution
├─ secondary mineral precipitation
├─ aqueous speciation
├─ vegetation element uptake / return
└─ dissolved weathering export
```

## published vegetation pathways

### 1. hydrology
Vegetation controls:
- evapotranspiration
- soil water
- vertical drainage
- runoff

These directly modify mineral-water contact and solute export.

### 2. soil CO2
Belowground respiration from the biosphere model sets soil CO2 forcing.

```
vegetation + litter / SOM respiration
 -> soil pCO2
 -> pH / carbonate chemistry
 -> mineral dissolution
```

### 3. nutrient uptake and return
Roelandt et al. 2010:
- element uptake is linked to NPP and PFT cover
- layer allocation follows transpiration water use
- aboveground litter returns elements to the surface layer
- root litter returns elements to rooted layers

Thus vegetation is a chemical source/sink, not merely a cover class.

## relation to LPJ-GUESS
B-WITCH used LPJ-DGVM, not LPJ-GUESS.

Nevertheless, the published interface variables map naturally to LPJ-GUESS:

```
LPJ PFT                  -> LPJ-GUESS PFT / cohort
LPJ NPP                  -> LPJ-GUESS NPP
LPJ water balance        -> LPJ-GUESS soil water / runoff
LPJ belowground C flux   -> LPJ-GUESS root + litter + SOM respiration states
LPJ biomass turnover     -> LPJ-GUESS litter / root turnover
```

Replacing LPJ by LPJ-GUESS is a **new coupling**.

## temporal issue
Roelandt et al. 2010 averages the final 20 years of LPJ forcing and then drives WITCH toward steady state.

Gounsa instead requires:

```
postfire year t vegetation state
 -> weathering forcing at t
 -> accumulated annual dissolved loss
```

This transient use is also a **new coupling**.

## feedback back to vegetation
Published B-WITCH is essentially one-way:
```
LPJ -> WITCH
```

ForSAFE demonstrates that dynamic two-way forest-soil chemistry feedback is feasible.

For Gounsa, the intended feedback:

```
WITCH nutrient release
 -> LPJ-GUESS-CNP available P / nutrient state
 -> vegetation growth
```

is a **new coupling** and must be implemented explicitly.

## relation to Hartmann / LPJ-GUESS-CNP
Current LPJ-GUESS-CNP weathering:

```
lithology + runoff + soil temperature + shielding
 -> P weathering
```

Vegetation enters mainly through its control on runoff.

This remains a useful low-cost benchmark but does not represent:
- soil CO2 from respiration
- biomass ion uptake/return
- root exudation
- organic-ligand effects

## relation to REWTCrunch
REWTCrunch adds:

```
root biomass(z)
 -> root exudation
 -> microbes / acidity
 -> mineral dissolution
```

This is the preferred advanced sensitivity for explicit rhizosphere chemistry.

## current Gounsa scope refinement

Gounsa does not copy every biological term from B-WITCH-derived lineages.

Required:
- hydrology / drainage
- soil and deep-root CO2
- vegetation element uptake / return
- litter / SOM forcing
- soil temperature

Optional sensitivity:
- non-mycorrhizal root-derived DOC / ligand source

Excluded:
- any mycorrhizal functional type
- fungal hyphal weathering
- fungal organic-acid allocation

Thus B-WITCH is used as a vegetation-weathering interface precedent, not as an instruction to reproduce all biological sub-processes.


## production judgment
Chemical weathering production target:

```
LPJ-GUESS
 -> B-WITCH-style vegetation interface
 -> WITCH/PROFILE-style mineral kinetics
 -> W_chem
```

Hartmann remains benchmark / low-complexity sensitivity.

REWTCrunch remains advanced root-exudation sensitivity/validation.

## critical separation
```
W_chem
!=
P_sand(H)
```

W_chem is dissolved chemical mass loss and elemental release.

P_sand(H) is the empirical bedrock-to-mobile-soil production/front-lowering law.

Do not convert one to the other without an explicit mass/volume/front model.

## references
- Goddéris et al. 2006. DOI 10.1016/j.gca.2005.11.018
- Roelandt et al. 2010. DOI 10.1029/2008GB003420
- Sverdrup & Warfvinge 1993. DOI 10.1016/0883-2927(93)90042-F
- Wallman et al. 2005. DOI 10.1016/j.foreco.2004.10.016
- Kronnäs et al. 2019. DOI 10.5194/soil-5-33-2019
- Roque-Malo et al. 2022. DOI 10.1029/2021JG006562
