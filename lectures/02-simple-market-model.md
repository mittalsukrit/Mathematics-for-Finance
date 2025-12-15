---
layout: default
title: A Simple Market Model
---

# A Simple Market Model

**Sukrit Mittal, Ph.D.**
Franklin Templeton Investments

---

## Outline

1. Basic notions and assumptions
2. No-arbitrage principle
3. One-step binomial model
4. Risk and return
5. Forward contracts
6. Call and put options
7. Foreign exchange
8. Managing risk with options

---

## 1. Basic Notions and Assumptions

We begin with the simplest possible financial market that still captures uncertainty.

### Traded Assets

We assume that **two assets** are traded:

* **One risk-free asset**
  Think of a bank deposit or a government-issued bond.

* **One risky asset**
  Typically a stock, but it could also be a commodity, currency, or any uncertain asset.

### Time Structure

We work with only **two points in time**:

* Today: $t = 0$
* A future date: $t = T$ (e.g., one year from now)

This is deliberately simplistic. Refinement will come later.

---

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

---

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

---

## Some Important Market Assumptions

### Divisibility

Assets can be held in fractional quantities. In practice, this is approximately true for large markets.

### Liquidity

There are no bounds on $x$ and $y$. Assets can be bought or sold in arbitrary quantities at market prices.

### Long and Short Positions

* **Long position**: holding a positive quantity of an asset
* **Short position**: holding a negative quantity (selling an asset you do not own)

---

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

---

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

---

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

---

## 3. One-Step Binomial Model

### Assumption

The future stock price can take **only two values**:

$$
S(T) =
\begin{cases}
S_u(T) & \text{with probability } p \
S_d(T) & \text{with probability } 1-p
\end{cases}
$$

with $0 < p < 1$ and $S_d(T) < S_u(T)$.

Despite its simplicity, this model captures the essence of uncertainty.

---

## Example

Suppose:

* $S(0) = 100$
* $S(T) = 125$ with probability $p$
* $S(T) = 105$ with probability $1-p$
* $A(0) = 100$, $A(T) = 110$

Then:

* Stock return: 25% (up), 5% (down)
* Risk-free return: 10%

---

## No-Arbitrage Constraint

To avoid arbitrage, the following condition must hold:

$$
\frac{S_d(T)}{S(0)} < \frac{A(T)}{A(0)} < \frac{S_u(T)}{S(0)}
$$

Violating either inequality leads to an arbitrage strategy.

The proof proceeds by constructing portfolios with zero initial cost and non-negative future payoff.

---

## 4. Risk and Return

### Example

Let:

* $A(0) = 100$, $A(T) = 110$
* $S(0) = 80$
* $S(T) = 100$ with probability 0.8
* $S(T) = 60$ with probability 0.2

Suppose you invest $10,000$ with:

* $x = 50$ shares
* $y = 60$ bonds

Then:

$$
V(T) =
\begin{cases}
11{,}600 & \text{if stock goes up} \
9{,}600 & \text{if stock goes down}
\end{cases}
$$

Corresponding returns:

$$
K_V =
\begin{cases}
16% \
-4%
\end{cases}
$$

---

### Expected Return and Risk

Expected return:

$$
E[K_V] = 0.8 \times 16% + 0.2 \times (-4%) = 12%
$$

Risk (standard deviation):

$$
\sigma_V = 8%
$$

Comparison:

* All bonds: $K_A = 10%$, $\sigma = 0$
* All stocks: $E[K_S] = 15%$, $\sigma = 20%$

---

## Exercise

Design a portfolio with initial wealth of $10{,}000$, split 50:50 between stocks and bonds.

Compute:

* Expected return
* Risk

Use the same asset prices as above.

---

## 5. Forward Contracts

A **forward contract** is an agreement to buy or sell an asset at a future time $T$ for a price $F$ fixed today.

* **Long forward**: obligation to buy
* **Short forward**: obligation to sell

Forwards are foundational instruments for pricing and hedging.

---

## 6. Call and Put Options

Options give the **right, but not the obligation**, to buy or sell an asset at a specified price.

They allow asymmetric payoff structures and controlled risk exposure.

(Details will be developed later.)

---

## 7. Foreign Exchange

Foreign exchange markets enable trading between currencies.

FX pricing, interest rate parity, and arbitrage constraints follow the same principles introduced here.

---

## 8. Managing Risk with Options

Options are central tools for:

* Hedging downside risk
* Designing payoff profiles
* Controlling exposure under uncertainty

They combine probabilistic thinking with no-arbitrage logic.

---

## Takeaway

Even the simplest market model reveals:

* Why arbitrage-free pricing matters
* How uncertainty enters asset prices
* How portfolios balance risk and return

This framework underlies everything that follows in mathematical finance.
