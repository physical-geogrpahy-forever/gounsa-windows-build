# Li & Tian (2026): LAI와 잎 경사각을 이용한 수관하 빗방울 운동에너지 모델

## 서지정보
Li, Z., & Tian, F. (2026). Derivation and validation of estimation model of rainfall kinetic energy under the canopy. *Hydrology and Earth System Sciences, 30*, 3203–3219. https://doi.org/10.5194/hess-30-3203-2026

## 이 논문을 검색한 이유
고운사의 억새와 참나무 맹아에서 LAI 및 수관형태 차이가 지표 토양박리 강우에너지에 미치는 영향. 기존 EUROSEM/SHETRAN형 단일 수관높이 공식의 경험적 한계를 넘어가는 최신 근거.

## 연구 유형, 공간구조, 적용환경
수관 내 빗방울 미세물리 기반 수관하 운동에너지 추정식 유도 및 현장 자료 검증. **유수침식 2D 수치모델, 토양유실량 및 유사수송 모형은 아님.** 수관구조와 빗방울 스펙트럼 관측 자료 9개를 이용한 검증. 한국 사암 고운사 산불 후 억새/참나무 맹아 현장 검증 아님.

## 핵심과정
잎에서 분리되어 떨어지는 dripping drops와 splash droplets를 구분, LAI, 잎 경사각, 접촉각과 pinning proportion, 강우강도 등이 에너지 및 수관하 입도에 미치는 영향을 추적. 하층식생을 단순 canopy-cover 상수로 치환하지 않는 최신 연구 근거.

## 식생입력, 핵심식과 파라미터 단위
LAI [m² m⁻²], leaf inclination [° or radians, follow original parameter definition], rainfall intensity [mm h⁻¹], under-canopy kinetic energy rate [J m⁻² h⁻¹]. Model source implementing a full 2D erosion solver was **not** identified; original complete equation and calibration coefficients require primary text if implementing. Do not invent formulas.

## 결과와 방법
9개 datasets, 총 수관하 KE의 R²=0.769, splash drop KE R²=0.572, dripping drop KE R²=0.773; respective RMSE 18.7, 2.0 and 18.7 J m⁻² h⁻¹. Note distinct observational methods and uncertainty; not erosion yield prediction accuracy. Authors note simplified branch-drip and parameter assumptions, need new vegetation environment verification.

## 고운사에서 사용할 수 있는 부분
현장 라이다로 관측한 억새와 참나무 맹아 LAI/leaf tilt/height에 따른 canopy-underfall energetics independent component; when combined with independent true2D erosion solver this is explicitly **new coupling** and requires validation. 

## 한계 및 최종 판정
**보조 문헌**: native 2D water/erosion solver 없음, field soil erosion quantitative validation 아님. No in-container executable numerical check in this session.

## 출처
https://hess.copernicus.org/articles/30/3203/2026/hess-30-3203-2026.html
