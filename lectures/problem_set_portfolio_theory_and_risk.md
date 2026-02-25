# Problem Set: Portfolio Theory, Asset Pricing, and Risk Management

---

## Problem 1: Portfolio Construction for a Financial Advisor

**The Scenario:**

You are a quantitative analyst at a wealth management firm. A financial advisor needs your help creating an optimal investment plan for a new client. The client has a moderate risk tolerance and wants to invest in a portfolio of three well-known stocks:
- **"TechGrowth Inc." (TGI)**
- **"SteadyDividends Corp." (SDC)**
- **"GlobalInnovate Ltd." (GIL)**

Your team has provided the following forecasts for the next year:

| Asset | Expected Return (E[R]) | Volatility (Std. Dev, σ) |
|-------|------------------------|--------------------------|
| TGI   | 15%                    | 30%                      |
| SDC   | 8%                     | 18%                      |
| GIL   | 12%                    | 25%                      |

The correlation matrix between the asset returns is:

|       | TGI   | SDC   | GIL   |
|-------|-------|-------|-------|
| **TGI** | 1.0   | 0.2   | 0.4   |
| **SDC** | 0.2   | 1.0   | 0.3   |
| **GIL** | 0.4   | 0.3   | 1.0   |

The current risk-free rate is 3%.

**Your Task:**

The advisor sends you a request:

> "I need to show the client how we can build a superior portfolio. Can you run the numbers? I want to see the efficient frontier, find the best possible risky portfolio, and then figure out the final allocation for a client with a risk-aversion coefficient of 3.5. Show your work so I can explain the logic."

**What to deliver:**

1.  **The Efficient Frontier:** Plot the efficient frontier of the three risky assets. Highlight the Global Minimum Variance (GMV) portfolio on your plot.
2.  **The Optimal Risky Portfolio:** Calculate the weights, expected return, and volatility of the tangency (optimal risky) portfolio.
3.  **The Capital Allocation Line (CAL):** What is the equation of the CAL that passes through the optimal risky portfolio?
4.  **The Client's Complete Portfolio:** Determine the optimal allocation for this specific client $(\gamma=3.5)$ between the risk-free asset and the optimal risky portfolio. What are the weights in TGI, SDC, and GIL for this client's final portfolio?

---

## Problem 2: Project Valuation using the Capital Asset Pricing Model (CAPM)

**The Scenario:**

You are a strategic finance analyst at a large technology conglomerate. The R&D division has proposed a new, ambitious project in the Artificial Intelligence space. The project requires a significant upfront investment and is expected to generate cash flows over the next 10 years.

The CFO is skeptical and has tasked you with evaluating whether the project's expected return justifies its risk.

Market Data:
- 10-Year Government Bond Rate (Risk-Free Rate): 4.0%
- Expected Return on the Market Portfolio (e.g., S&P 500): 11.0%

Project & Company Data:
- The project's internal rate of return (IRR) is estimated to be 14.5%.
- Your company's stock has a beta of 1.2.
- However, this AI project is significantly riskier than the company's average business. You have identified three publicly traded "pure-play" AI companies with the following betas:
  - AI Corp A: 1.6
  - AI Corp B: 1.8
  - AI Corp C: 1.7

**Your Task:**

The CFO emails you:

> "Is this AI project a go or no-go? Don't just use the IRR. I need a market-based assessment. Calculate the appropriate required rate of return for this specific project using CAPM. Is it creating value for our shareholders or is it just a risky bet?"

**What to deliver:**

1.  **Estimate the Project Beta:** Determine and justify an appropriate beta for the AI project. Why shouldn't you use your company's beta of 1.2?
2.  **Calculate the Required Rate of Return:** Using the CAPM, calculate the cost of equity (the required return) for this project.
3.  **Draw the Security Market Line (SML):** Sketch the SML and plot both the market portfolio and the proposed AI project on it.
4.  **Make a Recommendation:** Is the project's expected return of 14.5% sufficient to compensate for its systematic risk? Explain your recommendation to the CFO with reference to the SML and the concept of 'alpha'.

---

## Problem 3: Hedge Fund Risk Assessment with Utility and VaR

**The Scenario:**

You are a junior risk manager at a hedge fund. The fund's flagship "Global Macro" portfolio is valued at $500 million. Based on historical data, the portfolio's annual expected return is 18% with a volatility of 20%. You can assume the returns are approximately normally distributed.

The portfolio manager has a quadratic utility function of the form: $U=E[R] - \gamma \sigma^2 / 2$, with a risk aversion coefficient of 4.

**Your Task:**

The Chief Risk Officer (CRO) wants a risk report on the portfolio.

> "Give me a snapshot of our risk profile. First, tell me the 1-day 99% VaR. Our internal limit is $5 million. Are we in breach? Also, the PM is considering a new trade that would reduce volatility to 18% but also lower the expected return to 16.5%. Should she take it, from a utility perspective?"

**What to deliver:**

1.  **Utility Analysis:**
    a. Calculate the utility of the current portfolio for the manager.
    b. Calculate the utility of the proposed new portfolio (with the new trade).
    c. Based purely on this utility model, should the portfolio manager make the trade?

2.  **Value at Risk (VaR) Calculation:**
    a. Convert the annual return and volatility to daily figures. (Assume 252 trading days in a year).
    b. Calculate the 1-day Value at Risk (VaR) at a 99% confidence level in dollar terms.

3.  **Risk Limit Compliance:** Does the portfolio's 1-day 99% VaR exceed the internal limit of $5 million?

4.  **Conceptual Discussion:** The CRO follows up, "What if the portfolio returns are not normal, but have 'fat tails'? What does that mean for our VaR calculation? Is our current VaR estimate likely to be too high or too low in that case?" Provide a brief, non-technical explanation.