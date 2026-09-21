# 서지정보
Drever, J. I. (1994). The effect of land plants on weathering rates of silicate minerals. *Geochimica et Cosmochimica Acta, 58*(10), 2325-2332. DOI: 10.1016/0016-7037(94)90013-2.

# 이 논문을 찾은 이유
균근을 제외한 상태에서 식생이 silicate weathering에 미치는 기본 경로와, 그 효과의 부호가 항상 양(+)인지 확인하기 위해 검토했다.

# 연구 유형
- review / synthesis
- mineral-dissolution literature synthesis

# 공간 구조
- mineral surface
- rhizosphere
- soil/regolith profile

# 적용 환경
- silicate minerals
- soil systems
- land-plant weathering

# 핵심 과정
식생 영향은 다음으로 분리된다.

```
plant respiration
 -> soil CO2
 -> pH

root/soil organic ligands
 -> complexation / dissolution

plant-induced soil physical changes
 -> exposed mineral surface area
 -> water residence time

vegetation / erosion interaction
 -> fresh-mineral supply
```

# 식생 입력
- living roots / respiration
- organic acids / ligands
- soil-structure modification
- fine-particle binding

균근 관련 논의가 원문에 포함되지만, 고운사에서는 최신 scope decision에 따라 사용하지 않는다.

# 핵심 결과

## pH effect
silicate dissolution의 pH response는 비선형이다.

대체로:
- pH 약 4-5 이하: pH가 낮아질수록 dissolution 증가
- circumneutral: pH dependence 약함
- 높은 pH: 일부 silicate dissolution 증가

따라서:
```
more root CO2
!= universally proportional increase in weathering
```

## organic ligands
far-from-equilibrium laboratory conditions에서 oxalate effect는 mineral type에 따라 크게 달랐다.

즉:
```
organic ligand effect
= mineral-specific
```

## physical soil effects
식생이 fine particles와 soil structure를 바꾸어:
- reactive surface
- water residence time
- fresh-mineral exposure
를 바꾸는 간접효과가 chemical-solution chemistry effect보다 더 클 수 있다고 정리한다.

## long-term sign
장기에는 식생이 secondary products를 고정하거나 unweathered mineral을 meteoric water에서 격리하여 chemical weathering을 낮출 가능성도 제시한다.

# 파라미터와 단위
review이므로 단일 parameter set 없음.

중요 threshold:
- silicate acid-catalysis transition near pH 4-5

이 threshold도 고운사 universal coefficient로 hard-code하지 않고 mineral-specific kinetic law에서 처리한다.

# 원 논문의 구현 범위
land plants가 chemical weathering에 미치는 direct/indirect mechanisms를 정리한 고전 synthesis.

# 고운사에 직접 사용할 수 있는 부분
가장 중요한 제약:

```
vegetation effect
!= universal positive multiplier
```

현재 production에서:
- root respiration / CO2
- DOC / organic ligand
- hydrology / residence time
- fresh-mineral supply
를 별도 process로 분리하는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS state를:
- soil pCO2
- organic-ligand concentration
- hydrologic residence time
로 변환하는 것은 별도 coupling이다.

# 한계
- 1994 synthesis
- modern reactive-transport implementation 자체는 아님
- sandstone-specific quantitative law 없음

# 최종 판정
- **채택: non-mycorrhizal vegetation-weathering sign/structure constraint**
- 식생 multiplier 금지의 핵심 근거
- coefficient source가 아니라 architecture constraint

# 참고 링크 / DOI
https://doi.org/10.1016/0016-7037(94)90013-2
