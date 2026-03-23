"""
Generate figures for Lecture 13: Option Pricing.

Figures produced:
  two_step_tree.png       — Two-step recombining binomial tree (Section 3)
  american_put_tree.png   — American put pricing tree with early exercise (Section 6)
  greeks_surface.png      — Greeks (Delta, Gamma, Vega, Theta) vs S_0 for multiple T (Section 8)
"""

from pathlib import Path

import matplotlib
import numpy as np
from scipy.stats import norm

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# -- Shared style -------------------------------------------------------------
BLUE   = "#1f4e79"
RED    = "#b22222"
GREEN  = "#1a7a4a"
ORANGE = "#c76b00"
GREY   = "#555555"
PURPLE = "#6a3d9a"


# -- Black-Scholes helpers ----------------------------------------------------
def bs_call(S, K, T, r, sigma):
    S, T = np.asarray(S, float), np.asarray(T, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
    return np.where(T <= 0, np.maximum(S - K, 0.0),
                    S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))


def bs_d1(S, K, T, r, sigma):
    S, T = np.asarray(S, float), np.asarray(T, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))


# -- Figure 1: Two-step binomial tree -----------------------------------------
def generate_two_step_tree(output_dir: Path) -> Path:
    """Draw a two-step recombining binomial tree with stock prices and call payoffs."""
    S0 = 100; u = 1.1; d = 0.9; K = 100
    r = 0.05; dt = 0.5

    # Stock prices
    S_u = S0 * u;      S_d = S0 * d
    S_uu = S0 * u**2;  S_ud = S0 * u * d;  S_dd = S0 * d**2

    # Node positions: (x, y)
    nodes = {
        "S0":  (0.0, 0.5),
        "Su":  (0.4, 0.8),
        "Sd":  (0.4, 0.2),
        "Suu": (0.8, 1.0),
        "Sud": (0.8, 0.5),
        "Sdd": (0.8, 0.0),
    }

    prices = {
        "S0":  S0,
        "Su":  S_u,
        "Sd":  S_d,
        "Suu": S_uu,
        "Sud": S_ud,
        "Sdd": S_dd,
    }

    payoffs = {
        "Suu": max(S_uu - K, 0),
        "Sud": max(S_ud - K, 0),
        "Sdd": max(S_dd - K, 0),
    }

    edges = [
        ("S0", "Su"), ("S0", "Sd"),
        ("Su", "Suu"), ("Su", "Sud"),
        ("Sd", "Sud"), ("Sd", "Sdd"),
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-0.12, 1.05)
    ax.set_ylim(-0.15, 1.15)
    ax.axis("off")

    # Draw edges
    for n1, n2 in edges:
        x1, y1 = nodes[n1]
        x2, y2 = nodes[n2]
        color = GREEN if y2 > y1 else RED
        ax.plot([x1, x2], [y1, y2], color=color, lw=2.0, alpha=0.6, zorder=1)
        # label u or d on each edge
        mx, my = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
        label = "$u$" if y2 > y1 else "$d$"
        offset = 0.03 if y2 > y1 else -0.03
        ax.text(mx - 0.03, my + offset, label, fontsize=10, color=color,
                fontweight="bold", ha="center", va="center")

    # Draw nodes
    for name, (x, y) in nodes.items():
        S_val = prices[name]
        circle = plt.Circle((x, y), 0.045, color="white", ec=BLUE, lw=2.0, zorder=3)
        ax.add_patch(circle)
        ax.text(x, y, f"${S_val:.0f}$", fontsize=11, fontweight="bold",
                ha="center", va="center", zorder=4, color=BLUE)

    # Payoff annotations at terminal nodes
    for name in ["Suu", "Sud", "Sdd"]:
        x, y = nodes[name]
        pv = payoffs[name]
        color = BLUE if pv > 0 else GREY
        ax.text(x + 0.07, y, f"Payoff = ${pv:.0f}$", fontsize=9.5,
                ha="left", va="center", color=color,
                bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow", ec=color, alpha=0.8))

    # Time labels
    for label, x_pos in [(r"$t = 0$", 0.0), (r"$t = \Delta t$", 0.4), (r"$t = T$", 0.8)]:
        ax.text(x_pos, -0.10, label, fontsize=10, ha="center", color=GREY)

    ax.set_title(
        "Two-Step Recombining Binomial Tree\n"
        f"($S_0 = {S0}$,  $u = {u}$,  $d = {d}$,  $K = {K}$)",
        fontsize=13, fontweight="bold", pad=15,
    )

    plt.tight_layout()
    out = output_dir / "two_step_tree.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# -- Figure 2: American put tree with early exercise --------------------------
def generate_american_put_tree(output_dir: Path) -> Path:
    """Draw a two-step tree for an American put, highlighting early exercise."""
    S0 = 100; u = 1.1; d = 0.9; K = 100
    r = 0.05; dt = 0.5; q = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)

    # Stock prices
    S_u = S0 * u;      S_d = S0 * d
    S_uu = S0 * u**2;  S_ud = S0 * u * d;  S_dd = S0 * d**2

    # Terminal payoffs (put)
    f_uu = max(K - S_uu, 0)
    f_ud = max(K - S_ud, 0)
    f_dd = max(K - S_dd, 0)

    # Backward induction with early exercise
    # Up node
    cont_u = disc * (q * f_uu + (1 - q) * f_ud)
    exer_u = max(K - S_u, 0)
    early_u = exer_u > cont_u
    f_u = max(cont_u, exer_u)

    # Down node
    cont_d = disc * (q * f_ud + (1 - q) * f_dd)
    exer_d = max(K - S_d, 0)
    early_d = exer_d > cont_d
    f_d = max(cont_d, exer_d)

    # Root
    cont_0 = disc * (q * f_u + (1 - q) * f_d)
    exer_0 = max(K - S0, 0)
    early_0 = exer_0 > cont_0
    f_0 = max(cont_0, exer_0)

    # Node positions
    nodes = {
        "S0":  (0.0, 0.5),
        "Su":  (0.4, 0.8),
        "Sd":  (0.4, 0.2),
        "Suu": (0.8, 1.0),
        "Sud": (0.8, 0.5),
        "Sdd": (0.8, 0.0),
    }

    stock_prices = {"S0": S0, "Su": S_u, "Sd": S_d, "Suu": S_uu, "Sud": S_ud, "Sdd": S_dd}
    option_vals  = {"S0": f_0, "Su": f_u, "Sd": f_d, "Suu": f_uu, "Sud": f_ud, "Sdd": f_dd}
    early_flags  = {"S0": early_0, "Su": early_u, "Sd": early_d, "Suu": False, "Sud": False, "Sdd": False}

    edges = [
        ("S0", "Su"), ("S0", "Sd"),
        ("Su", "Suu"), ("Su", "Sud"),
        ("Sd", "Sud"), ("Sd", "Sdd"),
    ]

    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(-0.15, 1.12)
    ax.set_ylim(-0.20, 1.20)
    ax.axis("off")

    # Draw edges
    for n1, n2 in edges:
        x1, y1 = nodes[n1]
        x2, y2 = nodes[n2]
        ax.plot([x1, x2], [y1, y2], color=GREY, lw=1.5, alpha=0.5, zorder=1)

    # Draw nodes
    for name, (x, y) in nodes.items():
        S_val = stock_prices[name]
        f_val = option_vals[name]
        is_early = early_flags[name]

        node_color = RED if is_early else BLUE
        fc = "#ffe0e0" if is_early else "#e0ecf8"
        ec = RED if is_early else BLUE

        circle = plt.Circle((x, y), 0.055, color=fc, ec=ec, lw=2.2, zorder=3)
        ax.add_patch(circle)

        # Stock price on top, option value below
        ax.text(x, y + 0.015, f"$S = {S_val:.0f}$", fontsize=9,
                ha="center", va="center", zorder=4, color=GREY)
        ax.text(x, y - 0.02, f"$P = {f_val:.2f}$", fontsize=9.5, fontweight="bold",
                ha="center", va="center", zorder=4, color=node_color)

    # Annotations for early exercise
    if early_d:
        x, y = nodes["Sd"]
        ax.annotate(
            f"Early exercise!\nIntrinsic = ${exer_d:.0f}$ > Cont. = ${cont_d:.2f}$",
            xy=(x, y - 0.055), xytext=(x + 0.05, y - 0.16),
            fontsize=8.5, color=RED, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5),
            bbox=dict(boxstyle="round,pad=0.3", fc="#fff0f0", ec=RED, alpha=0.9),
        )

    if not early_u:
        x, y = nodes["Su"]
        ax.annotate(
            f"Hold: Cont. = ${cont_u:.2f}$ > Intrinsic = ${exer_u:.0f}$",
            xy=(x, y + 0.055), xytext=(x + 0.05, y + 0.14),
            fontsize=8.5, color=BLUE,
            arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.2),
            bbox=dict(boxstyle="round,pad=0.3", fc="#f0f4fa", ec=BLUE, alpha=0.9),
        )

    # Legend
    early_patch = mpatches.Patch(facecolor="#ffe0e0", edgecolor=RED, lw=1.5,
                                  label="Early exercise optimal")
    hold_patch  = mpatches.Patch(facecolor="#e0ecf8", edgecolor=BLUE, lw=1.5,
                                  label="Continuation optimal")
    ax.legend(handles=[hold_patch, early_patch], fontsize=10, loc="upper left",
              framealpha=0.9)

    # Time labels
    for t_label, x_pos in [("$t = 0$", 0.0), (r"$t = \Delta t$", 0.4), ("$t = T$", 0.8)]:
        ax.text(x_pos, -0.14, t_label, fontsize=10, ha="center", color=GREY)

    # Risk-neutral prob annotation
    ax.text(0.5, -0.19,
            f"$q = {q:.4f}$,  $K = {K}$,  $r = {int(r*100)}\\%$,  "
            f"American put price $P = {f_0:.3f}$",
            fontsize=9.5, ha="center", color=GREY)

    ax.set_title(
        "American Put Pricing on a Two-Step Binomial Tree\n"
        f"($S_0 = {S0}$,  $u = {u}$,  $d = {d}$,  $K = {K}$,  $T = 1$yr,  $N = 2$)",
        fontsize=13, fontweight="bold", pad=15,
    )

    plt.tight_layout()
    out = output_dir / "american_put_tree.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# -- Figure 3: Greeks as functions of S_0 for multiple maturities --------------
def generate_greeks_surface(output_dir: Path) -> Path:
    """Plot Delta, Gamma, Vega, Theta for a European call across S_0 and T."""
    K = 100; r = 0.05; sigma = 0.25
    S = np.linspace(60, 140, 500)
    maturities = [(1.0, BLUE, "-"), (0.5, GREEN, "--"), (0.25, ORANGE, ":")]

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    fig.suptitle(
        "European Call Greeks vs. Stock Price\n"
        f"($K={K}$,  $r={int(r*100)}\\%$,  $\\sigma={int(sigma*100)}\\%$)",
        fontsize=14, fontweight="bold",
    )

    for T_val, col, ls in maturities:
        d1 = bs_d1(S, K, T_val, r, sigma)
        d2 = d1 - sigma * np.sqrt(T_val)
        nprime_d1 = norm.pdf(d1)
        label = f"$T = {T_val}$yr"

        # Delta
        delta = norm.cdf(d1)
        axes[0, 0].plot(S, delta, color=col, lw=2.2, ls=ls, label=label)

        # Gamma
        gamma = nprime_d1 / (S * sigma * np.sqrt(T_val))
        axes[0, 1].plot(S, gamma, color=col, lw=2.2, ls=ls, label=label)

        # Vega (per 1% move in sigma, i.e. divide by 100 for display)
        vega = S * np.sqrt(T_val) * nprime_d1 / 100.0
        axes[1, 0].plot(S, vega, color=col, lw=2.2, ls=ls, label=label)

        # Theta (per year; negative for long calls)
        theta = (-(S * nprime_d1 * sigma) / (2 * np.sqrt(T_val))
                 - r * K * np.exp(-r * T_val) * norm.cdf(d2))
        # Convert to per-day for intuition: theta / 365
        axes[1, 1].plot(S, theta / 365, color=col, lw=2.2, ls=ls, label=label)

    # Decorate each subplot
    # Delta
    ax = axes[0, 0]
    ax.axhline(0.5, color=GREY, lw=0.8, ls="--", alpha=0.5)
    ax.axvline(K, color=GREY, lw=0.8, ls=":", alpha=0.5)
    ax.set(xlabel="$S_0$", ylabel=r"$\Delta$ (Delta)")
    ax.set_title(r"Delta $\Delta = \mathcal{N}(d_1)$", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9); ax.grid(alpha=0.25)
    ax.text(K + 1, 0.05, "$K$", fontsize=9, color=GREY)

    # Gamma
    ax = axes[0, 1]
    ax.axvline(K, color=GREY, lw=0.8, ls=":", alpha=0.5)
    ax.set(xlabel="$S_0$", ylabel=r"$\Gamma$ (Gamma)")
    ax.set_title(r"Gamma $\Gamma = \mathcal{N}'(d_1)\,/\,(S_0\sigma\sqrt{T})$",
                 fontsize=11, fontweight="bold")
    ax.legend(fontsize=9); ax.grid(alpha=0.25)
    ax.text(K + 1, ax.get_ylim()[0] * 0.9, "$K$", fontsize=9, color=GREY)

    # Vega
    ax = axes[1, 0]
    ax.axvline(K, color=GREY, lw=0.8, ls=":", alpha=0.5)
    ax.set(xlabel="$S_0$", ylabel=r"$\mathcal{V}$ (Vega per 1% $\sigma$)")
    ax.set_title(r"Vega $\mathcal{V} = S_0\sqrt{T}\,\mathcal{N}'(d_1)$",
                 fontsize=11, fontweight="bold")
    ax.legend(fontsize=9); ax.grid(alpha=0.25)
    ax.text(K + 1, 0.05, "$K$", fontsize=9, color=GREY)

    # Theta
    ax = axes[1, 1]
    ax.axhline(0, color=GREY, lw=0.8, ls="--", alpha=0.5)
    ax.axvline(K, color=GREY, lw=0.8, ls=":", alpha=0.5)
    ax.set(xlabel="$S_0$", ylabel=r"$\Theta$ (Theta per day, $)")
    ax.set_title(r"Theta $\Theta$ (daily time decay)", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9); ax.grid(alpha=0.25)
    ax.text(K + 1, ax.get_ylim()[0] * 0.1, "$K$", fontsize=9, color=GREY)

    plt.tight_layout()
    out = output_dir / "greeks_surface.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# -- Main ----------------------------------------------------------------------
def main() -> None:
    output_dir = Path(__file__).resolve().parent
    output_dir.mkdir(parents=True, exist_ok=True)

    steps = [
        ("two_step_tree.png",     generate_two_step_tree),
        ("american_put_tree.png", generate_american_put_tree),
        ("greeks_surface.png",    generate_greeks_surface),
    ]
    for name, fn in steps:
        print(f"Generating {name} ...", flush=True)
        path = fn(output_dir)
        print(f"  -> {path}")


if __name__ == "__main__":
    main()
