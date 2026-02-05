"""
Generate all figures for Lectures 07 & 08:
- Lecture 07: Multi-Asset Portfolios
- Lecture 08: Capital Asset Pricing Model (CAPM)

This script creates:
Lecture 07:
1. efficient_frontier_risky.png - Efficient frontier with MVP
2. three_asset_space.png - Portfolio possibilities in 3-asset space
3. diversification_benefits.png - Risk reduction with number of assets
4. tangency_with_risky_frontier.png - CAL with tangency portfolio

Lecture 08:
5. security_market_line.png - SML showing CAPM relationship
6. systematic_idiosyncratic_risk.png - Risk decomposition
7. characteristic_line.png - Asset return vs market return regression
8. beta_estimation.png - Scatter plot with regression line

Author: Generated for Mathematics for Finance course
Date: February 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse
import seaborn as sns
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 7)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['legend.fontsize'] = 10

# ============================================================================
# LECTURE 07: Multi-Asset Portfolios
# ============================================================================

def generate_efficient_frontier_risky():
    """Generate efficient frontier for risky assets only (hyperbola)"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Three assets with different risk-return profiles
    n_assets = 3
    mu = np.array([0.08, 0.12, 0.15])  # Expected returns
    
    # Covariance matrix
    Sigma = np.array([
        [0.04, 0.01, 0.02],
        [0.01, 0.09, 0.03],
        [0.02, 0.03, 0.16]
    ])
    
    # Compute MVP
    ones = np.ones(n_assets)
    Sigma_inv = np.linalg.inv(Sigma)
    w_mvp = Sigma_inv @ ones / (ones @ Sigma_inv @ ones)
    mu_mvp = w_mvp @ mu
    sigma_mvp = np.sqrt(w_mvp @ Sigma @ w_mvp)
    
    # Generate efficient frontier by varying target returns
    mu_targets = np.linspace(mu_mvp, 0.18, 100)
    sigmas_efficient = []

    for mu_target in mu_targets:
        # Solve minimum variance problem for target return (efficient branch)
        def objective(w):
            return w @ Sigma @ w

        constraints = [
            {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
            {'type': 'eq', 'fun': lambda w: w @ mu - mu_target}
        ]

        result = minimize(objective, x0=np.ones(n_assets)/n_assets, 
                         constraints=constraints, method='SLSQP')

        if result.success:
            sigma = np.sqrt(result.fun)
            sigmas_efficient.append(sigma)

    sigmas_efficient = np.array(sigmas_efficient)

    # Now compute the inefficient branch (for mu_targets below MVP)
    mu_targets_ineff = np.linspace(mu_mvp - 0.04, mu_mvp, 60)
    sigmas_inefficient = []
    for mu_target in mu_targets_ineff:
        def objective(w):
            return w @ Sigma @ w

        constraints = [
            {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
            {'type': 'eq', 'fun': lambda w: w @ mu - mu_target}
        ]

        result = minimize(objective, x0=np.ones(n_assets)/n_assets, 
                         constraints=constraints, method='SLSQP')

        if result.success:
            sigma = np.sqrt(result.fun)
            sigmas_inefficient.append(sigma)

    sigmas_inefficient = np.array(sigmas_inefficient)

    # Plot efficient frontier (upper branch)
    ax.plot(sigmas_efficient, mu_targets, 'b-', linewidth=3, 
           label='Efficient Frontier', zorder=3)

    # Plot inefficient frontier (lower branch)
    ax.plot(sigmas_inefficient, mu_targets_ineff, 'r--', 
           linewidth=2, alpha=0.6, label='Inefficient Portfolios', zorder=2)
    
    # Mark MVP
    ax.plot(sigma_mvp, mu_mvp, 'g*', markersize=20, 
           label='Minimum Variance Portfolio (MVP)', zorder=5)
    
    # Mark individual assets
    for i in range(n_assets):
        sigma_i = np.sqrt(Sigma[i, i])
        ax.plot(sigma_i, mu[i], 'ro', markersize=10, zorder=4)
        ax.annotate(f'Asset {i+1}', xy=(sigma_i, mu[i]), 
                   xytext=(10, -5), textcoords='offset points', fontsize=10)
    
    # Shade dominated region
    ax.fill_between(sigmas_efficient, mu_mvp, mu_targets, 
                    alpha=0.1, color='blue', label='Efficient Region')
    # Define valid_ineff to ensure matching lengths and valid values
    valid_ineff = (np.array(sigmas_inefficient).shape[0] == np.array(mu_targets_ineff).shape[0])
    if valid_ineff:
        ax.fill_between(sigmas_inefficient, 0, mu_targets_ineff, 
                        alpha=0.1, color='red')
    else:
        min_len = min(len(sigmas_inefficient), len(mu_targets_ineff))
        ax.fill_between(sigmas_inefficient[:min_len], 0, mu_targets_ineff[:min_len], 
                        alpha=0.1, color='red')
    
    # Annotations
    ax.annotate('Efficient portfolios\n(maximum return for given risk)', 
               xy=(0.20, 0.14), xytext=(0.25, 0.16),
               fontsize=10,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.5),
               arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    
    ax.annotate('Inefficient portfolios\n(dominated)', 
               xy=(0.25, 0.10), xytext=(0.30, 0.08),
               fontsize=10, color='red',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='pink', alpha=0.5),
               arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    
    ax.set_xlabel('Portfolio Risk (σ)', fontsize=13)
    ax.set_ylabel('Expected Return (μ)', fontsize=13)
    ax.set_title('Efficient Frontier: Multiple Risky Assets', fontsize=15, fontweight='bold')
    ax.legend(loc='lower right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.10, 0.45)
    ax.set_ylim(0.06, 0.18)
    
    # Format axes as percentages
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
    
    plt.tight_layout()
    plt.savefig('efficient_frontier_risky.png', dpi=300, bbox_inches='tight')
    print("✓ Generated efficient_frontier_risky.png")
    plt.close()


def generate_three_asset_space():
    """Generate 3D visualization of three-asset portfolio space"""
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    
    # Generate portfolios on the simplex (w1 + w2 + w3 = 1, all non-negative)
    n_points = 50
    w1_range = np.linspace(0, 1, n_points)
    w2_range = np.linspace(0, 1, n_points)
    
    portfolios = []
    for w1 in w1_range:
        for w2 in w2_range:
            w3 = 1 - w1 - w2
            if w3 >= 0:  # Valid portfolio
                portfolios.append([w1, w2, w3])
    
    portfolios = np.array(portfolios)
    
    # Asset parameters
    mu = np.array([0.08, 0.12, 0.15])
    Sigma = np.array([
        [0.04, 0.01, 0.02],
        [0.01, 0.09, 0.03],
        [0.02, 0.03, 0.16]
    ])
    
    # Compute portfolio returns and risks
    portfolio_returns = portfolios @ mu
    portfolio_risks = np.array([np.sqrt(w @ Sigma @ w) for w in portfolios])
    
    # Color by Sharpe ratio
    sharpe_ratios = (portfolio_returns - 0.03) / portfolio_risks
    
    # Create scatter plot
    scatter = ax.scatter(portfolios[:, 0], portfolios[:, 1], portfolio_risks,
                        c=portfolio_returns, cmap='viridis', s=20, alpha=0.6)
    
    # Mark corner portfolios (individual assets)
    corners = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    corner_returns = corners @ mu
    corner_risks = np.array([np.sqrt(w @ Sigma @ w) for w in corners])
    
    ax.scatter(corners[:, 0], corners[:, 1], corner_risks,
              c='red', s=200, marker='*', edgecolors='black', linewidths=2,
              label='Individual Assets', zorder=10)
    
    # Labels
    for i, (w, ret, risk) in enumerate(zip(corners, corner_returns, corner_risks)):
        ax.text(w[0], w[1], risk + 0.02, f'Asset {i+1}', fontsize=10, fontweight='bold')
    
    ax.set_xlabel('Weight in Asset 1 ($w_1$)', fontsize=12)
    ax.set_ylabel('Weight in Asset 2 ($w_2$)', fontsize=12)
    ax.set_zlabel('Portfolio Risk (σ)', fontsize=12)
    ax.set_title('Three-Asset Portfolio Space\n(Color = Expected Return)', 
                fontsize=14, fontweight='bold')
    
    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.6, aspect=10)
    cbar.set_label('Expected Return (μ)', fontsize=11)
    
    # Legend
    ax.legend(loc='upper right', fontsize=10)
    
    # View angle
    ax.view_init(elev=20, azim=45)
    
    plt.tight_layout()
    plt.savefig('three_asset_space.png', dpi=300, bbox_inches='tight')
    print("✓ Generated three_asset_space.png")
    plt.close()


def generate_diversification_benefits():
    """Generate plot showing risk reduction with number of assets"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Parameters
    sigma_individual = 0.30  # 30% individual asset volatility
    avg_correlation = 0.35   # Average pairwise correlation
    
    # Number of assets
    n_values = np.arange(1, 101)
    
    # Portfolio variance for equally-weighted portfolio
    # sigma_p^2 = (1/n)*sigma^2 + ((n-1)/n)*rho*sigma^2
    variance_portfolio = (1/n_values) * sigma_individual**2 + \
                         ((n_values - 1)/n_values) * avg_correlation * sigma_individual**2
    
    std_portfolio = np.sqrt(variance_portfolio)
    
    # Asymptotic limit (systematic risk)
    systematic_risk = np.sqrt(avg_correlation) * sigma_individual
    
    # Plot
    ax.plot(n_values, std_portfolio * 100, 'b-', linewidth=2.5, label='Portfolio Risk')
    ax.axhline(systematic_risk * 100, color='red', linestyle='--', linewidth=2,
              label=f'Systematic Risk Limit = {systematic_risk*100:.1f}%')
    ax.axhline(sigma_individual * 100, color='green', linestyle=':', linewidth=2,
              label=f'Individual Asset Risk = {sigma_individual*100:.0f}%')
    
    # Shade diversifiable risk
    ax.fill_between(n_values, systematic_risk * 100, std_portfolio * 100,
                    alpha=0.3, color='orange', label='Diversifiable Risk')
    
    # Mark key points
    key_n = [1, 5, 10, 20, 50]
    for n in key_n:
        idx = n - 1
        ax.plot(n, std_portfolio[idx] * 100, 'ko', markersize=8)
        if n <= 20:
            ax.annotate(f'n={n}\n{std_portfolio[idx]*100:.1f}%',
                       xy=(n, std_portfolio[idx] * 100),
                       xytext=(10, 10), textcoords='offset points',
                       fontsize=9, ha='left')
    
    # Annotations
    ax.annotate('Rapid risk reduction\nwith first few assets',
               xy=(10, 23), xytext=(30, 26),
               fontsize=10,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.5),
               arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    ax.annotate('Diminishing benefits\nas n increases',
               xy=(60, 19), xytext=(65, 22),
               fontsize=10,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.5),
               arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    ax.set_xlabel('Number of Assets in Portfolio (n)', fontsize=13)
    ax.set_ylabel('Portfolio Risk (%)', fontsize=13)
    ax.set_title('Diversification Benefits: Risk Reduction with Portfolio Size', 
                fontsize=15, fontweight='bold')
    ax.legend(loc='upper right', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 100)
    ax.set_ylim(15, 32)
    
    # Add text box with formula
    textstr = 'Equally-weighted portfolio:\n' + \
              r'$\sigma_p = \sqrt{\frac{1}{n}\sigma^2 + \frac{n-1}{n}\rho\sigma^2}$' + '\n' + \
              f'ρ = {avg_correlation:.2f}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.7)
    ax.text(0.65, 0.75, textstr, transform=ax.transAxes, fontsize=10,
           verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    plt.savefig('diversification_benefits.png', dpi=300, bbox_inches='tight')
    print("✓ Generated diversification_benefits.png")
    plt.close()


def generate_tangency_with_risky_frontier():
    """Generate CAL with tangency portfolio and risky efficient frontier"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Asset parameters
    n_assets = 3
    mu = np.array([0.08, 0.12, 0.15])
    Sigma = np.array([
        [0.04, 0.01, 0.02],
        [0.01, 0.09, 0.03],
        [0.02, 0.03, 0.16]
    ])
    R_f = 0.03
    
    # Compute MVP
    ones = np.ones(n_assets)
    Sigma_inv = np.linalg.inv(Sigma)
    w_mvp = Sigma_inv @ ones / (ones @ Sigma_inv @ ones)
    mu_mvp = w_mvp @ mu
    sigma_mvp = np.sqrt(w_mvp @ Sigma @ w_mvp)
    
    # Compute tangency (market) portfolio
    w_tangency = Sigma_inv @ (mu - R_f * ones) / (ones @ Sigma_inv @ (mu - R_f * ones))
    mu_tangency = w_tangency @ mu
    sigma_tangency = np.sqrt(w_tangency @ Sigma @ w_tangency)
    sharpe_tangency = (mu_tangency - R_f) / sigma_tangency
    
    # Generate efficient frontier
    mu_targets = np.linspace(mu_mvp, 0.18, 100)
    sigmas_efficient = []
    
    for mu_target in mu_targets:
        def objective(w):
            return w @ Sigma @ w
        
        constraints = [
            {'type': 'eq', 'fun': lambda w: np.sum(w) - 1},
            {'type': 'eq', 'fun': lambda w: w @ mu - mu_target}
        ]
        
        result = minimize(objective, x0=np.ones(n_assets)/n_assets, 
                         constraints=constraints, method='SLSQP')
        
        if result.success:
            sigmas_efficient.append(np.sqrt(result.fun))
    
    sigmas_efficient = np.array(sigmas_efficient)
    
    # Plot efficient frontier
    ax.plot(sigmas_efficient, mu_targets, 'r-', linewidth=2.5, 
           label='Efficient Frontier (Risky Assets)', zorder=2)
    
    # Plot CAL through tangency
    sigma_cal = np.linspace(0, 0.40, 100)
    mu_cal = R_f + sharpe_tangency * sigma_cal
    ax.plot(sigma_cal, mu_cal, 'b-', linewidth=3, 
           label='Capital Allocation Line (CAL)', zorder=3)
    
    # Mark key points
    ax.plot(0, R_f, 'go', markersize=12, label=f'Risk-Free Asset (R_f = {R_f*100:.0f}%)', zorder=5)
    ax.plot(sigma_mvp, mu_mvp, 'g*', markersize=18, label='Minimum Variance Portfolio', zorder=5)
    ax.plot(sigma_tangency, mu_tangency, 'r*', markersize=20, 
           label='Tangency Portfolio (Market)', zorder=6)
    
    # Mark individual assets
    for i in range(n_assets):
        sigma_i = np.sqrt(Sigma[i, i])
        ax.plot(sigma_i, mu[i], 'ko', markersize=8, zorder=4, alpha=0.6)
    
    # Draw tangent line from risk-free to tangency
    ax.plot([0, sigma_tangency], [R_f, mu_tangency], 'b--', linewidth=1.5, alpha=0.5)
    
    # Annotations
    ax.annotate('Tangency Portfolio\n(Highest Sharpe Ratio)',
               xy=(sigma_tangency, mu_tangency),
               xytext=(sigma_tangency + 0.05, mu_tangency + 0.02),
               fontsize=10,
               bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.6),
               arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    ax.annotate(f'Sharpe Ratio = {sharpe_tangency:.3f}',
               xy=(0.15, R_f + sharpe_tangency * 0.15),
               xytext=(0.20, 0.065),
               fontsize=10, color='blue',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.5),
               arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    
    # Shade dominated region
    ax.fill_between(sigmas_efficient, mu_mvp, mu_targets,
                    alpha=0.05, color='red')
    
    ax.set_xlabel('Portfolio Risk (σ)', fontsize=13)
    ax.set_ylabel('Expected Return (μ)', fontsize=13)
    ax.set_title('Capital Allocation Line and Tangency Portfolio', 
                fontsize=15, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 0.40)
    ax.set_ylim(0.02, 0.18)
    
    # Format axes as percentages
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x*100:.0f}%'))
    
    plt.tight_layout()
    plt.savefig('tangency_with_risky_frontier.png', dpi=300, bbox_inches='tight')
    print("✓ Generated tangency_with_risky_frontier.png")
    plt.close()


# ============================================================================
# LECTURE 08: CAPM
# ============================================================================

def generate_security_market_line():
    """Generate Security Market Line (SML)"""
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Parameters
    R_f = 0.03  # 3% risk-free rate
    R_m = 0.10  # 10% market return
    market_risk_premium = R_m - R_f
    
    # Beta range
    beta_range = np.linspace(-0.5, 2.0, 100)
    
    # SML: E[R] = R_f + beta * (E[R_m] - R_f)
    expected_returns = R_f + beta_range * market_risk_premium
    
    # Plot SML
    ax.plot(beta_range, expected_returns * 100, 'b-', linewidth=3, label='Security Market Line (SML)')
    
    # Mark key points
    ax.plot(0, R_f * 100, 'go', markersize=12, label='Risk-Free Asset (β=0)', zorder=5)
    ax.plot(1, R_m * 100, 'r*', markersize=20, label='Market Portfolio (β=1)', zorder=5)
    
    # Example assets
    assets = [
        {'name': 'Defensive Stock', 'beta': 0.6, 'color': 'green'},
        {'name': 'Aggressive Stock', 'beta': 1.4, 'color': 'red'},
        {'name': 'Market-Neutral', 'beta': 0.0, 'color': 'gray'},
    ]
    
    for asset in assets:
        beta = asset['beta']
        expected_return = R_f + beta * market_risk_premium
        ax.plot(beta, expected_return * 100, 'o', color=asset['color'], 
               markersize=10, label=asset['name'], zorder=4)
        ax.annotate(f"β={beta:.1f}\nE[R]={expected_return*100:.1f}%",
                   xy=(beta, expected_return * 100),
                   xytext=(10, -15), textcoords='offset points',
                   fontsize=9, ha='left')
    
    # Example of mispriced assets
    # Overpriced (below SML)
    beta_over = 1.2
    actual_return_over = R_f + 0.8 * beta_over * market_risk_premium
    capm_return_over = R_f + beta_over * market_risk_premium
    ax.plot(beta_over, actual_return_over * 100, 's', color='purple', 
           markersize=10, label='Overpriced Asset', zorder=4)
    ax.plot([beta_over, beta_over], [actual_return_over * 100, capm_return_over * 100],
           'k--', linewidth=1.5, alpha=0.5)
    ax.annotate('Negative α\n(Overpriced)',
               xy=(beta_over, actual_return_over * 100),
               xytext=(15, -20), textcoords='offset points',
               fontsize=8, color='purple')
    
    # Underpriced (above SML)
    beta_under = 0.8
    actual_return_under = R_f + 1.3 * beta_under * market_risk_premium
    capm_return_under = R_f + beta_under * market_risk_premium
    ax.plot(beta_under, actual_return_under * 100, '^', color='orange', 
           markersize=10, label='Underpriced Asset', zorder=4)
    ax.plot([beta_under, beta_under], [capm_return_under * 100, actual_return_under * 100],
           'k--', linewidth=1.5, alpha=0.5)
    ax.annotate('Positive α\n(Underpriced)',
               xy=(beta_under, actual_return_under * 100),
               xytext=(15, 5), textcoords='offset points',
               fontsize=8, color='orange')
    
    # Add CAPM equation
    textstr = 'CAPM Equation:\n' + \
              r'$\mathbb{E}[R_i] = R_f + \beta_i(\mathbb{E}[R_M] - R_f)$' + '\n\n' + \
              f'Market Risk Premium = {market_risk_premium*100:.0f}%\n' + \
              f'Slope of SML = {market_risk_premium*100:.0f}%'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.7)
    ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=10,
           verticalalignment='top', bbox=props)
    
    ax.axhline(R_f * 100, color='gray', linestyle=':', linewidth=1, alpha=0.5)
    ax.axvline(0, color='gray', linestyle=':', linewidth=1, alpha=0.5)
    ax.axvline(1, color='gray', linestyle=':', linewidth=1, alpha=0.5)
    
    ax.set_xlabel('Beta (β) - Systematic Risk', fontsize=13)
    ax.set_ylabel('Expected Return (%)', fontsize=13)
    ax.set_title('Security Market Line (SML)', fontsize=15, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9, ncol=2)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-0.2, 1.8)
    ax.set_ylim(1, 16)
    
    plt.tight_layout()
    plt.savefig('security_market_line.png', dpi=300, bbox_inches='tight')
    print("✓ Generated security_market_line.png")
    plt.close()


def generate_systematic_idiosyncratic_risk():
    """Generate risk decomposition: systematic vs idiosyncratic"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left panel: Stacked bar chart of risk decomposition
    assets = ['Defensive\n(β=0.5)', 'Market\n(β=1.0)', 'Aggressive\n(β=1.5)', 'High Idio.\n(β=1.0)']
    betas = [0.5, 1.0, 1.5, 1.0]
    sigma_m = 0.20  # Market volatility
    
    systematic_risk = [beta * sigma_m for beta in betas]
    idiosyncratic_risk = [0.10, 0.10, 0.10, 0.25]  # Different idiosyncratic risks
    
    total_risk = [np.sqrt(sys**2 + idio**2) for sys, idio in zip(systematic_risk, idiosyncratic_risk)]
    
    x = np.arange(len(assets))
    width = 0.6
    
    # Bars
    p1 = ax1.bar(x, systematic_risk, width, label='Systematic Risk (β·σ_M)', 
                 color='steelblue', alpha=0.8)
    p2 = ax1.bar(x, idiosyncratic_risk, width, bottom=systematic_risk,
                 label='Idiosyncratic Risk', color='coral', alpha=0.8)
    
    # Total risk markers
    ax1.plot(x, total_risk, 'ko', markersize=10, label='Total Risk', zorder=5)
    for i, (xi, risk) in enumerate(zip(x, total_risk)):
        ax1.plot([xi, xi], [0, risk], 'k--', linewidth=1.5, alpha=0.3)
    
    ax1.set_ylabel('Risk (Volatility)', fontsize=12)
    ax1.set_title('Risk Decomposition by Asset Type', fontsize=13, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(assets, fontsize=10)
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3, axis='y')
    ax1.set_ylim(0, 0.40)
    
    # Format y-axis as percentages
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    
    # Add annotations
    ax1.annotate('Only systematic risk\nis priced in CAPM',
                xy=(1, 0.10), xytext=(2, 0.35),
                fontsize=9,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
    
    # Right panel: R-squared interpretation
    r_squared_values = [0.25, 0.50, 0.75, 0.95]
    labels = ['Low\n(R²=0.25)', 'Moderate\n(R²=0.50)', 'High\n(R²=0.75)', 'Very High\n(R²=0.95)']
    
    systematic_fraction = r_squared_values
    idiosyncratic_fraction = [1 - r2 for r2 in r_squared_values]
    
    x2 = np.arange(len(labels))
    
    p3 = ax2.bar(x2, systematic_fraction, width, label='Systematic (Explained by Market)',
                color='steelblue', alpha=0.8)
    p4 = ax2.bar(x2, idiosyncratic_fraction, width, bottom=systematic_fraction,
                label='Idiosyncratic (Unexplained)', color='coral', alpha=0.8)
    
    ax2.set_ylabel('Fraction of Total Variance', fontsize=12)
    ax2.set_title('Variance Decomposition: R² Interpretation', fontsize=13, fontweight='bold')
    ax2.set_xticks(x2)
    ax2.set_xticklabels(labels, fontsize=10)
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.set_ylim(0, 1.05)
    
    # Format y-axis as percentages
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{y*100:.0f}%'))
    
    # Add formula
    textstr = r'$\text{Var}(R_i) = \beta_i^2 \text{Var}(R_M) + \text{Var}(\varepsilon_i)$' + '\n\n' + \
              r'$R^2 = \frac{\beta_i^2 \text{Var}(R_M)}{\text{Var}(R_i)}$'
    props = dict(boxstyle='round', facecolor='lightblue', alpha=0.7)
    ax2.text(0.5, 0.5, textstr, transform=ax2.transAxes, fontsize=10,
            verticalalignment='center', horizontalalignment='center', bbox=props)
    
    plt.tight_layout()
    plt.savefig('systematic_idiosyncratic_risk.png', dpi=300, bbox_inches='tight')
    print("✓ Generated systematic_idiosyncratic_risk.png")
    plt.close()


def generate_characteristic_line():
    """Generate characteristic line (regression of asset returns vs market)"""
    np.random.seed(42)
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Simulate data
    n_periods = 60
    R_f = 0.02 / 12  # Monthly risk-free rate
    
    # Market returns (monthly)
    R_m = np.random.normal(0.01, 0.04, n_periods)  # Mean 1%, std 4% monthly
    
    # Asset returns with different betas
    beta = 1.35
    alpha = 0.005  # 0.5% monthly alpha (6% annualized)
    idiosyncratic_vol = 0.03
    
    epsilon = np.random.normal(0, idiosyncratic_vol, n_periods)
    R_i = alpha + beta * R_m + epsilon
    
    # Excess returns
    excess_R_m = R_m - R_f
    excess_R_i = R_i - R_f
    
    # Regression
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(excess_R_m, excess_R_i)
    
    # Plot scatter
    ax.scatter(excess_R_m * 100, excess_R_i * 100, alpha=0.6, s=50,
              color='steelblue', edgecolors='black', linewidth=0.5,
              label='Monthly Excess Returns')
    
    # Plot regression line
    x_line = np.array([excess_R_m.min(), excess_R_m.max()])
    y_line = intercept * 100 + slope * (x_line * 100)
    ax.plot(x_line * 100, y_line, 'r-', linewidth=2.5,
           label=f'Characteristic Line: α={intercept*100:.2f}%, β={slope:.2f}')
    
    # Add reference line for zero alpha
    y_line_zero = slope * (x_line * 100)
    ax.plot(x_line * 100, y_line_zero, 'g--', linewidth=2, alpha=0.6,
           label='CAPM Prediction (α=0)')
    
    # Add 45-degree line (beta = 1)
    x_45 = np.array([excess_R_m.min() * 100, excess_R_m.max() * 100])
    ax.plot(x_45, x_45, 'k:', linewidth=1.5, alpha=0.4, label='β=1 Reference')
    
    # Annotations
    textstr = 'Regression Equation:\n' + \
              r'$R_i - R_f = \alpha + \beta(R_M - R_f) + \varepsilon$' + '\n\n' + \
              f'α (alpha) = {intercept*100:.2f}% per month\n' + \
              f'β (beta) = {slope:.2f}\n' + \
              f'R² = {r_value**2:.2f}\n' + \
              f't-stat(α) = {intercept/std_err:.2f}'
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
           verticalalignment='top', bbox=props)
    
    ax.axhline(0, color='gray', linestyle='-', linewidth=0.8, alpha=0.5)
    ax.axvline(0, color='gray', linestyle='-', linewidth=0.8, alpha=0.5)
    
    ax.set_xlabel('Market Excess Return (%) [R_M - R_f]', fontsize=13)
    ax.set_ylabel('Asset Excess Return (%) [R_i - R_f]', fontsize=13)
    ax.set_title('Characteristic Line: Asset Return vs Market Return', 
                fontsize=15, fontweight='bold')
    ax.legend(loc='lower right', fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('characteristic_line.png', dpi=300, bbox_inches='tight')
    print("✓ Generated characteristic_line.png")
    plt.close()


def generate_beta_estimation():
    """Generate beta estimation scatter plot with multiple assets"""
    np.random.seed(123)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 12))
    
    # Simulate market returns
    n_periods = 60
    R_f = 0.02 / 12
    R_m = np.random.normal(0.01, 0.05, n_periods)
    excess_R_m = R_m - R_f
    
    # Different assets with different betas
    assets = [
        {'name': 'Defensive Stock (β=0.6)', 'beta': 0.6, 'alpha': 0.001, 'idio_vol': 0.03, 'ax': ax1},
        {'name': 'Market-Like Stock (β=1.0)', 'beta': 1.0, 'alpha': 0.000, 'idio_vol': 0.02, 'ax': ax2},
        {'name': 'Aggressive Stock (β=1.5)', 'beta': 1.5, 'alpha': 0.002, 'idio_vol': 0.04, 'ax': ax3},
        {'name': 'Low Correlation (β=0.3)', 'beta': 0.3, 'alpha': 0.003, 'idio_vol': 0.06, 'ax': ax4},
    ]
    
    for asset in assets:
        ax = asset['ax']
        beta_true = asset['beta']
        alpha_true = asset['alpha']
        idio_vol = asset['idio_vol']
        
        # Generate asset returns
        epsilon = np.random.normal(0, idio_vol, n_periods)
        R_i = alpha_true + beta_true * R_m + epsilon
        excess_R_i = R_i - R_f
        
        # Regression
        from scipy import stats
        slope, intercept, r_value, p_value, std_err = stats.linregress(excess_R_m, excess_R_i)
        
        # Scatter plot
        ax.scatter(excess_R_m * 100, excess_R_i * 100, alpha=0.6, s=40,
                  color='steelblue', edgecolors='black', linewidth=0.5)
        
        # Regression line
        x_line = np.array([excess_R_m.min(), excess_R_m.max()])
        y_line = intercept * 100 + slope * (x_line * 100)
        ax.plot(x_line * 100, y_line, 'r-', linewidth=2)
        
        # True relationship (if different from estimated)
        y_true = alpha_true * 100 + beta_true * (x_line * 100)
        ax.plot(x_line * 100, y_true, 'g--', linewidth=1.5, alpha=0.5, label='True β')
        
        ax.axhline(0, color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
        ax.axvline(0, color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
        
        # Annotations
        textstr = f'Estimated: β̂={slope:.2f}, α̂={intercept*100:.2f}%\n' + \
                  f'True: β={beta_true:.2f}, α={alpha_true*100:.2f}%\n' + \
                  f'R²={r_value**2:.2f}, SE(β̂)={std_err:.2f}'
        props = dict(boxstyle='round', facecolor='lightyellow', alpha=0.8)
        ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=8,
               verticalalignment='top', bbox=props)
        
        ax.set_xlabel('Market Excess Return (%)', fontsize=10)
        ax.set_ylabel('Asset Excess Return (%)', fontsize=10)
        ax.set_title(asset['name'], fontsize=11, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=8, loc='lower right')
    
    plt.suptitle('Beta Estimation: Different Asset Types (60 monthly observations)', 
                fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig('beta_estimation.png', dpi=300, bbox_inches='tight')
    print("✓ Generated beta_estimation.png")
    plt.close()


# ============================================================================
# Main execution
# ============================================================================

def main():
    """Generate all figures for Lectures 07 and 08"""
    print("\n" + "="*70)
    print("Generating figures for Lectures 07 & 08")
    print("="*70 + "\n")
    
    print("LECTURE 07: Multi-Asset Portfolios")
    print("-" * 70)
    generate_efficient_frontier_risky()
    generate_three_asset_space()
    generate_diversification_benefits()
    generate_tangency_with_risky_frontier()
    
    print("\nLECTURE 08: Capital Asset Pricing Model (CAPM)")
    print("-" * 70)
    generate_security_market_line()
    generate_systematic_idiosyncratic_risk()
    generate_characteristic_line()
    generate_beta_estimation()
    
    print("\n" + "="*70)
    print("All figures generated successfully!")
    print("="*70 + "\n")
    print("Generated files:")
    print("\nLecture 07:")
    print("  1. efficient_frontier_risky.png")
    print("  2. three_asset_space.png")
    print("  3. diversification_benefits.png")
    print("  4. tangency_with_risky_frontier.png")
    print("\nLecture 08:")
    print("  5. security_market_line.png")
    print("  6. systematic_idiosyncratic_risk.png")
    print("  7. characteristic_line.png")
    print("  8. beta_estimation.png")
    print()


if __name__ == "__main__":
    main()
