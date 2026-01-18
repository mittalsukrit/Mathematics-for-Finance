"""
Generate all figures for Lecture 06: Risk-Free Asset, Indifference Curves, and Lagrange Multipliers

This script creates:
1. CAL.png - Capital Allocation Line
2. tangency.png - Tangency Portfolio with efficient frontier
3. indifference_curves.png - Indifference curves in risk-return space
4. optimal_portfolio.png - Optimal portfolio choice showing tangency

Author: Generated for Mathematics for Finance course
Date: January 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 7)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['legend.fontsize'] = 10

def generate_CAL():
    """Generate Capital Allocation Line figure"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Parameters
    R_f = 0.03  # 3% risk-free rate
    mu_risky = 0.10  # 10% expected return on risky asset
    sigma_risky = 0.20  # 20% volatility
    
    # Sharpe ratio (slope of CAL)
    sharpe = (mu_risky - R_f) / sigma_risky
    
    # Generate CAL
    sigma_vals = np.linspace(0, 0.35, 100)
    mu_CAL = R_f + sharpe * sigma_vals
    
    # Plot CAL
    ax.plot(sigma_vals, mu_CAL, 'b-', linewidth=2.5, label='Capital Allocation Line (CAL)')
    
    # Mark key points
    ax.plot(0, R_f, 'go', markersize=12, label=f'Risk-Free Asset ($R_f$ = {R_f*100:.0f}%)', zorder=5)
    ax.plot(sigma_risky, mu_risky, 'ro', markersize=12, label='Risky Asset', zorder=5)
    
    # Mark some portfolio points
    weights = [0.25, 0.5, 0.75]
    for w in weights:
        sigma_p = w * sigma_risky
        mu_p = R_f + w * (mu_risky - R_f)
        ax.plot(sigma_p, mu_p, 'o', color='orange', markersize=8, zorder=4)
        ax.annotate(f'w={w:.2f}', xy=(sigma_p, mu_p), xytext=(5, 5), 
                   textcoords='offset points', fontsize=9)
    
    # Mark leveraged portfolio (w > 1)
    w_lev = 1.5
    sigma_lev = w_lev * sigma_risky
    mu_lev = R_f + w_lev * (mu_risky - R_f)
    ax.plot(sigma_lev, mu_lev, 's', color='purple', markersize=10, label='Leveraged (w=1.5)', zorder=4)
    
    # Shade dominated region
    ax.fill_between(sigma_vals, 0, mu_CAL, alpha=0.1, color='blue', label='Unattainable Region')
    
    # Add annotations
    ax.annotate(f'Slope = Sharpe Ratio = {sharpe:.2f}', 
               xy=(0.15, R_f + sharpe * 0.15), 
               xytext=(0.20, 0.06),
               fontsize=11, color='blue',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3),
               arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    
    ax.set_xlabel('Portfolio Risk (σ)', fontsize=13)
    ax.set_ylabel('Expected Return (μ)', fontsize=13)
    ax.set_title('Capital Allocation Line (CAL)', fontsize=15, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.35)
    ax.set_ylim(0, 0.15)
    
    # Format axes as percentages
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
    
    plt.tight_layout()
    plt.savefig('CAL.png', dpi=300, bbox_inches='tight')
    print("✓ Generated CAL.png")
    plt.close()


def generate_tangency():
    """Generate tangency portfolio with efficient frontier"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Parameters for multiple risky assets
    R_f = 0.02  # 2% risk-free rate
    
    # Simulate efficient frontier (hyperbola)
    # Using parametric approach
    t = np.linspace(-2, 2, 200)
    sigma_ef = 0.10 + 0.08 * t**2  # Parabolic in sigma
    mu_ef = 0.06 + 0.04 * t + 0.02 * t**2
    
    # Find tangency portfolio (maximize Sharpe ratio)
    sharpe_ratios = (mu_ef - R_f) / sigma_ef
    tangency_idx = np.argmax(sharpe_ratios)
    sigma_tangency = sigma_ef[tangency_idx]
    mu_tangency = mu_ef[tangency_idx]
    sharpe_tangency = sharpe_ratios[tangency_idx]
    
    # Plot efficient frontier
    ax.plot(sigma_ef, mu_ef, 'r-', linewidth=2.5, label='Efficient Frontier (Risky Assets)')
    
    # Plot CAL through tangency
    sigma_cal = np.linspace(0, 0.40, 100)
    mu_cal = R_f + sharpe_tangency * sigma_cal
    ax.plot(sigma_cal, mu_cal, 'b-', linewidth=2.5, label='Capital Allocation Line (CAL)')
    
    # Mark key points
    ax.plot(0, R_f, 'go', markersize=12, label=f'Risk-Free Asset ($R_f$ = {R_f*100:.0f}%)', zorder=5)
    ax.plot(sigma_tangency, mu_tangency, 'r*', markersize=20, 
           label=f'Tangency Portfolio M', zorder=6)
    
    # Draw tangent line annotation
    ax.annotate('Tangency Point\n(Optimal Risky Portfolio)', 
               xy=(sigma_tangency, mu_tangency), 
               xytext=(sigma_tangency + 0.05, mu_tangency + 0.02),
               fontsize=10,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.5),
               arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    # Mark some portfolio points on CAL
    for w in [0.4, 0.8, 1.2]:
        sigma_p = w * sigma_tangency
        mu_p = R_f + w * (mu_tangency - R_f)
        if sigma_p < 0.40:
            ax.plot(sigma_p, mu_p, 'o', color='orange', markersize=8, zorder=4)
    
    # Shade dominated region
    ax.fill_between(sigma_ef[tangency_idx:], mu_ef[tangency_idx:], 0, 
                    alpha=0.05, color='red', label='Inefficient Portfolios')
    
    ax.set_xlabel('Portfolio Risk (σ)', fontsize=13)
    ax.set_ylabel('Expected Return (μ)', fontsize=13)
    ax.set_title('Tangency Portfolio and the Capital Market Line', fontsize=15, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.40)
    ax.set_ylim(0, 0.16)
    
    # Format axes as percentages
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
    
    plt.tight_layout()
    plt.savefig('tangency.png', dpi=300, bbox_inches='tight')
    print("✓ Generated tangency.png")
    plt.close()


def generate_indifference_curves():
    """Generate indifference curves"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Parameters for indifference curves
    gamma_values = [1, 2, 4]  # Different risk aversion levels
    U_values = [0.02, 0.04, 0.06, 0.08]  # Different utility levels
    colors = ['blue', 'green', 'red']
    
    sigma_vals = np.linspace(0.01, 0.30, 300)
    
    # Plot indifference curves for different risk aversions
    for gamma_idx, gamma in enumerate([2]):  # Use gamma=2 for main plot
        for U in U_values:
            # mu = U + (gamma/2) * sigma^2
            mu = U + (gamma / 2) * sigma_vals**2
            
            # Only plot reasonable values
            mask = mu < 0.20
            ax.plot(sigma_vals[mask], mu[mask], '-', 
                   linewidth=2, alpha=0.7,
                   label=f'U = {U*100:.0f}%' if gamma_idx == 0 else '')
    
    # Add CAL for reference
    R_f = 0.03
    sharpe = 0.35
    mu_cal = R_f + sharpe * sigma_vals
    ax.plot(sigma_vals, mu_cal, 'k--', linewidth=2.5, alpha=0.7, label='CAL (for reference)')
    
    # Mark risk-free rate
    ax.plot(0, R_f, 'ro', markersize=10, label='Risk-Free Asset', zorder=5)
    
    # Add annotations
    ax.annotate('Higher Utility →', 
               xy=(0.15, 0.05), xytext=(0.15, 0.09),
               fontsize=11, ha='center',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.3),
               arrowprops=dict(arrowstyle='->', color='black', lw=2))
    
    ax.annotate('Indifference curves\nare parabolic:\nμ = U + (γ/2)σ²', 
               xy=(0.22, 0.08), xytext=(0.24, 0.12),
               fontsize=10,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.5),
               arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    
    ax.set_xlabel('Portfolio Risk (σ)', fontsize=13)
    ax.set_ylabel('Expected Return (μ)', fontsize=13)
    ax.set_title('Indifference Curves in Mean-Variance Space (γ=2)', fontsize=15, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.30)
    ax.set_ylim(0, 0.20)
    
    # Format axes as percentages
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
    
    plt.tight_layout()
    plt.savefig('indifference_curves.png', dpi=300, bbox_inches='tight')
    print("✓ Generated indifference_curves.png")
    plt.close()


def generate_optimal_portfolio():
    """Generate optimal portfolio choice showing tangency between CAL and indifference curve"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # CAL parameters
    R_f = 0.03
    mu_risky = 0.11
    sigma_risky = 0.20
    sharpe = (mu_risky - R_f) / sigma_risky
    
    # Generate CAL
    sigma_vals = np.linspace(0, 0.35, 300)
    mu_cal = R_f + sharpe * sigma_vals
    ax.plot(sigma_vals, mu_cal, 'b-', linewidth=3, label='Capital Allocation Line (CAL)', zorder=3)
    
    # Different investors with different risk aversions
    gamma_values = [1, 2, 4, 8]
    colors = ['red', 'green', 'purple', 'orange']
    labels = ['Low Risk Aversion (γ=1)', 'Moderate (γ=2)', 'High (γ=4)', 'Very High (γ=8)']
    
    for gamma, color, label in zip(gamma_values, colors, labels):
        # Optimal weight: w* = (mu - R_f) / (gamma * sigma^2)
        w_star = (mu_risky - R_f) / (gamma * sigma_risky**2)
        
        # Optimal portfolio
        sigma_opt = w_star * sigma_risky
        mu_opt = R_f + w_star * (mu_risky - R_f)
        
        # Plot optimal point
        ax.plot(sigma_opt, mu_opt, 'o', color=color, markersize=12, 
               label=label, zorder=5)
        
        # Draw multiple indifference curves for THIS investor (concentric/parallel parabolas)
        # U = mu - (gamma/2)*sigma^2
        U_opt = mu_opt - (gamma / 2) * sigma_opt**2
        
        # Plot 3 indifference curves: below optimal, at optimal, and above optimal
        U_levels = [U_opt - 0.015, U_opt, U_opt + 0.015]  # Three utility levels
        
        for U_level in U_levels:
            # Generate indifference curve: mu = U + (gamma/2)*sigma^2
            sigma_indiff = np.linspace(0.001, 0.35, 200)
            mu_indiff = U_level + (gamma / 2) * sigma_indiff**2
            
            # Only plot reasonable values
            mask = (mu_indiff > 0) & (mu_indiff < 0.20)
            
            # Different line styles for different utility levels
            if U_level == U_opt:
                # Optimal indifference curve (tangent to CAL)
                ax.plot(sigma_indiff[mask], mu_indiff[mask], '-', 
                       color=color, linewidth=2.5, alpha=0.8, zorder=2)
            else:
                # Other indifference curves (for reference)
                ax.plot(sigma_indiff[mask], mu_indiff[mask], ':', 
                       color=color, linewidth=1.5, alpha=0.4, zorder=1)
        
        # Add tangency annotation for one investor
        if gamma == 2:
            ax.annotate('Tangency:\nOptimal Choice', 
                       xy=(sigma_opt, mu_opt), 
                       xytext=(sigma_opt + 0.05, mu_opt - 0.02),
                       fontsize=10,
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.5),
                       arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    # Mark risk-free asset and risky asset
    ax.plot(0, R_f, 'go', markersize=12, label='Risk-Free Asset', zorder=6)
    ax.plot(sigma_risky, mu_risky, 'r*', markersize=15, label='Risky Asset', zorder=6)
    
    # Add text box explaining
    textstr = 'Each investor has\nconcentric indifference\ncurves (same γ)\n\nDifferent γ values\n→ different curvatures'
    ax.text(0.24, 0.025, textstr, fontsize=9,
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    ax.set_xlabel('Portfolio Risk (σ)', fontsize=13)
    ax.set_ylabel('Expected Return (μ)', fontsize=13)
    ax.set_title('Optimal Portfolio Choice: Different Risk Aversions', fontsize=15, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9, ncol=2)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.35)
    ax.set_ylim(0, 0.16)
    
    # Format axes as percentages
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
    
    plt.tight_layout()
    plt.savefig('optimal_portfolio.png', dpi=300, bbox_inches='tight')
    print("✓ Generated optimal_portfolio.png")
    plt.close()


def main():
    """Generate all figures"""
    print("\n" + "="*60)
    print("Generating figures for Lecture 06")
    print("Risk-Free Asset, Indifference Curves, and Lagrange Multipliers")
    print("="*60 + "\n")
    
    generate_CAL()
    generate_tangency()
    generate_indifference_curves()
    generate_optimal_portfolio()
    
    print("\n" + "="*60)
    print("All figures generated successfully!")
    print("="*60 + "\n")
    print("Generated files:")
    print("  1. CAL.png - Capital Allocation Line")
    print("  2. tangency.png - Tangency Portfolio with efficient frontier")
    print("  3. indifference_curves.png - Indifference curves")
    print("  4. optimal_portfolio.png - Optimal portfolio choice")
    print()


if __name__ == "__main__":
    main()
