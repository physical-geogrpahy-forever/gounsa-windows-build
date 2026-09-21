# 서지정보
Hudson Rasmussen, B. M., Huang, M.-H., Hahm, W. J., Rempe, D. M., Dralle, D., & Nelson, M. D. (2023). Mapping variations in bedrock weathering with slope aspect under a sedimentary ridge-valley system using near-surface geophysics and drilling. *Journal of Geophysical Research: Earth Surface, 128*(7). DOI: 10.1029/2023JF007254.

# 이 논문을 찾은 이유
현재 식생과 미기후가 aspect별로 달라도 sedimentary bedrock의 weathering thickness가 반드시 aspect를 따라가는지 확인하고, sandstone-like sedimentary setting의 hillslope-position control을 검토하기 위해 검색했다.

# 연구 유형
- seismic refraction
- borehole/drilling
- rock-physics interpretation
- hillslope geophysics

# 공간 구조
- sedimentary ridge-valley hillslopes
- north/south aspects
- ridge to channel profiles
- bedding-parallel/perpendicular surveys

# 적용 환경
- Rancho Venada, California
- sedimentary bedrock
- seasonal Mediterranean climate
- contrasting aspect vegetation/microclimate

# 핵심 과정
- bedrock weathering
- saprolite thickness
- inherited fractures
- porosity
- hillslope position
- aspect legacy

# 식생 입력
current vegetation/aspect contrast가 존재하지만 dynamic vegetation model은 없음.

# 핵심 결과
high seismic-velocity-gradient transition:
```
~4-13 m below ridgetops
```
에서 material strength와 chemical depletion transitions와 대응.

중요하게:
```
saprolite thickness
```
는 north/south aspect에 따라 명확히 달라지지 않았다.

반면:
```
weathering profile
= thicker upslope
-> tapers downslope toward channels
```
의 hillslope-position pattern이 나타났다.

상부 약 6 m porosity에서 inherited fractures의 기여가 컸다.

저자들은 aspect-independent present-day architecture가:
```
past climate / vegetation legacy
```
를 반영할 수 있다고 해석한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 caution.

```
current aspect / current vegetation
!= current weathering-profile thickness
```

일 수 있다.

고운사 100년 postfire simulation에서는 initial subsurface weathering architecture를 current LPJ-GUESS vegetation에서 새로 equilibrium시키면 안 된다.

필요:
```
initial inherited weathering profile
+ 100-year incremental change
```

또 ridge/midslope/toeslope position을 aspect와 별도로 봐야 한다.

# 새로운 coupling이 필요한 부분
initial C/Cr/weathered-bedrock profile을 geologic/topographic prior로 설정하고 vegetation-driven incremental weathering만 추가하는 것은 new model initialization rule이다.

# 한계
- no dynamic vegetation
- specific sedimentary structure
- bedding/fracture inheritance strong
- soil-production rate law 직접 제공 안 함

# 최종 판정
- **채택: sedimentary hillslope-position weathering + legacy constraint**
- 100-year 모델 초기조건 설계에 핵심
- aspect multiplier 금지 강화

# 참고 링크 / DOI
https://doi.org/10.1029/2023JF007254
