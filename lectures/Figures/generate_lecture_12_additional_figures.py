"""
Generate additional figures for Lecture 12: Options — General Properties.

Figures produced:
  option_bounds.png              — European no-arbitrage price bounds (Section 7)
  intrinsic_time_value.png       — Intrinsic + time-value decomposition (Section 4)
  early_exercise_boundary.png    — American put early-exercise boundary S*(t) (Section 9)
  volatility_effect.png          — Option price vs volatility σ (Section 10)
  time_decay.png                 — Time-value hump and theta decay (Section 11)
"""

from pathlib import Path

import matplotlib
import numpy as np
from scipy.stats import norm

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── Shared parameters ─────────────────────────────────────────────────────────
K     = 100
r     = 0.05
SIGMA = 0.25
T     = 1.0

BLUE   = "#1f4e79"
RED    = "#b22222"
GREEN  = "#1a7a4a"
ORANGE = "#c76b00"
GREY   = "#555555"
ALPHA  = 0.13


# ── Black-Scholes formulas ────────────────────────────────────────────────────
def bs_call(S, K, T, r, sigma):
    S, T = np.asarray(S, float), np.asarray(T, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return np.where(T <= 0, np.maximum(S - K, 0.0), price)


def bs_put(S, K, T, r, sigma):
    S, T = np.asarray(S, float), np.asarray(T, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return np.where(T <= 0, np.maximum(K - S, 0.0), price)


# ── American put via CRR binomial tree (vectorised over S0) ──────────────────
def american_put_vec(S0_vec: np.ndarray, K: float, tau: float,
                     r: float, sigma: float, N: int = 100) -> np.ndarray:
    """Return American put prices for an array of initial stock prices."""
    S0_vec = np.asarray(S0_vec, float)
    if tau <= 1e-12:
        return np.maximum(K - S0_vec, 0.0)

    dt   = tau / N
    u    = np.exp(sigma * np.sqrt(dt))
    d    = 1.0 / u
    p    = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)

    # Terminal stock prices: (M, N+1)
    j  = np.arange(N + 1, dtype=float)
    ST = S0_vec[:, None] * (u ** j) * (d ** (N - j))
    V  = np.maximum(K - ST, 0.0)

    for step in range(N - 1, -1, -1):
        jj      = np.arange(step + 1, dtype=float)
        S_node  = S0_vec[:, None] * (u ** jj) * (d ** (step - jj))
        intrinsic    = np.maximum(K - S_node, 0.0)
        continuation = disc * (p * V[:, 1:step + 2] + (1 - p) * V[:, :step + 1])
        V = np.maximum(intrinsic, continuation)

    return V[:, 0]


# ── Figure 1: European no-arbitrage price bounds ─────────────────────────────
def generate_option_bounds(output_dir: Path) -> Path:
    S = np.linspace(1, 200, 800)

    lower_c = np.maximum(S - K * np.exp(-r * T), 0.0)
    upper_c = S.copy()
    c_bs    = bs_call(S, K, T, r, SIGMA)

    lower_p = np.maximum(K * np.exp(-r * T) - S, 0.0)
    upper_p = np.full_like(S, K * np.exp(-r * T))
    p_bs    = bs_put(S, K, T, r, SIGMA)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle(
        r"European Option No-Arbitrage Price Bounds"
        f"\n($K={K}$,  $T={T}$yr,  $r={int(r*100)}\\%$,  $\\sigma={int(SIGMA*100)}\\%$)",
        fontsize=13, fontweight="bold",
    )

    # Call
    ax = axes[0]
    ax.fill_between(S, lower_c, upper_c, color=BLUE, alpha=ALPHA, label="Feasible region")
    ax.plot(S, upper_c, color=BLUE, lw=1.8, ls="--",
            label=r"Upper: $c \leq S_0$")
    ax.plot(S, lower_c, color=BLUE, lw=1.8, ls=":",
            label=r"Lower: $c \geq \max(S_0 - Ke^{-rT},\,0)$")
    ax.plot(S, c_bs, color=ORANGE, lw=2.8, label="Black-Scholes $c(S_0)$")
    ax.axvline(K, color=GREY, lw=1.0, ls=":", alpha=0.5)
    ax.text(K + 1.5, 4, "$K$", fontsize=9, color=GREY)
    ax.set(xlim=(0, 200), ylim=(-2, 200),
           xlabel="$S_0$", ylabel="Call price  $c$")
    ax.set_title("European Call", fontsize=12, fontweight="bold")
    ax.legend(fontsize=8.5, loc="upper left")
    ax.grid(alpha=0.25)

    # Put
    ax = axes[1]
    ax.fill_between(S, lower_p, upper_p, color=GREEN, alpha=ALPHA, label="Feasible region")
    ax.plot(S, upper_p, color=GREEN, lw=1.8, ls="--",
            label=r"Upper: $p \leq Ke^{-rT}$")
    ax.plot(S, lower_p, color=GREEN, lw=1.8, ls=":",
            label=r"Lower: $p \geq \max(Ke^{-rT} - S_0,\,0)$")
    ax.plot(S, p_bs, color=ORANGE, lw=2.8, label="Black-Scholes $p(S_0)$")
    ax.axvline(K, color=GREY, lw=1.0, ls=":", alpha=0.5)
    ax.text(K + 1.5, 2, "$K$", fontsize=9, color=GREY)
    ax.set(xlim=(0, 200), ylim=(-1, K * np.exp(-r * T) + 5),
           xlabel="$S_0$", ylabel="Put price  $p$")
    ax.set_title("European Put", fontsize=12, fontweight="bold")
    ax.legend(fontsize=8.5, loc="upper right")
    ax.grid(alpha=0.25)

    plt.tight_layout()
    out = output_dir / "option_bounds.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# ── Figure 2: Intrinsic value + time value decomposition ─────────────────────
def generate_intrinsic_time_value(output_dir: Path) -> Path:
    S = np.linspace(60, 140, 500)

    c     = bs_call(S, K, T, r, SIGMA)
    p     = bs_put(S, K, T, r, SIGMA)
    iv_c  = np.maximum(S - K * np.exp(-r * T), 0.0)   # adjusted intrinsic
    iv_p  = np.maximum(K * np.exp(-r * T) - S, 0.0)   # adjusted intrinsic
    tv_c  = c - iv_c
    tv_p  = p - iv_p    # can be negative for deep-ITM European puts

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle(
        "Option Price = Intrinsic Value + Time Value\n"
        f"($K={K}$,  $T={T}$yr,  $r={int(r*100)}\\%$,  $\\sigma={int(SIGMA*100)}\\%$)",
        fontsize=13, fontweight="bold",
    )

    # Call
    ax = axes[0]
    ax.plot(S, c,    color=BLUE,   lw=2.5, label="BS call price $c$")
    ax.plot(S, iv_c, color=ORANGE, lw=2.0, ls="--",
            label=r"Adjusted intrinsic  $\max(S_0 - Ke^{-rT},\,0)$")
    ax.fill_between(S, iv_c, c, color=BLUE, alpha=0.18, label="Time value (optionality)")
    ax.axvline(K, color=GREY, lw=1.0, ls=":", alpha=0.6)
    ax.text(K + 0.7, 0.8, "ATM\n$K$", fontsize=8.5, color=GREY, va="bottom")
    ax.set(xlim=(60, 140), ylim=(-1, 55), xlabel="$S_0$", ylabel="Value ($)")
    ax.set_title("European Call\n(time value always ≥ 0)", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.25)

    # Put
    ax = axes[1]
    ax.plot(S, p,    color=GREEN,  lw=2.5, label="BS put price $p$")
    ax.plot(S, iv_p, color=ORANGE, lw=2.0, ls="--",
            label=r"Adjusted intrinsic  $\max(Ke^{-rT} - S_0,\,0)$")
    ax.fill_between(S, iv_p, p, where=(tv_p >= 0),
                    color=GREEN, alpha=0.18, label="Time value > 0")
    ax.fill_between(S, iv_p, p, where=(tv_p < 0),
                    color=RED,   alpha=0.22, label="Time value < 0 (deep ITM, forced to wait)")
    ax.axhline(0, color=GREY, lw=0.8, ls="--", alpha=0.4)
    ax.axvline(K, color=GREY, lw=1.0, ls=":", alpha=0.6)
    ax.text(K + 0.7, 0.8, "ATM\n$K$", fontsize=8.5, color=GREY, va="bottom")
    ax.set(xlim=(60, 140), ylim=(-1, 45), xlabel="$S_0$", ylabel="Value ($)")
    ax.set_title("European Put\n(time value can be negative deep ITM)", fontsize=11, fontweight="bold")
    ax.legend(fontsize=9, loc="upper right")
    ax.grid(alpha=0.25)

    plt.tight_layout()
    out = output_dir / "intrinsic_time_value.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# ── Figure 3: American put early-exercise boundary ───────────────────────────
def generate_early_exercise_boundary(output_dir: Path) -> Path:
    N_tau  = 50
    N_S    = 250
    N_tree = 80

    tau_vals  = np.linspace(0.005, T, N_tau)
    S_grid    = np.linspace(40, 110, N_S)
    boundary  = np.empty(N_tau)

    for i, tau in enumerate(tau_vals):
        put_am    = american_put_vec(S_grid, K, tau, r, SIGMA, N=N_tree)
        intrinsic = np.maximum(K - S_grid, 0.0)
        diff      = put_am - intrinsic          # > 0 in continuation, ≈ 0 in exercise
        hold_idx  = np.where(diff > 0.05)[0]
        boundary[i] = S_grid[hold_idx[0]] if len(hold_idx) else S_grid[0]

    # Calendar time t = T - tau; sort ascending for clean plot
    t_vals  = T - tau_vals
    idx     = np.argsort(t_vals)
    t_sort  = np.append(t_vals[idx], T)          # add exact endpoint t=T
    b_sort  = np.append(boundary[idx], float(K)) # S*(t=T) = K exactly

    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.fill_between(t_sort, 40, b_sort,
                    color=RED,  alpha=0.15, label="Early exercise region  ($P = K - S_t$)")
    ax.fill_between(t_sort, b_sort, 110,
                    color=BLUE, alpha=0.10, label="Continuation region  (hold the option)")
    ax.plot(t_sort, b_sort, color=RED, lw=2.8,
            label="$S^*(t)$ — exercise boundary")
    ax.axhline(K, color=GREY, lw=1.5, ls="--", alpha=0.7, label=f"Strike  $K = {K}$")

    ax.annotate(
        f"$S^*(T) = K = {K}$\n(exercise if ITM at maturity)",
        xy=(T, K), xytext=(T - 0.38, K + 7),
        fontsize=8.5, color=GREY,
        arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.2),
    )
    ax.text(0.04, 48,  "Exercise immediately\n$(K - S_t >$ hold value$)$",
            fontsize=8.5, color=RED,  alpha=0.9)
    ax.text(0.04, 100, "Hold option\n$(P_t > K - S_t)$",
            fontsize=8.5, color=BLUE, alpha=0.9)

    ax.set(xlim=(0, T), ylim=(40, 110),
           xlabel="Calendar time  $t$", ylabel="Stock price  $S_t$")
    ax.set_title(
        "American Put: Early Exercise Boundary $S^*(t)$\n"
        f"($K={K}$,  $T={T}$yr,  $r={int(r*100)}\\%$,  $\\sigma={int(SIGMA*100)}\\%$)",
        fontsize=13, fontweight="bold",
    )
    ax.legend(fontsize=9, loc="upper left")
    ax.grid(alpha=0.25)

    plt.tight_layout()
    out = output_dir / "early_exercise_boundary.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# ── Figure 4: Option price vs volatility σ ───────────────────────────────────
def generate_volatility_effect(output_dir: Path) -> Path:
    sigma_vals  = np.linspace(0.01, 0.70, 300)
    S0          = 100.0   # ATM

    c_eu  = bs_call(S0, K, T, r, sigma_vals)
    p_eu  = bs_put(S0,  K, T, r, sigma_vals)

    # American put on a coarser grid (binomial tree is slow per call)
    sigma_am = sigma_vals[::6]
    p_am     = np.array([
        float(american_put_vec(np.array([S0]), K, T, r, sv, N=80)[0])
        for sv in sigma_am
    ])

    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.plot(sigma_vals, c_eu, color=BLUE,   lw=2.5,
            label="European call $c$  (= American call $C$ for no-div stock)")
    ax.plot(sigma_vals, p_eu, color=GREEN,  lw=2.5, ls="--",
            label="European put $p$")
    ax.plot(sigma_am,   p_am, color=RED,    lw=2.5, ls=":",
            label="American put $P$  (binomial tree)")

    # Mark σ = 25% reference dots
    ax.axvline(SIGMA, color=GREY, lw=1.0, ls=":", alpha=0.5)
    ax.scatter([SIGMA], [bs_call(S0, K, T, r, SIGMA)], color=BLUE,  zorder=5, s=60)
    ax.scatter([SIGMA], [bs_put(S0,  K, T, r, SIGMA)], color=GREEN, zorder=5, s=60)
    ax.text(SIGMA + 0.005, 1, f"$\\sigma = {int(SIGMA*100)}\\%$", fontsize=8.5, color=GREY)

    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x*100)}%"))
    ax.set(xlim=(0, 0.70), ylim=(0, None),
           xlabel="Volatility  $\\sigma$", ylabel="Option price ($)")
    ax.set_title(
        "Effect of Volatility on Option Prices\n"
        f"(ATM: $S_0 = K = {K}$,  $T={T}$yr,  $r={int(r*100)}\\%$)",
        fontsize=13, fontweight="bold",
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.25)

    plt.tight_layout()
    out = output_dir / "volatility_effect.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# ── Figure 5: Time-value hump and theta decay ─────────────────────────────────
def generate_time_decay(output_dir: Path) -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Time Value of Options", fontsize=14, fontweight="bold")

    # Left: hump of time value across moneyness for different T
    ax = axes[0]
    S = np.linspace(60, 140, 500)
    tv_colors = [ORANGE, GREEN, BLUE]
    for Tv, col in zip([0.25, 0.5, 1.0], tv_colors):
        c  = bs_call(S, K, Tv, r, SIGMA)
        iv = np.maximum(S - K * np.exp(-r * Tv), 0.0)
        ax.plot(S, c - iv, color=col, lw=2.2, label=f"$T = {Tv}$yr")

    ax.axvline(K, color=GREY, lw=1.0, ls=":", alpha=0.6)
    ax.text(K + 0.5, 0.3, "ATM", fontsize=8.5, color=GREY)
    ax.set(xlim=(60, 140), ylim=(-0.5, None),
           xlabel="$S_0$", ylabel="Call time value ($)")
    ax.set_title("Time Value vs. Moneyness\n(hump peaks at ATM, grows with $T$)",
                 fontsize=11, fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.25)

    # Right: theta decay — call price as T shrinks to 0 (x-axis inverted)
    ax = axes[1]
    T_range = np.linspace(1e-4, 1.0, 500)
    scenarios = [
        (80,  f"OTM call ($S_0 = 80$,  $K = {K}$)",  ORANGE, "--"),
        (100, f"ATM call ($S_0 = 100$, $K = {K}$)",  BLUE,   "-"),
        (120, f"ITM call ($S_0 = 120$, $K = {K}$)",  GREEN,  ":"),
    ]
    for S0, lbl, col, ls in scenarios:
        ax.plot(T_range, bs_call(S0, K, T_range, r, SIGMA),
                color=col, lw=2.2, ls=ls, label=lbl)
        ax.scatter([0], [max(S0 - K, 0)], color=col, zorder=5, s=50)

    ax.invert_xaxis()   # time flows left → right as T decreases
    ax.set(xlim=(1.0, 0), ylim=(-0.5, None),
           xlabel="Time to expiry  $T$ (years)", ylabel="Call price ($)")
    ax.set_title("Theta Decay: Price Converges to Intrinsic at Expiry\n"
                 "(← time passes; dots mark intrinsic value at $T = 0$)",
                 fontsize=11, fontweight="bold")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.25)

    plt.tight_layout()
    out = output_dir / "time_decay.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return out


# ── Main ──────────────────────────────────────────────────────────────────────
def main() -> None:
    output_dir = Path(__file__).resolve().parent
    output_dir.mkdir(parents=True, exist_ok=True)

    steps = [
        ("option_bounds.png",           generate_option_bounds),
        ("intrinsic_time_value.png",    generate_intrinsic_time_value),
        ("early_exercise_boundary.png", generate_early_exercise_boundary),
        ("volatility_effect.png",       generate_volatility_effect),
        ("time_decay.png",              generate_time_decay),
    ]
    for name, fn in steps:
        print(f"Generating {name} ...", flush=True)
        path = fn(output_dir)
        print(f"  → {path}")


if __name__ == "__main__":
    main()
