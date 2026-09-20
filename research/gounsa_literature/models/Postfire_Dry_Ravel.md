# Postfire dry-ravel and loose-sediment lineage

## 핵심 기준 논문
Lamb et al. (2011), A model for fire-induced sediment yield by dry ravel in steep landscapes.

## 과정 구분
이 계보는 유수침식이 아니라 vegetation에 의해 사면에 저장되던 loose sediment가 산불 뒤 방출되는 중력성 sediment-storage process다.

## 핵심 구조
`Vc = Vci * c * Ab`

산불로 vegetation storage capacity가 줄면 저장되던 sediment가 channel 방향으로 방출된다.

## 고운사 적용
고운사에서 관찰된 fire spall, loose gravel, detached mineral soil을 `S_loose`라는 별도 pool로 두고 postfire dry-ravel/spall redistribution을 계산하는 구조에 사용한다.

## 새로운 coupling
LPJ-GUESS vegetation state에서 sediment-storage capacity를 계산하는 변환은 Lamb 원 논문에 없으므로 새로운 coupling이다.

## 제한
- San Gabriel chaparral parameter 직접 사용 금지
- angle-of-repose 및 steep-slope applicability를 확인해야 함

## 관련 논문
- ../papers/2011_Lamb_PostfireDryRavel.md
- ../papers/2005_Roering_Gerber_PostfireHillslopeTransport.md

## 판정
- postfire loose-sediment/spall 구조: 채택
