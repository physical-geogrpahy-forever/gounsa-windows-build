# 서지정보
Wei, L.-z., & Kinouchi, T. (2014). Improvement of CASC2D model for rainfall-runoff simulations in a forested catchment. *Journal of Japan Society of Civil Engineers, Ser. B1 (Hydraulic Engineering), 70*(4), I_157–I_162. https://doi.org/10.2208/jscejhe.70.I_157

# 이 논문을 검색한 이유
TREX/CASC2D 계열의 LAI 기반 수관저류 개선이 실제 published native 연구인지, 이 변형이 고운사 5–10cm 수관차단+2D 유수침식 통합 모델로 사용 가능한지 분리 검토.

# 연구 유형
수치모델 개발 및 산림유역 강우유출 모의. 지표유출 및 유사모형 CASC2D에서 산림 수문현상을 표현하기 위해 개량.

# 공간 구조
CASC2D의 분포형 2D surface routing 계열. 수리학적으로 full SWE가 아니라 기존 CASC2D 2D diffusion-wave 계열. 이 연구에서 5–10cm 격자 실제 실행 근거 없음.

# 적용 환경
일본 후쿠시마현 Kuchibuto River 산림유역. 2011년 강우사상 4개 보정, 2012년 7개 검증.

# 핵심 과정
수관차단 및 침투 개선, 증발산, 지하수 저장, 토양수 횡류와 유출 모의. 논문 초록의 검증 결과는 강우유출 hydrograph에 관한 것이며 같은 실행판의 격자별 유사 박리, 이송, 퇴적까지 정량 검증했다고 읽어서는 안 됨.

# 식생 입력
LAI 연동 수관최대저류량 개선식 제시. 원본 CSU TREX archived C 구현과 이 2014년 산림 개량판은 동일 바이너리 또는 소스코드라고 입증되지 않음.

# 핵심 식
최대 수관저류량의 회귀식(기존 문헌의 이식):
`S_max [mm] = 0.935 + 0.498 LAI - 0.00575 LAI^2`.
LAI 무차원. 이 식의 원출처와 매개변수 적용 범위를 논문 본문에서 재확인할 필요 있음.

# 파라미터와 단위
S_max [mm], LAI [-]. 침식계수, 입경별 퇴적계수 및 5–10cm 격자에서 필요한 안정도 한계는 이 논문의 검증정보로 확인되지 않음.

# 원 논문의 구현 범위
CASC2D 산림 연속 수문에 관한 개량은 확인되나, 공개 소스 패키지, 해당 개량판 원본 체크섬, 수관차단+강우 박리+2D 유사퇴적의 동일 사상 계산, 초고해상도 현장 검증은 확인 못 함.

# 고운사에 직접 사용할 수 있는 부분
LAI 연동 canopy storage의 문헌상 대안이라는 학술 참고근거. 고운사 주모델 원본으로는 미채택.

# 새로운 coupling이 필요한 부분
산림 개량판의 원래 유사수송 코드가 동일 실행파일에 연결되어 있는지 미확인. 다른 공개 TREX 소스에 수관차단식을 새로 이식하는 것은 본 프로젝트의 요구인 원본 단일모델 검증을 충족하지 않으며 새로운 coupling이므로 선택지로 권고하지 않음.

# 한계
(1) 현장유출 검증 위주, (2) 5–10cm 실제 계산 사례 없음, (3) 동일 공개 실행원본 코드 미확보, (4) 격자별 침식/퇴적와 유사수지 검증 없음, (5) 원래 코드와 수정판 차이를 버전/해시로 추적 불가.

# 최종 판정
**보조근거.** 산림 LAI 수관차단의 실제 모델 연구임은 확인하되 사용자 필수조건의 5–10cm 공개 단일 유수침식 원본으로 채택 불가.

# 참고 링크 / DOI
- DOI: https://doi.org/10.2208/jscejhe.70.I_157
- J-STAGE 원문: https://www.jstage.jst.go.jp/article/jscejhe/70/4/70_27/_article/-char/en
- 후속 산림유역 침식 연구: https://www.sciencedirect.com/science/article/abs/pii/S157064431630065X
- 공개 고전 TREX C 소스 별도: https://github.com/WatershedModels/trex_src_csu
- 관련 기존 정리: ../papers/2008_Velleux_England_Julien_TREX_2D.md
