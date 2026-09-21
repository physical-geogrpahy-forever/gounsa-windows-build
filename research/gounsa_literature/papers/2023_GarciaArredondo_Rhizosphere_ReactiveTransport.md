# 서지정보
Garcia-Arredondo, M., Fang, Y., Jones, M., Yabusaki, S. B., Cardon, Z., & Keiluweit, M. (2023). Resolving dynamic mineral-organic interactions in the rhizosphere by combining in-situ microsensors with plant-soil reactive transport modeling. *Soil Biology and Biochemistry, 184*, 109097. DOI: 10.1016/j.soilbio.2023.109097.

# 이 논문을 찾은 이유
root exudation을 weathering source로 바로 가정하기 전에, exudate carbon이 실제 soil mineral surface, microbes, redox 반응 사이에서 어떻게 partition되는지 고시간해상도 모델로 확인하기 위해 검토했다.

# 연구 유형
- plant-soil reactive transport model
- in-situ microsensor constrained modeling
- rhizosphere experiment

# 공간 구조
- 3D plant-soil reactive transport framework
- root-soil interface
- diel temporal resolution

# 적용 환경
- Vicia faba rhizosphere
- live soil
- Fe-oxide-rich mineral-organic system

# 핵심 과정
- root-derived DOC
- microbial respiration
- Fe reduction
- mineral surface sorption/desorption
- redox dynamics
- plant physiological forcing

# 식생 입력
- aboveground plant physiological measurements
- diel photosynthesis-linked root DOC release
- root-zone exudate dynamics

# 핵심 식
핵심 competition:

```
root DOC
 -> microbial consumption
 OR
 -> mineral adsorption
 OR
 -> redox-mediated transformations
```

모델은 관측된 daytime DOC spike 소멸이 단순 respiration보다 Fe-oxide adsorption으로 더 잘 설명됨을 보였다.

# 파라미터와 단위
- DOC release
- oxygen / redox state
- microbial reaction rates
- Fe oxide sorption
- mineral-organic equilibrium
- plant physiological diel forcing

# 원 논문의 구현 범위
root-derived organic C가 mineral surfaces 및 microbes와 어떻게 상호작용하는지 고해상도로 계산한다.

# 고운사에 직접 사용할 수 있는 부분
중요한 제약이다.

```
root exudate
!=
all available for mineral dissolution
```

exudate 일부는:
- sorption
- microbial consumption
- redox reaction
으로 소모/저장될 수 있다.

따라서 REWTCrunch-like exudation weathering을 단순 organic-acid source만으로 과대평가하지 않도록 한다.

# 새로운 coupling이 필요한 부분
LPJ-GUESS root-C flux를:
- reactive DOC
- sorbed C
- microbially consumed C
로 partition하는 것은 새 coupling이다.

# 한계
- primary focus는 soil carbon/mineral association
- silicate soil-production rate 직접 출력 아님
- crop/rhizosphere experimental scale

# 최종 판정
- **보조 채택: root-exudate availability와 mineral-organic competition 제약**
- REWTCrunch advanced sensitivity를 보정하는 근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.soilbio.2023.109097
