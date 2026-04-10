"""
Generate figures for Lecture 14: Financial Engineering.

This script creates:
1. straddle_profit.png  — Long straddle profit diagram at maturity
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── Parameters ────────────────────────────────────────────────────────────────
K = 100       # strike price
c = 4.5       # call premium
p = 4.0       # put premium
total_premium = c + p  # 8.5

S = np.linspace(70, 130, 1_000)   # range of stock prices at maturity

# ── Helper computations ───────────────────────────────────────────────────────
call_payoff = np.maximum(S - K, 0)
put_payoff  = np.maximum(K - S, 0)
straddle_payoff = call_payoff + put_payoff          # |S_T - K|
straddle_profit = straddle_payoff - total_premium   # |S_T - K| - 8.5

breakeven_low  = K - total_premium   # 91.5
breakeven_high = K + total_premium   # 108.5

# ── Shared style ──────────────────────────────────────────────────────────────
BLUE   = "#1f4e79"
RED    = "#b22222"
GREEN  = "#1a7a4a"
ZERO_COLOR = "#555555"
ALPHA_FILL = 0.15


# ── Figure 1: Long Straddle Profit ───────────────────────────────────────────
def generate_straddle_profit(output_dir: Path) -> Path:
    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Main profit line
    ax.plot(S, straddle_profit, color=BLUE, linewidth=2.5,
            label="Long straddle profit")

    # Shade profit zones (green) and loss zone (red)
    ax.fill_between(S, 0, straddle_profit,
                    where=(straddle_profit > 0),
                    color=GREEN, alpha=ALPHA_FILL, label="Profit zone")
    ax.fill_between(S, 0, straddle_profit,
                    where=(straddle_profit < 0),
                    color=RED, alpha=ALPHA_FILL, label="Loss zone")

    # Zero line and strike line
    ax.axhline(0, color=ZERO_COLOR, linewidth=1.0, linestyle="--", alpha=0.7)
    ax.axvline(K, color=ZERO_COLOR, linewidth=1.0, linestyle=":", alpha=0.5)

    # Break-even markers
    ax.axvline(breakeven_low, color=GREEN, linewidth=1.0, linestyle=":",
               alpha=0.6)
    ax.axvline(breakeven_high, color=GREEN, linewidth=1.0, linestyle=":",
               alpha=0.6)

    # Premium line (maximum loss)
    ax.axhline(-total_premium, color=RED, linewidth=0.8, linestyle="--",
               alpha=0.5)

    # Annotations
    ax.annotate(f"Max loss = ${total_premium:.1f}$",
                xy=(K, -total_premium), xytext=(K + 3, -total_premium - 2.5),
                fontsize=9, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))

    ax.annotate(f"$S_T = {breakeven_low:.1f}$",
                xy=(breakeven_low, 0), xytext=(breakeven_low - 8, 4),
                fontsize=9, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=0.8))

    ax.annotate(f"$S_T = {breakeven_high:.1f}$",
                xy=(breakeven_high, 0), xytext=(breakeven_high + 2, 4),
                fontsize=9, color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=0.8))

    ax.text(K + 0.5, ax.get_ylim()[0] + 1, "$K$",
            fontsize=9, color=ZERO_COLOR)

    # Labels and formatting
    ax.set_title("Long Straddle: Profit at Maturity\n"
                 f"$K = {K}$, call premium $= {c}$, put premium $= {p}$",
                 fontsize=12, fontweight="bold", pad=10)
    ax.set_xlabel("$S_T$", fontsize=11)
    ax.set_ylabel("Profit ($)", fontsize=11)
    ax.tick_params(labelsize=9)
    ax.set_xlim([S[0], S[-1]])
    ax.grid(alpha=0.25)
    ax.legend(fontsize=9, loc="upper left")

    fig.tight_layout()
    out = output_dir / "straddle_profit.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved {out}")
    return out


# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    output_dir = Path(__file__).resolve().parent
    print("Generating Lecture 14 figures ...")
    generate_straddle_profit(output_dir)
    print("Done.")
