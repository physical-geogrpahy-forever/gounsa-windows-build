# LPJ-GUESS weathering coupling lineage

## 관련 논문
- Oeser et al. (2020), 기존 저장 파일 참고
- Taylor et al. (2012), DGVM weathering 비교선례
- 2025 LPJ-GUESS phosphorus-cycle implementation: 정확한 서지정보는 현재 채팅에서 미복구
- Yang et al. (2026), LPJ-GUESS-CSLE 계열은 erosion 연결로 별도 저장

## 현재 채팅에서 확인한 weathering 구조
2025 LPJ-GUESS P-cycle 구현에서 patch prognostic runoff q가 weathering flux 계산에 들어가는 식을 확인했다.

F_PW = F_CW,i * F_T * F_s,i
F_CW,i = (b_carbonate + b_silicate)_i * p_i * q

정확한 저자, 제목, DOI는 원문 재검증 필요.

## 고운사에서의 역할
외부 climate proxy만 쓰기보다 LPJ-GUESS 내부 runoff, temperature, root-depth/NPP를 weathering module에 쓰는 방향의 계보상 근거.

## 한계
P weathering과 geomorphic regolith production은 동일하지 않다.

## 새로운 coupling
LPJ-GUESS weathering flux를 R->C 또는 C/Cr thickness production으로 변환하는 것은 **새로운 coupling**이다.

## 판정
보류. 정확한 2025 원문 재검증 필요.
