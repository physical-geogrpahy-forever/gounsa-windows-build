# 서지정보
Xiao, Q., McPherson, E. G., Simpson, J. R., & Ustin, S. L. (2007). Hydrologic processes at the urban residential scale. Hydrological Processes, 21, 2174–2188. https://doi.org/10.1002/hyp.6482

# 이 논문을 찾은 이유
수관저류와 수관통과우 및 수간유하우를 포함한 강우 분배가 침투와 지표유출까지 한 수문모형에서 연결되는지 확인.

# 연구 유형
수치모델 및 현장 검증.

# 공간 구조
도시 주택 필지 내 토지피복별 공간 요소. 산지 genuine 2D shallow-water 모형 아님.

# 적용 환경
미국 LA 주거지의 수목 및 토양, 저류시설. 산지 검증 아님.

# 핵심 과정
식생 수관저류, 자유수관통과우 계수, 줄기 배수비율, 잎 배수, 증발, Green-Ampt 침투, Manning형 지표유출과 지표수심 물수지. 1시간 계산.

# 식생 입력
수관저류 용량, free-fall 및 stem-fall 계수, 수관 배수와 수목수분 수지.

# 핵심 식
논문 식 (4): dC/dt = p - f_g*p - f_s*p - d - e.
논문 식 (7): dh/dt = p + q_in - f - e - q_out.
논문 식 (8): Green-Ampt 침투능 식. 원문 도식 및 식을 직접 확인.

# 파라미터와 단위
C,h [m]; p,d,e,f,q_in,q_out [m/s]; f_g,f_s [-]; 시간 계산 간격 1 h.

# 원 논문의 구현 범위
강우 식생차단-침투-지표유출의 물수지 통합. 토사박리 및 침식 계산 없음. 공간별 stemflow 국지 침투를 산림사면에서 검증한 연구 아님.

# 고운사에 직접 사용할 수 있는 부분
3성분 수관배수에서 유출까지 모형 연계의 published precedent.

# 새로운 coupling이 필요한 부분
지형격자별 stemflow 분포, 수관적하 운동에너지 및 SWEHR 침식 연결.

# 한계
도시 연구. 산불 산림, 급경사, 침식 및 수간유하 우선유동에 대해 직접 검증하지 않음.

# 최종 판정
보조근거. 수문 연결식 선례.

# 참고 링크 / DOI
https://www.fs.usda.gov/psw/publications/mcpherson/psw_2007_mcpherson001_xiao.pdf
https://doi.org/10.1002/hyp.6482
