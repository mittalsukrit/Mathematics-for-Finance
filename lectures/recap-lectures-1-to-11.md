---
layout: default
title: "Recap: Lectures 1-11"
---

<style>
  .slides {
    scroll-snap-type: y mandatory;
    overflow-y: scroll;
    height: 100vh;

    /* Start slide counter */
    counter-reset: slide;
  }

  .slide {
    scroll-snap-align: start;
    min-height: 100vh;
    padding: 4rem;
    padding-top: 1rem;
    box-sizing: border-box;

    /* Ensure relative positioning for numbering */
    position: relative;
  }

  /* Nice-to-have: smoother feel */
  html { scroll-behavior: smooth; }

  /* Automatic slide numbering */
  .slide::before {
    counter-increment: slide;
    content: "Slide " counter(slide);
    position: absolute;
    top: 1rem;   /* footer-like placement */
    right: 2rem;
    font-size: 1rem;
    color: #666;
  }
</style>

<div class="slides" markdown="1">

<section class="slide" markdown="1">

# Recap: Lectures 1--11

**Sukrit Mittal**
Franklin Templeton Investments

*Where we've been, and why it matters for what comes next.*

</section>

<section class="slide" markdown="1">

## The Big Picture

We have built a toolkit -- layer by layer -- for understanding how financial markets work mathematically.

| Block | Lectures | Core question |
|-------|----------|---------------|
| **Foundations** | 1--4 | How do we model markets and the value of money? |
| **Portfolio Theory** | 5--8 | How should an investor allocate capital? |
| **Risk Measurement** | 9--10 | How do we quantify and manage risk? |
| **Derivatives** | 11 | How do we price contracts whose value derives from other assets? |

Each block answers a question that the next block depends on.

</section>

<section class="slide" markdown="1">

## Foundations (Lectures 1--4)

### Lecture 1 -- Financial Systems
*What is a financial market, mathematically?* Defined the objects of study: assets, prices, time, uncertainty. Established that finance is not storytelling -- it is **structure and abstraction**.

### Lecture 2 -- A Simple Market Model
*What is the simplest non-trivial market?* The one-step binomial model. Two states, one period -- yet rich enough to introduce **no-arbitrage**, the single most important principle in all of mathematical finance.

### Lecture 3 -- Time Value of Money
*Why is \$1 today worth more than \$1 tomorrow?* Opportunity cost, inflation, risk. Moved from simple to compound to **continuous compounding** -- the language derivatives pricing speaks in.

### Lecture 4 -- Money Market
*How do we price time itself?* Bonds, discount factors, term structure. The **yield curve** encodes the market's collective view of the future cost of money.

</section>

<section class="slide" markdown="1">

## Portfolio Theory (Lectures 5--8)

### Lecture 5 -- Introduction to Portfolios
*How do risk and return trade off?* Defined return (simple, log), variance as risk, and the fundamental insight: **you cannot earn more without accepting more risk** -- but you can be smart about *which* risks you take.

### Lecture 6 -- Risk-Free Asset and Optimization
*What happens when you can lend and borrow at a risk-free rate?* The **Capital Allocation Line**: every efficient portfolio is a mix of the risk-free asset and one optimal risky portfolio. Introduced constrained optimization via Lagrange multipliers.

### Lecture 7 -- Multi-Asset Portfolios
*How does diversification work with many assets?* Matrix/vector formulation. The **efficient frontier** as a hyperbola. Diversification doesn't just reduce risk -- it reshapes the entire opportunity set.

### Lecture 8 -- CAPM
*How are assets priced in equilibrium?* If all investors optimize, the market portfolio *is* the optimal risky portfolio. An asset's expected return depends only on its **systematic risk** (beta), not its total risk.

</section>

<section class="slide" markdown="1">

## Risk Measurement (Lectures 9--10)

### Lecture 9 -- Utility Functions
*Why do different investors hold different portfolios?* Expected utility theory formalizes **risk aversion**. Utility functions encode preferences; concavity measures how much an investor dislikes uncertainty. This is the theoretical backbone behind mean-variance analysis.

### Lecture 10 -- Value at Risk
*How bad can it get?* VaR asks: *"What is my maximum loss at a given confidence level?"* Three methods -- parametric, historical simulation, Monte Carlo. Powerful but limited: VaR says nothing about **how bad** losses can be beyond the threshold.

</section>

<section class="slide" markdown="1">

## Derivatives I (Lecture 11)

### Lecture 11 -- Forwards and Futures
*How do you lock in a price today for a transaction tomorrow?*

Forward contracts: **symmetric** obligations. Priced by **no-arbitrage replication** -- construct a portfolio that exactly mimics the payoff, and the price follows. Futures add daily margining to manage counterparty risk.

**Key insight:** the forward price is *not* a forecast. It is the unique price that prevents free money.

</section>

<section class="slide" markdown="1">

## One Concept Per Lecture -- The Unique Value

| Lecture | The one thing to remember |
|---------|--------------------------|
| 1. Financial Systems | Finance = mathematical structure, not intuition |
| 2. Simple Market Model | **No-arbitrage** -- the anchor of all pricing |
| 3. Time Value of Money | Continuous compounding as the natural language |
| 4. Money Market | The yield curve prices time |
| 5. Intro to Portfolios | Risk-return is a trade-off, not a choice |
| 6. Risk-Free + Optimization | One optimal risky portfolio for everyone |
| 7. Multi-Asset Portfolios | Diversification reshapes opportunity |
| 8. CAPM | Only systematic risk is rewarded |
| 9. Utility Functions | Preferences explain behaviour |
| 10. Value at Risk | Quantify downside, but respect its limits |
| 11. Forwards & Futures | Price by replication, not prediction |

</section>

<section class="slide" markdown="1">

## The Story So Far

$$
\boxed{\text{Model a market}} \;\longrightarrow\; \boxed{\text{Price time (bonds)}} \;\longrightarrow\; \boxed{\text{Combine assets (portfolios)}}
$$

$$
\longrightarrow\; \boxed{\text{Quantify risk (utility, VaR)}} \;\longrightarrow\; \boxed{\text{Price derivatives (forwards)}}
$$

Every step rests on one principle: **no-arbitrage**.

- We used it to price bonds (Lecture 4).
- We used it to derive CAPM (Lecture 8).
- We used it to price forwards (Lecture 11).

What if we want a contract that gives us the **right, but not the obligation**, to trade?

</section>

<section class="slide" markdown="1">

## Looking Ahead: Lecture 12 -- Options

A forward contract is a **symmetric** bet: both sides are equally exposed.

But what if you could keep the upside and **cut off the downside**?

That is an **option** -- and its asymmetric payoff changes everything:

- Payoffs are no longer linear, so replication is harder.
- The right to walk away has a **price** (the premium).
- New relationships emerge: **put-call parity**, pricing bounds, and the interplay of time, volatility, and moneyness.

No-arbitrage still rules -- but the arguments become richer.

</section>

</div>
