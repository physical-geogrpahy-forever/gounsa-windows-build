# Kim, Han, and Cho (2014) tRIBS-FEaST

## 서지정보
김종호, 한세종, 조용식. (2014). 유역기반의 수문, 수리, 침식 및 유사이송 모의를 위한 통합모형. *한국방재학회논문집, 14*(5), 351–358. https://doi.org/10.9798/KOSHAM.2014.14.5.351

## 검토 이유
유역 내 수관차단-침투-지표유출-2D Hairsine–Rose 물리침식의 native 결합으로 고운사에 재현 가능한 실제 공개판이 있는지 확인.

## 연구 유형, 관측 및 실험방법
국내 peer-reviewed original integrated model method paper. tRIBS-FEaST combines water-balance interception, evapotranspiration, infiltration, runoff and groundwater with 2D Saint-Venant momentum/continuity and Hairsine–Rose size-dependent erosion and deposition. Original study compares simulated sediment/flow with measured experimental flume data, reports satisfactory agreement and size-dependent deposition timing/hysteresis (not a numerical value claimed here). It argues non-uniqueness of sediment response under identical storm. Primarily flume validation, **not observed Korean postfire steep-sandstone hillslope rill network/TLS**.

## 식생입력 및 구현 경계
Hydrologic interception supported in described parent tRIBS system, but no explicit native verified LAI-to-interception-to-throughfall vs leafdrip impact erosion implementation in released **FEaST source**. Contemporary official MIT repository `tRIBS-Model/tRIBS` contains `src/tHydro/tIntercept.cpp` Rutter, but NO compiled Hairsine–Rose integration code.

## 핵심식과 변수
2D Saint-Venant water depth h [m], flow momentum [(m²/s)], Hairsine–Rose size-fraction sediment concentrations [mass/volume], primary and loose bed-sediment storage [kg/m²] depending specific formulation, rainfall- and flow-induced entrainment source terms. Full published numerical constants require article/source; source binary not obtained.

## 새로운 coupling / 고운사 한계
Unless exact FEaST scientific release is obtained, recreating hydrology+dynamic 2D erosion is **new implementation**, not a native feature of official modern tRIBS. Native snow/forest/LAI direct vs leaf drip effects, RLD dynamics, root detachment, fire spall, rock armouring, shallow-soil stock and site observations absent/unverified.

## 최종 판정
**탈락 as full publicly downloadable reproducible source**, important published process reference. Domestic publication itself does not guarantee public source or stable native 2026 executable.

## 원문 링크
https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001925519
https://doi.org/10.9798/KOSHAM.2014.14.5.351
