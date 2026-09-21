# 서지정보
Johnstone, S. A., & Hilley, G. E. (2015). *Lithologic control on the form of soil-mantled hillslopes*. Geology, 43, 83-86. DOI: 10.1130/G36052.1.

# 이 논문을 찾은 이유
고운사처럼 얕은 mobile soil이 있는 사면에서 transport flux가 soil thickness에 의해 제한되는 published hillslope-transport structure를 확인하기 위해 검토했다.

# 연구 유형
- hillslope transport theory
- lithologic/topographic analysis
- numerical/analytic landscape interpretation

# 공간 구조
- soil-mantled hillslopes
- local slope and soil-thickness dependent flux

# 핵심 과정
- depth-dependent hillslope sediment transport
- lithologic control through soil thickness
- slope-dependent creep

# 핵심 구조
The model lineage motivates a depth-dependent hillslope flux in which the mobile-soil thickness limits the vertically integrated transport.

Landlab later implements this lineage as:

```
q_s
=
K H_* (1 - exp(-H/H_*)) S
```

where:
- `K`: transport velocity coefficient
- `H_*`: soil transport decay depth
- `H`: mobile soil thickness
- `S`: slope

For shallow soil:

```
H << H_*
```

then:

```
1-exp(-H/H_*) approx H/H_*
```

and therefore:

```
q_s approx K H S
```

This recovers the desired soil-availability-limited behavior.

# 고운사에 직접 사용할 수 있는 부분
This is a stronger implementation basis than a constant diffusivity because:

```
H -> 0
=> q_s -> 0
```

For the current Gounsa condition:

```
sandstone + shallow soil
```

the thin-soil approximation means the flux is approximately proportional to available mobile-soil thickness.

# relation to Furbish 2009
Furbish provides the statistical/kinematic basis for depth-dependent transport.

Johnstone-Hilley provides a practical exponential-depth transport structure that is already implemented in Landlab.

Both are compatible in the thin-soil limit.

# limitations
- no dynamic vegetation
- no root-growth transport
- no dry ravel
- no wildfire
- coefficient K remains an effective residual parameter

# current judgment
**채택: practical depth-dependent residual-creep functional form.**

For Gounsa it can replace the simplified:

```
q_bg = -D*_bg H grad(z)
```

with the full saturating form:

```
q_bg
=
-K_bg H_* (1-exp(-H_active/H_*)) grad(z)
```

The linear-in-H expression remains its shallow-soil approximation.

# 참고 링크 / DOI
https://doi.org/10.1130/G36052.1
