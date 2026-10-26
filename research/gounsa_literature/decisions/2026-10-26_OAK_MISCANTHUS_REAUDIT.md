# 2026-10-26 억새와 참나무 맹아 생태수문 재검증

## 핵심 판정
가상 식생구조, 계절, 생육단계에 따라 두 식생의 유출 순위가 반전되므로 기존 일괄적인 억새 우세 주장은 기각한다. 실제 고운사 현장 침식량 우열은 미결이다.

## 원본 모형 단위 오류 정정
EUROSEM 1998 원본 가이드는 PLANTH 입력단위를 cm로 정의한다. 기존 가상 실험은 2.5m를 수치 2.5로 입력하여 실제 2.5cm로 작동했고 억새1.2m도 실제 1.2cm였다. 이후 원본 유효강우/침식 에너지 결과에서 식생 높이의 실제 효과를 논할 수 없다. PLANGLE은 줄기와 지표 사이 각도, PBASE는 기부면적 관련 비율, SHAPE1은 풀잎형, 2는 넓은 잎형이다. PLANTH는 하층식생과 낙엽의 최저 차단면을 고려한 유효 낙하높이여야 한다.

## 생태 관측과 확정 한계
1998 이헌호·박재철: 상수리 성숙림 장기간 누적 SF 3.8%, TF76.9%; Zuo et al. 2026 굴참나무 성숙림 SF 2.25%; Bahmani et al. 2012 다른 참나무종 SF0.4%; 고운사 어린 맹아의 단일 사건 값이 아니다.
Holder et al. 2018 다른 억새계열 M.×giganteus 강우776mm 중 수간유하133mm(17.1%); 고운사 M.sinensis의 1시간 값이 아니다.
Gregory et al. 2018 M.sinensis 6년차 시험포 0–10cm 포기내 뿌리밀도 15.5±3.1kg/m³, 포기사이 2.2±0.4kg/m³; 고운사 산불 후 1–2년생 표준값이 아니다.
Waggy 2011: 억새는 산불 후 지하경에서 회복. Kim et al. 2020: 참나무는 기존 그루터기와 뿌리에서 맹아발생. Jo & Oh 2026: 고운사 등 2025년 경북 산불 현장피해 연구이나 동일 조사구 관측이라고 주장 금지.

## 원본시험 상태
원본 EUROSEM은 TF/적하우/SF 분리 후 사면 계산에서 균일 유효강우로 합산하므로 줄기기부 집중 침식을 검증 불가. SWEHR는 초기조건/경계조건 복구후 물수지와 독립 유사수지를 통과했지만 원본 줄기별 SF 공급이 없다.
기존 110회 원본모형 실험은 시험 매개변수의 민감도일 뿐 실제 식생 피해 복원에 적용한 연구결과가 아니다. 새로운 6개 계절상태×5 강우강도×2 엔진 60회 가상 시나리오는 각 모형에서 토양을 동일하게 둬 생육단계 영향을 분리한다.

## 재현 자료
원본 및 수정 소스: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/swehr-water-sediment-closure-20261026/experiments/rainfall_10_50
첫 생육단계 실행: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40260566970
PLANTH cm 수정 재실행: https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40261338013
원본 가이드: https://dcs.ufla.br/images/imagens_dcs/pdf/Prof%20Marx/Aula%205/Art%20estudo/Morgan%20et%20al_%201998_EUROSEM_MANUAL.pdf

## 다음 필수 단계
현장 참나무 맹아와 억새 줄기수 및 줄기각, 수관의 높이와 낙엽층, 포기와 빈틈의 RD/RLD, 암편/토양의 공간분포, 줄기기부 Ks와 SF/TF를 측정해 2D 보존적 침식 엔진과 결합해야 한다. 기존 Iber+ 및 SSSPAM/mARM 모형 선택 유지.
