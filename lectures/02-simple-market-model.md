---
layout: default
title: A Simple Market Model
---

<style>
  .slides {
    scroll-snap-type: y mandatory;
    overflow-y: scroll;
    height: 100vh;

    /* 🔢 Start slide counter */
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

  /* 🔢 Automatic slide numbering */
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

# A Simple Market Model

**Sukrit Mittal**  
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Basic notions and assumptions
2. No-arbitrage principle
3. One-step binomial model
4. Risk and return
5. Forward contracts
6. Call and put options
7. Foreign exchange
8. Managing risk with options

</section>

<section class="slide" markdown="1">

## Basic Notions and Assumptions

We begin with the simplest possible financial market that still captures uncertainty. This abstraction, while highly simplified, is powerful enough to demonstrate fundamental principles of quantitative finance.

### Why Start Simple?

Before tackling continuous-time models and multiple assets, we need to understand:
* How uncertainty affects asset prices
* What prevents arbitrage opportunities
* How derivatives can be priced without predicting the future

The two-period, two-asset model is the "hydrogen atom" of mathematical finance—simple enough to solve exactly, yet rich enough to contain the key insights.

### Traded Assets

We assume that **two assets** are traded:

* **One risk-free asset**
  Think of a bank deposit or a government-issued bond. In practice, this could be a treasury bill or a savings account with guaranteed interest. The key property: **its future value is known today with certainty**.

* **One risky asset**
  Typically a stock, but it could also be a commodity, currency, or any uncertain asset. The key property: **its future value is random and unknown today**.

This dichotomy between certainty and uncertainty is fundamental to all of finance.

</section>

<section class="slide" markdown="1">

### Time Structure

We work with only **two points in time**:

* Today: $t = 0$ (the present, when we make decisions)
* A future date: $t = T$ (e.g., one year from now, when uncertainty resolves)

This is deliberately simplistic. Real markets trade continuously, but the two-period model:
* Eliminates mathematical complications
* Focuses attention on the core logic
* Can be extended to multi-period models later (binomial trees)

**Interpretation**: Between $t=0$ and $t=T$, no trading occurs. We set up our portfolio at $t=0$, wait, and observe the outcome at $t=T$. This "buy-and-hold" assumption will be relaxed in more advanced models.

</section>

<section class="slide" markdown="1">

## Risky and Risk-Free Assets

### Risky Asset (Stock)

* Described by the number of shares held
* Current price $S(0)$ is known (observable in the market)
* Future price $S(T)$ is **uncertain** (depends on future states of the world)

**Example**: A share of Apple stock costs $S(0) = 175$ today, but its price in one year could be anywhere from $150$ to $200$ depending on earnings, economic conditions, etc.

### Risk-Free Asset (Bond)

* Described by money in a bank account or bonds held
* Current price $A(0)$ is known (typically normalized to $1$ or $100$)
* Future price $A(T)$ is **known with certainty** via the risk-free rate $r$

**Example**: A bond with $A(0) = 100$ and annual interest rate $r = 5\%$ will be worth exactly $A(T) = 105$ in one year.

### Returns

$$
K_S = \frac{S(T) - S(0)}{S(0)}, \qquad
K_A = \frac{A(T) - A(0)}{A(0)} = r
$$

</section>

<section class="slide" markdown="1">

## Portfolio

Consider an investor holding:

* $x$ shares of stock (can be fractional)
* $y$ units of the risk-free asset (e.g., dollars in a bank account)

The **portfolio value** at time $t$ is

$$
V(t) = x S(t) + y A(t)
$$

The pair $(x, y)$ is called a **portfolio**. Here, $x$ and $y$ are called **positions**.

### Interpretation

* $V(0)$ is the initial wealth (how much capital you invest)
* $V(T)$ is the final wealth (what you end up with)
* The portfolio $(x, y)$ is chosen at $t=0$ and held until $t=T$

### Change in Wealth

Between $t = 0$ and $t = T$, your wealth changes by:

$$
V(T) - V(0) = x\big(S(T) - S(0)\big) + y\big(A(T) - A(0)\big)
$$

</section>

<section class="slide" markdown="1">

### Portfolio Return

The **return** on the portfolio is:

$$
K_V = \frac{V(T) - V(0)}{V(0)} = \frac{x\big(S(T) - S(0)\big) + y\big(A(T) - A(0)\big)}{xS(0) + yA(0)}
$$

This return can be rewritten in terms of asset returns. Dividing numerator and denominator appropriately:

$$
K_V = w_S K_S + w_A K_A
$$

where $w_S = \frac{xS(0)}{V(0)}$ and $w_A = \frac{yA(0)}{V(0)}$ are the **portfolio weights** (fractions of wealth invested in each asset). Note that $w_S + w_A = 1$.

</section>

<section class="slide" markdown="1">

## Some Important Market Assumptions

These assumptions are idealizations, but they approximate reality in liquid, developed markets.

### Divisibility

Assets can be held in fractional quantities. 

**Rationale**: While you cannot buy 0.5 shares of a single stock in retail markets, institutional investors trading millions of dollars can effectively achieve any fractional exposure through various instruments or by treating portfolios as continuous.

### Liquidity

There are no bounds on $x$ and $y$. Assets can be bought or sold in arbitrary quantities at market prices without affecting those prices.

**Rationale**: This is the "price taker" assumption. In reality, large orders move prices (market impact), but for sufficiently liquid markets and moderate position sizes, this effect is negligible.

</section>

<section class="slide" markdown="1">

### Solvency

Investors can always meet their obligations. No bankruptcy or counterparty risk.

### No Transaction Costs

No fees, taxes, or bid-ask spreads. Every trade executes at the quoted price.

**Reality check**: These last two assumptions are clearly false but simplify the analysis. More realistic models incorporate these frictions.

</section>

<section class="slide" markdown="1">

### Long and Short Positions

* **Long position**: $x > 0$ or $y > 0$—holding a positive quantity of an asset. You profit if the price rises.
* **Short position**: $x < 0$ or $y < 0$—holding a negative quantity. You profit if the price falls.

Short positions require borrowing assets (for stocks) or money (for bonds).

</section>

<section class="slide" markdown="1">

## Shorting an Asset

**Can you profit if a stock price goes down?** Yes—by short selling.

### Mechanics of Short Selling

Steps:

1. **Borrow** shares from a broker (who lends them from their inventory or other clients)
2. **Sell** them immediately at the current market price $S(0)$
3. **Wait** for the price to (hopefully) fall
4. **Buy back** the shares at the new price $S(T)$
5. **Return** the borrowed shares to the broker

### Profit/Loss

* If the price **falls** ($S(T) < S(0)$): you profit by $S(0) - S(T)$ per share
* If the price **rises** ($S(T) > S(0)$): you lose $S(T) - S(0)$ per share

**Example**: Short 100 shares at $50$. If the price drops to $40$, you profit $10 \times 100 = 1000$. If it rises to $60$, you lose $10 \times 100 = 1000$.

</section>

<section class="slide" markdown="1">

### Risks of Short Selling

* **Unlimited loss potential**: A stock price can rise indefinitely, but can only fall to zero
* **Margin requirements**: Brokers require collateral to ensure you can buy back the shares
* **Short squeeze**: If many investors short a stock and the price rises, they may all rush to buy back shares, driving the price even higher

### Portfolio Representation

Short positions correspond to **negative holdings**. For example, a portfolio with $x = -10$ means you are short 10 shares.

The value is:
$$
V(t) = -10 \cdot S(t) + y A(t)
$$

At $t=0$, shorting 10 shares gives you $+10 \cdot S(0)$ in cash, which you can invest in bonds or use as collateral.

</section>

<section class="slide" markdown="1">

## 2. The No-Arbitrage Principle

### What Is Arbitrage?

**Arbitrage** is the possibility of making a **risk-free profit with no net investment**.

In mathematical terms, arbitrage exists if there is a portfolio $(x, y)$ such that:
1. $V(0) = 0$ (no initial investment)
2. $V(T) \geq 0$ with probability 1 (never lose money)
3. $V(T) > 0$ with positive probability (sometimes make money)

Classic example:

* Buy gold in Delhi at ₹60,000 per 10g
* Simultaneously sell the same gold in Mumbai at ₹60,300 per 10g
* Pocket the difference instantly: ₹300 profit with zero risk

Key features:

* **Simultaneous transactions** (no time risk)
* **No risk** (prices are locked in)
* **No capital committed** (borrow to buy, repay from sale proceeds)

</section>

<section class="slide" markdown="1">

### Why This Is "Free Money"

If such an opportunity existed and was known, rational investors would:
1. Borrow unlimited money
2. Execute the arbitrage
3. Scale profits to infinity

But this would immediately drive prices back into equilibrium (buying in Delhi raises prices there, selling in Mumbai lowers prices there).

</section>

<section class="slide" markdown="1">

## Why Arbitrage Should Not Exist

We assume that markets **do not allow arbitrage opportunities**.

### Why This Assumption Is Reasonable

* **Speed**: Arbitrage is exploited by high-frequency trading algorithms in microseconds
* **Competition**: Thousands of traders and algorithms scan for arbitrage 24/7
* **Self-correcting**: The act of exploiting arbitrage eliminates the opportunity
  - Buying the cheap asset raises its price
  - Selling the expensive asset lowers its price
  - Prices converge until the arbitrage disappears

**Real-world timing**: In modern electronic markets, arbitrage opportunities vanish in **milliseconds**, not hours or days.

### Exceptions

* **Transaction costs**: Small price differences may persist if they're less than the cost to trade
* **Market frictions**: Liquidity constraints, margin requirements, or regulatory barriers
* **Rare events**: During market crashes or flash crashes, temporary arbitrage can appear

But these are exceptions. For liquid, developed markets, the no-arbitrage assumption is excellent.

</section>

<section class="slide" markdown="1">

### Mathematical Statement

There is **no portfolio** $(x, y)$ such that:

* $V(0) = 0$ (zero initial cost)
* $V(T) \ge 0$ with probability 1 (never negative)
* $V(T) > 0$ with positive probability (sometimes positive)

**Equivalent statement** (contrapositive): If two portfolios have the same payoff at $T$ in all possible states, they must have the same price at $t=0$.

This principle is the foundation of **derivative pricing**: We price options by replicating their payoffs with portfolios of simpler assets.

</section>

<section class="slide" markdown="1">

## 3. One-Step Binomial Model

### Assumption

The future stock price can take **only two values**:

$$
S(T) =
\begin{cases}
S_u(T) & \text{with probability } p \text{ (up state)}\\
S_d(T) & \text{with probability } 1-p \text{ (down state)}
\end{cases}
$$

with $0 < p < 1$ and $S_d(T) < S_u(T)$.

### Why Only Two States?

This is the **simplest model of uncertainty**:
* One state represents "good news" (stock goes up)
* One state represents "bad news" (stock goes down)
* All information about the future is captured by which state occurs

Despite its simplicity, this model:
* Captures the essence of risk and uncertainty
* Admits no-arbitrage pricing
* Can be extended to multi-period binomial trees (next lectures)
* Converges to continuous-time models (Black-Scholes) as we add more periods

</section>

<section class="slide" markdown="1">

## Example

Suppose:

* $S(0) = 100$
* $A(0) = 100$
* **Stock return**: 

$$
K_S(T)= \begin{cases} 25\% & \text{with probability } p \text{ (up state)}\\ 5\% & \text{with probability } 1-p \text{ (down state)}\end{cases}
$$

* **Risk-free return**: $K_A = 10\%$ (deterministic, same in both states)

### Observations

1. The stock has **higher average return** (assuming $p > 0.5$): $E(K_S) > 10\%$
2. But the stock has **risk**: sometimes returns only 5%
3. The bond has **guaranteed return**: always 10%
4. Investors face a **risk-return tradeoff**

### Expected Stock Return

If $p = 0.6$ (60% chance of up state):

$$
E(K_S) = 0.6 \times 25\% + 0.4 \times 5\% = 15\% + 2\% = 17\%
$$

The **risk premium** is $17\% - 10\% = 7\%$—the extra expected return for bearing risk.

</section>

<section class="slide" markdown="1">

## No-Arbitrage Constraint

To avoid arbitrage, the following condition must hold:

$$
\frac{S_d(T)}{S(0)} < \frac{A(T)}{A(0)} < \frac{S_u(T)}{S(0)}
$$

**Interpretation**: The risk-free **growth factor** $(1+r) = \frac{A(T)}{A(0)}$ must lie **strictly between** the down and up growth factors of the stock.

Equivalently, in terms of returns:

$$
K_d < r < K_u
$$

where $K_d = \frac{S_d(T) - S(0)}{S(0)}$ and $K_u = \frac{S_u(T) - S(0)}{S(0)}$.

### Why This Must Hold

**Intuition**: 
* If $r \geq K_u$, the bond **dominates** the stock (higher return with no risk) → everyone sells the stock
* If $r \leq K_d$, the stock **dominates** the bond (higher return in both states) → everyone sells the bond

Either case creates arbitrage. We'll prove this formally in the next slides.

### Our Example

Check: $\frac{105}{100} = 1.05 < \frac{110}{100} = 1.10 < \frac{125}{100} = 1.25$ ✓

Or: $5\% < 10\% < 25\%$ ✓

The no-arbitrage condition is satisfied.

</section>

<section class="slide" markdown="1">

## Case-1: Arbitrage When Bond Return Is Too Low

**Suppose** $\frac{A(T)}{A(0)} \leq \frac{S_d(T)}{S(0)}$ (equivalently, $r \leq K_d$).

This means the stock beats the bond **even in the worst case**. That's too good to be true!

### Arbitrage Strategy

At $t=0$:
* **Borrow** the amount $S(0)$ at the risk-free rate (short bond)
* **Buy** one share of stock for $S(0)$

**Initial cost**: $V(0) = 1 \cdot S(0) - \frac{S(0)}{A(0)} \cdot A(0) = 0$ ✓

Portfolio: $x=1$, $y = -\frac{S(0)}{A(0)}$

</section>

<section class="slide" markdown="1">

### Payoff at Time $T$

$$
V(T) = S(T) - \frac{S(0)}{A(0)} A(T)
$$

In the up state:
$$
V(T) = S_u(T) - \frac{S(0)}{A(0)} A(T) > 0 \quad \text{(strictly positive)}
$$

In the down state:
$$
V(T) = S_d(T) - \frac{S(0)}{A(0)} A(T) \geq 0 \quad \text{(non-negative by assumption)}
$$

**Result**: We invested nothing, we never lose money, and we sometimes make money. This is arbitrage!

### Numerical Example

Let $S(0) = 100$, $S_d(T) = 110$, $A(0) = 100$, $A(T) = 105$.

Check: $\frac{110}{100} = 1.10 > \frac{105}{100} = 1.05$ (condition violated).

Portfolio: Buy 1 share, borrow 100.

Payoff: $V(T) = S(T) - 105 \in \{110-105, 125-105\} = \{5, 20\}$ (always positive!). 

</section>

<section class="slide" markdown="1">

## Case-2: Arbitrage When Bond Return Is Too High

**Suppose** $\frac{A(T)}{A(0)} \geq \frac{S_u(T)}{S(0)}$ (equivalently, $r \geq K_u$).

This means the bond beats the stock **even in the best case**. Why would anyone hold the stock?

### Arbitrage Strategy

At $t=0$:
* **Sell short** one share for $S(0)$ (borrow and sell the stock)
* **Invest** the proceeds $S(0)$ at the risk-free rate

**Initial cost**: $V(0) = -1 \cdot S(0) + \frac{S(0)}{A(0)} \cdot A(0) = 0$ ✓

Portfolio: $x=-1$, $y = \frac{S(0)}{A(0)}$

</section>

<section class="slide" markdown="1">

### Payoff at Time $T$

You must buy back the stock to return it. Your portfolio is worth:

$$
V(T) = -S(T) + \frac{S(0)}{A(0)} A(T)
$$

In the up state:
$$
V(T) = -S_u(T) + \frac{S(0)}{A(0)} A(T) \geq 0 \quad \text{(non-negative by assumption)}
$$

In the down state:
$$
V(T) = -S_d(T) + \frac{S(0)}{A(0)} A(T) > 0 \quad \text{(strictly positive)}
$$

**Result**: Again, we have arbitrage!

### Numerical Example

Let $S(0) = 100$, $S_u(T) = 105$, $A(0) = 100$, $A(T) = 110$.

Check: $\frac{105}{100} = 1.05 < \frac{110}{100} = 1.10$ (condition violated).

Portfolio: Short 1 share, invest 100.

Payoff: $V(T) = -S(T) + 110 \in \{-105+110, -95+110\} = \{5, 15\}$ (always positive!).

</section>

<section class="slide" markdown="1">

## 4. Risk and Return

How do we measure the **risk** and **expected return** of a portfolio? This section introduces the key statistical tools.

### Example Setup

Let:

* $A(0) = 100$; $A(T) = 110$ (risk-free rate $r = 10\%$)
* $S(0) = 80$; 

$$
S(T)=\begin{cases} 100 & \text{with probability } 0.8 \\ 60 & \text{with probability } 0.2 \end{cases}
$$

**Stock returns**:
$$
K_S = \begin{cases} \frac{100-80}{80} = 25\% & \text{with probability } 0.8 \\ \frac{60-80}{80} = -25\% & \text{with probability } 0.2 \end{cases}
$$

</section>

<section class="slide" markdown="1">

### Portfolio Construction

Suppose you invest $10,000$ with: $x = 50$ shares; $y = 60$ bonds.

**Initial value**: $V(0) = 50 \times 80 + 60 \times 100 = 4000 + 6000 = 10{,}000$ ✓

**Weights**: 40% in stocks, 60% in bonds

### Portfolio Value at $T$

$$
V(T) = 50 \times S(T) + 60 \times 110 = 50 \times S(T) + 6600
$$

$$
V(T) =
\begin{cases}
50 \times 100 + 6600 = 11{,}600 & \text{if stock goes up} \\
50 \times 60 + 6600 = 9{,}600 & \text{if stock goes down}
\end{cases}
$$

**Corresponding returns**:

$$
K_V =
\begin{cases}
\frac{11600-10000}{10000} = 16\% & \text{with probability } 0.8 \\
\frac{9600-10000}{10000} = -4\% & \text{with probability } 0.2
\end{cases}
$$

</section>

<section class="slide" markdown="1">

### Expected Return and Risk

**Expected return** (mean):

$$
E(K_V) = 16\% \times 0.8 + (-4\%) \times 0.2 = 12.8\% - 0.8\% = 12\%
$$

**Risk** (standard deviation):

First, compute the variance:

$$
\text{Var}(K_V) = E[(K_V - E(K_V))^2] = (16\% - 12\%)^2 \times 0.8 + (-4\%-12\%)^2 \times 0.2
$$

$$
= (4\%)^2 \times 0.8 + (-16\%)^2 \times 0.2 = 0.0016 \times 0.8 + 0.0256 \times 0.2
$$

$$
= 0.00128 + 0.00512 = 0.0064
$$

Standard deviation:

$$
\sigma_V = \sqrt{0.0064} = 0.08 = 8\%
$$

</section>

<section class="slide" markdown="1">

### Comparison with Pure Strategies

* **All bonds**: 
  - Return: $K_A = 10\%$ (deterministic)
  - Risk: $\sigma_A = 0\%$

* **All stocks**: 
  - Expected return: $E(K_S) = 25\% \times 0.8 + (-25\%) \times 0.2 = 20\% - 5\% = 15\%$
  - Variance: $(25\% - 15\%)^2 \times 0.8 + (-25\% - 15\%)^2 \times 0.2 = 0.01 \times 0.8 + 0.16 \times 0.2 = 0.04$
  - Risk: $\sigma_S = \sqrt{0.04} = 20\%$

**Mixed portfolio (60-40)**: $E(K_V) = 12\%$, $\sigma_V = 8\%$

**Observation**: The mixed portfolio has **intermediate** risk and return, demonstrating **diversification**.

</section>

<section class="slide" markdown="1">

## Exercise

Design a portfolio with initial wealth of $10{,}000$, split **50:50 between stocks and bonds** (by value).

Compute:

1. The portfolio $(x, y)$
2. Final portfolio value $V(T)$ in each state
3. Expected return $E(K_V)$
4. Risk (standard deviation) $\sigma_V$

Use the same asset prices as above:
* $A(0)=100$ and $A(T)=110$ dollars
* $S(0)=80$ and 

$$
S(T) = 
        \begin{cases}
            100 & \text{with probability } 0.8 \\
            60 & \text{with probability } 0.2
        \end{cases}
$$

</section>

<section class="slide" markdown="1">

### Solution Sketch

**Initial wealth**: 10,000, split 50-50.
- Stock investment: 5,000 → $x = 5000/80 = 62.5$ shares
- Bond investment: 5,000 → $y = 5000/100 = 50$ bonds

**Final value**:
$$
V(T) = 62.5 \times S(T) + 50 \times 110 = 62.5 \times S(T) + 5500
$$

Up state: $V(T) = 6250 + 5500 = 11{,}750$ → Return = 17.5%

Down state: $V(T) = 3750 + 5500 = 9{,}250$ → Return = -7.5%

**Expected return**: $E(K_V) = 0.8 \times 17.5\% + 0.2 \times (-7.5\%) = 14\% - 1.5\% = 12.5\%$

**Variance**: $(17.5\% - 12.5\%)^2 \times 0.8 + (-7.5\% - 12.5\%)^2 \times 0.2 = 25 \times 0.8 + 400 \times 0.2 = 20 + 80 = 100$

**Risk**: $\sigma_V = \sqrt{100} = 10\%$

**Insight**: More stocks → higher expected return (12.5% vs 12%) but also higher risk (10% vs 8%).

</section>

<section class="slide" markdown="1">

## 5. Forward Contracts

A **forward contract** is an agreement to buy or sell a risky asset at a specified future time (the **delivery date**) for a price $F$ fixed today (the **forward price**).

### Key Features

* **Obligation** (not an option): Both parties must complete the transaction
* **No upfront payment**: The contract itself costs nothing to enter
* **Settlement at maturity**: Exchange happens at $t=T$

### Terminology

* **Long forward position**: Agrees to **buy** the asset at $t=T$ for price $F$
  - Profits if $S(T) > F$ (bought cheap)
  - Loses if $S(T) < F$ (overpaid)

* **Short forward position**: Agrees to **sell** the asset at $t=T$ for price $F$
  - Profits if $S(T) < F$ (sold high)
  - Loses if $S(T) > F$ (sold too cheap)

</section>

<section class="slide" markdown="1">

### Payoff at Maturity

* **Long forward payoff**: $S(T) - F$
* **Short forward payoff**: $F - S(T)$

Note these are **symmetric**: one party's gain is the other's loss (zero-sum).

### Pricing the Forward

What should $F$ be? If $F$ is set wrong, one party gets a guaranteed advantage—that's arbitrage!

**No-arbitrage forward price**:

$$
F = S(0) \cdot \frac{A(T)}{A(0)} = S(0) \cdot (1+r)
$$

**Intuition**: The forward price is the current stock price "grown" at the risk-free rate.

</section>

<section class="slide" markdown="1">

### Derivation

Consider two strategies to own the stock at time $T$:

**Strategy 1**: Enter a long forward contract (costs $0$ today, pay $F$ at time $T$)

**Strategy 2**: Buy stock today for $S(0)$, financed by borrowing $S(0)$ at rate $r$ (costs $0$ today, owe $S(0)(1+r)$ at time $T$)

Both strategies deliver one stock at $T$ and cost zero today. By no-arbitrage, they must cost the same at $T$:

$$
F = S(0)(1+r)
$$

</section>

<section class="slide" markdown="1">

## 6. Call and Put Options

Unlike forward contracts (which are obligations), **options** give you **rights without obligations**.

### Definitions

**Call Option**: The right (but not obligation) to **buy** an asset at a predetermined price $X$ (the **strike price**) at time $T$.

**Put Option**: The right (but not obligation) to **sell** an asset at strike price $X$ at time $T$.

### Why "Option"?

You **choose** whether to exercise:
* **Call**: Exercise if $S(T) > X$ (buy cheap, sell at market price)
* **Put**: Exercise if $S(T) < X$ (buy at market price, sell high)

If exercising would lose money, simply walk away—that's the power of an option.

</section>

<section class="slide" markdown="1">

### Payoff at Maturity

* **Call option payoff**: 
$$
C(T) = \max(S(T) - X, 0) = \begin{cases} S(T) - X & \text{if } S(T) > X \\ 0 & \text{if } S(T) \leq X \end{cases}
$$

* **Put option payoff**: 
$$
P(T) = \max(X - S(T), 0) = \begin{cases} X - S(T) & \text{if } S(T) < X \\ 0 & \text{if } S(T) \geq X \end{cases}
$$

### Key Observation

Options have **asymmetric payoffs**:
* Upside: unlimited (for calls) or up to $X$ (for puts)
* Downside: limited to zero (you just don't exercise)

This asymmetry has **value**, so you must pay a **premium** $C(0)$ or $P(0)$ to acquire the option.

</section>

<section class="slide" markdown="1">

### Example

Stock at $S(0) =  100$. Buy a call option with strike $X =  100$ for premium $C(0) =  10$.

At maturity:
- If $S(T) =  120$: Exercise, profit = $120 -  100 -  10 =  10$
- If $S(T) =  80$: Don't exercise, loss = $- 10$ (just the premium)

**Maximum loss**: 10. **Maximum gain**: unlimited!

</section>

<section class="slide" markdown="1">

## Options Pricing: The Replication Method

**Goal**: Find the fair price $C(0)$ for a call option.

**Key idea**: Construct a portfolio of stocks and bonds that **replicates** the option's payoff in every possible state. By no-arbitrage, the portfolio and the option must have the same price.

### Extended Portfolio Representation

Let us represent portfolios as $(x, y, z)$ where:
- $x$ = shares of stock
- $y$ = units of bond
- $z$ = options held

Portfolio value:

$$V(t) = xS(t) + yA(t) + zC(t)$$

To price the option, we find $C(0)$ such that a replicating portfolio exists.

</section>

<section class="slide" markdown="1">

### Example

$$
S(0) = 100, \quad S(T) = \begin{cases} 120 & \text{with probability } p \\ 80 & \text{with probability } 1-p \end{cases}
$$

Call option with strike $X = 100$:

$$
C(T) = \max(S(T) - 100, 0) = \begin{cases} 20 & \text{(up state)} \\ 0 & \text{(down state)} \end{cases}
$$

Risk-free asset: $A(0) = 100$, $A(T) = 110$ (so $r = 10\%$).

</section>

<section class="slide" markdown="1">

## Replicating the Option

We seek a portfolio $(x, y)$ such that:

$$
xS(T) + yA(T) = C(T) \quad \text{in both states}
$$

This gives us a **system of two equations** (one for each state):

$$
\begin{cases}
x \cdot 120 + y \cdot 110 = 20 & \text{(up state)} \\
x \cdot 80 + y \cdot 110 = 0 & \text{(down state)}
\end{cases}
$$

### Solving for $(x, y)$

**Step 1**: Subtract the second equation from the first:

$$
x(120 - 80) = 20 - 0 \implies 40x = 20 \implies x = \frac{1}{2}
$$

**Step 2**: Substitute $x = 1/2$ into the second equation:

$$
\frac{1}{2} \cdot 80 + y \cdot 110 = 0 \implies 40 + 110y = 0 \implies y = -\frac{40}{110} = -\frac{4}{11}
$$

</section>

<section class="slide" markdown="1">

### Interpretation

The replicating portfolio is:
- **Buy** $1/2$ share of stock (costs $\frac{1}{2} \times 100 = 50$)
- **Short** $4/11$ bonds (borrow $\frac{4}{11} \times 100 = 36.36$)

**Net cost today**:

$$
C(0) = \frac{1}{2} \times 100 - \frac{4}{11} \times 100 = 50 - 36.36 = 13.64
$$

### Verification

Up state: $V(T) = \frac{1}{2} \times 120 - \frac{4}{11} \times 110 = 60 - 40 = 20$ ✓

Down state: $V(T) = \frac{1}{2} \times 80 - \frac{4}{11} \times 110 = 40 - 40 = 0$ ✓

The portfolio perfectly replicates the option payoff, so by no-arbitrage: **$C(0) = 13.64$**.

</section>

<section class="slide" markdown="1">

## 7. Foreign Exchange

Foreign exchange (FX) markets enable trading between currencies. They are among the largest and most liquid markets in the world.

### Setting

* **Domestic currency**: Your home currency (e.g., USD, INR)
* **Foreign currency**: Another currency (e.g., EUR, GBP)
* **Exchange rate** $X(t)$: Price of one unit of foreign currency in domestic currency

**Example**: If $X(t) = 83$ INR/USD, then 1 USD costs 83 INR.

### Assets in FX Markets

1. **Domestic risk-free asset**: Bank account in domestic currency
   - Grows at domestic rate: $A_d(T) = A_d(0)(1 + r_d)$

2. **Foreign risk-free asset**: Bank account in foreign currency
   - Grows at foreign rate: $A_f(T) = A_f(0)(1 + r_f)$
   - Value in domestic currency: $A_f(t) \cdot X(t)$

</section>

<section class="slide" markdown="1">

### Portfolio Representation

$$
V(t) = y_d A_d(t) + y_f A_f(t) X(t)
$$

where:
- $y_d$ = units of domestic currency held
- $y_f$ = units of foreign currency held
- $X(t)$ converts foreign holdings to domestic value

**Key insight**: The exchange rate $X(t)$ is uncertain, making foreign holdings risky from the domestic investor's perspective.

</section>

<section class="slide" markdown="1">

## Binomial Model for Exchange Rate

Apply the same binomial framework to exchange rates:

* Exchange rate uncertainty:

$$
X(T) = \begin{cases} X_u(T) & \text{with probability } p \text{ (foreign currency appreciates)} \\ X_d(T) & \text{with probability } 1-p \text{ (foreign currency depreciates)} \end{cases}
$$

### No-Arbitrage Condition (Interest Rate Parity)

By analogy with the stock-bond case, to rule out arbitrage:

$$ 
\frac{X_d(T)}{X(0)} < \frac{1+r_d}{1+r_f} < \frac{X_u(T)}{X(0)} 
$$

**Economic interpretation**:

The ratio $\frac{1+r_d}{1+r_f}$ is the **relative interest rate factor**. 

* If $r_d > r_f$: Domestic rates are higher, so domestic currency should depreciate (foreign currency appreciates) on average
* The expected exchange rate growth should compensate for the interest rate differential

This is the foundation of **covered interest rate parity**, one of the most fundamental relationships in international finance.

</section>

<section class="slide" markdown="1">

### Intuition

If this condition is violated:
- **Borrow** in the low-rate currency
- **Invest** in the high-rate currency
- **Lock in** the exchange rate
- **Profit** risk-free (carry trade arbitrage)

Such opportunities are immediately exploited by banks and hedge funds, keeping exchange rates and interest rates in equilibrium.

</section>

<section class="slide" markdown="1">

## FX Forward and Option

### FX Forward Rate

By no-arbitrage, the **forward exchange rate** must be:

$$
F = X(0) \cdot \frac{1+r_d}{1+r_f}
$$

**Interpretation**: If domestic rates are higher ($r_d > r_f$), the foreign currency must trade at a **forward premium** ($F > X(0)$) to prevent arbitrage.

**Example**: 
- Spot: $X(0) = 80$ INR/USD
- Indian rate: $r_d = 7\%$
- US rate: $r_f = 3\%$
- Forward: $F = 80 \times \frac{1.07}{1.03} = 80 \times 1.0388 \approx 83.11$ INR/USD

</section>

<section class="slide" markdown="1">

### Currency Call Option

A **currency call option** gives the right to buy foreign currency at strike $K$ (in domestic currency).

**Payoff**: $C(T) = \max(X(T) - K, 0)$

**Use case**: An Indian company expects to pay 1M in one year. Buy a call option with strike $K = 85$ INR/USD to cap the cost.
- If INR weakens ($X(T) = 90$): Exercise, pay only 85 INR/USD (plus premium)
- If INR strengthens ($X(T) = 80$): Don't exercise, buy USD at spot

### Replication

Just as with stock options, currency options can be priced by replicating their payoff using portfolios of domestic and foreign bonds.

The same algebra applies:
1. Set up two equations (one for each state)
2. Solve for the replicating portfolio $(y_d, y_f)$
3. Compute the option price as the portfolio cost 

</section>

<section class="slide" markdown="1">

## 8. Managing Risk with Options

Options are not just for speculation—they are powerful tools for **risk management** and **designing specific payoff profiles**.

### Three Key Uses

1. **Hedging downside risk** (insurance)
2. **Enhancing yield** (selling options for premium income)
3. **Constructing tailored exposures** (combining options with underlying assets)

Options combine:
- **Probabilistic thinking** (understanding states and probabilities)
- **No-arbitrage logic** (replication and fair pricing)
- **Strategic flexibility** (choosing when to exercise)

Let's explore some concrete strategies.

</section>

<section class="slide" markdown="1">

## Example 1: Speculative Use of Options

**Scenario**: You have $1000$ to invest. Stock trades at $S(0) = 100$:

$$
S(T) = \begin{cases} 120 & \text{with probability } 0.5 \\ 80 & \text{with probability } 0.5 \end{cases}
$$

### Strategy A: Buy Stock Directly

Buy 10 shares for $1000$.

**Payoff**: 
* Up state: $V(T) = 10 \times 120 = 1200$ (20% gain)
* Down state: $V(T) = 10 \times 80 = 800$ (20% loss)

**Expected value**: $E(V) = 0.5 \times 1200 + 0.5 \times 800 = 1000$ (0% expected return—fair bet)

**Risk (std dev)**: $200$

</section>

<section class="slide" markdown="1">

### Strategy B: Buy Call Options

Assume call options (strike $X = 100$) cost $C(0) = 13.64$ each.

Buy $\frac{1000}{13.64} \approx 73.3$ options.

**Payoff**:
* Up state: $V(T) = 73.3 \times (120 - 100) = 73.3 \times 20 = 1466$
* Down state: $V(T) = 73.3 \times 0 = 0$

**Expected value**: $E(V) = 0.5 \times 1466 + 0.5 \times 0 = 733$

**Risk (std dev)**: $733$

</section>

<section class="slide" markdown="1">

### Comparison

| Strategy | Up State | Down State | Expected | Risk |
|----------|----------|------------|----------|------|
| Stock | $1200$ | $800$ | $1000$ | $200$ |
| Options | $1466$ | $0$ | $733$ | $733$ |

**Observation**: Options provide **leverage**—higher potential upside (1466 vs 1200) but also higher risk (can lose everything). The expected return is actually **negative** due to the premium you pay.

> Purchasing options is **riskier and more speculative** than buying the stock directly. 

</section>

<section class="slide" markdown="1">

## Example 2: Covered Call (Risk Reduction)

Now let's see how options can **reduce** risk, not increase it.

**Scenario**: You own a volatile stock with $S(0) = 100$:

$$
S(T) = \begin{cases} 160 & \text{with probability } 0.5 \text{ (if up)} \\ 40 & \text{with probability } 0.5 \text{ (if down)} \end{cases}
$$

### Strategy: Covered Call

**At $t=0$**:
1. **Own** 1 share of stock (worth $100$)
2. **Sell** 1 call option (strike $X = 100$) for premium $C(0) = 31.81$
3. **Invest** the premium at 10% risk-free rate

The $31.81$ premium grows to $31.81 \times 1.10 = 35$ by time $T$.

</section>

<section class="slide" markdown="1">

### Payoff at $T$

Your portfolio value is:

$$
V(T) = S(T) - C(T) + 35
$$

where $C(T) = \max(S(T) - 100, 0)$ is the call payoff **you owe** (since you sold it).

**Up state** ($S(T) = 160$):
- Stock value: $160$
- Call obligation: $-(160 - 100) = -60$
- Premium growth: $35$
- **Total**: $160 - 60 + 35 = 135$

**Down state** ($S(T) = 40$):
- Stock value: $40$
- Call obligation: $0$ (option expires worthless)
- Premium growth: $35$
- **Total**: $40 - 0 + 35 = 75$

</section>

<section class="slide" markdown="1">

## Covered Call: Risk Analysis

Let's compare the risk profiles:

### Holding Stock Only (No Option)

Payoffs: $S(T) \in \{40, 160\}$

**Range**: $40$ to $160$  
**Risk (spread)**: $160 - 40 = 120$  
**Expected value**: $E(V) = 0.5 \times 160 + 0.5 \times 40 = 100$

### Covered Call Strategy

Payoffs: $V(T) \in \{75, 135\}$

**Range**: $75$ to $135$  
**Risk (spread)**: $135 - 75 = 60$  
**Expected value**: $E(V) = 0.5 \times 135 + 0.5 \times 75 = 105$

</section>

<section class="slide" markdown="1">

### Key Insights

1. **Risk reduced by 50%**: The spread decreased from $120$ to $60$
2. **Downside protection**: Worst case improved from $40$ to $75$ (the premium provides a cushion)
3. **Capped upside**: You give up gains above $135$ (trade-off for receiving premium)
4. **Expected value increased**: From $100$ to $105$ (you collect premium income)

**Interpretation**: By selling the call, you:
- Give up unlimited upside potential
- In exchange for immediate premium income
- Which cushions against losses

This is a **risk-reducing** strategy, popular among investors who own stocks and want to generate income while limiting volatility.

**Real-world use**: Portfolio managers use covered calls to enhance yields during sideways markets.

</section>

<section class="slide" markdown="1">

## Takeaway

Even the simplest market model—two periods, two assets, two states—reveals profound insights:

### Key Principles Established

1. **No-arbitrage pricing**: Assets must be priced consistently to prevent risk-free profits
2. **Replication**: Derivatives can be priced by constructing portfolios that mimic their payoffs
3. **Risk-return tradeoff**: Higher expected returns come with higher risk
4. **Diversification**: Combining assets can reduce risk

### Mathematical Tools Introduced

* Portfolio representation: $V(t) = xS(t) + yA(t)$
* Expected value and variance for measuring risk
* Systems of linear equations for replication
* No-arbitrage constraints

### Derivative Insights

* Forwards lock in future prices
* Options provide asymmetric payoffs (limited downside, unlimited upside)
* Options have value due to this asymmetry
* Strategies combining options and stocks can either increase or decrease risk

</section>

</div>