"""
Generate figures for Lecture 10: Value at Risk (VaR).

This script creates:
1. loss_distribution_quantiles.png
"""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def normal_pdf(x: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    """Probability density function for N(mu, sigma^2)."""
    coeff = 1.0 / (sigma * np.sqrt(2.0 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coeff * np.exp(exponent)


def generate_loss_distribution_quantiles(output_dir: Path) -> Path:
    """
    Plot a normal loss distribution and highlight VaR at 95% and 99% levels.

    We use the lecture convention:
    - portfolio return R ~ N(mu_R, sigma^2)
    - loss L = -R ~ N(-mu_R, sigma^2)
    """
    mu_return = 0.001   # 0.10% expected daily return
    sigma = 0.01        # 1.00% daily volatility
    mu_loss = -mu_return

    # Standard normal quantiles for 95% and 99% confidence.
    z_95 = 1.6448536269514722
    z_99 = 2.3263478740408408
    var_95 = mu_loss + sigma * z_95
    var_99 = mu_loss + sigma * z_99

    x = np.linspace(mu_loss - 4 * sigma, mu_loss + 5 * sigma, 2000)
    y = normal_pdf(x, mu_loss, sigma)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, color="#1f4e79", linewidth=2.5, label="Loss density")

    mask95 = x >= var_95
    mask99 = x >= var_99
    ax.fill_between(x[mask95], y[mask95], color="#f2a104", alpha=0.28, label="Tail beyond VaR 95%")
    ax.fill_between(x[mask99], y[mask99], color="#b22222", alpha=0.45, label="Tail beyond VaR 99%")

    ax.axvline(var_95, color="#f2a104", linestyle="--", linewidth=2, label=f"VaR 95% = {var_95*100:.2f}%")
    ax.axvline(var_99, color="#b22222", linestyle="--", linewidth=2, label=f"VaR 99% = {var_99*100:.2f}%")
    ax.axvline(mu_loss, color="#666666", linestyle=":", linewidth=1.5, label=f"Mean loss = {mu_loss*100:.2f}%")

    ax.set_title("Loss Distribution and VaR Quantiles", fontsize=14, fontweight="bold")
    ax.set_xlabel("Loss (L = -R)", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)

    xticks = np.array([-0.03, -0.02, -0.01, 0.0, 0.01, 0.02, 0.03, 0.04])
    ax.set_xticks(xticks)
    ax.set_xticklabels([f"{v*100:.0f}%" for v in xticks])
    ax.grid(alpha=0.3)
    ax.legend(loc="upper right", fontsize=9)

    output_path = output_dir / "loss_distribution_quantiles.png"
    fig.tight_layout()
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    output_dir = Path(__file__).resolve().parent
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = generate_loss_distribution_quantiles(output_dir)
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    main()
