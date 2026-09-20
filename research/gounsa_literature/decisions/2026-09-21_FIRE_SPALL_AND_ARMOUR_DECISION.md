# 결정: fire spall과 surface armour

날짜: 2026-09-21

## 결정 내용
fire spall은 기존 토양석력이나 C/Cr와 합치지 않고 별도 coarse-sediment reservoir로 추적한다.

최소 상태:
```text
M_spall
CF_surface
```

가능하면 mobile과 stable 상태를 분리한다.

## 근거
- 박경 등 (2009): 국내 산불지 flaking 현장근거
- Shtober-Zisu et al. (2018): spall의 장기 잔류와 재, 세립질 물질 포획
- Buckman et al. (2021): spall 두께, 면적, 질량과 장기 침식률
- Pala et al. (2025): spall이 산불 후 토석류 퇴적물로 이동하는 현장증거
- Nyssen et al. (2001), Zavala et al. (2010): 일반 표면 석력의 soil-loss 억제효과

## 생성
고운사 제안식:
```text
Delta M_sp = rho_r A_exposed d_sp f_sp
```
이는 Buckman의 두께와 면적 개념을 사건단위 질량보존으로 바꾼 새로운 coupling이다.

## 질량보존
spall이 C/Cr 또는 R에서 생성되면 source layer에서 같은 질량이 빠져야 한다.

## 이동과 잔류
```text
M_sp(t+1) = M_sp(t) + P_sp - E_sp - B_sp
```
이 reservoir 식도 고운사 새로운 coupling이다.

## armour
surface coarse fraction이 커지면 fine-soil erodibility가 낮아질 수 있다.
```text
K_fine,eff = K_fine g(CF_surface),  g' < 0
```
정확한 함수형태는 아직 확정하지 않는다.

## 문헌공백
현재 확인 범위에서는 산불피해 사면에서 spall을 유지한 처리와 제거한 처리를 직접 비교해 runoff와 fine-soil loss 변화를 정량화한 연구를 찾지 못했다. Pala et al.은 이동을 보여주지만 spall만의 독립효과를 분리하지 않는다.

## 새로운 coupling
- mobile/stable spall 분리
- source-layer 질량보존
- coarse entrainment
- armour 함수
모두 published fire-spall model의 기존 기능이라고 부르면 안 된다.

## 최종 판정
fire spall은 생성, 이동, 잔류/armour를 분리한 별도 과정으로 채택한다. 정량 transport와 armour 함수는 미확정이다.
