# 2026-09-21 Gounsa literature recovery session handoff

## 세션 목적
대화 길이 제한과 반복적인 전송 시간 초과로 유실 위험이 커진 고운사 문헌조사 결과를 GitHub에 논문별로 영구 보존하고, 모델 계보/의사결정/MASTER를 구축했다.

## 이 세션에서 직접 복구 및 검증한 핵심

### 유수침식 2D 계보
- Wu et al. 2020: genuine 2D, explicit interrill/rill, no dynamic vegetation state
- Wu & Chen 2020: evolving representative rills, but not fully emergent branching/merging raster network
- PSEM_2D: genuine 2D Saint-Venant, rainfall/runoff erosion separation, no dynamic vegetation state
- Iber+ 2024: modern GPU finite-volume 2D erosion engine, rainfall-driven/flow-driven source separation, multiclass sediment, Exner update
- SERGHEI-SE 2025/2026: modern HPC finite-volume 2D hydro-erosion, no dynamic root biomass/RLD core state
- OpenLISEM: spatial/2D postfire precedent; root cohesion input exists but is externally supplied and cover-weighted
- McGuire 2013: emergent rill network from microtopography-flow-erosion feedback
- RillGrow 2025: cellular-automaton emergent rill benchmark, D8/plot scale

### quantitative vegetation -> erosion resistance
- WEPP official documentation: live/dead root mass and buried residue directly adjust Ki/Kr
- Lee et al. 2022: WEPP erodibility/critical-shear parameter behavior
- Mao et al. 2010: VIC + WEPP coupling; vegetation/root/residue states used for erodibility adjustment
- Gould et al. 2016: VIC-WEPP lineage applied to wildfire mountain watershed in northern Rockies
- DANSAT 2009: dynamic plant/root/residue + interrill/rill/channel erosion
- PROMET/Waldmann 2010: dynamic vegetation -> RLD -> erosion resistance
- ELM-Erosion: PFT-specific root biomass -> erosion resistance

### empirical root-effect support
- Ghidey & Alberts 1997: root density/RLD vs interrill erodibility
- Gyssels et al. 2005: exponential SEP = exp(-b RP) synthesis; stronger root effect for rill than splash/interrill

### other process modules
- Hales 2018: root reinforcement/slope stability
- Lamb et al. 2011: fire-induced dry-ravel storage/release
- Bai et al. 2017: vertical root distribution auxiliary relation
- Millares et al. 2019 / WiMMed lineage: mountain distributed rill/gully/headcut processes, but not genuine 2D
- existing archive from other chats also includes Gabet, Pelletier, Pelak, LORICA/HydroLorica, tree throw, weathering, root-trait experiments

## 확정 결정

1. 다음 네 조건을 모두 만족하는 단일 published model은 현재까지 확인되지 않았다.
   - genuine 2D
   - mountain/steep forest or postfire applicability
   - quantitative vegetation state
   - interrill/rill or rainfall/flow separation

2. therefore:
   - 2D engine lineage와
   - quantitative vegetation-erodibility lineage를
   기능별로 구분한다.

3. 서로 결합하면 반드시 **새로운 coupling**이라고 기록한다.

4. COPLAS는 최종 고운사 모델 근거에서 제외한다.

5. MUSLE는 최종 산지 유수침식식에서 제외한다.

6. Wu vs WEPP를 다시 양자택일 문제로 열지 않는다.
   - Wu: 2D erosion skeleton lineage
   - WEPP: quantitative vegetation -> Ki/Kr lineage

7. root effect on Ki/Kr를 별도 근거 없이 tau_c까지 자동 확장하지 않는다.

8. OpenLISEM external root cohesion map을 dynamic root biomass model이라고 부르지 않는다.

9. WiMMed/D8 routing을 genuine 2D라고 부르지 않는다.

10. McGuire output -> Wu rill mask는 원 published workflow가 아니라 새로운 coupling이다.

## 이 세션에서 생성한 model files
- models/WEPP.md
- models/VIC_WEPP.md
- models/DANSAT_ANSWERS2000.md
- models/Wu_2D.md
- models/PSEM_2D.md
- models/Iber.md
- models/OpenLISEM.md
- models/PROMET_DANUBIA.md
- models/WiMMed_HEMINGS.md
- models/McGuire_RillNetwork.md
- models/RillGrow.md
- models/SERGHEI_SE.md
- models/ELM_Erosion.md

## 이 세션에서 생성한 decision files
- decisions/2026-09-21_STRICT_2D_QUANTITATIVE_VEGETATION.md
- decisions/2026-09-21_EXCLUSIONS.md
- decisions/2026-09-21_COUPLING_BOUNDARY.md
- decisions/2026-09-21_PROCESS_ARCHITECTURE.md

## MASTER
MASTER.md를 단순 골격에서 실제 통합 문헌 요약본으로 교체했다.
현재 모델구조, 확정 식, 채택/탈락, unresolved gaps, 각 과정 모듈의 역할을 한 문서에서 볼 수 있다.

## 중요한 unresolved gaps
1. thermal fire-spall production의 정량식/수치모델
2. LPJ-GUESS FineRootC -> erosion-model root mass/RLD의 단위와 depth mapping
3. fire mortality 후 dead-root pool temporal dynamics
4. litter biomass -> rainfall/interrill protection의 가장 방어적인 non-cover-only published interface
5. 최종 2D engine 선택 및 구현비용 비교
6. coarse-fragment supply vs armour dynamics
7. shallow-landslide root architecture conversion
8. 100-year scale long-term creep/weathering magnitude

## Git branch
이 세션은 다른 채팅의 동시 main 쓰기 충돌을 피하기 위해 다음 전용 브랜치에서 저장했다.

`gounsa-literature-recovery-2026-09-21-chat`

다음 작업자는 main merge 여부를 먼저 확인하고, 이미 merge됐다면 main의 SYSTEM/MASTER/INDEX를 기준으로 이어간다.

## 다음 채팅이 바로 시작할 지점
새 문헌조사를 시작하기 전에 반드시:
1. SYSTEM.md
2. MASTER.md
3. INDEX.md
4. decisions/
를 읽는다.

그 뒤 unresolved gaps 중 하나만 골라 조사한다.
이미 끝난 Wu-WEPP-Mao-Gould 검증을 반복하지 않는다.
