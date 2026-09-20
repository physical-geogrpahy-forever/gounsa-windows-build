# 결정: 고운사 토양, 풍화층, 석력 상태구조

날짜: 2026-09-21

## 결정 내용
고운사에서는 기존의 고정 단일 토심 구조를 사용하지 않고 최소한 다음을 분리한다.

```text
R -> C/Cr -> AB
```

필수 상태변수:
```text
H_AB
H_C
z_R
CF_surface
CF_AB
CF_C
W_AB
W_C
```

가능하면 coarse fraction은 비율만 저장하기보다 fine/coarse 질량으로 추적하고 CF를 파생변수로 계산한다.

```text
CF = M_coarse / (M_coarse + M_fine)
```

## 왜 결정했는가
고운사 현장에서는 상부토양이 얕고 석력이 많으며 뿌리가 C 또는 Cr까지 들어가는 것이 관찰되었다. 따라서 mobile soil thickness와 root-accessible depth를 동일시할 수 없다.

```text
root-accessible depth > H_AB
```
를 허용한다.

## 근거 문헌
- Yoo & Mudd (2008): PDZ와 CAZ를 구분한 기능적 토양층 구조
- Pelletier et al. (2013): regolith thickness에 따른 weathering/soil-production 구조
- Welivitiya et al. (2019): 수직 particle-size profile을 동적으로 추적하는 soilscape-landform model
- van der Meij et al. (2020): 다층 soil profile에서 gravel, sand, silt, clay와 수문을 결합
- Lapides et al. (2024): LPJ-GUESS에서 weathered-bedrock water storage와 plant access를 구현

## 풍화 경계
두 개의 경계를 구분한다.

```text
R -> C/Cr
C/Cr -> AB
```

R->C/Cr는 장기 풍화전선 이동으로, C/Cr->AB는 물리적 교란과 이동성 토양생산으로 취급한다. 같은 경험식이나 같은 생산률을 두 경계에 중복 적용하지 않는다.

## 새로운 coupling
다음은 기존 단일 published model 기능이 아니라 고운사 새로운 coupling이다.
- Pelletier 식을 H_AB + H_C shielding으로 확장
- dynamic H_AB/H_C를 LPJ-GUESS storage에 연결
- CF_surface, CF_AB, CF_C를 final erosion/hydrology engine과 연결
- root-accessible depth를 H_AB와 분리

## coarse fraction 처리
최소 두 입도군으로 시작한다.
```text
fine   < 2 mm
coarse > 2 mm
```

세립질 선택적 침식은 CF_surface를 증가시킬 수 있고, coarse export 또는 deposition은 CF_surface를 다시 낮추거나 높일 수 있다.

## 수문 주의
```text
H_fine = H (1-CF)
```
처럼 단순히 fine fraction만으로 available water capacity를 계산하지 않는다. 석력은 infiltration, preferential flow, storage, evaporation에 복합적인 영향을 줄 수 있으므로 별도의 문헌기반 함수가 필요하다.

## 아직 해결되지 않은 문제
- C/Cr->AB 생산률의 고운사 매개변수
- coarse fraction의 hydrologic pedotransfer relation
- 최종 2D erosion engine에서 fine/coarse transport를 어떻게 분리할지
- 실제 고운사 초기 CF(z) 자료

## 최종 판정
이 구조는 현재 고운사 vertical profile의 기준안으로 채택한다. 단, 각 전이율과 수문계수는 미보정 상태다.
