# LPJ-GUESS weathered-bedrock hydrology

## 핵심 논문
Lapides, D. A., Hahm, W. J., Forrest, M., Rempe, D. M., Hickler, T., & Dralle, D. N. (2024). Inclusion of bedrock vadose zone in dynamic global vegetation models is key for simulating vegetation structure and function. *Biogeosciences, 21*, 1801–1826. https://doi.org/10.5194/bg-21-1801-2024

## 고운사에서 검토한 이유
고운사 현장에서 뿌리가 A+B 토양층보다 깊은 C/Cr까지 들어가는 관찰을 LPJ-GUESS 수문구조에 반영할 수 있는지 확인하기 위해 검토했다.

## 원 모델 구조
- LPJ-GUESS 4.0.1 기반
- 각 grid cell은 1-D column
- 상부 soil storage와 하부 weathered-bedrock storage를 분리
- PFT별 root distribution으로 두 저장고에서 물을 흡수

## 핵심 변화
기본 LPJ-GUESS의 고정 깊이 두 층 대신 상부는 soil water-storage capacity, 하부는 rock-moisture storage capacity로 정의한다.

## 고운사 채택 방향
고운사에서는 최소한 다음을 분리한다.
```text
W_AB = mobile upper-soil water
W_C  = C/Cr weathered-substrate water
```

그리고
```text
root-accessible depth >= H_AB
```
를 허용한다.

## 새로운 coupling
- H_AB와 H_C가 지형변화에 따라 바뀌면 LPJ-GUESS의 storage capacity도 갱신
- coarse fraction에 따른 effective storage와 infiltration 수정
- 셀 간 same-day run-on을 LPJ-GUESS column에 외부입력으로 전달
- weathering front와 LPJ-GUESS hydrology 연결

위 기능은 Lapides et al. 원 논문에 그대로 구현된 기능이 아니며 새로운 coupling이다.

## 한계
- 원 모델은 weathered-bedrock moisture를 다루지만 풍화전선 자체를 동적으로 움직이지 않음
- coarse fraction과 pedogenesis를 동적으로 생성하지 않음
- lateral flow는 LPJ-GUESS column 내부 기능이 아님

## 최종 판정
- C/Cr 수분저장과 뿌리접근 구조: 채택 근거
- 동적 지형과의 결합: 새로운 coupling
