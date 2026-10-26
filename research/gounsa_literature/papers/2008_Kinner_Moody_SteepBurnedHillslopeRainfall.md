# 서지정보
Kinner, D. A., & Moody, J. A. (2008). *Infiltration and runoff measurements on steep burned hillslopes using a rainfall simulator with variable rain intensities*. U.S. Geological Survey Scientific Investigations Report 2007-5211. https://doi.org/10.3133/sir20075211

# 이 논문을 찾은 이유
10,20,30,40,50 mm/h 실험에서 유출을 발생시키는 강우 역치와 침투능이 원본 모형에 어떻게 반영되어야 하는가 비교.

# 연구 유형
실측 인공강우 및 수문 관측. 수치모델 아님.

# 공간 구조
1 m² 시험구, 30~40% 경사의 산불 사면 4곳에서 14차례 실험.

# 적용 환경
미국 Colorado Overland Fire, 화산재 두께가 다양한 산불사면. 고운사와 토양/기반암 다름.

# 핵심 과정
약 20, 35, 50 mm/h 세 강우강도에서 지표유출, 침투, 부유사 농도, 재층 두께 관측. 50 mm/h에서 준정상 침투량 약 20~35 mm/h; 유출 개시 강우강도 약 20 mm/h 근처라는 보고(지점별 차이 존재).

# 식생 입력
산불 잔재/재층과 노출토 조건, canopy/stemflow 직접 모델 미포함.

# 핵심 식
현장 자료의 준정상 유출에 대한 비교. 시간별 soil erosion 모형식은 본문에서 구현하지 않음.

# 파라미터와 단위
강우/침투: mm/h, 유출: mm 또는 유량, 토사: 농도(원문 측정). 14회 3강도.

# 원 논문의 구현 범위
실측 침투/유출 역치 검증. 10-50 mm/h 결과를 모든 토양에 보편 적용하지 말 것.

# 고운사에 직접 사용할 수 있는 부분
침투능 분포와 초기 토양수분을 바꿔야 한다는 현장 근거. SWEHR Ks=0 예제의 부적합성 대조.

# 새로운 coupling이 필요한 부분
수간유하우 줄기 국지 유입 및 2D 침식 반응.

# 한계
시험구 1m² 소규모, 20~50 mm/h 연구이고 수간유하와 뿌리 효과는 미분리.

# 최종 판정
수문 민감도 실측 비교 근거.

# 참고 링크 / DOI
https://doi.org/10.3133/sir20075211
https://pubs.usgs.gov/publication/sir20075211
