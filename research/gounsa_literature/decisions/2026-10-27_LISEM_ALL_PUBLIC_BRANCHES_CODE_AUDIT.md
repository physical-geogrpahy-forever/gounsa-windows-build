# 2026-10-27 신형 LISEM 3개 공개 브랜치와 릴리스 태그 전수 감사

## 질문
신형 LISEM이 공개가 안 된 것인지, GitHub 브랜치를 누락해서 잘못 결론 내린 것인지 확인. 공식 작성자 bastianvandenbout/LISEM의 모든 공개 브랜치 `main`, `develop`, `website`와 공개 source 태그를 GitHub API로 직접 열어 교차검증한다.

## 정확히 확인한 Git refs
| Ref | commit | commit UTC | 계산 코드 | 선언 버전 |
|---|---|---|---|---|
| main | 6a5ef17d87bab4227d48673c95c12c61462114dd | 2022-08-10 20:06 | 있음 | `0.2.3` |
| develop | 1e55e6c0bfda28d56a9e1d37e1c21c616820c6a1 | 2022-12-12 10:08 | 있음 | `0.2.5` |
| website | 09c9f060324c85cb83ff33e02644816169293d54 | 2022-09-22 07:40 | **없음** (`lisem/` directory absent) | 해당 없음 |
| tag `source` | 6a5ef17d87bab4227d48673c95c12c61462114dd | 2022-08-10 main과 같음 | 있음 | **0.2.3** |

공식 GitHub 릴리스 `Beta 0.2.4`는 2022-08-23 게시, tag `source`를 가리킴. 이 태그는 실제로 **main 0.2.3 소스**이다. release assets는 비어있음.
공식 SourceForge는 별도로 2022-09-07 `LISEM-0.2.4-win64.exe` **317.7MB**, Portable 0.2.4 및 Python wheel 0.2.4 공개; 0.2.4 실행파일과 `source` tag가 정확 같은 소스라는 근거 없음.
개발자 2022-07-09 https://lisemmodel.com/blog/2022/07/09/Release-0.2.4/ 는 0.2.3 GUI interfaced model precipitation issue가 0.2.4에서 fixed 되었다고 주장. **배포 바이너리는 분석 전이므로 옛 소스의 오류를 0.2.4 실행파일에 전가 금지.**

## 10개 주요 파일의 Git Blob SHA 동일성 대조
GitHub fetch_file에서 동일 SHA는 파일바이트가 정확히 같다는 근거.
| 파일 | main vs develop |
|---|---|
| `lisem/model/kernels/model_hydrology.cl` | **동일** SHA 673d676dc4f161822d50cce691cd4082779a812e |
| `lisem/model/kernels/model_evapotranspiration.cl` | **동일** SHA 7dc53f0bb0ef44ff40d108828d18deba9a36c10f |
| `lisem/model/kernels/model_sediment.cl` | **동일** SHA a3ac0e60f3c5cc1d5bb778ae1ad3d4e9d2c08ed9 |
| `lisem/model/modelruncompile.cpp` | **동일** SHA a8f6a966dd0fa6c7635db69b90a22236659ec8cb |
| `lisem/model/kernels/model_flow.cl` | **달라짐** main ade43fc..., develop b51e4857... |
| `lisem/model/modelrun.cpp` | **달라짐** main bbfd86d..., develop a863f770... |
| `lisem/model/modelruninit.cpp` | **달라짐** main 1403bb9..., develop 7d23ef8... |
| `lisem/model/parameters/parametermanager.h` | **달라짐** |
| `CMakeLists.txt` | **동일** SHA f4df94d9db836ebaa4febe37a380d6059138bf97 |
| `README.md` | **동일** SHA 995e9039afb5f1aa6e44d4020c10fa0ef97d2f9d |

main→develop 비교는 7개 후속 커밋(ahead=7; behind=0).

## 필수과정: 두 코드 브랜치 모두 경로별 감사
### (1) LAI 기반 수관저류 및 지면강우
**두 브랜치 모두 `model_hydrology.cl` 완전 동일**. 289 `store_canopy=SCANOPY`, 302 `Smaxc=SMAX_CANOPY`, **그후 Smaxc 사용 없음**, 310 `h=h+store_canopy`, 326 `h=h+rain`, 397 `SCANOPYN=0`. 증발산 `model_evapotranspiration.cl`도 동일 (L151 Smaxc read unused, L169 LAI expression commented out, L192 SCANOPYN=0).
`modelruncompile.cpp` L1417는 hydrology rain scalar Arg38 `0.0`. main `modelrun.cpp` L166 / develop L161 또한 hydrology rain=0. 한편 실제 유동 solver `model_flow.cl`에 rain texture `T_RAIN` 직접 전달 (compile.cpp L1266), `flow.cl` L247에서 읽어 지표수에 추가. **발견된 native 2022 통합모델 경로에서 canopy maximum storage가 강우를 가로채는 물수지 로직 확인되지 않음**.

### (2) 강우박리와 수관적하 충격
**두 브랜치 모두 `model_sediment.cl` 완전 동일**, L204 rain_m scalar; L369 Int from rain_m; L381 `directrain=(1-vegcover)*rain_m*1000`; L384-386 vegetation height droplet energy & `throughfall=vegcover*rain_m*1000`; L397–408 detachment rain terms.
**두 브랜치 모두 `modelruncompile.cpp` L1637 erosion argument 81 `0.0f`**, main `modelrun.cpp` L546 / develop L541에서 해당 인자 0으로 재설정. 다른 해당 인자 nonzero 설정은 확인되지 않음. 그래서 이 통합경로의 `rain_m=0`으로 rain splash part 0. 별도 스크립트 함수 `AS_SplashErosion` 존재는 native GUI model의 수정 증거 아님.
`model_sediment.cl` L507–510의 `qfsout=qfsout+z_x1 < -1000 ? sflux_x1:0`는 괄호 누락에 따른 외부 유사배출 집계 오류 후보를 두 브랜치 모두 유지.

### (3) 유동: develop에서 실제 수정된 부분
main `model_flow.cl` L447–450:
`qfout = qfout +z_x1 < -1000? flux_x1 : 0.0;`
develop에서:
`qfout = qfout +(z_x1 < -1000? flux_x1 : 0.0);`
→ **수문 격자 경계유출량 집계에서 삼항연산자 괄호를 수정**. 그러나 `model_sediment.cl`의 동형 `qfsout` 식은 두 브랜치 모두 수정 안 됨.
main `model_flow.cl` L532 `hn = hn - infil_act + rain * dt_hydro/max(1e-10f,dt);`
develop 같은 줄 L532 `hn = hn - infil_act + rain * dt/max(1e-10f,dt_hydro);`
→ 강우 시간환산 계수가 **정반대로 변경**됨. 어느 식이 물리적으로 맞는지는 `rain`, `dt`, `dt_hydro`의 호출값/단위 및 네이티브 강우수지 실험을 보고 평가해야 함; 이 정적 변경만으로 안정성 향상 단정 금지.
`modelruninit.cpp`는 develop에서 `m_DoRainfall` 플래그를 사용해 time-input rain-file load를 조건부 수행하는 코드 추가.

### (4) 코드 외 리소스
`website` 브랜치는 Jekyll/`_docs`/`_pages` 등 문서자료 중심이고 `lisem/` 및 CMake 소스가 없음. 공식 컴파일 설명 https://lisemmodel.com/docs/compiling/ 이 직접 3개 브랜치 이름과 역할을 밝힘.

## 한계 및 판정
- **공개 브랜치 누락 여부:** 모든 GitHub 브랜치 3개 확인, 미조사 브랜치 없음.
- **공개 소스 통합모델 내부의 실제 수관차단 및 강우박리 연결:** `main(0.2.3)`, `develop(0.2.5)` 모두 소스상 문제 유지, 이에 한정 **NO-GO**.
- **배포된 별도 공식 0.2.4 Windows 실행파일**은 아직 내용과 실행결과를 직접 검증하지 않았으며 **판정 보류**. 수정 공지 존재하기 때문에 추론으로 탈락시키지 않음.
- **Epple et al. (2025) 1cm 사용본**은 특정 Git SHA/Windows 바이너리 버전 인용 증거가 없고, 논문이 실제 쓴 스크립트 로직은 별도 경로일 수 있음. 선행연구 존재와 공개 브랜치의 원본 적합성은 구분.
- 강우사상별 수관 저장량, 경계 물배출/유사배출, 토양재고, 시간격자 수렴, DoD는 어느 브랜치도 이번 감사에서 네이티브 실행하지 않았음.

## 직접 열람할 출처
- https://github.com/bastianvandenbout/LISEM/tree/6a5ef17d87bab4227d48673c95c12c61462114dd
- https://github.com/bastianvandenbout/LISEM/tree/1e55e6c0bfda28d56a9e1d37e1c21c616820c6a1
- https://github.com/bastianvandenbout/LISEM/tree/website
- https://github.com/bastianvandenbout/LISEM/releases/tag/source
- https://github.com/bastianvandenbout/LISEM/blob/develop/lisem/model/kernels/model_hydrology.cl
- https://github.com/bastianvandenbout/LISEM/blob/develop/lisem/model/kernels/model_sediment.cl
- https://github.com/bastianvandenbout/LISEM/blob/develop/lisem/model/modelruncompile.cpp
- https://github.com/bastianvandenbout/LISEM/blob/develop/lisem/model/kernels/model_flow.cl
- https://lisemmodel.com/docs/compiling/
- https://lisemmodel.com/blog/2022/07/09/Release-0.2.4/
- https://sourceforge.net/projects/lisem/files/LISEM%20%28beta%20release%20new%20software%29/Installer/
