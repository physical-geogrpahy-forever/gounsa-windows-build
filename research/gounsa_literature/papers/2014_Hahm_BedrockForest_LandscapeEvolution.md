# 서지정보
Hahm, W. J., Riebe, C. S., Lukens, C. E., & Araki, S. (2014). Bedrock composition regulates mountain ecosystems and landscape evolution. *Proceedings of the National Academy of Sciences, 111*(9), 3338-3343. DOI: 10.1073/pnas.1315667111.

# 이 논문을 찾은 이유
식생 -> 풍화/지형 feedback뿐 아니라 반대방향인:
```
bedrock chemistry -> vegetation -> erosion/weathering
```
을 산지에서 정량적으로 확인한 연구를 찾기 위해 검토했다.

# 연구 유형
- mountain field study
- bedrock geochemistry
- remotely sensed canopy/productivity
- erosion-rate comparison

# 공간 구조
- Sierra Nevada mountain terrain
- multiple plutons
- adjacent forested and barren/soil-poor hillslopes

# 적용 환경
- granitic Sierra Nevada Batholith
- climate range를 좁게 유지한 lithologic contrast

# 핵심 과정
- bedrock nutrient composition
- forest productivity
- soil mantle presence
- erosion rate
- landscape evolution

# 식생 입력
- tree-canopy cover as forest-productivity proxy

# 핵심 결과

Tree-canopy cover는 site 간 1 order of magnitude 이상 달랐고 mapped pluton contacts와 급격히 변했다.

Bedrock의 plant-essential elements, 특히 P concentration과 vegetation productivity가 연결되었다.

Nutrient-poor, nearly vegetation-free areas:
```
erosion rate
<
surrounding nutrient-rich, soil-mantled forest areas
```

평균적으로 2배 이상 느린 차이가 보고되었다.

따라서:
```
bedrock chemistry
 -> nutrient supply / productivity
 -> soil and vegetation cover
 -> erosion / landscape evolution
```
의 bottom-up feedback이 존재한다.

# 파라미터와 단위
- bedrock elemental concentration
- P concentration
- canopy cover [%]
- cosmogenic erosion rate

# 원 논문의 구현 범위
field evidence이며 dynamic coupled model은 아니다.

# 고운사에 직접 사용할 수 있는 부분
중요한 feedback 방향:

```
weathering/mineralogy
 -> nutrient release
 -> LPJ-GUESS-CNP productivity
 -> vegetation
 -> geomorphic processes
```

을 강하게 지지한다.

즉 W_chem에서 나온 nutrient release를 LPJ-GUESS-CNP로 되돌리는 current new coupling의 생태지형적 타당성을 높인다.

또 고운사 sandstone petrography/mineralogy가:
- weathering kinetics
뿐 아니라
- vegetation recovery
에도 직접 영향을 줄 수 있음을 의미한다.

# 새로운 coupling이 필요한 부분
```
sandstone mineral weathering
 -> nutrient release
 -> LPJ-GUESS-CNP
```
mass-conserved mapping은 새로운 coupling이다.

# 한계
- granite/plutonic lithology
- field association
- fire recovery를 직접 다루지 않음
- canopy cover를 LPJ-GUESS state와 직접 동일시할 수 없음

# 최종 판정
- **채택: lithology -> vegetation -> hillslope evolution feedback의 핵심 field evidence**
- nutrient-return feedback을 유지할 강한 근거
- coefficient direct transfer 금지

# 참고 링크 / DOI
https://doi.org/10.1073/pnas.1315667111
