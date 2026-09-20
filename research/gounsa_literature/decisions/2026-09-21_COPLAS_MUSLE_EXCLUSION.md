# 결정 내용
- COPLAS는 고운사 최종모델의 근거에서 제외한다.
- MUSLE는 고운사 최종 산지 유수침식식에서 제외한다.

# 왜 결정했는가
COPLAS는 기관별 biomass pool을 사용한다는 장점이 있으나 big-leaf 구조로 understory와 overstory를 구분하지 못하고, leaf biomass가 splash와 creep이 함께 포함된 diffusion coefficient를 동시에 낮추며, living wood의 직접 geomorphic effect가 없다. 또한 site-specific normalized biomass를 사용한다.
MUSLE는 고운사의 산지 2D runoff-detachment 구조와 맞지 않으며 최종 유수침식 engine으로 사용하지 않는다.

# 근거 논문
- Quijano-Baron et al. 2022 COPLAS
- Saco & Moreno-de las Heras 2013
- Tan et al. 2022 ELM-Erosion
- 최근 root-trait detachment 문헌들

# 무엇을 제외했는가
- COPLAS를 최종모델 근거로 다시 사용하는 것
- MUSLE 기반 최종 산지 유수침식식

# 아직 해결되지 않은 문제
- genuine 2D flow field와 quantitative vegetation state를 직접 결합하는 최종 erosion engine
- rainfall-driven/interrill와 runoff-driven/rill의 최종 분리방식

# 기존 결론 변화
COPLAS의 biomass-pool 철학은 비교개념으로만 보존한다.
