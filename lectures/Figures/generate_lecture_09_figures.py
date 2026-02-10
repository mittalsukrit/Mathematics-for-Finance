"""
Generate figures for Lecture 09: Utility Functions and Risk Aversion
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
colors = sns.color_palette("husl", 8)

# Create output directory if it doesn't exist
import os
os.makedirs('.', exist_ok=True)

# Figure 1: Utility Function Shapes
def plot_utility_functions():
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    W = np.linspace(0.1, 200, 1000)

    # Quadratic utility
    gamma_quad = 0.01
    W_quad = W[W < 1/gamma_quad]  # Only valid before satiation
    u_quad = W_quad - 0.5 * gamma_quad * W_quad**2
    axes[0].plot(W_quad, u_quad, linewidth=2.5, color=colors[0])
    axes[0].axvline(x=1/gamma_quad, color='red', linestyle='--', alpha=0.5, label='Satiation point')
    axes[0].set_xlabel('Wealth W', fontsize=11)
    axes[0].set_ylabel('Utility u(W)', fontsize=11)
    axes[0].set_title('Quadratic Utility\n$u(W) = W - \\frac{\\gamma}{2}W^2$', fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim([0, 120])

    # Exponential utility (CARA)
    gamma_exp = 0.02
    u_exp = -np.exp(-gamma_exp * W)
    axes[1].plot(W, u_exp, linewidth=2.5, color=colors[1])
    axes[1].set_xlabel('Wealth W', fontsize=11)
    axes[1].set_ylabel('Utility u(W)', fontsize=11)
    axes[1].set_title('Exponential Utility (CARA)\n$u(W) = -e^{-\\gamma W}$', fontsize=12, fontweight='bold')
    axes[1].grid(True, alpha=0.3)

    # Power utility (CRRA)
    gamma_power = 2
    u_power = (W**(1-gamma_power)) / (1-gamma_power)
    axes[2].plot(W, u_power, linewidth=2.5, color=colors[2], label='$\\gamma = 2$')

    # Also plot log utility
    u_log = np.log(W)
    axes[2].plot(W, u_log, linewidth=2.5, color=colors[3], linestyle='--', label='Log ($\\gamma = 1$)')

    axes[2].set_xlabel('Wealth W', fontsize=11)
    axes[2].set_ylabel('Utility u(W)', fontsize=11)
    axes[2].set_title('Power Utility (CRRA)\n$u(W) = \\frac{W^{1-\\gamma}}{1-\\gamma}$', fontsize=12, fontweight='bold')
    axes[2].legend(fontsize=9)
    axes[2].grid(True, alpha=0.3)
    axes[2].set_ylim([-2, 5])

    plt.tight_layout()
    plt.savefig('utility_function_shapes.png', dpi=300, bbox_inches='tight')
    print("Generated: utility_function_shapes.png")
    plt.close()

# Figure 2: Concavity and Risk Aversion
def plot_concavity_risk_aversion():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Wealth values
    W1, W2 = 50, 150
    W_mean = (W1 + W2) / 2
    W = np.linspace(30, 170, 1000)

    # Log utility (concave)
    u = np.log(W)
    u1, u2 = np.log(W1), np.log(W2)
    u_mean = np.log(W_mean)
    u_expected = 0.5 * u1 + 0.5 * u2

    # Find certainty equivalent
    CE = np.exp(u_expected)

    # Plot utility function
    ax.plot(W, u, linewidth=3, color=colors[0], label='Utility function u(W) = ln(W)')

    # Plot secant line (expected utility)
    ax.plot([W1, W2], [u1, u2], 'o-', markersize=10, linewidth=2,
            color=colors[1], label='Lottery outcomes')

    # Show expected value and expected utility
    ax.plot(W_mean, u_expected, 'D', markersize=12, color=colors[2],
            label=f'Expected utility at E[W]={W_mean}', zorder=5)
    ax.plot(W_mean, u_mean, 's', markersize=12, color=colors[3],
            label=f'u(E[W]) = u({W_mean})', zorder=5)

    # Show certainty equivalent
    ax.plot(CE, u_expected, 'v', markersize=12, color=colors[4],
            label=f'Certainty equivalent CE={CE:.1f}', zorder=5)

    # Draw lines
    ax.plot([W_mean, W_mean], [2.5, u_expected], 'k--', alpha=0.3, linewidth=1)
    ax.plot([W_mean, W_mean], [u_expected, u_mean], 'r-', alpha=0.6, linewidth=3,
            label=f'Risk Premium = {W_mean - CE:.1f}')
    ax.plot([CE, W_mean], [u_expected, u_expected], 'r-', alpha=0.6, linewidth=3)

    # Annotations
    ax.annotate('u(E[W]) > E[u(W)]', xy=(W_mean, (u_mean + u_expected)/2),
                xytext=(W_mean + 20, (u_mean + u_expected)/2),
                fontsize=11, fontweight='bold',
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))

    ax.set_xlabel('Wealth W', fontsize=12)
    ax.set_ylabel('Utility u(W)', fontsize=12)
    ax.set_title('Concavity and Risk Aversion: Why Investors Prefer Certainty',
                 fontsize=13, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim([2.5, 5.2])

    plt.tight_layout()
    plt.savefig('concavity_risk_aversion.png', dpi=300, bbox_inches='tight')
    print("Generated: concavity_risk_aversion.png")
    plt.close()

# Figure 3: Marginal Utility - Diminishing Returns
def plot_marginal_utility():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    W = np.linspace(1, 200, 1000)

    # Left: Log utility and its derivative
    u_log = np.log(W)
    u_prime_log = 1 / W

    axes[0].plot(W, u_log, linewidth=2.5, color=colors[0], label="u(W) = ln(W)")
    ax2 = axes[0].twinx()
    ax2.plot(W, u_prime_log, linewidth=2.5, color=colors[1], linestyle='--',
             label="u'(W) = 1/W")

    axes[0].set_xlabel('Wealth W', fontsize=11)
    axes[0].set_ylabel('Utility u(W)', fontsize=11, color=colors[0])
    ax2.set_ylabel("Marginal Utility u'(W)", fontsize=11, color=colors[1])
    axes[0].set_title('Log Utility: Diminishing Marginal Utility',
                      fontsize=12, fontweight='bold')
    axes[0].tick_params(axis='y', labelcolor=colors[0])
    ax2.tick_params(axis='y', labelcolor=colors[1])
    axes[0].legend(loc='upper left', fontsize=9)
    ax2.legend(loc='upper right', fontsize=9)
    axes[0].grid(True, alpha=0.3)

    # Right: Compare marginal utilities across functions
    u_prime_quad = 1 - 0.01 * W
    u_prime_quad[u_prime_quad < 0] = np.nan  # Satiation
    u_prime_exp = 0.02 * np.exp(-0.02 * W)
    u_prime_power = W**(-2)

    axes[1].plot(W, u_prime_log, linewidth=2.5, color=colors[0], label='Log: $u\'(W) = 1/W$')
    axes[1].plot(W, u_prime_power, linewidth=2.5, color=colors[2], label='Power ($\\gamma=2$): $u\'(W) = W^{-2}$')
    axes[1].plot(W, u_prime_exp, linewidth=2.5, color=colors[1], label='Exponential: $u\'(W) = \\gamma e^{-\\gamma W}$')
    axes[1].plot(W[W < 100], u_prime_quad[W < 100], linewidth=2.5, color=colors[3],
                 label='Quadratic: $u\'(W) = 1 - \\gamma W$')

    axes[1].set_xlabel('Wealth W', fontsize=11)
    axes[1].set_ylabel("Marginal Utility u'(W)", fontsize=11)
    axes[1].set_title('Comparing Marginal Utilities', fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim([0, 0.05])

    plt.tight_layout()
    plt.savefig('marginal_utility.png', dpi=300, bbox_inches='tight')
    print("Generated: marginal_utility.png")
    plt.close()

# Figure 4: Absolute and Relative Risk Aversion
def plot_risk_aversion_measures():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    W = np.linspace(1, 200, 1000)
    gamma = 2

    # Absolute Risk Aversion
    ARA_quad = 0.01 / (1 - 0.01 * W)
    ARA_quad[W >= 100] = np.nan
    ARA_exp = np.ones_like(W) * 0.01
    ARA_power = gamma / W
    ARA_log = 1 / W

    axes[0].plot(W, ARA_log, linewidth=2.5, color=colors[0], label='Log: A(W) = 1/W')
    axes[0].plot(W, ARA_power, linewidth=2.5, color=colors[2], label=f'Power ($\\gamma={gamma}$): A(W) = {gamma}/W')
    axes[0].plot(W, ARA_exp, linewidth=2.5, color=colors[1], label='Exponential (CARA): A(W) = 0.01')
    axes[0].plot(W[W < 99], ARA_quad[W < 99], linewidth=2.5, color=colors[3],
                 label='Quadratic (IARA): A(W) increasing')

    axes[0].set_xlabel('Wealth W', fontsize=11)
    axes[0].set_ylabel('Absolute Risk Aversion A(W)', fontsize=11)
    axes[0].set_title('Absolute Risk Aversion: $A(W) = -u\'\'(W)/u\'(W)$',
                      fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim([0, 0.05])

    # Relative Risk Aversion
    RRA_quad = (0.01 * W) / (1 - 0.01 * W)
    RRA_quad[W >= 100] = np.nan
    RRA_exp = 0.01 * W
    RRA_power = np.ones_like(W) * gamma
    RRA_log = np.ones_like(W)

    axes[1].plot(W, RRA_log, linewidth=2.5, color=colors[0], label='Log (CRRA): R(W) = 1')
    axes[1].plot(W, RRA_power, linewidth=2.5, color=colors[2], label=f'Power (CRRA): R(W) = {gamma}')
    axes[1].plot(W, RRA_exp, linewidth=2.5, color=colors[1], label='Exponential (IRRA): R(W) = 0.01W')
    axes[1].plot(W[W < 90], RRA_quad[W < 90], linewidth=2.5, color=colors[3],
                 label='Quadratic (IRRA): R(W) increasing')

    axes[1].set_xlabel('Wealth W', fontsize=11)
    axes[1].set_ylabel('Relative Risk Aversion R(W)', fontsize=11)
    axes[1].set_title('Relative Risk Aversion: $R(W) = -W \\cdot u\'\'(W)/u\'(W)$',
                      fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_ylim([0, 5])

    plt.tight_layout()
    plt.savefig('risk_aversion_measures.png', dpi=300, bbox_inches='tight')
    print("Generated: risk_aversion_measures.png")
    plt.close()

# Figure 5: Comparison of Risk Premiums
def plot_risk_premiums():
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Define lottery parameters
    W1, W2 = 50, 150
    p1, p2 = 0.5, 0.5
    E_W = p1 * W1 + p2 * W2

    W_range = np.linspace(40, 160, 1000)

    # Utility functions to compare
    utilities = [
        (lambda W: np.sqrt(W), "Square Root (CRRA, γ=0.5)", 0),
        (lambda W: np.log(W), "Log (CRRA, γ=1)", 1),
        (lambda W: -1/W, "Inverse (CRRA, γ=2)", 2),
        (lambda W: W**(1-3)/(1-3), "Power (CRRA, γ=3)", 3)
    ]

    for idx, (u_func, title, pos) in enumerate(utilities):
        row, col = pos // 2, pos % 2
        ax = axes[row, col]

        # Calculate utilities
        u_range = u_func(W_range)
        u1, u2 = u_func(W1), u_func(W2)
        E_u = p1 * u1 + p2 * u2
        u_E = u_func(E_W)

        # Find CE
        CE = None
        for w in W_range:
            if abs(u_func(w) - E_u) < 0.001:
                CE = w
                break
        if CE is None:
            CE = W_range[np.argmin(np.abs(u_range - E_u))]

        RP = E_W - CE

        # Plot
        ax.plot(W_range, u_range, linewidth=2.5, color=colors[idx])
        ax.plot([W1, W2], [u1, u2], 'o-', markersize=10, linewidth=2, color=colors[idx+1])
        ax.plot(E_W, E_u, 'D', markersize=10, color=colors[2])
        ax.plot(E_W, u_E, 's', markersize=10, color=colors[3])
        ax.plot(CE, E_u, 'v', markersize=10, color=colors[4])

        # Annotations
        ax.plot([CE, E_W], [E_u, E_u], 'r-', linewidth=3, alpha=0.6)
        ax.text(E_W - 5, E_u - 0.1, f'RP = {RP:.2f}', fontsize=10, ha='right',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        ax.set_xlabel('Wealth W', fontsize=10)
        ax.set_ylabel('Utility', fontsize=10)
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.grid(True, alpha=0.3)

    plt.suptitle('Risk Premium Across Different Utility Functions',
                 fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('risk_premiums_comparison.png', dpi=300, bbox_inches='tight')
    print("Generated: risk_premiums_comparison.png")
    plt.close()

# Figure 6: Normal vs Skewed Returns (Mean-Variance Failure)
def plot_normal_vs_skewed():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Generate return distributions
    x = np.linspace(-0.4, 0.6, 1000)

    # Normal distribution: mean=0.1, std=0.2
    from scipy.stats import norm, skewnorm
    mu, sigma = 0.1, 0.2
    normal_pdf = norm.pdf(x, mu, sigma)

    # Right-skewed distribution with same mean and variance
    # Use skewnorm with parameters chosen to match
    a = 5  # skewness parameter
    skew_dist = skewnorm(a, loc=0.02, scale=0.15)
    skewed_pdf = skew_dist.pdf(x)

    # Normalize to have same area
    skewed_pdf = skewed_pdf / np.trapz(skewed_pdf, x) * np.trapz(normal_pdf, x)

    # Plot distributions
    axes[0].fill_between(x, 0, normal_pdf, alpha=0.3, color=colors[0], label='Normal')
    axes[0].fill_between(x, 0, skewed_pdf, alpha=0.3, color=colors[1], label='Right-skewed')
    axes[0].plot(x, normal_pdf, linewidth=2.5, color=colors[0])
    axes[0].plot(x, skewed_pdf, linewidth=2.5, color=colors[1])

    axes[0].axvline(x=mu, color='red', linestyle='--', linewidth=2, label=f'Mean = {mu}')
    axes[0].set_xlabel('Return', fontsize=11)
    axes[0].set_ylabel('Probability Density', fontsize=11)
    axes[0].set_title('Same Mean & Variance, Different Skewness', fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=10)
    axes[0].grid(True, alpha=0.3)

    # Right panel: Expected utility comparison
    gammas = [0.5, 1, 2, 3, 5]
    eu_normal = []
    eu_skewed = []

    for gamma in gammas:
        # Calculate expected utilities
        W0 = 100
        W_normal = W0 * (1 + x)
        W_skewed = W0 * (1 + x)

        if gamma == 1:
            u_normal = np.log(np.maximum(W_normal, 0.01))
            u_skewed = np.log(np.maximum(W_skewed, 0.01))
        else:
            u_normal = (np.maximum(W_normal, 0.01)**(1-gamma)) / (1-gamma)
            u_skewed = (np.maximum(W_skewed, 0.01)**(1-gamma)) / (1-gamma)

        eu_n = np.trapz(u_normal * normal_pdf, x)
        eu_s = np.trapz(u_skewed * skewed_pdf, x)

        eu_normal.append(eu_n)
        eu_skewed.append(eu_s)

    # Normalize for comparison
    eu_normal = np.array(eu_normal)
    eu_skewed = np.array(eu_skewed)
    preference_diff = ((eu_skewed - eu_normal) / np.abs(eu_normal)) * 100

    axes[1].bar(range(len(gammas)), preference_diff, color=colors[2], alpha=0.7, edgecolor='black')
    axes[1].axhline(y=0, color='black', linestyle='-', linewidth=1)
    axes[1].set_xlabel('Risk Aversion Parameter γ', fontsize=11)
    axes[1].set_ylabel('Preference for Skewed over Normal (%)', fontsize=11)
    axes[1].set_title('Mean-Variance Misses Skewness Preference', fontsize=12, fontweight='bold')
    axes[1].set_xticks(range(len(gammas)))
    axes[1].set_xticklabels(gammas)
    axes[1].grid(True, alpha=0.3, axis='y')
    axes[1].text(2, max(preference_diff)*0.8,
                 'Positive: Skewed preferred\nNegative: Normal preferred',
                 fontsize=9, ha='center',
                 bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))

    plt.tight_layout()
    plt.savefig('normal_vs_skewed_returns.png', dpi=300, bbox_inches='tight')
    print("Generated: normal_vs_skewed_returns.png")
    plt.close()

# Figure 7: Portfolio Allocation with Different Utilities
def plot_portfolio_allocation():
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Parameters
    R_f = 0.05
    mu_s = 0.15
    sigma_s = 0.30
    W0_range = np.linspace(10, 200, 100)

    # Optimal allocations
    # CARA: w* = (mu - R_f) / (gamma * sigma^2 * W0)
    gamma_cara = 0.01
    w_cara = (mu_s - R_f) / (gamma_cara * sigma_s**2 * W0_range)

    # CRRA: w* = (mu - R_f) / (gamma * sigma^2)
    gamma_crra_1 = 1
    gamma_crra_2 = 2
    gamma_crra_3 = 3

    w_crra_1 = np.ones_like(W0_range) * (mu_s - R_f) / (gamma_crra_1 * sigma_s**2)
    w_crra_2 = np.ones_like(W0_range) * (mu_s - R_f) / (gamma_crra_2 * sigma_s**2)
    w_crra_3 = np.ones_like(W0_range) * (mu_s - R_f) / (gamma_crra_3 * sigma_s**2)

    # Left panel: Fraction invested
    axes[0].plot(W0_range, w_cara, linewidth=2.5, color=colors[0],
                 label=f'CARA (γ={gamma_cara})')
    axes[0].plot(W0_range, w_crra_1, linewidth=2.5, color=colors[1], linestyle='--',
                 label=f'CRRA (γ={gamma_crra_1})')
    axes[0].plot(W0_range, w_crra_2, linewidth=2.5, color=colors[2], linestyle='--',
                 label=f'CRRA (γ={gamma_crra_2})')
    axes[0].plot(W0_range, w_crra_3, linewidth=2.5, color=colors[3], linestyle='--',
                 label=f'CRRA (γ={gamma_crra_3})')

    axes[0].axhline(y=1, color='red', linestyle=':', alpha=0.5, label='100% (no leverage)')
    axes[0].set_xlabel('Initial Wealth $W_0$', fontsize=11)
    axes[0].set_ylabel('Fraction Invested in Risky Asset', fontsize=11)
    axes[0].set_title('Portfolio Allocation: CARA vs CRRA', fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim([0, 2])

    # Right panel: Dollar amount invested
    dollar_cara = w_cara * W0_range
    dollar_crra_1 = w_crra_1 * W0_range
    dollar_crra_2 = w_crra_2 * W0_range
    dollar_crra_3 = w_crra_3 * W0_range

    axes[1].plot(W0_range, dollar_cara, linewidth=2.5, color=colors[0],
                 label=f'CARA (γ={gamma_cara})')
    axes[1].plot(W0_range, dollar_crra_1, linewidth=2.5, color=colors[1], linestyle='--',
                 label=f'CRRA (γ={gamma_crra_1})')
    axes[1].plot(W0_range, dollar_crra_2, linewidth=2.5, color=colors[2], linestyle='--',
                 label=f'CRRA (γ={gamma_crra_2})')
    axes[1].plot(W0_range, dollar_crra_3, linewidth=2.5, color=colors[3], linestyle='--',
                 label=f'CRRA (γ={gamma_crra_3})')

    axes[1].set_xlabel('Initial Wealth $W_0$', fontsize=11)
    axes[1].set_ylabel('Dollar Amount in Risky Asset', fontsize=11)
    axes[1].set_title('Dollar Investment: Scale-Invariance of CRRA', fontsize=12, fontweight='bold')
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)

    # Add annotations
    axes[0].text(150, 0.3, 'CARA: Fraction decreases\nwith wealth', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
    axes[0].text(150, 1.3, 'CRRA: Fraction constant', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    axes[1].text(150, 50, 'CRRA: Linear in wealth\n(proportional investment)', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    plt.tight_layout()
    plt.savefig('portfolio_allocation_utilities.png', dpi=300, bbox_inches='tight')
    print("Generated: portfolio_allocation_utilities.png")
    plt.close()

# Generate all figures
if __name__ == "__main__":
    print("Generating Lecture 09 figures...")
    print("-" * 50)

    plot_utility_functions()
    plot_concavity_risk_aversion()
    plot_marginal_utility()
    plot_risk_aversion_measures()
    plot_risk_premiums()
    plot_normal_vs_skewed()
    plot_portfolio_allocation()

    print("-" * 50)
    print("All figures generated successfully!")
    print("\nGenerated files:")
    print("1. utility_function_shapes.png")
    print("2. concavity_risk_aversion.png")
    print("3. marginal_utility.png")
    print("4. risk_aversion_measures.png")
    print("5. risk_premiums_comparison.png")
    print("6. normal_vs_skewed_returns.png")
    print("7. portfolio_allocation_utilities.png")
