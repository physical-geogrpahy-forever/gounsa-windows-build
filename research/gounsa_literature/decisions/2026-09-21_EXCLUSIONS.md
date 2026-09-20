# 결정: 제외 모델과 금지된 해석

날짜: 2026-09-21

## COPLAS
고운사 최종모델에서 완전히 제외한다.

제외 범위:
- 식
- 철학
- parameterization

문헌사적 감사파일은 저장해도 되지만 최종 모델 근거로 사용하지 않는다.

## MUSLE
고운사 산지 유수침식 최종식에서 사용하지 않는다.

## cover-only 접근
vegetation cover fraction 하나로:
- interrill
- rill
- root reinforcement
- hillslope transport
를 모두 조정하는 접근은 최종 구조에서 사용하지 않는다.

## HyLands
현재 고운사 목적에서는 우선순위가 낮다.
Pelletier/기존 장기사면 계열과 역할이 겹치고 quantitative vegetation-controlled rill/interrill 문제를 해결하지 않는다.

## 주의할 오해
- distributed model이라고 genuine 2D라고 부르지 않는다.
- D8/local routing을 2D SWE로 부르지 않는다.
- external root cohesion map을 dynamic root biomass model이라고 부르지 않는다.
- field regression을 실제 numerical-model implementation이라고 부르지 않는다.
- McGuire rill network를 단순 Wu mask generator라고 부르지 않는다.
- root biomass effect on Ki/Kr를 root effect on tau_c로 자동 확대하지 않는다.

## 근거
SYSTEM.md의 절대금지 규칙과 이 채팅의 반복 검증 결과.
