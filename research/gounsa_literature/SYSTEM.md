# Gounsa Literature Archive Operating System

이 파일은 고운사 관련 모든 ChatGPT 채팅이 공통으로 따라야 할 문헌관리 규칙이다.

## 1. 작업 시작 시

항상 다음 순서로 확인한다.

1. `MASTER.md`
2. `INDEX.md`
3. `decisions/`의 최신 결정 파일
4. 관련 `papers/` 또는 `models/` 파일
5. 필요할 때만 새 검색 시작

이미 검토된 논문과 이미 끝난 갈림길을 다시 조사하지 않는다.

## 2. 논문별 저장 규칙

새 논문을 확인하면 반드시 `papers/` 아래에 논문별 Markdown 파일을 만든다.

권장 파일명:

`YEAR_FirstAuthor_ShortTitle.md`

각 파일은 최소한 다음 항목을 포함한다.

```
# 서지정보
# 이 논문을 찾은 이유
# 연구 유형
- 수치모델 / 현장실험 / 리뷰 / 방법론 / 기타

# 공간 구조
- 1D / 2D / distributed / D8 / finite-volume / 기타

# 적용 환경
- 산지 / 산림 / 농경지 / 산불 후 / 실험사면 / 기타

# 핵심 과정
- interrill
- rill
- concentrated flow
- splash
- hillslope diffusion
- landslide
- spall
- 기타

# 식생 입력
- root biomass
- live root
- dead root
- RLD
- root cohesion
- litter biomass
- AGB
- vegetation cover
- 기타

# 핵심 식
# 파라미터와 단위
# 원 논문의 구현 범위
# 고운사에 직접 사용할 수 있는 부분
# 새로운 coupling이 필요한 부분
# 한계
# 최종 판정
- 채택 / 보조근거 / 보류 / 탈락
# 참고 링크 / DOI
```

## 3. 모델 계보 파일

논문 여러 편에 걸친 모델은 `models/`에 별도 파일을 만든다.

예:
- `WEPP.md`
- `OpenLISEM.md`
- `PROMET.md`
- `Iber.md`
- `Wu_2D.md`

여기에는 버전별 차이와 논문별 확장을 누적한다.

## 4. 결정 기록

모델 선택이나 제외 결정이 바뀌면 `decisions/`에 별도 파일을 만든다.

예:
`2026-09-21_EROSION_ENGINE_DECISION.md`

각 결정 파일에는 다음을 쓴다.

- 결정 내용
- 왜 결정했는가
- 어떤 논문이 근거인가
- 무엇을 제외했는가
- 아직 해결되지 않은 문제
- 기존 결론을 뒤집는다면 무엇이 바뀌었는가

## 5. MASTER 갱신

`MASTER.md`는 논문 원문 요약을 전부 반복하는 문서가 아니다.

MASTER에는 다음만 누적한다.

- 현재 확정된 모델 구조
- 채택 논문과 역할
- 탈락 논문과 핵심 이유
- unresolved gaps
- 다음 조사 우선순위
- 최신 결정 파일 링크
- 전체 논문 인덱스 링크

## 6. 세션 종료 규칙

채팅이 길어지기 전에 반드시 `sessions/`에 인계서를 저장한다.

파일명:

`YYYY-MM-DD_HHMM_SESSION_HANDOFF.md`

포함 항목:

- 이번 세션에서 새로 찾은 논문
- 새로 확인한 식
- 판정 변화
- GitHub에 저장한 파일 목록
- 아직 검증하지 못한 것
- 다음 채팅이 바로 시작할 지점

## 7. 절대 금지

- COPLAS를 최종 고운사 모델 근거로 다시 사용하지 않는다.
- MUSLE를 산지 유수침식 최종식으로 사용하지 않는다.
- vegetation cover를 root biomass 또는 RLD와 동일시하지 않는다.
- 현장실험 회귀식을 이미 검증된 수치모델이라고 쓰지 않는다.
- 논문에 없는 coupling을 기존 모델 기능이라고 쓰지 않는다.
- Wu와 WEPP 등의 조합을 기존 단일 published model이라고 부르지 않는다.
- McGuire rill network를 단순 mask generator라고 부르지 않는다.
- distributed라는 이유만으로 D8/1D routing을 genuine 2D라고 부르지 않는다.
- 이미 MASTER/decision에서 확정된 내용을 이유 없이 재검색하지 않는다.

## 8. 고운사 현재 핵심 목표

최우선 유수침식 문제:

```
genuine 2D
+ mountain/steep forest
+ quantitative vegetation state
+ interrill/rill or rainfall/flow separation
```

이 네 조건을 한 번에 만족하는 published model을 우선 탐색한다.

없다면 기능별 published equations를 사용하되, 결합부를 반드시 `새로운 coupling`으로 표시한다.
