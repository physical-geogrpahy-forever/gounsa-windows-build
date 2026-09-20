# 서지정보
Park, M. (2026). *Analysis of Topographic, Structural, and Vegetation Factors Influencing Snow-Induced Uprooting of Pinus densiflora for. erecta*. Ecology and Resilient Infrastructure, 13(1), 1-9. DOI: 10.17820/eri.2026.13.1.001.

# 이 논문을 찾은 이유
한국 소나무류에서 DBH, slope, edge effect 같은 실제 구조/지형변수가 전도 취약성과 어떻게 연결되는지 지역 제약자료를 확보하기 위해 검토했다.

# 연구 유형
- UAV post-event mapping
- multivariate factor analysis
- susceptibility analysis

# 적용 환경
- Pinus densiflora for. erecta
- heavy-snow disturbance
- Korea

# 자료
UAV orthomosaic에서:
```
2,031 uprooted trees
```
의 위치와 DBH 등을 판독했다.

FAMD를 이용해 topographic, structural, vegetation factors를 통합 분석했다.

# 핵심 결과
가장 강한 전도 취약성 관련요인은:
```
slope gradient
```
였다.

또한:
- DBH
- forest-edge distance
- aspect
- surrounding vegetation structure

가 복합적으로 공간 패턴을 만들었다.

특히 활엽수림 경계 주변의 대경목 금강소나무가 폭설 조건에서 높은 전도 취약성을 보였다.

# 고운사에 직접 사용할 수 있는 부분
한국 pine system에서:

```
uprooting probability
!= DBH-only
```

이며:
```
DBH + slope + edge/exposure + disturbance load
```
를 함께 고려해야 함을 보여준다.

이는 ForestGALES의 stand/exposure structure와 잘 맞는 지역 검증근거다.

# 중요한 제한
이 연구는 event 후 **전도된 개체를 분석한 susceptibility study**이며, mechanistic annual uprooting-probability model이 아니다.

따라서 FAMD loading을 그대로 annual probability로 쓰지 않는다.

# 새로운 coupling
snow loading을 production Gounsa model에 넣는 경우:
- snow load
- wind pressure
- edge/exposure
- LPJ-GUESS cohort state
를 기계적 stability model에 결합해야 하며 이는 새로운 coupling이다.

# 최종 판정
**보조 지역근거.**

Live-tree event probability 자체는 ForestGALES/fgr 같은 mechanistic model을 우선하고, 이 논문은 한국 slope/edge/DBH vulnerability를 검증하는 데 사용한다.

# 참고 링크 / DOI
https://doi.org/10.17820/eri.2026.13.1.001
