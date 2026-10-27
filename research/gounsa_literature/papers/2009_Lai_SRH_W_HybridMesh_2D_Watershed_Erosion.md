# 서지정보
Lai, Y. G. (2009). Watershed runoff and erosion modeling with a hybrid mesh model. *Journal of Hydrologic Engineering*, 14(1), 15–26. https://doi.org/10.1061/(ASCE)1084-0699(2009)14:1(15)

# 이 논문을 찾은 이유
지금까지 검토하지 않은 원본 연구용 2D 강우사상 수문 + sediment 침식/퇴적 모델의 혼합격자 보존법 및 **정확 동일 연구 실행판 공개 여부**를 소스 우선으로 확인.

# 연구 유형
Peer-reviewed model-development technical paper with verification/validation test cases. 2009 ASCE publisher full abstract, bib records verified. **전체 본문 수식/실험 grid 정보를 획득하지 못함**, 따라서 무단 추정 금지.

# 공간 구조
Hybrid structured/unstructured polygonal mesh, finite-volume water mass conservative 2D watershed hydrodynamics. 2D watershed flow solver and erosion model as published research are documented. Whether momentum solved as full SWE vs diffusive approximation in article exact simulation configuration is not established from abstract and manuals; therefore not label fully dynamic without code evidence.

# 적용 환경
Small-to-large watershed rain runoff and some erosion test cases. Explicit high-res oak/grass (Miscanthus) forest hill slope with 5–10cm published computational mesh not verified.

# 핵심 과정
- 2009 published improvement over CASC2D and other watershed erosion models: hybrid mesh conservation formulation, runoff, erosion model, multiple verification/validation applications.
- 2006/2007 government official **SRH-W v1.1** released user manual explicitly states: "Only flow hydraulics and water runoff are modeled. Erosion and sediment transport are not available at present;" as limitations §1.3, and "Only flow routing module has been developed and released." This is a version-specific statement, **not proof that post-2007 paper's model was never developed**.
- 2009 article's matching complete runoff+erosion source and matching program runfiles publicly accessible: **unverified**.

# 식생 입력
SRH-W v1.1 Manual §4/5 states land use classes with Manning roughness and **fixed rainfall interception depth** (intial/cumulative retention). No direct LAI→dynamical C(t)/Smax+drainage, leafdrop impact KE in released manual as inspected text. Do not infer rain drop response from simple interception loss.

# 핵심 식
2D finite-volume runoff conservation from 2009 abstract and official manual's diffusive wave routing. Precise sediment source terms and exponent/units of 2009 erosion implementation not visible in available 2009 full text; none invented.

# 파라미터와 단위
v1.1 intercept depth [length], Manning roughness; Green-Ampt soil hydraulic conductivity/soil suction/moisture deficit units in manual. 5cm computing Δx, sediment output/time-step: not verified.

# 원 논문의 구현 범위
Actual 2009 **peer-reviewed runoff and erosion research model** exists, but **2007 publicly documented operational SRH-W v1.1 = hydrologic-only**. Version gap can reflect a later unpublished/unfound 2009 erosion development; no author-exact release SHA to close.

# 고운사에 직접 사용할 수 있는 부분
Independent precedent for flexible hybrid mesh 2D hydrodynamic/watershed sediment design; paper method may inform comparative numerical mesh choices.

# 새로운 coupling이 필요한 부분
Published-matching executable/source first; dynamic LAI throughfall/leaf-drip KE, separate rain and water detachment, highres 10cm cross-slope sediment mass and 4-edge free boundaries all unverified or would require new work.

# 한계
- Source/distribution mismatch: 2009 scientific model, 2007 SRH-W manual that explicitly excludes erosion in its **released version**.
- Government later SRH-2D 3.3.1 executable and manual describe sediment but **SRH-2D is separate river hydraulics product**, not verified identical to 2009 SRH-W forest rainfall program.
- Publisher abstract paper mesh, actual 2009 erosion sources, LAI, canopy/drip, 5–10cm native stability not verified.
- Official government 2007 PDF about 11.8MB was indexed/search excerpts but direct web.open refused length; **exact document file was not fully read/screenshotted**, only snippet; preserve limitation.

# 최종 판정
**Model paper existence PASS, original same-version executable sediment FAIL/UNVERIFIED, LAI canopy, sub10cm full 2D soil erosion FAIL/UNVERIFIED. Cannot adopt unmodified for Gounsa.**

# 원본 링크
https://doi.org/10.1061/(ASCE)1084-0699(2009)14:1(15)
https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/downloads/SRH-W%20v1.1%20User%20Manual%20June2007.pdf
https://www.usbr.gov/tsc/techreferences/computer%20software/models/srh2d/index.html
https://www.wra.gov.tw/wrapen/cp.aspx?n=46794
