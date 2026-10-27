# [2026-10-27 범위 정정] 기존 인계서의 장기 모델 중심 해석 폐기

원래 이 문서는 사용자의 18:00 마감을 장기 식생-토양-지형 결합으로 잘못 해석했습니다. **실제 과업: 1ha 미만 고운사 단일 사면에 참나무 맹아와 억새가 혼재한 상태의 동일 단일 강우사상, 수관차단 OFF/ON 2개 2D 침식·퇴적 사건 모의를 비교**.

읽어야 할 새 정본: [2026-10-27 단일 강우사상 혼재식생 수관차단 대조 모델 설계 및 자료검증](../decisions/2026-10-27_SINGLE_STORM_MIXED_OAK_MISCANTHUS_CANOPY_ABLATION_PROTOCOL.md).

**변경하지 말아야 하는 조건:** 사면 DEM, 사전 식생배치, 뿌리/낙엽/지표조도, 토양 및 암편, 초기수분, 강우. **달라지는 조건:** 시변 LAI 기반 수관저장·직접통과·적하·선택적 수간유하우 및 강우충격 에너지 분배. 구별할 출력은 국지 gross original detachment, redetachment, deposition, net z change 및 ON−OFF raster 차분. 고운사 실제 지형/식생/강우 데이터 확보 및 SWEHR modified+Rutter 결합 실행과 보존/수렴은 아직 미완료.

과거 잘못된 인계문 원본은 Git 커밋 `563d47451d18a225b1181b54aff3fc781e38f3fc`에 역사 기록으로 보존.
