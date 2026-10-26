# 서지정보
Mayor, Á. G., Bautista, S., Small, E. E., Dixon, M., & Bellot, J. (2008). Measurement of the connectivity of runoff source areas as determined by vegetation pattern and topography: A tool for assessing potential water and soil losses in drylands. *Water Resources Research, 44*(10). https://doi.org/10.1029/2007WR006367

# 이 논문을 검색한 이유
빽빽한 억새군락과 드문드문 놓인 참나무 맹아에서 지표유출 연결성이 얼마나 다른지를, 단순 COVER가 아니라 정량적 경로지표로 표현하기 위해서다.

# 연구 유형
공간 분석기법 개발 및 실측 대조. 지표유출/유사량을 새 2D 유동방정식으로 계산한 모형이 아니다.

# 공간 구조
Raster vegetation patches, microtopography, source-sink runoff pathways. 6개 시험구, 3개 소유역의 runoff and sediment yield로 Flowlength 연결성지표를 검증.

# 적용 환경
스페인 남동부 반건조 산지 초본-관목 mosaics, 평균 토심 약 15 cm 이하; 고운사 산불 후 습윤 온대 억새/맹아 사면과 다른 기후, 식생, 지질.

# 핵심 과정
식생 피복률이 비슷해도 무식생 노출토양의 패치 크기/공간연결성이 달라 runoff·sediment yield가 달라짐. 가로막는 식생, 낙엽, 잔존 고사목과 미세지형 웅덩이가 runoff 연결을 끊을 수 있음. Flowlength가 증가하면 runoff·sediment yield가 증가한 사례를 보고.

# 식생 입력
Vegetation/bare interpatch map + microtopographic DEM. Root biomass and canopy TF/SF not directly implemented.

# 핵심 식과 단위
Flowlength = raster cells에서 예상 유출경로 길이의 공간평균, m (구체적 routing과 경로 정의는 원문 구현에 따름). 일반적인 Shannon patch index로 대체하면 안 됨.

# 고운사에 직접 사용할 수 있는 부분
같은 canopy- or ground-cover percentage를 적용하는 기존 원본 EUROSEM/SWEHR 단일요소 접근만으로는 dense Miscanthus vs scattered oak coppice 비교가 부적절함을 입증. UAV/TLS에서 실제 stem/tussock 및 bare-area connections를 측정하고 경계 배출량과 비교.

# 새로운 coupling
Vegetation segmentation → unprotected surface flow connectivity and 2D actual rainfall infiltration/sediment solver coupling, not original paper's existing engine.

# 한계
Flowlength는 연결성 지표이지 강우, 침투 및 유사수지를 닫는 물리 침식모형이 아니며 건조지 경향을 고운사에 무조건 전이할 수 없음.

# 최종 판정
공간배치 분석 핵심 채택. EUROSEM 단일 평균식 대체 필요성의 직접 문헌 근거.

# 참고 링크
https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2007WR006367
