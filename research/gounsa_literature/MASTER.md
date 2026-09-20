# Gounsa Literature Master

업데이트: 2026-09-21

이 문서는 전체 문헌검토의 살아 있는 통합본이다.

## 현재 상태

기존 여러 채팅에서 상당한 문헌검토가 수행되었으나 일부 대화가 길이 제한으로 유실되었다.

따라서 앞으로 모든 결과는 논문별 파일에 먼저 저장하고, 확정 결론만 이 MASTER에 누적한다.

## 현재 고정 원칙

- COPLAS 최종모델 근거에서 제외
- MUSLE 최종 산지 유수침식식에서 제외
- quantitative vegetation state 우선
- genuine 2D 우선
- interrill/rill 또는 rainfall-driven/flow-driven 구분
- 기존 논문식 우선
- 새로운 coupling은 명시

## 현재 조사 대상

1. 유수침식
2. 사면확산 및 biogenic transport
3. 산사태
4. 산불 후 spall
5. coarse fragments / armour
6. LPJ-GUESS와 지형과정 coupling

## 이전 채팅에 요청할 작업

각 이전 채팅은 자신이 검토한 논문과 결론을 이 저장소 구조로 옮긴다.

1. 논문별로 `papers/` 파일 생성
2. 모델 계보는 `models/` 파일 생성
3. 중요한 결정은 `decisions/` 파일 생성
4. 전체 핵심 결론은 이 MASTER에 병합
5. 마지막에 `sessions/` 인계서 생성


## 2026-09-21 LPJ-GUESS biomass-geomorph 복구

이번 채팅에서 유수침식, 사면확산/biogenic transport, 풍화/soil production을 LPJ-GUESS의 동적 PFT/cohort biomass와 연결하는 문헌을 복구했다.

### 현재 확정 원칙
- COPLAS는 최종 고운사 모델 근거에서 제외한다. 비교대상으로만 보존한다.
- MUSLE는 최종 산지 유수침식식에서 제외한다.
- 단일 vegetation cover 대신 PFT/cohort별 quantitative vegetation state를 우선한다.
- root-access depth는 AB soil thickness와 동일시하지 않는다. C/Cr까지 root access를 허용한다.
- 현장실험 회귀식과 실제 수치모델을 구분한다.
- 서로 다른 published model의 결합은 모두 `새로운 coupling`으로 표시한다.

### 유수침식
핵심 모델근거:
- Saco & Moreno-de las Heras 2013: biomass -> SIBERIA erodibility의 직접 선례
- Tan et al. 2022 ELM-Erosion: PFT별 topsoil root biomass effect
- Wang et al. 2024 VED: detachment capacity와 transport capacity에 vegetation effect를 별도 적용

최신 실험근거의 방향:
- FineRootC 자체보다 RMD, RLD, RSAD, SRL, root architecture가 Dc/Kr/tau_c 설명에 더 직접적
- grass, shrub, forest 또는 fibrous/tap root를 동일 계수로 처리하지 않는다
- forest biomass 증가가 erosion resistance의 단조증가를 의미하지 않는다

### 사면확산 및 biogenic transport
현재 작업구조:
`q_hill = q_creep + q_rootgrowth + q_treethrow`

근거:
- Gabet et al. 2003: root mass, turnover, rooting-depth distribution
- Gabet & Mudd 2010: root fracture와 tree throw
- Doane et al. 2021/2023/2024: tree throw와 hillslope roughness 계보
- Adams et al. 2023: post-fire CWD sediment storage/connectivity

산불 후 dead wood는 SurfaceLitC로만 보내지 않고 CWD 상태를 별도 검토한다.

### 풍화 및 soil/regolith production
현재 작업구조:
`W_total = W_hydroclimatic + W_deep_root_chemical + W_woody_mechanical`

근거:
- Pelak et al. 2016: biomass-driven soil production의 최소모델
- Gabet & Mudd 2010: woody mechanical weathering
- REWTCrunch 2022: root biomass/exudation -> reactive weathering
- Pawlik et al. 2023/2024: living tree roots와 soil formation의 최근 현장근거
- Osorio-Leon et al. 2025: deep roots가 bedrock-vadose-zone silicate weathering을 정량적으로 강화
- Billings et al. 2025: deep root-regolith interaction의 biome-scale 근거
- Bemis et al. 2026: bare rock -> moss -> grass -> shrub -> tree succession과 Critical Zone 생성

### 최신 결정 파일
- [COPLAS/MUSLE 제외](decisions/2026-09-21_COPLAS_MUSLE_EXCLUSION.md)
- [LPJ-GUESS quantitative biomass coupling](decisions/2026-09-21_LPJGUESS_BIOMASS_COUPLING.md)
- [세 지형과정 구조](decisions/2026-09-21_THREE_PROCESS_GEOMORPH_STRUCTURE.md)

### 남은 핵심 gap
1. FineRootC -> RMD/RLD/RSAD/SRL의 PFT별 변환
2. genuine 2D 산지 flow solver와 biomass-dependent detachment 식의 최종 결합
3. WoodC/cohort mortality -> tree throw/CWD의 정량 변환
4. deep-root chemical weathering flux -> R/C/Cr mass or thickness production 변환
5. 2025 LPJ-GUESS P-weathering 논문의 정확한 서지정보 재복구
