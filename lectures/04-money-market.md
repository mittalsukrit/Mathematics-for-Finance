---

layout: default
title: Money Market
-------------------

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

  html { scroll-behavior: smooth; }
</style>

<div class="slides" markdown="1">

<section class="slide" markdown="1">

# Money Market

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Motivation: why money markets matter
2. Risk-free assets and modeling assumptions
3. Zero-coupon bonds: definition and pricing
4. Discount factors and term structure
5. Coupon bonds: cash-flow decomposition
6. Yield measures and their limitations
7. Money market account
8. No-arbitrage relationships
9. Worked examples
10. Exercises

</section>

<section class="slide" markdown="1">

## 1. Motivation: Why Study the Money Market?

The money market is where **time itself is priced**.

Before equities, before derivatives, before fancy models, finance had one problem:

> How much is a sure rupee tomorrow worth today?

Everything else in mathematical finance is built on the answer to that question.

If you misunderstand the money market, all later pricing formulas are numerology.

</section>

<section class="slide" markdown="1">

### What the Money Market Is *Not*

* It is not about speculation
* It is not about beating benchmarks
* It is not about taking risk

Its job is boring by design:

* Preserve capital
* Provide liquidity
* Anchor the risk-free rate

Boring markets are the most important ones.

</section>

<section class="slide" markdown="1">

## 2. Risk-Free Assets and Modeling Assumptions

In theory, we assume the existence of a **risk-free asset**.

Meaning:

* Known payoff
* No default
* No uncertainty

In reality, nothing is perfectly risk-free.

But theory is about **controlled lies**.

</section>

<section class="slide" markdown="1">

### Common Abstractions

We collapse many instruments into a few idealized objects:

* Treasury bills
* Bank deposits
* Interbank lending

All are modeled as **deterministic cash flows**.

This abstraction is old. It works. And it scales.

</section>

<section class="slide" markdown="1">

## 3. Zero-Coupon Bonds

A **zero-coupon bond** is the cleanest financial instrument imaginable.

Definition:

* Pays exactly 1 unit of currency at time $T$
* Pays nothing before maturity

Notation:

* $P(0,T)$: price at time 0

Think of it as a *time machine for money*.

</section>

<section class="slide" markdown="1">

### Why Zero-Coupon Bonds Matter

They isolate **time value** from everything else.

No coupons. No reinvestment assumptions. No ambiguity.

If you understand zero-coupon bonds, you understand:

* Discounting
* Interest rates
* Present value

They are the atoms of fixed income.

</section>

<section class="slide" markdown="1">

### Pricing with Continuous Compounding

Assume a constant continuously compounded rate $r$.

Then:

$$
P(0,T) = e^{-rT}
$$

Interpretation:

* Future certainty discounted exponentially
* Time erodes value smoothly

Exponential discounting is not a choice. It is forced by consistency.

</section>

<section class="slide" markdown="1">

### Pricing with Discrete Compounding

If interest is compounded once per period:

$$
P(0,T) = \frac{1}{(1+r)^T}
$$

If compounded $n$ times per year:

$$
P(0,T) = \left(1+\frac{r}{n}\right)^{-nT}
$$

Different conventions. Same economics.

</section>

<section class="slide" markdown="1">

## 4. Discount Factors and Term Structure

Each maturity $T$ has its own discount factor $P(0,T)$.

The collection:

$$
{P(0,T) : T > 0}
$$

is called the **term structure of interest rates**.

This curve encodes the market’s view of time and liquidity.

</section>

<section class="slide" markdown="1">

### Spot Rates

Define the **spot rate** $r(0,T)$ by:

$$
P(0,T) = e^{-r(0,T)T}
$$

Each maturity has its own rate.

Flat curves are special cases, not defaults.

Markets are rarely that polite.

</section>

<section class="slide" markdown="1">

## 5. Coupon Bonds

A **coupon bond** pays periodic interest plus principal.

Parameters:

* Face value: 1
* Coupon: $c$
* Maturity: $T$

Cash flows:

$$
c, c, \dots, c, 1 + c
$$

This is a bundle, not a primitive object.

</section>

<section class="slide" markdown="1">

### Coupon Bonds as Portfolios

A coupon bond is a portfolio of zero-coupon bonds.

Price at time 0:

$$
P = \sum_{t=1}^{T} c,P(0,t) + P(0,T)
$$

No assumptions. No probabilities. No equilibrium.

Just accounting and no-arbitrage.

</section>

<section class="slide" markdown="1">

### Why This Decomposition Matters

Because it tells you:

* What drives bond prices
* Why yield measures can mislead
* How to hedge interest-rate risk

If you price bonds any other way, you are guessing.

</section>

<section class="slide" markdown="1">

## 6. Yield to Maturity (YTM)

Market convention compresses all cash flows into a single number.

$y$ solves:

$$
P = \sum_{t=1}^{T} \frac{c}{(1+y)^t} + \frac{1}{(1+y)^T}
$$

This number is convenient.

It is also dangerous.

</section>

<section class="slide" markdown="1">

### Limitations of YTM

* Assumes flat term structure
* Assumes coupons reinvested at the same rate
* Not additive across portfolios

YTM is a *quoting convention*, not a pricing principle.

Respect it. Don’t worship it.

</section>

<section class="slide" markdown="1">

## 7. Money Market Account

The **money market account** models continuous reinvestment.

Let $B(t)$ denote its value.

With constant rate $r$:

$$
B(t) = B(0)e^{rt}
$$

This asset defines the baseline growth of wealth.

</section>

<section class="slide" markdown="1">

### Discrete-Time Version

In discrete time:

$$
B(t+1) = (1+r)B(t)
$$

Starting from $B(0)=1$:

$$
B(t) = (1+r)^t
$$

This will later become the **numeraire**.

</section>

<section class="slide" markdown="1">

## 8. No-Arbitrage Relationships

No-arbitrage principle:

> Identical cash flows must have identical prices.

Implications:

* Discount factors are unique
* Coupon bonds are pinned down
* Risk-free growth is dominant

Break consistency, and arbitrage strategies appear.

</section>

<section class="slide" markdown="1">

### Preview: What Comes Next

Soon, interest rates will:

* Vary over time
* Become random
* Interact with risky assets

But all of that rests on today’s foundation.

Weak foundations collapse silently.

</section>

<section class="slide" markdown="1">

## 9. Worked Example

Suppose:

* $P(0,1)=0.95$
* $P(0,2)=0.90$
* $P(0,3)=0.85$

Coupon bond:

* $c=0.04$
* $T=3$

Price:

$$
P = 0.04(0.95+0.90+0.85)+0.85 = 0.04(2.70)+0.85 = 0.958
$$

Nothing mystical happened.

</section>

<section class="slide" markdown="1">

## 10. Exercises

### Exercise 1

Compute $P(0,5)$ for a zero-coupon bond under:

1. Simple interest $r=6%$
2. Annual compounding $r=6%$
3. Continuous compounding $r=6%$

Compare results.

</section>

<section class="slide" markdown="1">

### Exercise 2

Given discount factors:

| $T$ | $P(0,T)$ |
| --- | -------- |
| 1   | 0.97     |
| 2   | 0.94     |
| 3   | 0.90     |

Price a 3-year coupon bond with $c=0.05$.

</section>

<section class="slide" markdown="1">

### Exercise 3

A bond trades at price $0.92$ with:

* $T=2$
* $c=0.06$

Compute its yield to maturity.

Then explain why two bonds with the same YTM may have different prices.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* Money markets price time, not risk
* Zero-coupon bonds are the foundation
* Coupon bonds are portfolios
* Yields summarize, discount factors price
* No-arbitrage enforces discipline

If this lecture feels slow, good.

Finance rewards patience before cleverness.

</section>

</div>
