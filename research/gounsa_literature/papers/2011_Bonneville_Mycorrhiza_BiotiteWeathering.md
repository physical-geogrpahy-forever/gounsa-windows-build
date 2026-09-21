# 서지정보
Bonneville, S., Morgan, D. J., Schmalenberger, A., Bray, A., Brown, A., Banwart, S. A., & Benning, L. G. (2011). Tree-mycorrhiza symbiosis accelerate mineral weathering: Evidences from nanometer-scale elemental fluxes at the hypha-mineral interface. *Geochimica et Cosmochimica Acta, 75*(22), 6988-7005. DOI: 10.1016/j.gca.2011.08.041.

# 이 논문을 찾은 이유
mycorrhizal weathering을 단순 qualitative mechanism이 아니라 실제 mineral-interface kinetics로 정량화한 근거가 있는지 확인하기 위해 검토했다.

# 연구 유형
- mineral-interface experiment
- quantitative alteration model

# 공간 구조
- nanometer-scale hypha-biotite interface
- living tree-root mycorrhizal association

# 적용 환경
- Pinus sylvestris
- Paxillus involutus ectomycorrhiza
- biotite mineral surface

# 핵심 과정
- hyphal attachment
- microscale acidification
- elemental depletion
- biotite alteration
- chemical and biomechanical fungal effects

# 식생 입력
- living tree-root symbiosis
- surface-bound fungal hypha
- fungal activity

# 핵심 식
논문은 hypha-mineral interface의 solid-state elemental flux와 alteration depth를 이용해 quantitative alteration model을 제시한다.

관측:
- hypha microenvironment pH < 약 4.6
- K, Mg, Fe, Al의 강한 depletion
- abiotic dissolution과 비교 가능한 fungal alteration kinetics 산출

reported close-to-natural hypha-associated alteration rate:
```
~0.04 μmol biotite m^-2 h^-1
```
수준.

이 값은 고운사 sandstone coefficient로 직접 전이하지 않는다.

# 파라미터와 단위
- pH
- elemental concentration depth profile
- alteration flux [μmol mineral m^-2 h^-1]
- hyphal-mineral contact geometry

# 원 논문의 구현 범위
living tree-mycorrhiza가 mineral surface를 국소적으로 산성화하고 원소를 제거하는 속도를 정량화한다.

# 고운사에 직접 사용할 수 있는 부분
mycorrhiza-mediated weathering을:
- proton source
- organic-ligand source
- reactive microsite
로 chemical-weathering sensitivity에 넣을 물리적 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS PFT/mycorrhizal state를 local reactive surface fraction과 acid/ligand source로 변환하는 것은 새 coupling.

# 한계
- biotite
- micro/nanoscale
- whole-soil or sandstone front-production rate로 직접 upscale 불가

# 최종 판정
- **핵심 보조근거: mycorrhizal mineral-weathering kinetics**
- direct landscape coefficient로 사용하지 않음

# 참고 링크 / DOI
https://doi.org/10.1016/j.gca.2011.08.041
