# 서지정보
Cuomo, S. (2018). Modelling of rainfall-induced runoff and superficial erosion in unsaturated air-fall soil deposits. *Rivista Italiana di Geotecnica*, 2018(3), 31–43. https://doi.org/10.19199/2018.3.0557-1405.31
원문: https://associazionegeotecnica.it/wp-content/uploads/2018/11/RIG_3_2018_031_CUOMO-1.pdf

# 이 논문을 검색한 이유
고운사 필수 5–10cm 실제 계산격자, 식생 LAI 수관차단, 강우유출/침식 동일 원본 연구가 Maggioli et al.(2022) 외에도 존재하는지 추가 탐색.

# 연구 유형
기존 LISEM 물리모델의 강우모사 실험 재현과 이탈리아 여러 소유역 적용. 모델의 신규 공개 구현/버전 연구가 아닌 활용 및 실험 비교 연구.

# 공간 구조
실험사면 LISEM 계산격자는 **0.1m**로 명시, 계산시간간격은 cell size의 0.2배 규칙으로 **0.02s**. 소유역 계산은 5m/5s. 본문에서 0.1m 시험의 수리해법이 자유로운 2D X/Y full SWE였다는 확인 근거 없음. 이전 classic LISEM kinematic 해법과 구분 필요.

# 적용 환경
사면 나지 0% 및 초본 35% 피복 강우모사 결과를 LISEM으로 역모의. 원 관측은 Pan & Shangguan (2006) 실험 자료. 이탈리아 남부 화산쇄설성 토양 유역 확장 모의는 **5m 계산격자**이므로 cm급 산지 현장 검증으로 표현 금지.

# 핵심 과정
Green–Ampt 침투 및 강우유출, 강우충격과 유수에 의한 침식, 유사농도/유사유출량 계산. 총유출량·최대유량·유사농도 관측과 비교. 10cm 격자별 국지 퇴적고 실측 DoD 검증은 원문에서 확인 안 됨.

# 식생 입력
35% 피복 실험 입력에 LAI **6**, 식생 높이 0.07m, 뿌리로 인한 추가 점착력 **3.32kPa**. 논문 §4.2에서 LISEM clumped grasses용 LAI 연동 최대 수관저류 식을 사용했다고 명시. 식생 입력값은 문헌에서 선정한 모형 입력이며 현장 식생의 실측 LAI로 과장해서는 안 됨.

# 핵심 식
논문 §3에서 canopy maximum storage (clumped grasses) uses LAI. 개별 식과 단위는 원문 표·문단에서 확인해야 하며 여기서 Maggioli의식을 함부로 동일시하지 않음.

# 파라미터와 단위
격자 dx=0.1m, 시간간격 dt=0.02s(문장에 기재된 0.2 × dx 규칙에 따른 산술값), LAI=6 [-], cover=35% (실험 조건), vegetation height=0.07m, root-related cohesion addition=3.32kPa, RR=0.05cm. 소유역은 dx=5m, dt=5s. Table I 참조.

# 원 논문의 구현 범위
유출·유사량 피크의 자료 비교 포함. 최고시간(peak timing)의 모의 정확도는 상대적으로 낮다는 한계를 저자가 명시. 버전·실행원본 SHA나 공개된 재현용 input package 확인 못 함. LISEM 논문의 기능과 고운사 OpenLISEM 7.5.2 정량수지 안정성을 동등시 금지.

# 고운사에 직접 사용할 수 있는 부분
**10cm LAI 수관저류 + 강우 침식 실험모의가 실제 발표되었다는 추가 선행연구 근거.** classic LISEM 모델 신뢰도 평가에서 Maggioli2022와 독립적인 실험 근거.

# 새로운 coupling이 필요한 부분
수관차단 활성 0.1m 실험과 freely spreading genuine 2D 동수력학, 실제 국지퇴적 DoD, 안정된 유사수지를 같은 공개 실행코드에서 입증해야 함. 이 논문만으로 충족되는 사항이 아님.

# 한계
(1) 동일 배포 공개 원본 코드 버전 불명, (2) 0.1m 계산격자의 2D 자유유동 모듈 확인 불가, (3) 입력/출력 공개 재현자료 미확인, (4) 국지퇴적 격자검증 없음, (5) 기존 LISEM 7.5.2 수치 비수렴 사례를 무효화하지 않음.

# 최종 판정
**보조근거 (10cm + LAI 수관차단 + 침식 실증) / 주모델 보류.**
저자 논문은 조건 일부를 만족하지만 전체를 충족하는 다운로드 가능 단일 공개 원본 실행판은 여전히 미확인.

# 참고 링크 / DOI
https://doi.org/10.19199/2018.3.0557-1405.31
https://associazionegeotecnica.it/wp-content/uploads/2018/11/RIG_3_2018_031_CUOMO-1.pdf
