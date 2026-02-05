# Figure Generation for Lectures 7 & 8

## Summary

I've created a comprehensive Python script to generate all necessary figures for Lectures 7 (Multi-Asset Portfolios) and 8 (Capital Asset Pricing Model). The figures have been integrated into both lecture files.

## Generated Files

### Script Location
- `/Users/hydmbk165294/Desktop/mathematics-for-finance/lectures/Figures/generate_lecture_07_08_figures.py`

### Figures to be Generated

#### Lecture 07: Multi-Asset Portfolios
1. **efficient_frontier_risky.png** - Efficient frontier showing the hyperbola of risky portfolios with MVP marked
2. **three_asset_space.png** - 3D visualization of the portfolio simplex for three assets
3. **diversification_benefits.png** - Plot showing risk reduction as number of assets increases
4. **tangency_with_risky_frontier.png** - CAL tangent to the efficient frontier at the market portfolio

#### Lecture 08: Capital Asset Pricing Model (CAPM)
5. **security_market_line.png** - SML showing the beta-return relationship with example assets
6. **systematic_idiosyncratic_risk.png** - Two-panel figure decomposing risk components
7. **characteristic_line.png** - Regression of asset returns vs market returns
8. **beta_estimation.png** - Four-panel comparison of beta estimation for different asset types

## Running the Script

### Prerequisites
Install required Python packages:
```bash
pip3 install numpy matplotlib seaborn scipy
```

### Execute
```bash
cd /Users/hydmbk165294/Desktop/mathematics-for-finance/lectures/Figures
python3 generate_lecture_07_08_figures.py
```

The script will generate all 8 figures and save them in the `Figures/` directory.

## Figure Integration

All figures have been integrated into the lecture files at appropriate locations:

### Lecture 07 Updates
- Section 5 (Three Risky Securities): Added 3D portfolio space visualization
- Section 4 (Diversification): Added diversification benefits plot
- Section 7 (Minimum Variance Line): Updated existing figure reference with better caption
- Section 8 (Adding Risk-Free Asset): Added tangency portfolio with CAL figure

### Lecture 08 Updates
- Section 6 (Security Market Line): Added SML figure
- Section 7 (Systematic vs Idiosyncratic Risk): Added risk decomposition figure
- Section 8 (Characteristic Line): Added characteristic line regression figure
- Section 8 (Estimating Beta): Added multi-panel beta estimation figure

## Technical Details

### Style Consistency
The script follows the same style as your `generate_lecture_06_figures.py`:
- Uses seaborn whitegrid style
- 10x7 inch figure size
- Professional color schemes
- Detailed annotations and labels
- Percentage formatting on axes where appropriate
- 300 DPI resolution for publication quality

### Figure Features
Each figure includes:
- Clear titles and axis labels
- Legends with descriptive text
- Annotations explaining key concepts
- Mathematical formulas where relevant
- Color-coding for clarity
- Grid lines for readability

### Error Handling
The script uses:
- Numerical optimization (scipy.optimize.minimize) for portfolio problems
- Linear regression (scipy.stats.linregress) for CAPM estimation
- Robust random seed setting for reproducibility

## Next Steps

1. Install the required packages (if not already installed)
2. Run the script to generate all figures
3. Verify that all 8 PNG files are created in the Figures/ directory
4. View the updated lecture files to see the integrated figures

All figure references in the markdown files use relative paths and include descriptive captions.
