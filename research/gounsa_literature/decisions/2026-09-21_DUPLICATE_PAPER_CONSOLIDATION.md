# 2026-09-21 논문 중복 통합 감사

## 목적
여러 고운사 채팅이 동시에 문헌을 GitHub로 복구하면서 동일 논문이 다른 파일명으로 중복 저장된 항목을 점검하고 canonical 파일로 통합했다.

## 검사 방법
1. `papers/` 228개 파일의 blob SHA를 비교했다.
2. 완전 동일 blob은 없었다.
3. 파일명을 `연도 + 제1저자` 기준으로 군집화해 19개 다중파일군을 조사했다.
4. 제목과 `# 서지정보`, DOI, 내용이 같은 항목만 중복으로 판정했다.
5. 같은 저자/연도라도 제목, DOI, 연구대상이 다른 논문은 유지했다.

## 통합한 동일 논문

### Kirkby 1989
canonical:
- `papers/1989_Kirkby_HillslopeRegolithModel.md`

삭제:
- `papers/1989_Kirkby_HillslopeRegolithBiomass.md`

### Gabet et al. 2003
canonical:
- `papers/2003_Gabet_BioturbationSedimentTransport.md`

삭제:
- `papers/2003_Gabet_RootBioturbation.md`

### Lamb et al. 2011
canonical:
- `papers/2011_Lamb_Dry_Ravel_Postfire.md`

삭제:
- `papers/2011_Lamb_PostfireDryRavel.md`

### Hwang et al. 2015
canonical:
- `papers/2015_Hwang_RootBiomass_SlopeStability.md`

삭제:
- `papers/2015_Hwang_RootBiomass.md`

정확한 서지를 DOI 10.1002/2014JG002824 기준으로 보완했다.

### Hales 2018
canonical:
- `papers/2018_Hales_Biome_Root_Reinforcement_Slope_Stability.md`

삭제:
- `papers/2018_Hales_RootBiomass.md`
- `papers/2018_Hales_RootReinforcementSlopeStability.md`

중복본의 modified Wu/Waldron 식과 상세 mechanics 설명을 canonical 파일에 병합했다.

## 확인했으나 중복이 아닌 논문
- Abe & Ziemer 1991 두 파일
- Cho & Mostaghimi 2009 DANSAT development/application
- Wu 2020 두 논문
- Wu/OpenLISEM 2021 Part 1/Part 2
- Parhizkar 2021 두 논문
- Ma 2022 두 논문
- Parhizkar 2024 두 논문
- Pawlik 2024 두 논문
- Wang 2026 두 논문
- Zhang 2026 두 논문

## 결과
- 정리 전 paper files: 228
- 삭제된 duplicate files: 6
- 정리 후 paper files: 222

## 원칙
향후 동일 DOI가 확인되면 파일명이 달라도 canonical paper file 하나로 병합한다.
같은 저자와 연도라는 이유만으로 합치지 않는다.
