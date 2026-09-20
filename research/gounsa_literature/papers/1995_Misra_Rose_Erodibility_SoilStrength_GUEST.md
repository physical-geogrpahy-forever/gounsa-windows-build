# 서지정보
Misra, R. K., & Rose, C. W. (1995). *An examination of the relationship between erodibility parameters and soil strength*. Australian Journal of Soil Research, 33(4), 715-732. DOI: 10.1071/SR9950715.

# 이 논문을 찾은 이유
Hairsine-Rose/GUEST 계열의 runoff erodibility parameter `J`가 실제 soil strength와 연결되는지 확인하여, root-enhanced soil resistance를 2D Hairsine-Rose 엔진에 연결할 물리적 경로가 있는지 검토했다.

# 연구 유형
- rainfall/runon erosion experiment
- process-based GUEST model parameter estimation
- soil-strength/erodibility relationship study

# 공간 구조
- 1 m wide, 5.8 m long laboratory soil beds
- multiple slopes
- separate rainfall-only detachment trays
- full catchment 2D model 아님

# 적용 환경
- krasnozem soil
- compacted versus uncompacted soil
- simulated rainfall and overland flow

# 핵심 과정
- rainfall-driven detachment
- runoff-driven entrainment
- rilling
- aggregate breakdown
- soil-strength controls on erodibility

# 식생 입력
없음.
이 논문은 식생모델이 아니라 soil strength와 erosion parameters의 관계를 규명한다.

# 핵심 식
GUEST/Hairsine-Rose 계열에서 runoff-driven erosion resistance is represented by:
- `J`: specific energy of entrainment, energy required to entrain unit mass of original soil
- an approximate runoff erodibility parameter beta/related parameterization

The experiment shows:
- higher soil strength -> lower rainfall detachability
- higher soil strength -> higher `J`
- higher soil strength -> lower approximate runoff erodibility

즉:
```
soil strength ↑
 -> rainfall detachability ↓
 -> J ↑
 -> runoff-driven erosion resistance ↑
```

# 파라미터와 단위
- `J`: J kg^-1 = m2 s^-2
- soil strength: measured by hand vane and pocket penetrometer
- rainfall detachability: GUEST parameter
- sediment concentration and settling-velocity distributions

# 원 논문의 구현 범위
두 개의 contrasting soil-strength states에서 GUEST erodibility parameters를 역산하여 soil strength와의 관계를 검증한다.

# 고운사에 직접 사용할 수 있는 부분
매우 중요한 bridge:
```
root-enhanced soil strength/cohesion
 -> Hairsine-Rose/GUEST specific energy of entrainment J
```
라는 방향은 물리적으로 문헌에 부합한다.

또한 root/litter/soil-structure recovery가 rainfall detachability와 runoff entrainment resistance에 서로 다른 방향과 강도로 영향을 줄 수 있다는 근거가 된다.

# 새로운 coupling이 필요한 부분
본 논문은 root state를 다루지 않는다.
따라서:
```
LPJ-GUESS RLD/RMD
 -> root-enhanced cohesion/soil strength
 -> J
```
의 root-to-strength 부분과 정량적인 strength-to-J transfer는 별도 문헌 또는 calibration이 필요하다.

**현재 이 논문만으로 universal `C -> J` 식을 만들면 안 된다.**

# 한계
- 단일 soil family와 compaction treatment
- root-reinforced soil 아님
- soil-strength instrument measurements와 erosion-specific cohesion이 항상 동일하지 않음
- J uncertainty increases where rainfall-driven erosion dominates

# 최종 판정
- **채택: soil strength -> Hairsine-Rose/GUEST erodibility bridge**
- Hairsine-Rose engine에 root mechanics를 연결할 핵심 중간근거
- universal quantitative conversion은 아직 미확정

# 참고 링크 / DOI
https://doi.org/10.1071/SR9950715
