# 서지정보
Parhizkar, M., Shabanpour, M., Khaledian, M., & Asadi, H. (2021). The evaluation of soil detachment capacity induced by vegetal species based on the comparison between natural and planted forests. *Journal of Hydrology, 595*, 126041.

# 이 논문을 찾은 이유
자연림과 조림지, 여러 교목종의 root system 차이가 soil detachment에 미치는 효과를 확인하기 위해 검토했다.

# 연구 유형
- 현장/실험

# 공간 구조
- forest plots

# 적용 환경
- 자연림 / 조림지

# 핵심 과정
- soil detachment
- rill erodibility

# 식생 입력
- tree species별 root system

# 핵심 식
자연림과 조림지의 `D_c`, `K_r` 차이를 비교. 정확한 원식은 원문 재검증 필요.

# 파라미터와 단위
root-system attributes, rill erodibility.

# 원 논문의 구현 범위
6개 교목종 및 자연림/조림지를 비교.

# 고운사에 직접 사용할 수 있는 부분
목본 PFT 내부에서도 침식저항 차이가 존재할 수 있다는 근거.

# 새로운 coupling이 필요한 부분
LPJ-GUESS woody PFT별 erosion parameter를 만들면 새로운 coupling.

# 한계
수치모델 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.jhydrol.2021.126041
