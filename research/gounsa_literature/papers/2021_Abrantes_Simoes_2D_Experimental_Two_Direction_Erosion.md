# 서지정보
Abrantes, J. R. C. B., Simões, N. E., de Lima, J. L. M. P., & Montenegro, A. A. A. (2021). Two-dimensional (2D) numerical modelling of rainfall induced overland flow, infiltration and soil erosion: Comparison with laboratory rainfall-runoff simulations on a two-directional slope soil flume. *Journal of Hydrology and Hydromechanics, 69*(2), 140–150. https://doi.org/10.2478/johh-2021-0003

# 이 논문을 검색한 이유
OpenLISEM 계열 제외, **실제로 자유 X/Y 방향 강우유출+세류 및 세류간 침식+퇴적을 계산하고 두 방향 출구에서 검증**한 문헌의 재현 가능성 확인. 기존 INDEX 473편에 동일 DOI 없음 검증.

# 연구 유형
동료심사 수치모델 개발과 강우모사 실험실 검증. 본 세션 직접 확인 범위는 학술지 공식 본문 정보, DOI 및 공개 초록과 서지정보. 출판사 PDF 주소는 확인했지만 PDF 원문 전체 열람은 콘텐츠 형식 제약으로 완료하지 못함. 원문 모든 식과 계수를 읽었다고 주장하지 않음.

# 공간구조
2D unsteady overland flow equations, 2D sediment transport, spatial infiltration. **유출과 유사량을 X 및 Y 양방향에서 측정하는 설계**. 제목의 '2D'가 단순한 지형도 표시가 아니라 두 방향 보존방정식임을 초록이 명시. 다만 'full SWE'인지 특별한 diffusion-wave 근사인지 원문 전체 수식으로 마지막 판정이 필요함.

# 적용환경과 실험 방법
가로 2.00m 세로 2.00m 실내 사면 모형. X축 1% 및 Y축 10%로 경사 차이를 설정하고 강우를 모사. 실험에서 방향별 유출량 및 유사 이동량 관측을 numerical prediction과 비교. X방향의 관측 유출과 sediment load는 Y에 비해 작으며 수치모델은 특히 작은 X방향의 유출과 유사량을 과소추정. Y방향 결과 및 X+Y 합산 hydrograph/sedigraph는 비교적 우수하다고 보고.

# 핵심 과정
(1) 2D 비정상 지표유동 보존방정식; (2) Horton-SCS 침투; (3) 2D 유사수송 보존방정식; (4) 세류 및 세류간 침식 분리; (5) 퇴적. 모델 성능평가는 독립 지형고도 DoD 측정이 아니라 실험실 유출/유사 hydrograph와 관측비교.

# 식생 입력
초록 및 모델 설명에서 **LAI, 수관저류, 수관통과우, 식생 수관적하 운동에너지 과정이 확인되지 않음**. 실험은 식생혼합 산림사면이 아닌 soil flume. 뿌리/피복 등 외부계수를 canopy interception equation으로 동일시하지 않음.

# 핵심 식 및 파라미터와 단위
2D unsteady flow and sediment continuity with interrill and rill source and sediment deposition, Horton-SCS infiltration. 정확 friction formulation, numerical grid Δx/Δy [m], dt [s], splash KE and detachment constants are **full paper mathematical body inspection outstanding**. 2m 물리사면 크기를 2cm 계산격자라고 혼동 금지. **5~10cm 실제 계산격자라고 주장할 수 없음**.

# 코드 및 입력 공개 검증
출판사 초록에 exact public Git SHA / repository / downloadable complete source or reproducibility archive not listed. GitHub repository keyword search `Abrantes erosion 2D`, `Abrantes Simoes erosion`, DOI `johh-2021-0003` found no matching author solver. 이는 비공개임을 절대 증명하는 것이 아니라 이 조사에서 다운로드 가능한 원본을 확보하지 못했음을 뜻함.

# 고운사에 사용할 수 있는 부분
진정한 두 방향으로 유수침식/퇴적 flux를 계산해야 한다는 요구를 실험실 수문 및 유사 관측으로 검증한 실제 전례. 경사가 서로 다른 X/Y 방향에서 오차 비대칭성이 발생한다는 연구결과를 4면 개방경계 검증설계 근거로 활용 가능.

# 필요한 새로운 coupling
Canopy LAI/interception/leaf drip added manually = **새로운 coupling**, user does not want this presented as original same-model code. Currently cannot recommend as exact available main model.

# 한계 및 최종 판정
**보조근거.** Both-axis sediment model verified in published 2×2m soil flume; quantitative canopy missing; 5/10cm actual computational grid not established; publicly reproducible original full source not found. 원문 전체 본문 검증은 PDF 원문 파일 접근 성공시 재개.

# 참고
https://doi.org/10.2478/johh-2021-0003
https://reference-global.com/article/10.2478/johh-2021-0003?tab=abstract
https://sciendo.com/2/v2/download/article/10.2478/johh-2021-0003.pdf
