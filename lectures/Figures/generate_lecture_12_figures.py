"""
Generate figures for Lecture 12: Options — General Properties.

This script creates:
1. option_payoffs.png        — All four basic payoff diagrams (no premium)
2. option_profits.png       — All four profit diagrams (including premium)
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── Parameters ────────────────────────────────────────────────────────────────
K = 100     # strike price
c = 7       # call premium
p = 5       # put premium

S = np.linspace(50, 160, 1_000)   # range of stock prices at maturity


# ── Helper computations ───────────────────────────────────────────────────────
call_payoff  = np.maximum(S - K, 0)
put_payoff   = np.maximum(K - S, 0)

long_call_profit  =  call_payoff - c
long_put_profit   =  put_payoff  - p
short_call_profit = -call_payoff + c
short_put_profit  = -put_payoff  + p


# ── Shared style ──────────────────────────────────────────────────────────────
BLUE   = "#1f4e79"
RED    = "#b22222"
GREEN  = "#1a7a4a"
ORANGE = "#c76b00"
ZERO_COLOR = "#555555"
ALPHA_FILL = 0.15

def _decorate(ax, title, xlabel="$S_T$", ylabel="Payoff ($)"):
    ax.axhline(0, color=ZERO_COLOR, linewidth=1.0, linestyle="--", alpha=0.7)
    ax.axvline(K, color=ZERO_COLOR, linewidth=1.0, linestyle=":", alpha=0.7)
    ax.set_title(title, fontsize=12, fontweight="bold", pad=8)
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.tick_params(labelsize=9)
    ax.set_xlim([S[0], S[-1]])
    ax.grid(alpha=0.25)
    # strike annotation
    ax.text(K + 0.8, ax.get_ylim()[0] + 2, "$K$", fontsize=9, color=ZERO_COLOR)


# ── Figure 1: Payoff diagrams ─────────────────────────────────────────────────
def generate_payoff_diagrams(output_dir: Path) -> Path:
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Option Payoff Diagrams at Maturity",
                 fontsize=14, fontweight="bold", y=1.01)

    # ── Long call ──────────────────────────────────────────────────────────────
    ax = axes[0, 0]
    ax.plot(S, call_payoff, color=BLUE, linewidth=2.5, label="Long call payoff")
    ax.fill_between(S, 0, call_payoff, where=(call_payoff > 0),
                    color=BLUE, alpha=ALPHA_FILL)
    ax.annotate(f"Exercise if $S_T > K$",
                xy=(K + 15, 15), fontsize=8.5, color=BLUE)
    _decorate(ax, "Long Call\n$\\max(S_T - K,\\;0)$")
    ax.set_ylabel("Payoff ($)")

    # ── Short call ─────────────────────────────────────────────────────────────
    ax = axes[0, 1]
    ax.plot(S, -call_payoff, color=RED, linewidth=2.5, label="Short call payoff")
    ax.fill_between(S, 0, -call_payoff, where=(-call_payoff < 0),
                    color=RED, alpha=ALPHA_FILL)
    ax.annotate("Unlimited downside →", xy=(K + 12, -20), fontsize=8.5, color=RED)
    _decorate(ax, "Short Call\n$-\\max(S_T - K,\\;0)$")
    ax.set_ylabel("Payoff ($)")

    # ── Long put ───────────────────────────────────────────────────────────────
    ax = axes[1, 0]
    ax.plot(S, put_payoff, color=GREEN, linewidth=2.5, label="Long put payoff")
    ax.fill_between(S, 0, put_payoff, where=(put_payoff > 0),
                    color=GREEN, alpha=ALPHA_FILL)
    ax.annotate(f"Exercise if $S_T < K$",
                xy=(S[0] + 2, 20), fontsize=8.5, color=GREEN)
    _decorate(ax, "Long Put\n$\\max(K - S_T,\\;0)$")
    ax.set_ylabel("Payoff ($)")

    # ── Short put ──────────────────────────────────────────────────────────────
    ax = axes[1, 1]
    ax.plot(S, -put_payoff, color=ORANGE, linewidth=2.5, label="Short put payoff")
    ax.fill_between(S, 0, -put_payoff, where=(-put_payoff < 0),
                    color=ORANGE, alpha=ALPHA_FILL)
    ax.annotate("← Max loss = $K$", xy=(S[0] + 2, -35), fontsize=8.5, color=ORANGE)
    _decorate(ax, "Short Put\n$-\\max(K - S_T,\\;0)$")
    ax.set_ylabel("Payoff ($)")

    # fix y-axis tick annotation after limits are set
    for ax in axes.flat:
        ylim = ax.get_ylim()
        for txt in ax.texts:
            if txt.get_text() == "$K$":
                txt.set_position((K + 0.8, ylim[0] + (ylim[1] - ylim[0]) * 0.03))

    plt.tight_layout()
    out = output_dir / "option_payoffs.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# ── Figure 2: Profit diagrams ─────────────────────────────────────────────────
def generate_profit_diagrams(output_dir: Path) -> Path:
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Option Profit Diagrams at Maturity (after premium)",
                 fontsize=14, fontweight="bold", y=1.01)

    breakeven_call = K + c    # S_T where long call breaks even
    breakeven_put  = K - p    # S_T where long put breaks even

    # ── Long call profit ───────────────────────────────────────────────────────
    ax = axes[0, 0]
    ax.plot(S, long_call_profit, color=BLUE, linewidth=2.5)
    ax.fill_between(S, 0, long_call_profit, where=(long_call_profit > 0),
                    color=BLUE, alpha=ALPHA_FILL, label="Profit zone")
    ax.fill_between(S, long_call_profit, 0, where=(long_call_profit < 0),
                    color=RED, alpha=ALPHA_FILL, label="Loss zone")
    ax.axhline(-c, color=BLUE, linestyle="--", linewidth=1.2, alpha=0.6)
    ax.axvline(breakeven_call, color="grey", linestyle=":", linewidth=1.2, alpha=0.7)
    ax.text(breakeven_call + 0.5, ax.get_ylim()[0] * 0.7 if ax.get_ylim()[0] < 0 else 1,
            f"BE = {breakeven_call}", fontsize=8, color="grey")
    ax.text(S[0] + 1, -c - 3, f"Max loss = $c = {c}$", fontsize=8.5, color=BLUE)
    _decorate(ax, f"Long Call Profit\n$\\max(S_T-K,0) - c$  [$c={c}$]",
              ylabel="Profit ($)")

    # ── Short call profit ──────────────────────────────────────────────────────
    ax = axes[0, 1]
    ax.plot(S, short_call_profit, color=RED, linewidth=2.5)
    ax.fill_between(S, 0, short_call_profit, where=(short_call_profit > 0),
                    color=BLUE, alpha=ALPHA_FILL, label="Profit zone")
    ax.fill_between(S, short_call_profit, 0, where=(short_call_profit < 0),
                    color=RED, alpha=ALPHA_FILL, label="Loss zone")
    ax.axhline(c, color=RED, linestyle="--", linewidth=1.2, alpha=0.6)
    ax.axvline(breakeven_call, color="grey", linestyle=":", linewidth=1.2, alpha=0.7)
    ax.text(breakeven_call + 0.5, c * 0.3,
            f"BE = {breakeven_call}", fontsize=8, color="grey")
    ax.text(S[0] + 1, c + 1.5, f"Max gain = $c = {c}$", fontsize=8.5, color=RED)
    _decorate(ax, f"Short Call Profit\n$c - \\max(S_T-K,0)$  [$c={c}$]",
              ylabel="Profit ($)")

    # ── Long put profit ────────────────────────────────────────────────────────
    ax = axes[1, 0]
    ax.plot(S, long_put_profit, color=GREEN, linewidth=2.5)
    ax.fill_between(S, 0, long_put_profit, where=(long_put_profit > 0),
                    color=GREEN, alpha=ALPHA_FILL, label="Profit zone")
    ax.fill_between(S, long_put_profit, 0, where=(long_put_profit < 0),
                    color=RED, alpha=ALPHA_FILL, label="Loss zone")
    ax.axhline(-p, color=GREEN, linestyle="--", linewidth=1.2, alpha=0.6)
    ax.axvline(breakeven_put, color="grey", linestyle=":", linewidth=1.2, alpha=0.7)
    ax.text(breakeven_put + 0.5, ax.get_ylim()[0] * 0.7 if ax.get_ylim()[0] < 0 else 1,
            f"BE = {breakeven_put}", fontsize=8, color="grey")
    ax.text(S[0] + 1, -p - 3, f"Max loss = $p = {p}$", fontsize=8.5, color=GREEN)
    _decorate(ax, f"Long Put Profit\n$\\max(K-S_T,0) - p$  [$p={p}$]",
              ylabel="Profit ($)")

    # ── Short put profit ───────────────────────────────────────────────────────
    ax = axes[1, 1]
    ax.plot(S, short_put_profit, color=ORANGE, linewidth=2.5)
    ax.fill_between(S, 0, short_put_profit, where=(short_put_profit > 0),
                    color=BLUE, alpha=ALPHA_FILL, label="Profit zone")
    ax.fill_between(S, short_put_profit, 0, where=(short_put_profit < 0),
                    color=RED, alpha=ALPHA_FILL, label="Loss zone")
    ax.axhline(p, color=ORANGE, linestyle="--", linewidth=1.2, alpha=0.6)
    ax.axvline(breakeven_put, color="grey", linestyle=":", linewidth=1.2, alpha=0.7)
    ax.text(breakeven_put + 0.5, p * 0.3,
            f"BE = {breakeven_put}", fontsize=8, color="grey")
    ax.text(S[0] + 1, p + 1.5, f"Max gain = $p = {p}$", fontsize=8.5, color=ORANGE)
    _decorate(ax, f"Short Put Profit\n$p - \\max(K-S_T,0)$  [$p={p}$]",
              ylabel="Profit ($)")

    # fix breakeven label y-positions after layout
    plt.tight_layout()
    out = output_dir / "option_profits.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    output_dir = Path(__file__).resolve().parent
    output_dir.mkdir(parents=True, exist_ok=True)

    p1 = generate_payoff_diagrams(output_dir)
    print(f"Generated: {p1}")

    p2 = generate_profit_diagrams(output_dir)
    print(f"Generated: {p2}")


if __name__ == "__main__":
    main()
