---
layout: default
title: A Simple Market Model
---

<style>
  .slides {
    scroll-snap-type: y mandatory;
    overflow-y: scroll;
    height: 100vh;
  }

  .slide {
    scroll-snap-align: start;
    min-height: 100vh;
    padding: 4rem;
    box-sizing: border-box;
  }

  /* Nice-to-have: smoother feel */
  html { scroll-behavior: smooth; }
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

## 1. Basic Notions and Assumptions

We begin with the simplest possible financial market that still captures uncertainty.

### Traded Assets

We assume that **two assets** are traded:

* **One risk-free asset**
  Think of a bank deposit or a government-issued bond.

* **One risky asset**
  Typically a stock, but it could also be a commodity, currency, or any uncertain asset.

</section>

<section class="slide" markdown="1">

### Time Structure

We work with only **two points in time**:

* Today: $t = 0$
* A future date: $t = T$ (e.g., one year from now)

This is deliberately simplistic. Refinement will come later.

</section>

<section class="slide" markdown="1">

## Risky and Risk-Free Assets

### Risky Asset

* Described by the number of shares held
* Current price $S(0)$ is known
* Future price $S(T)$ is **uncertain**

### Risk-Free Asset

* Described by money in a bank account or bonds held
* Current price $A(0)$ is known
* Future price $A(T)$ is **known with certainty**

### Returns

The return on an asset is defined as the fractional change in price:

$$
K_S = \frac{S(T) - S(0)}{S(0)}, \qquad
K_A = \frac{A(T) - A(0)}{A(0)}
$$

</section>

<section class="slide" markdown="1">

## Portfolio

Consider an investor holding:

* $x$ shares of stock
* $y$ units of the risk-free asset

The **portfolio value** at time $t$ is

$$
V(t) = x S(t) + y A(t)
$$

The pair $(x, y)$ is called a **portfolio**.

### Change in Wealth

Between $t = 0$ and $t = T$:

$$
V(T) - V(0) = x\big(S(T) - S(0)\big) + y\big(A(T) - A(0)\big)
$$

### Portfolio Return

$$
K_V = \frac{V(T) - V(0)}{V(0)}
$$

</section>

<section class="slide" markdown="1">

## Some Important Market Assumptions

### Divisibility

Assets can be held in fractional quantities. In practice, this is approximately true for large markets.

### Liquidity

There are no bounds on $x$ and $y$. Assets can be bought or sold in arbitrary quantities at market prices.

### Long and Short Positions

* **Long position**: holding a positive quantity of an asset
* **Short position**: holding a negative quantity (selling an asset you do not own)

</section>

<section class="slide" markdown="1">

## Shorting an Asset

Can you profit if a stock price goes down? Yes—by short selling.

Steps:

1. Borrow shares from a broker
2. Sell them at the current market price
3. Buy them back later
4. Return the shares

* If the price falls: you profit
* If the price rises: you incur a loss

### Portfolio Representation

Short positions correspond to negative holdings. For example:

$$
V(t) = -x S(t) - y A(t) + C(t) \ge 0
$$

where $C(t)$ is a cash reserve or collateral ensuring obligations can be met.

</section>

<section class="slide" markdown="1">

## 2. The No-Arbitrage Principle

### What Is Arbitrage?

**Arbitrage** is the possibility of making a **risk-free profit with no net investment**.

Classic example:

* Buy gold in Delhi at ₹60,000 per 10g
* Sell the same gold in Mumbai at ₹60,300 per 10g
* Pocket the difference instantly

Key features:

* Simultaneous transactions
* No risk (in theory)
* No capital committed

</section>

<section class="slide" markdown="1">

## Why Arbitrage Should Not Exist

We assume that markets **do not allow arbitrage opportunities**.

Why?

* Arbitrage is rapidly exploited by algorithms
* Opportunities vanish in milliseconds
* Prices are forced back into consistency

This assumption is not perfect, but it is close enough for modeling.

### Mathematical Statement

There is **no portfolio** $(x, y)$ such that:

* $V(0) = 0$
* $V(T) \ge 0$ with probability 1
* $V(T) > 0$ with positive probability

</section>

<section class="slide" markdown="1">

## 3. One-Step Binomial Model

### Assumption

The future stock price can take **only two values**:

$$
S(T) =
\begin{cases}
S_u(T) & \text{with probability } p \\
S_d(T) & \text{with probability } 1-p
\end{cases}
$$

with $0 < p < 1$ and $S_d(T) < S_u(T)$.

Despite its simplicity, this model captures the essence of uncertainty.

</section>

<section class="slide" markdown="1">

## Example

Suppose:

* $S(0) = 100$
* $S(T) = 125$ with probability $p$
* $S(T) = 105$ with probability $1-p$
* $A(0) = 100$, $A(T) = 110$

Then:

* Stock return: 

$$
K_S(T)= \begin{cases} 25\% & \text{with probability } p \\ 5\% & \text{with probability } 1-p \end{cases}
$$

* Risk-free return: $K_A=10\%$

</section>

<section class="slide" markdown="1">

## No-Arbitrage Constraint

To avoid arbitrage, the following condition must hold:

$$
\frac{S_d(T)}{S(0)} < \frac{A(T)}{A(0)} < \frac{S_u(T)}{S(0)}
$$

Violating either inequality leads to an arbitrage strategy.

The proof proceeds by constructing portfolios with zero initial cost and non-negative future payoff.

</section>

<section class="slide" markdown="1">

## Case-1

Suppose $\frac{A(T)}{A(0)} \leq \frac{S^d(T)}{S(0)}$. In this case, at $t=0$:
* borrow the amount $S(0)$ risk free;
* buy one share of stock for $S(0)$. 

This way, the portfolio $(x,y)$ will have:  

$$
x=1; \text{ } y = -\frac{S(0)}{A(0)}; \text{ } V(0) = 0
$$

At time $T$, the value will become:

$$
V(T) = 
        \begin{cases}
            S^u(T) - \frac{S(0)}{A(0)}A(T) & \text{if stock goes up,} \\
            S^d(T) - \frac{S(0)}{A(0)}A(T) & \text{if stock goes down.}
        \end{cases}
$$

$V(T) \geq 0$ implies there is an arbitrage opportunity, violating the No-arbitrage principle. 

</section>

<section class="slide" markdown="1">

## Case-2

Suppose $\frac{A(T)}{A(0)} \geq \frac{S^u(T)}{S(0)}$. In this case, at $t=0$:
* sell short one share for $S(0)$;
* invest the amount $S(0)$ risk free. 

This way, the portfolio $(x,y)$ will have:  

$$
x=-1; \text{ } y = \frac{S(0)}{A(0)}; \text{ } V(0) = 0
$$

At time $T$, the value will become:

$$
V(T) = 
        \begin{cases}
            -S^u(T) + \frac{S(0)}{A(0)}A(T) & \text{if stock goes up,} \\
            -S^d(T) + \frac{S(0)}{A(0)}A(T) & \text{if stock goes down.}
        \end{cases}
$$

Again, $V(T) \geq 0$ implies there is an arbitrage opportunity, violating the No-arbitrage principle. 

</section>

<section class="slide" markdown="1">

## 4. Risk and Return

### Example

Let:

* $A(0) = 100$; $A(T) = 110$
* $S(0) = 80$; 

$$
S(T)=\begin{cases} 100 & \text{with probability } 0.8 \\ 60 & \text{with probability } 0.2 \end{cases}
$$

Suppose you invest $10,000$ with: $x = 50$ shares; $y = 60$ bonds.

Then:

$$
V(T) =
\begin{cases}
11{,}600 & \text{if stock goes up} \\
9{,}600 & \text{if stock goes down}
\end{cases}
$$

Corresponding returns:

$$
K_V =
\begin{cases}
16\% & \text{if stock goes up} \\
-4\% & \text{if stock goes down}
\end{cases}
$$

</section>

<section class="slide" markdown="1">

### Expected Return and Risk

Expected return:

$$
E(K_V) = 16\% \times 0.8 - 4\% \times 0.2 = 12\%
$$

Risk (standard deviation):

$$
\sigma_V = \sqrt{(16\% - 12\%)^2 \times 0.8 + (-4\%-12\%)^2 \times 0.2} = 8\%
$$

Comparison:

* All bonds: $K_A = 10\%$; $\sigma_A = 0\%$
* All stocks: $E(K_S)=25\% \times 0.8 - 25\% \times 0.2 = 15\%$; $\sigma_S = 20\%$

</section>

<section class="slide" markdown="1">

## Exercise

Design a portfolio with initial wealth of $10{,}000$, split 50:50 between stocks and bonds.

Compute:

* Expected return
* Risk

Use the same asset prices as above. 
* $A(0)=100$ and $A(T)=110$ dollars.
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

## 5. Forward Contracts

**Forward contract** is an agreement to buy or sell a risky asset at a specified future
time, known as the **delivery date**, for a price $F$ fixed at the present moment, called the
**forward price**.
* An investor who agrees to buy the asset is said to *enter into a long forward contract
or to take a long forward position*.
* An investor who agrees to sell the asset is said to *enter into a short forward contract
or to take a short forward position*.
* No upfront payment.

</section>

<section class="slide" markdown="1">

## 6. Call and Put Options

**Option** is a financial contract giving the right but not the obligation to buy or sell an
asset.
* **Call Option**: right to buy at strike $X$.
* **Put Option**: right to sell at strike $X$.

A premium is paid today to receive this flexibility.


Payoff formulas:
* **Call**: Payoff = $\max (S(T)-X, 0)$
* **Put**: Payoff = $\max (X − S(T), 0)$

</section>

<section class="slide" markdown="1">

## Options Pricing

Let us change the portfolio representation to: $(𝑥, 𝑦, 𝑧)$

$$𝑉 (𝑡) = 𝑥𝑆 (𝑡) + 𝑦𝐴 (𝑡) + 𝑧C(𝑡)$$

Pricing the option is equivalent to identifying $𝐶(0)$.

$$
𝑆(𝑇) = \begin{cases} 120 & \text{with probability } p \\
80 & \text{with probability } 1-p \end{cases}
$$

Call option:

$$
C(𝑇) = \begin{cases} 20 & \text{with probability } p \\
0 & \text{with probability } 1-p \end{cases}
$$

Assume $𝐴 (0) = 100$ and $𝐴 (1) = 110$.

</section>

<section class="slide" markdown="1">

## Replicating the Option

$$
xS(T) + yA(T) = \begin{cases} x120 + y110, & \text{if stock goes up} \\
x80 + y110, & \text{if stock goes down} \end{cases}
$$

Hence, 

$$
C(T) = \begin{cases} x120 + y110 = 20 \\
x80 + y110 = 0 \end{cases}
$$

Solving these equations give: $x = \frac{1}{2}$ ; $y = -\frac{4}{11}$.

This means that to replicate this option, we need to buy 1/2 stock and take a short position on -4/11 bonds (borrow $400/11 in cash).

$$
C(0) = \frac{1}{2} \times 100 - \frac{4}{11} \times 100 = 13.64
$$

</section>

<section class="slide" markdown="1">

## 7. Foreign Exchange

Foreign exchange markets enable trading between currencies.

* Define the exchange rate $X(t)$ as the price of foreign currency in domestic currency. 
* Introduce domestic and foreign risk-free assets with rates $r_d$ and $r_f$. 
* Portfolio representation:

$$
V(t) = y_d A_d(t) + y_f A_f(t)X(t)
$$

</section>

<section class="slide" markdown="1">

## Binomial Model for Exchange Rate

* Exchange rate uncertainty:

$$
X(T) = \begin{cases} X_u(T) & \text{with probability } p \\ X_d(T) & \text{with probability } 1-p \end{cases}
$$

* No-arbitrage condition (interest rate pairity)

  * Constraint: 
  
  $$ 
  \frac{X_d(T)}{X(0)} < \frac{1+r_d}{1+r_f} < \frac{X_u(T)}{X(0)} 
  $$

  * Economic interpretation

</section>

<section class="slide" markdown="1">

## FX Forward and Option

* **Forward rate** formula: 

$$
F = X(0) . \frac{1+r_d}{1+r_f}
$$

* Currency **call option** with strike $K$.
* Replication using portfolio of domestic and foreign assets. 

</section>

<section class="slide" markdown="1">

## 8. Managing Risk with Options

Options are central tools for:

* Hedging downside risk
* Designing payoff profiles
* Controlling exposure under uncertainty

They combine probabilistic thinking with no-arbitrage logic.

</section>

<section class="slide" markdown="1">

## Managing Risk with Options

If I have $1000: 
* It becomes $1200 if the stock goes up. 
* Else it becomes $800. 

Instead, I can buy 73.33 options priced at $13.64 each. 
* Becomes $1466 if the stock goes up. 
* Else $0. 

> Purchasing an option clearly seems riskier. 

</section>

<section class="slide" markdown="1">

## Managing Risk with Options

Alternatively, assume a risky asset with $S(0) = 100$:
$$
S(T) = \begin{cases} 160 & \text{if stock goes up} \\ 40 & \text{if stock goes down} \end{cases}
$$

**Strategy: Covered Call**

At $t=0$:
* Own 1 share of stock (worth $100)
* **Sell** 1 call option (strike $X=100$) for $31.81
* Invest the premium at 10% risk-free rate

At $t=T$, the premium grows to $35.

**Portfolio value:** $V(T) = S(T) - C(T) + 35$

</section>

<section class="slide" markdown="1">

## Managing Risk with Options

Where $C(T) = \max(S(T) - 100, 0)$ is the call payoff you owe.

$$
V(T) = \begin{cases} 
160 - 60 + 35 = 135 & \text{if stock goes up} \\ 
40 - 0 + 35 = 75 & \text{if stock goes down} 
\end{cases}
$$

**Risk comparison:**
* Holding stock only: payoffs range from 40 to 160 (risk = $120)
* Covered call strategy: payoffs range from 75 to 135 (risk = $60)

> The risk (spread between outcomes) has been reduced by 50%.

</section>

<section class="slide" markdown="1">

## Takeaway

Even the simplest market model reveals:

* Why arbitrage-free pricing matters
* How uncertainty enters asset prices
* How portfolios balance risk and return

This framework underlies everything that follows in mathematical finance.

</section>

</div>