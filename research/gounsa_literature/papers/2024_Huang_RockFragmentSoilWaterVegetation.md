# 서지정보
Huang, L., Bao, W., Hu, H., & Li, F. (2024). Rock fragment content mediates the plant effect on soil water content in the arid valley of southwest China. *CATENA, 246*, 108414. https://doi.org/10.1016/j.catena.2024.108414

# 이 논문을 찾은 이유
`석력비율 -> soil moisture -> species/PFT performance` 연결이 실제 식생 연구에서 확인되는지 검토하기 위해 찾았다.

# 연구 유형
- 식생-토양수분 실험/관측

# 공간 구조
- soil profile, 10-50 cm 중심
- species treatments

# 적용 환경
- arid valley
- stony soil
- native plant species

# 핵심 과정
- soil-water storage
- rock-fragment content
- rooting traits
- species-dependent soil-water response

# 식생 입력
- four native species
- plant functional/root traits

# 핵심 식
rock-fragment content 0-75% 조건에서 soil water content와 relative soil-water deficit을 비교했다.
증가한 RFC는 대부분 식생처리에서 10-50 cm soil water content를 감소시켰으며, 영향은 종과 root distribution/architecture에 따라 달랐다.

# 파라미터와 단위
- RFC: 0-75% v/v
- soil-water content
- relative soil-water deficit
- root/plant traits

# 원 논문의 구현 범위
rock-fragment content와 식생이 독립적으로가 아니라 상호작용하여 soil-water profile을 결정한다.

# 고운사에 직접 사용할 수 있는 부분
- `coarse-fragment content -> soil-water state -> PFT/species filtering` 경로의 직접 근거
- 모든 하층식생에 동일 soil-moisture response를 적용하지 않을 근거

# 새로운 coupling이 필요한 부분
고운사 LPJ-GUESS PFT parameter에 RFC-sensitive soil-water stress를 추가하는 것은 **새로운 coupling**이다.

# 한계
건조계곡 식생이며 산불 후 한국 온대림에 직접 계수를 이식할 수 없다.

# 최종 판정
- 핵심 보조근거
- fragment-soil moisture-vegetation bridge

# 참고 링크 / DOI
https://doi.org/10.1016/j.catena.2024.108414
