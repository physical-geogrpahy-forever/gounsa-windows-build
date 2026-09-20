# 서지정보
Parhizkar, M., Shabanpour, M., Miralles, I., Cerdà, A., Tanaka, N., Asadi, H., Lucas-Borja, M. E., & Zema, D. A. (2021). Evaluating the effects of forest tree species on rill detachment capacity in a semi-arid environment. *Ecological Engineering, 161*, 106158.

# 이 논문을 찾은 이유
교목종별 root system 차이가 rill detachment capacity, rill erodibility, critical shear stress를 어떻게 바꾸는지 확인하기 위해 검토했다.

# 연구 유형
- 현장/실험

# 공간 구조
- plot

# 적용 환경
- 반건조 산림

# 핵심 과정
- rill detachment

# 식생 입력
- tree species별 root system biomass 및 토양응집체 특성

# 핵심 식
종별 `D_c`, `K_r`, critical shear stress 차이를 비교. 원식 세부는 원문 재검증 필요.

# 파라미터와 단위
rill erodibility, critical shear, root system attributes.

# 원 논문의 구현 범위
4개 교목종의 토양 침식저항 차이를 비교.

# 고운사에 직접 사용할 수 있는 부분
woody PFT를 하나의 universal root coefficient로 묶지 않을 근거.

# 새로운 coupling이 필요한 부분
PFT별 root properties를 `K_r`, critical shear에 연결하면 새로운 coupling.

# 한계
수치 지형모델 아님.

# 최종 판정
- 보조근거

# 참고 링크 / DOI
https://doi.org/10.1016/j.ecoleng.2021.106158
