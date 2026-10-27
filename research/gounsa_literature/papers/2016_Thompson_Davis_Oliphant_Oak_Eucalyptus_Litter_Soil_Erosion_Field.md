# 서지정보
Thompson, A., Davis, J. D., & Oliphant, A. J. (2016). Surface runoff and soil erosion under eucalyptus and oak canopy. *Earth Surface Processes and Landforms, 41*, 1018–1026. https://doi.org/10.1002/esp.3881. Author-hosted full original preprint https://environment.sfsu.edu/sites/default/files/2022-05/ThompsonDavisOliphant_preprint_esp3881_Rev.pdf.

# 이 논문을 찾은 이유
고운사 **듬성듬성 참나무 맹아 + 억새 패치에서 강우 수관차단 ON/OFF 차이의 현장 인과 해석** 시, 낙엽층과 소수성 토양의 동반변화를 무시해도 되는지 검증. `INDEX.md`에서 제목/DOI 미등재 확인.

# 연구 유형
자연강우 현장 관측 연구, 직접 Numerical SWE/erosion modeling **아님**. 2006년 10월–2008년 2월 샌프란시스코 만 일대 8개 페어드 입지 × Quercus agrifolia/eucalyptus 구획. 현장 논문의 author-hosted **9페이지 PDF 전체 텍스트 검토 및 web screenshot p2,p6 시각 검증**.

# 공간 구조 및 적용환경
각 Gerlach trough 입구50cm 폭, 상부 길이 약3m로 약 **1.5m² 집수 플롯**, 사이드 개방. 참나무 평균 경사21.4°와 유칼립투스19.1° (각 입지 조건 맞춤), 두 식생 플롯 간 거리 24–87m 등. 토양은 사암/셰일, 셰일 및 세립 사암 등 다수 토양군; 고운사 사암 산지와 비교 가치 있으나 동일토양·동일 식생 아님. 조사 플롯 크기와 낙엽 깊이 5cm는 native 계산격자 5cm 뜻이 아님.

# 핵심 과정 및 실험 방법
강우관측소의 시간별 tipping-bucket 및 수관 아래 우량계, 현장 21개 rain gauges, runoff Gerlach trough 및 유출 bucket, 집수 유사량과 litter 건조무게, TDR/토심0–10cm 수분, critical surface tension 토양 발수성, 3개 현장지점 낙엽 두께 cm. 약 12회 natural storm observation 2006–07, 이후 2008년 1월 강수 집중.

# 핵심 결과
- Oak canopy **평균 litter depth 5cm**, Eucalyptus canopy **10cm** (paper p1–2), heavy rain January2008 about **450mm** cumulative during major storms with daily max ~123mm; earlier year daily max ~70mm.
- 2006–07 wet season: eucalyptus paired sites runoff generally > oak, correlating with soil water repellency; little measurable mineral sediment that year.
- Heavy January2008 storms: **oak sites collected more mineral sediment than eucalyptus**; oak mean thinner litter suggested as main control. Original tests sediment oak > eucalyptus ANOVA p=0.019 and Wilcoxon p=0.0325 (preprint p6); no universal conclusion that lower canopy interception yields greater erosion. Oak native species **Quercus agrifolia** not Korean oak coppice.
- Authors limited observations to **undisturbed intact-litter sites**, no postfire field validation; event-scale high flows overflowed collection buckets so runoff volume during major storm incomplete.

# 식생 입력
Canopy type pair and understory rain direct gauges, throughfall, litter depth, soil repellency, surface protection. **No measured LAI canopy bucket or actual stand LAI model** claimed, no causal isolated canopy-interception scenario (litter, hydrophobicity vary together). Miscanthus absent.

# 핵심 식 및 파라미터 단위
Slope [degrees], litter [cm], rainfall [mm], runoff [L], soil sediment [g or g/m²], soil moisture %, repellency CST [mN/m]. Original rain/runoff table and statistical figures. No original 2D SWE or transport/exner governing code.

# 원 논문의 구현 범위
Paired observed oak/eucalyptus runoff and sediment responses, not physically-based model; readily downloadable structured (tidied) **runoff and rainfall dataset** reproduced as `tidy_eucoak.rda` in original data-science GitHub https://github.com/iGISc/iGIScData/tree/master/data and `man/tidy_eucoak.Rd` 180 observations × 12 variables [site,tree,date,rain_mm,rain_subcanopy,slope,aspect,runoff_L,surface_tension,runoff_rainfall_ratio...]. **This tidied package does not document event sediment grams, and is not a 5cm soil erosion input package**. Provenance as derivative educational data not original paper archived supplemental repository; independent audit needed before quantitative benchmarking.

# 고운사 활용
Warn **cannot attribute canopy and erosion difference exclusively to LAI** if litter/repellency also change. An analytically isolated canopy toggle must keep the rest fixed; subsequent physically realistic plant-patch comparison should include litter effects separately.

# 새로운 coupling / 한계
Not standalone executable, no 5cm actual calculation, no 2D numerical sediment routing. Not substitute for user required pre-existing model.

# 최종 판정
**Strong oak+forest interrill/soil-loss observation comparator**, primary model candidate **NO**.

# 근거
https://doi.org/10.1002/esp.3881
https://environment.sfsu.edu/index.php/publication/surface-runoff-and-soil-erosion-under-eucalyptus-and-oak-canopy
https://github.com/iGISc/iGIScData/blob/master/man/tidy_eucoak.Rd
https://environment.sfsu.edu/sites/default/files/2022-05/ThompsonDavisOliphant_preprint_esp3881_Rev.pdf
