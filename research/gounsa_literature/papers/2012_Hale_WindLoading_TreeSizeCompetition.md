# 서지정보
Hale, S. E., Gardiner, B. A., Wellpott, A., Nicoll, B. C., & Achim, A. (2012). *Wind loading of trees: influence of tree size and competition*. European Journal of Forest Research, 131, 203-217. DOI: 10.1007/s10342-010-0448-2.

# 이 논문을 찾은 이유
LPJ-GUESS가 계산하는 개체 또는 cohort 수준의 DBH, 수고, 경쟁상태를 실제 windthrow risk로 전달할 수 있는 mechanistic individual-tree 선례를 확인하기 위해 검토했다.

# 연구 유형
- field wind-loading measurements
- mechanistic model development
- ForestGALES individual-tree lineage

# 핵심 과정
- individual-tree wind loading
- turning moment coefficient
- tree size
- local competition/sheltering
- critical wind loading

# 식생 입력
- DBH
- tree height
- crown/competition indices
- local stand structure

# 핵심 결과
기존 stand-average ForestGALES를 individual-tree risk 쪽으로 확장하기 위한 turning-moment-coefficient 접근을 개발했다.

Tree size와 competition은 wind loading을 크게 바꾸며, 개별 나무의 critical wind speed를 계산할 수 있는 구조를 제공한다.

# 고운사에 직접 사용할 수 있는 부분
LPJ-GUESS woody cohort가 다음을 제공할 경우:

```
DBH
height
density/spacing
competition proxy
```

ForestGALES/fgr individual-tree method에 가까운 상태변수 연결이 가능하다.

# 새로운 coupling
LPJ-GUESS cohort average state를 ForestGALES individual-tree inputs로 변환하는 것은 새로운 coupling이다.

특히 cohort 내부 DBH 분산을 무시하면 큰 나무의 전도위험을 과소평가할 수 있으므로 representative-tree 또는 size-bin 처리가 필요하다.

# 한계
- 주로 영국 침엽수림 계보
- 뿌리 anchorage parameterization은 별도 ForestGALES 계보에 의존
- 산불 고사목 root decay를 다루지 않음
- snow loading이 고운사에서 필요할 경우 별도 검토 필요

# 최종 판정
**채택: live-tree individual wind-loading architecture의 핵심 선례.**

# 참고 링크 / DOI
https://doi.org/10.1007/s10342-010-0448-2
