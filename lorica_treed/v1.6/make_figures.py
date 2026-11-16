#!/usr/bin/env python3
"""Figures for the v1.6 landslide-response runs (reads committed results only)."""
import csv, sys, math
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

for f in ["/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"]:
    if Path(f).exists():
        font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Noto Sans CJK JP"
plt.rcParams["axes.unicode_minus"] = False

RUN = Path(sys.argv[1])            # results/runs/<id>_ab
OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
EXTRA = [Path(p) for p in sys.argv[3:]]   # optional C run roots (lorica-v16-C_* dirs)

INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3de", "#fcfcfb"
S1, S2, S3, S4 = "#2a78d6", "#eb6834", "#1baf7a", "#6250d6"


def rcsv(p):
    with open(p, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def asc(p):
    L = Path(p).read_text().splitlines()[6:]
    return [[float(v) for v in l.split()] for l in L if l.strip()]


def style(ax):
    ax.set_facecolor(SURF)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=8)
    ax.grid(True, color=GRID, lw=0.6)
    ax.set_axisbelow(True)


A = RUN / "lorica-v16-A_no_landslide" / "run"
B = RUN / "lorica-v16-B_landslide_original" / "run"
cellsA = {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in rcsv(A / "cell_timeseries.csv")}
cellsB = {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in rcsv(B / "cell_timeseries.csv")}
status = dict(l.split("=", 1) for l in (B / "run_status.txt").read_text().splitlines() if "=" in l)
EY = int(status["event_year"])
years = sorted({k[0] for k in cellsB})
mask = {(r, c): int(cellsB[(EY, r, c)]["event_mask"]) for r in range(5) for c in range(5)}

# ---------------- Figure 1: event maps
fig, axs = plt.subplots(1, 4, figsize=(12, 3.3))
dem0 = asc(B / "initial_dtm_m.asc")
pre = asc(B / ("year_%02d" % EY) / "pre_slide" / "soildepth_m.asc")
post = asc(B / ("year_%02d" % EY) / "post_slide" / "soildepth_m.asc")
ero = asc(B / ("year_%02d" % EY) / "post_slide" / "ero_slid_m.asc")
sed = asc(B / ("year_%02d" % EY) / "post_slide" / "sed_slid_m.asc")
net = [[sed[r][c] + ero[r][c] for c in range(5)] for r in range(5)]
panels = [("초기 DEM (m)", dem0, "Greys", None, None),
          ("산사태 직후 토심 (m)", post, "Blues", 0, 3),
          ("사건 순변화 (퇴적+침식, m)", net, "RdBu", -2, 2),
          ("사건 마스크", [[mask[(r, c)] for c in range(5)] for r in range(5)], "Greys", 0, 3)]
for ax, (t, g, cm, lo, hi) in zip(axs, panels):
    im = ax.imshow(g, cmap=cm, vmin=lo, vmax=hi)
    ax.set_title(t, fontsize=9, color=INK)
    ax.set_xticks(range(5)); ax.set_yticks(range(5))
    ax.tick_params(labelsize=7, colors=INK2)
    for r in range(5):
        for c in range(5):
            v = g[r][c]
            txt = ("%d" % v) if t == "사건 마스크" else ("%.2f" % v if abs(v) < 100 else "%.0f" % v)
            nv = im.norm(v)
            dark = (cm in ("Blues", "Greys") and nv > 0.55) or (cm == "RdBu" and abs(nv - 0.5) > 0.3)
            ax.text(c, r, txt, ha="center", va="center", fontsize=6.5, color="white" if dark else INK)
    if t != "사건 마스크":
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03).ax.tick_params(labelsize=7)
fig.text(0.5, 0.01, "마스크: 0 미피해, 1 침식(scar), 2 퇴적, 3 침식+퇴적.  행 0 = 상부(북), 출구 = 행 4 중앙.  %d년 차 사건" % EY,
         ha="center", fontsize=8, color=INK2)
fig.tight_layout(rect=(0, 0.05, 1, 1))
fig.savefig(OUT / "fig1_event_maps.png", dpi=160, facecolor="white")
plt.close(fig)

# ---------------- Figure 2: per-cell type time series, raw vs effective
groups = {}
for k, m in mask.items():
    sd = float(cellsB[(EY + 1, k[0], k[1])]["input_soildepth_m"]) if EY + 1 in years else 1
    if m in (1, 3):
        name = "완전 박리 scar (토심 0)" if sd <= 1e-6 else "부분 침식 scar"
    elif m == 2:
        name = "퇴적 격자"
    else:
        name = "미피해"
    groups.setdefault(name, []).append(k)
order = [g for g in ["완전 박리 scar (토심 0)", "부분 침식 scar", "퇴적 격자", "미피해"] if g in groups]
vars_ = [("raw_fpc", "TREED 원시 FPC"), ("effective_fpc", "LORICA 유효 FPC"),
         ("raw_rootC_gC_m2", "TREED 원시 rootC (gC/m2)"), ("root_cohesion_kPa", "뿌리 점착력 (kPa)"),
         ("input_paw_mm", "TREED 입력 PAW (mm)"), ("input_soildepth_m", "TREED 입력 토심 (m)")]
extra_runs = []
for p in EXTRA:
    rr = p / "run"
    nm = p.name.replace("lorica-v16-", "")
    nm = {"C_rec_tau4_k032": "C 실험모듈 (τ=4년, k=0.32/년)", "C_rec_tau8_k018": "C 실험모듈 (τ=8년, k=0.18/년)"}.get(nm, nm)
    extra_runs.append((nm,
                       {(int(r["year"]), int(r["row"]), int(r["col"])): r for r in rcsv(rr / "cell_timeseries.csv")}))
cols = [S3, S4]
fig, axs = plt.subplots(len(order), len(vars_), figsize=(16, 2.4 * len(order)), squeeze=False)
xs = [y - EY for y in years]
for i, g in enumerate(order):
    for j, (v, lab) in enumerate(vars_):
        ax = axs[i][j]; style(ax)
        mA = [sum(float(cellsA[(y, r, c)][v]) for r, c in groups[g]) / len(groups[g]) for y in years]
        mB = [sum(float(cellsB[(y, r, c)][v]) for r, c in groups[g]) / len(groups[g]) for y in years]
        ax.plot(xs, mA, color=S1, lw=2, label="A 산사태 없음")
        ax.plot(xs, mB, color=S2, lw=2, label="B 원본 결합 산사태")
        for (nm, ce), col in zip(extra_runs, cols):
            mC = [sum(float(ce[(y, r, c)][v]) for r, c in groups[g]) / len(groups[g]) for y in years]
            ax.plot(xs, mC, color=col, lw=2, ls="--", label=nm)
        ax.axvline(0, color=INK2, lw=0.8, ls=":")
        ax.ticklabel_format(axis="y", useOffset=False, style="plain")
        if i == 0:
            ax.set_title(lab, fontsize=9, color=INK)
        if j == 0:
            ax.set_ylabel("%s\n(n=%d)" % (g, len(groups[g])), fontsize=8, color=INK)
        if i == len(order) - 1:
            ax.set_xlabel("사건 후 경과 연수", fontsize=8, color=INK2)
h, l = axs[0][0].get_legend_handles_labels()
fig.legend(h, l, loc="upper center", ncol=2 + len(extra_runs), fontsize=9, frameon=False)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig(OUT / "fig2_cell_type_timeseries.png", dpi=150, facecolor="white")
plt.close(fig)
print("figures written", [p.name for p in OUT.glob("*.png")])
print("groups", {g: groups[g] for g in order})

# ---------------- Figure 3: cumulative outlet sediment export after the event
def ann(p):
    return {int(r["year"]): r for r in rcsv(p / "annual_state.csv")}
series = [("A 산사태 없음", ann(A), S1, "-"), ("B 원본 결합 산사태", ann(B), S2, "-")]
for (nm, _), p, col in zip(extra_runs, EXTRA, [S3, S4]):
    series.append((nm, ann(p / "run"), col, "--"))
fig, ax = plt.subplots(figsize=(7, 3.6)); style(ax)
for nm, D, col, ls in series:
    ys = [y for y in sorted(D) if y > EY]
    cum, acc = [], 0.0
    for y in ys:
        acc += float(D[y]["explicit_water_export_kg"]); cum.append(acc)
    ax.plot([y - EY for y in ys], cum, color=col, lw=2, ls=ls, label="%s: %.1f kg" % (nm, cum[-1]))
ax.set_xlabel("사건 후 경과 연수", fontsize=9, color=INK2)
ax.set_ylabel("출구 누적 유사 배출 (kg)", fontsize=9, color=INK2)
ax.set_xlim(0, max(years) - EY)
ax.legend(fontsize=8, frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(OUT / "fig3_cumulative_export.png", dpi=160, facecolor="white")
plt.close(fig)
