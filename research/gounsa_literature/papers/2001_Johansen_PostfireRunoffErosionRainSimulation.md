# 서지정보
Johansen, M. P., Hakonson, T. E., & Breshears, D. D. (2001). Post-fire runoff and erosion from rainfall simulation: Contrasting forests with shrublands and grasslands. *Hydrological Processes, 15*(15), 2953–2965. https://doi.org/10.1002/hyp.384

# 이 논문을 찾은 이유
산불 사면의 10–50 mm/h 강우 민감도 결과가 어느 범위에서 가능한지, 수치모형이 아닌 현장 관측으로 비교할 기준 확보.

# 연구 유형
인공강우 현장실험. 수치모델 아님.

# 공간 구조
산불 전후 대비용 국지 사면 시험구. genuine 2D 계산 해당 없음.

# 적용 환경
New Mexico Cerro Grande 대형 산불 이후 ponderosa pine 산림의 중증 소실 토양; shrubland/grassland 비교. 고운사 사암사면의 직접 관측자료는 아님.

# 핵심 과정
60 mm/h 인공강우 3회(2일간), 총 120 mm 강우 동안 runoff와 sediment yield 측정. 연소지 유출률 약 45%, 비연소지 23%. 연소지 토사 76 kg ha^-1 mm-rain^-1, 비연소지 3 kg ha^-1 mm-rain^-1; 약 25배 차이. 강우강도가 60mm/h인 연구의 현장조건에서 얻은 값이며 10~50 mm/h 보편 함수가 아님.

# 식생 입력
연소 표면의 노출 광물토 피율 74%, 비연소지 약 3%. 재와 토양노출의 영향 측정. root biomass numerical coupling 없음.

# 핵심 식
모델이 아니라 비교 관측. 단위 환산: 76 kg ha^-1 mm^-1 = 0.076 t ha^-1 per mm of rainfall. 동일 조건 120 mm에 비례 환산하면 약 9.12 t/ha이지만 10–50 mm/h로 직접 선형 외삽 불가.

# 파라미터와 단위
강우 60 mm/h; 토양유실률 kg ha^-1 mm^-1; 단일 사건 vs 여러 반복 사건 구분.

# 원 논문의 구현 범위
산불 전후의 유출 및 토사유출량 실측; hydrological/erosion engine 없음.

# 고운사에 직접 사용할 수 있는 부분
단시간 강우에서 수 t/ha 수준 침식량 가능함을 보여주는 현장 비교. 고운사 해당 수치 채택 불가.

# 새로운 coupling이 필요한 부분
고운사 수관차단/수간유하/침투/2D 침식 원본 모델과 직접 연결되지 않음.

# 한계
다른 식생, 다른 지질, 인공강우 60 mm/h, 반복 120 mm 총량. 조건과 스케일이 다름.

# 최종 판정
현장 대조 기준 채택(값 외삽 금지).

# 참고 링크 / DOI
https://doi.org/10.1002/hyp.384
https://experts.arizona.edu/en/publications/post-fire-runoff-and-erosion-from-rainfall-simulation-contrasting/
