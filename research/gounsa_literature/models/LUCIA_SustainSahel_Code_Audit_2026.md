# LUCIA SustainSahel 원본 코드 감사 (2026-10-27)

## 모델 식별
Land Use Change Impact Assessment (LUCIA), University of Hohenheim; 공식 연구페이지 https://lucia.uni-hohenheim.de/en/research-applications . 공개 모델 https://github.com/gcadisch/LUCIA_SustainSahel (`main`).

## 새로 찾은 이유
LAI 기반 식생/수관차단, 강우타격 및 유수박리, 격자별 입경별 퇴적을 단일 공개 모형에 결합한 후보인지 검토.

## 공개 원본 직접 확인
GitHub connector로 `src/erodep/erodepModule.py` blob SHA **60d894f05504be50217c634f8d77bb5a05813292** 직접 열람.
- 약 65행 `self.LDD = lupy.LDD`
- 약 150행 `accufractionflux(self.LDD, self.runoff_patch, self.stream_id)`로 지표유출 누적
- 약 178행 `self.intercept_evap = lupy.interception`
- 약 279행 canopy-cover/LAI 관련 식 일부는 주석 처리되어 있으므로 코드 활성 확인 없이 주장 금지
- 약 320–327행 free throughfall + canopy throughfall에 따른 빗방울 박리원 `E_detach_throughfall_1`, `E_detach_throughfall_2`
- 약 343–380행 모래/실트/점토 클래스 유사이동, 퇴적 및 토양수지; `accufractionstate(self.LDD,...)`, `accufractionflux(self.LDD,...)` 사용
- 약 391–402행 하도/경사면 유사 이동 분배/유출.

## 공간 및 시간 구조
공식 문서: 일 간격 주모델, 침투/유출/침식은 1시간 이내 하위 시간 간격; 사용자 정의 격자 크기. 공개 예시 자료 6m, 30m, 100m. **5–10cm에서 원본 전체 실행 검증 자료 없음**. LDD 흐름은 raster 기반 지형하류 방향 경로, 수심·X/Y 운동량 연립하는 2D SWE가 아님.

## 식생 수관차단 정확한 확인 수준
기존 LUCIA 수관저류 변수 및 free/canopy throughfall 분기식이 원본에 있음. 그러나 완전 동적 Rutter canopy drainage와 stemflow, LAI 연동 저장용량 활성 여부까지 확인한 것은 아님.

## 판정
**탈락: 지형 하류 방향(LDD) 유동이 고운사의 자유로운 2D 수문 조건과 충돌.** 5–10cm 실제 published 실행 근거 없음. 수관과 침식 부분이 구현됐다는 사실은 유지하되 주모델 또는 신규 coupling 제안 금지.

## 관련 링크
https://github.com/gcadisch/LUCIA_SustainSahel/blob/main/src/erodep/erodepModule.py
https://lucia.uni-hohenheim.de/en/materials
https://lucia.uni-hohenheim.de/en/research-applications
