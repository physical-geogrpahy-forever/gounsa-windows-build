# SIBERIA model lineage

## 범위
고운사 문헌검토에서 SIBERIA 및 그 vegetation coupling 확장계보를 통합한다.

## 기본 지형식
대표적으로 다음 mass-balance 구조를 사용한다.

`dz/dt = -(div qs + div qd) + U`

fluvial sediment transport는 `qs = beta1 q^m1 S^n1`, diffusive transport는 단순형에서 `qd = D S`로 표현된다.

## 확인된 vegetation coupling
### Saco & Moreno-de las Heras (2013)
absolute plant biomass density P가 erodibility-related parameter beta1을 직접 낮춘다. 지역별 biomass maximum normalization은 사용하지 않는다.

### COPLAS (Quijano-Baron et al., 2022)
root, leaf, litter, soil-carbon pool을 서로 다른 geomorphic parameters에 연결한다. 그러나 site-normalized biomass 처리와 big-leaf 구조 때문에 고운사 최종모델 근거에서 제외한다.

## 고운사에 사용할 수 있는 부분
- 지형 mass-balance 골격
- absolute biomass를 erodibility에 직접 넣는 published precedent
- 여러 vegetation pools를 process-specific하게 분리해야 한다는 설계 철학

## 새로운 coupling
PFT별 FineRootC, LeafC, LitterC를 각각 다른 SIBERIA coefficients로 연결하는 것은 Saco 2013의 원래 식과 동일하지 않으며 새로운 coupling이다.

## 제한
- 반건조 patterned vegetation 문헌이 주류
- 고운사 산림 PFT 및 understory를 그대로 표현하지 않음
- COPLAS normalization은 사용하지 않음

## 관련 논문
- ../papers/2013_Saco_MorenoDeLasHeras_EcogeomorphicCoevolution.md
- ../papers/2022_QuijanoBaron_COPLAS.md

## 판정
- Saco 2013: 보조근거
- COPLAS: 탈락
