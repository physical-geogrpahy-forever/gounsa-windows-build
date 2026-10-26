# 2026-10-26 SWEHR 공식 원본 1.0 코드 동일성 및 2016 논문 구현차이 확인

## 결론
**우선 모형은 원본 SWEHR이며 인위적으로 만든 식생/침식계수 연계 실험을 SWEHR 원본의 식생 반응으로 해석하지 않는다.**

2016 McGuire et al. DOI 10.1002/2016JF003867의 원문은 §3.2 식(3)–(4) canopy rain-splash shield \((1-C_v)+T_cC_v\), §3.5 식(24)–(26) time-varying Rutter C(t), D(C)와 soil-reached rainfall 계산을 논의한다. 그러나 저자가 CSDMS 공식 SWEHR로 지정한 공개 V1.0 C 구현에서는 이러한 독립 함수와 상태변수를 찾지 못했다. 따라서 **공개된 공식 배포 원본은 논문의 모든 vegetation components를 실행하는 연구용 전체 코드라고 입증할 수 없다.** 동일하다고 가정하지 않는다.

## 원저자 공식 원본 출처
- CSDMS SWEHR official developer Luke McGuire, model V1.0 DOI https://doi.org/10.5281/zenodo.824087 .
- CSDMS 원문 https://csdms.colorado.edu/wiki/Model:SWEHR : July 2017 공개, GNU GPL v2, 원본 GitHub https://github.com/csdms-contrib/swehr .
- GitHub V1.0 release https://github.com/csdms-contrib/swehr/releases/tag/V1.0 , 2017-07-07 공개. 원본 Git의 최초 제출 커밋 **4e6f783f335ac6dc1c116ef0d516c2f3d1b911e2** (2017-07-06), 부모 없는 초기 커밋. 현재 master 브랜치는 단일 커밋이며 별도 source update/extra branch 확인되지 않음.
- 공식 배포에 파일 정확히 7개: License.txt, SWEHR.c, input.txt, particlepercentin.txt, particlesizein.txt, rain.txt, topoin.txt.
- 원본 파일 일체를 **byte-for-byte 변경 없이** 개인 연구 저장소의 `third_party/SWEHR_original_v1_0_2017/` 에 보존, `main` 브랜치. Git blob SHA 원본 대 보존본 모두 7/7 동일함.
- C source 원본 Git blob: **e8505221a37d245ebb387b3304d8f325addd9ada**; 보존본도 동일.
- 전체 7개 원본 Git blob SHA:
  - License.txt: d159169d1050894d3ea3b98e1c965c4058208fe1
  - SWEHR.c: e8505221a37d245ebb387b3304d8f325addd9ada
  - input.txt: 5c46fbb08b055af402abd8221cb7fd8afba4adbb
  - particlepercentin.txt: d00491fd7e5bb6fa28c517a0bb32b8b506539d4d
  - particlesizein.txt: d683bfa22c2087c545ca77624c732380e7cb3a18
  - rain.txt: a2936cc4b00077a246c222ad1f4770b64f461e77
  - topoin.txt: 68e0c609078febdc42e42a1e6ba94ab8ceb88239

## 공개 버전 정밀 구문 감사
- 원본 `SWEHR.c`에는 `R=RAIN[rind]`(약 L814)가 있으며 `E[1],E[2]` 강우박리와 `U[1]+=dt R` 강우 물 공급(약 L1338,L1343,L1427)이 같은 원시 R을 사용한다.
- `(1-Cv)+TcCv` canopy mechanical shielding factor 및 독립 Rutter `C, Tc, S, Kc, gc, D(C)` 입력/함수 없음.
- `SF[i][j]`는 Manning friction slope이지 stemflow가 아님.
- `H` 퇴적층 차폐, `h>h0` 빗방울충격 수심 감쇠 및 Green-Ampt 침투는 원본 C에 존재함.
- 원본 `SWEHR.c`에는 강제 external sediment-and-water inflow on upper j=ny edge 및 demo-specific arrays, example rain.txt typically 0 rain values. 언뜻 보기만 해서 rainfall-only erosion 모델로 간주하지 않음.
- 2016 원논문 부록 제공물은 Supporting Information 6 PDF (methods and figures)이며 함께 업로드된 완전한 연구 당시 C 코드 파일은 목록에서 발견되지 않음. 본문에서 data available upon request to corresponding author.
- 2019 Tang et al., 2020 Tang et al. 역시 source location을 똑같이 공식 CSDMS SWEHR 페이지로 안내하며, 독립적인 2016 식생모형 완전코드를 확인할 다른 공개 위치는 현재 찾지 못함.

## 한 글자 수정하지 않은 공식 V1.0의 컴파일과 실행
- archived 7 files를 GitHub Actions Linux runner의 임시 디렉터리에 그대로 복사 후 컴파일 `gcc -O2 -std=gnu99 -Wall -Wextra SWEHR.c -lm` (unused variable and unchecked fscanf warnings generated).
- 공식 원본 `input.txt`, `rain.txt`, `topoin.txt` 등 예제 그대로 실행. **native exit 0**, modified model/canopy coupling code 없음.
- CI run https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40272368386 . `.github/workflows/swehr_official_v1_untouched_smoke.yml`.
- **컴파일 및 원본 예제 작동 확인은 논문 물리식 전부 검증/현장 물수지 검증/식생 침식량 재현을 뜻하지 않는다**.

## 기존 연구 결론의 필수 정정
- `spatial-vegetation-runoff-erosion-20261026` 브랜치의 `spatial_patch_swehr.py` 와 `swehr-water-sediment-closure-20261026` 의 `verify_swehr_closure.py` 는 공식 original이 아닌 **SWEHR-derived engineering fork**이다.
- 식생격자 Ks4e-6m/s vs bare Ks1e-6m/s, Manning .18/.08, a .07/.25, J90/30, canopy storage0.8mm per event, stemflow hypothetical 10% 등은 원논문 실험값을 재현하지 못하고 일률적 기상/식생 가정이므로 “원본 SWEHR에서 억새가 4.2× erosion reduction”이라는 표현 전면 철회.
- 38개 QA 통과는 **수정된 포크에서 생성된 수치 보존 레저** 검증 기록. 논문의 Rutter+canopy shielding 구현/검증과 구분해야 한다.
- 이 단계에서 포크의 높은 numerical conservation precision은 원본 source의 scientific implementation correctness와 별개다.
- 원본 코드를 사용하겠다는 연구 원칙을 충족하기 위한 선택은 (A) 공개 공식 V1.0을 그 한계 그대로 적용해 이론 범위를 제한하거나, (B) McGuire 2016 연구 당시 식생 모듈 포함 원래 구현 코드를 저자에게 요청하여 그 출처/버전/조건을 검증하는 것뿐이다. `임의로 복원한 함수`를 `McGuire original`이라 부르지 않는다.

## 증거와 재현
- 본인의 동일성 검증: GitHub Trees API의 source와 destination 7개 blob SHA를 정확히 일대일 비교했고 **7/7 true** 확인.
- official original https://github.com/csdms-contrib/swehr/blob/master/SWEHR.c
- preserved byte identical https://github.com/physical-geogrpahy-forever/gounsa-windows-build/tree/main/third_party/SWEHR_original_v1_0_2017
- native smoke test https://github.com/physical-geogrpahy-forever/gounsa-windows-build/actions/runs/40272368386
- McGuire et al. full text https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016JF003867

## Pending
소프트웨어 저자에게 실제 McGuire 2016 Fig9 vegetation recovery experiments용 C source revision, Rutter C(t), D(t), `Cv`/Tc shielding, sample calibrated model input files and original boundary conditions 요청. 수령 이전에는 이 논문 주요 식생 민감도 수치가 재현됐다고 주장 불가.
