# Problem Set: Foundations of Mathematical Finance

**Course:** Mathematics for Finance  
**Instructor:** Sukrit Mittal, Franklin Templeton Investments  
**Total Problems:** 3 (Real-world, industry-grade problems)

---

## Problem 1: Structured Product Design at a Investment Bank

**The Scenario:**

You work in the Product Development team at a major investment bank. A wealthy client approaches you with an interesting request:

> "I want to invest ₹1 crore in a 1-year structured product. I'm worried about downside risk—if the market crashes, I want a cushion. But I also want to participate in any upside. Can you design something that costs exactly ₹1 crore today?"

Your team has identified a suitable underlying risky bond for this product. The bond currently trades at ₹100. Market analysis shows it could reach ₹130 (if conditions improve) or ₹70 (if they deteriorate) in one year. The risk-free rate is 5% per annum.

**What You Know:**
- Underlying bond: current price ₹100, future values ₹130 (up) or ₹70 (down)
- Risk-free rate: 5% per annum
- Product budget: Must cost exactly ₹100 (sells at par)
- Client's preferences: Downside protection + upside participation

**Your Task:**

Your boss walks into your office and says:

> "Design a payoff structure that satisfies the client. Figure out what guarantees we can offer and what upside the client can capture. Then verify your design actually works—make sure there's no hidden arbitrage. Use pricing theory, not guesses."

**What to deliver:**

1. A proposed payoff structure with specific strike price and participation rate
2. Proof that your design is arbitrage-free
3. Verification that your product prices at exactly ₹100
4. A brief explanation to the client (non-technical) of why they can't have 100% downside protection AND 100% upside participation simultaneously

---

## Problem 2: Currency Hedging Strategy for a Multinational Corporation

**The Scenario:**

You're a treasurer at a multinational corporation. Your company has just acquired subsidiaries in three countries and inherited their debt obligations. You now manage a mixed-currency bond portfolio:

| Currency | Asset | Amount | Coupon | Maturity |
|----------|-------|--------|--------|----------|
| INR (Domestic) | Govt Bond | ₹100 crore | 5% p.a. | 2 years |
| USD (Foreign) | Treasury | $30 million | 3% p.a. | 2 years |
| EUR (Foreign) | Corp Bond | €20 million | 4% p.a. | 2 years |

Your CFO just sent you this message:

> "We have foreign currency risk now. Our shareholders are in India, so our P&L is in INR. Every time the rupee strengthens, we lose on our USD and EUR bonds. Every time it weakens, we gain. This is unpredictable. Should we hedge? What's our true economic exposure? And how much would hedging cost us?"

Current market conditions:
- INR rate: 5.5% (continuously compounded)
- USD rate: 2.5%
- EUR rate: 3.0%
- Spot rates: 83 INR/USD, 90 INR/EUR

**Your Task:**

1. **Value the portfolio:** Convert everything to INR. What's the total value today?

2. **Identify the exposure:** What does interest rate parity tell you about expected currency movements? Is the rupee likely to appreciate or depreciate?

3. **Calculate hedging costs:** If you use forward contracts to lock in exchange rates, what rates would you be locking in? How do they compare to current spot rates?

4. **Scenario analysis:** 
   - What happens to your portfolio if INR rates spike 100 bps while foreign rates stay flat?
   - What happens if the rupee suddenly strengthens by 2.4% against the dollar?

5. **Hedging recommendation:** Based on your analysis, should the corporation hedge its foreign exposure? What would be the trade-offs of hedging vs. not hedging?

**What you deliver:**

- Current portfolio valuation in INR
- Calculation of no-arbitrage forward exchange rates
- Sensitivity analysis under different scenarios
- A recommendation memo to the CFO with clear reasoning on whether to hedge and why

---

## Why These Problems Matter

**Problem 1** teaches you the essence of derivatives pricing: how to design financial products that satisfy constraints (cost, payoff profile) while respecting no-arbitrage.

**Problem 2** reveals why multinational corporations exist in a web of currency risks. Every foreign investment is also a currency bet. Understanding interest rate parity and forward pricing is central to corporate finance.

All three problems ask you to think like a finance professional: diagnose the problem, apply theory, calculate precisely, and communicate the results to decision-makers.

Welcome to real-world finance!