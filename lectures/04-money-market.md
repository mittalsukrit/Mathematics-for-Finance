---
layout: default
title: Money Market
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

### What Makes an Asset "Risk-Free"?

Three conditions must hold:

1. **Deterministic payoff**: We know exactly what we'll receive
2. **Zero credit risk**: The counterparty cannot default
3. **Known timing**: Payments occur at specified dates

In practice:

* US Treasury bills ≈ risk-free for USD calculations
* German bunds ≈ risk-free for EUR calculations
* Government securities of stable economies

The approximation is good enough for modeling. Perfect is the enemy of useful.

</section>

<section class="slide" markdown="1">

### Common Abstractions

We collapse many instruments into a few idealized objects:

* Treasury bills
* Bank deposits
* Interbank lending

All are modeled as **deterministic cash flows**.

This abstraction is old. It works. And it scales.

### The Modeling Philosophy

Real markets feature:

* Credit spreads
* Liquidity premia
* Operational risk

Our model ignores these. Why?

Because we're isolating **pure time value**.

Once we understand discounting in a frictionless world, we can add back complexity piece by piece.

Start simple. Complexify only when forced.

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

**Why exponential?**

Consider dividing time $T$ into $n$ intervals. In each interval $\Delta t = T/n$, the discount factor is $(1+r\Delta t)^{-1} \approx (1-r\Delta t)$ for small $\Delta t$.

Compounding:

$$
P(0,T) = \lim_{n \to \infty} (1-r\cdot T/n)^{-n}
$$

Standard limit:

$$
\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = e^x
$$

Setting $x = -rT$ gives $P(0,T) = e^{-rT}$.

This isn't arbitrary. It's the only way to make time-consistent discounting work.

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

**Numerical Example:**

For $r = 6\%$ and $T = 5$ years:

* Annual: $P(0,5) = (1.06)^{-5} \approx 0.7473$
* Semi-annual ($n=2$): $P(0,5) = (1.03)^{-10} \approx 0.7441$
* Quarterly ($n=4$): $P(0,5) = (1.015)^{-20} \approx 0.7425$
* Continuous: $P(0,5) = e^{-0.3} \approx 0.7408$

Notice: more frequent compounding → lower present value.

The differences are small but matter at scale.

</section>

<section class="slide" markdown="1">

## 4. Discount Factors and Term Structure

Each maturity $T$ has its own discount factor $P(0,T)$.

The collection:

$$
\{P(0,T) : T > 0\}
$$

is called the **term structure of interest rates**.

This curve encodes the market's view of time and liquidity.

### Properties of Discount Factors

Well-behaved term structures satisfy:

1. **Boundary condition**: $P(0,0) = 1$ (money today equals money today)
2. **Monotonicity**: $P(0,T_1) > P(0,T_2)$ if $T_1 < T_2$ (longer waits mean deeper discounts)
3. **Positivity**: $P(0,T) > 0$ for all $T$ (money doesn't become worthless)
4. **Smoothness**: $P(0,T)$ varies continuously in $T$

These aren't assumptions. They're **arbitrage-free requirements**.

If $P(0,2) > P(0,1)$, you could:
* Borrow at 2 years
* Lend at 1 year
* Relend for another year
* Lock in risk-free profit

Markets eliminate such opportunities quickly.

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

**Solving for spot rates:**

Given discount factors, we can extract:

$$
r(0,T) = -\frac{1}{T} \ln P(0,T)
$$

**Example:** If $P(0,3) = 0.85$, then:

$$
r(0,3) = -\frac{1}{3} \ln(0.85) = -\frac{1}{3}(-0.1625) \approx 0.0542 = 5.42\%
$$

This is the annualized continuously compounded rate for 3-year money.

</section>

<section class="slide" markdown="1">

### Forward Rates

We can also define **forward rates** $f(0,T_1,T_2)$: the rate agreed today for borrowing between times $T_1$ and $T_2$.

No-arbitrage requires:

$$
P(0,T_2) = P(0,T_1) \cdot e^{-f(0,T_1,T_2)(T_2-T_1)}
$$

Solving:

$$
f(0,T_1,T_2) = \frac{\ln P(0,T_1) - \ln P(0,T_2)}{T_2-T_1}
$$

Forward rates let you lock in future borrowing costs today.

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
P = \sum_{t=1}^{T} c \cdot P(0,t) + P(0,T)
$$

No assumptions. No probabilities. No equilibrium.

Just accounting and no-arbitrage.

**Decomposition logic:**

Think of buying:
* $c$ units of 1-year zeros
* $c$ units of 2-year zeros
* ...
* $c$ units of $T$-year zeros
* 1 unit of $T$-year zero (for principal)

Total cost must equal bond price, otherwise arbitrage exists.

</section>

<section class="slide" markdown="1">

**Example with numbers:**

Suppose we have a 3-year bond with $c=0.05$ (5% coupon) and discount factors:

* $P(0,1) = 0.96$
* $P(0,2) = 0.92$
* $P(0,3) = 0.88$

Price:

$$
P = 0.05(0.96) + 0.05(0.92) + 1.05(0.88)
$$
$$
= 0.048 + 0.046 + 0.924 = 1.018
$$

This bond trades at a **premium** (above par) because coupons exceed the market rate.

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

**What YTM represents:**

It's the internal rate of return (IRR) of the bond's cash flows.

If you:
* Buy the bond at price $P$
* Hold to maturity
* Reinvest all coupons at rate $y$

Then your realized return equals $y$.

That's a lot of "ifs".

</section>

<section class="slide" markdown="1">

### Limitations of YTM

* Assumes flat term structure
* Assumes coupons reinvested at the same rate
* Not additive across portfolios

YTM is a *quoting convention*, not a pricing principle.

Respect it. Don't worship it.

**Why these limitations matter:**

1. **Flat term structure**: YTM treats all maturities as having the same discount rate. Reality: 1-year rates ≠ 10-year rates.

2. **Reinvestment assumption**: If you can't reinvest coupons at $y$, your realized return differs from YTM.

3. **Non-additivity**: If Bond A has YTM = 5% and Bond B has YTM = 6%, their portfolio doesn't have YTM = 5.5%.

**When YTM is useful:**

* Comparing similar bonds
* Quick market quotes
* Rough intuition

**When YTM fails:**

* Pricing exotic structures
* Risk management
* Hedging calculations

For serious work, always go back to discount factors.

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

**Interpretation:**

Imagine a bank account where:
* Interest is credited continuously
* You never withdraw
* The rate stays constant

This is the "risk-free growth process."

**Why it matters:**

* It's the benchmark for all other returns
* In derivatives pricing, we discount at this rate
* It defines what "risk-neutral" means

Starting with $B(0) = 1$, we get $B(t) = e^{rt}$.

The reciprocal $e^{-rt}$ is exactly our discount factor.

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

**Relationship to discounting:**

If $B(t) = (1+r)^t$ grows wealth forward, then $P(0,t) = (1+r)^{-t}$ brings it back.

These are inverse operations:

$$
B(t) \cdot P(0,t) = (1+r)^t \cdot (1+r)^{-t} = 1
$$

**Preview of risk-neutral pricing:**

Later, we'll price derivatives by:
1. Computing expected payoffs
2. Discounting at the risk-free rate

The money market account is the denominator in that calculation.

For now: it's just a modeling device for time value.

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

**What is arbitrage?**

A trading strategy that:
* Costs nothing (or makes money) today
* Never loses money in the future
* Makes money with positive probability

**Example of arbitrage:**

Suppose:
* A 1-year zero-coupon bond costs $P_1 = 0.95$
* A 2-year zero-coupon bond costs $P_2 = 0.91$
* A 1-year forward contract starting in 1 year costs $F = 0.94$

No-arbitrage requires: $P_2 = P_1 \cdot F$, so $F = P_2/P_1 = 0.91/0.95 \approx 0.9579$.

If market quotes $F = 0.94 < 0.9579$:

**Arbitrage strategy:**
* Buy the 2-year zero for $0.91$
* Sell the 1-year zero for $0.95$ (borrow)
* Sell forward at $F=0.94$

**Cash flows:**
* Today: $-0.91 + 0.95 = +0.04$ (profit now)
* Year 1: Pay back 1 unit (from short), receive $1/F = 1/0.94$ forward
* Year 2: Receive 1 from bond, pay $1/F$ forward = net $1 - 1.0638 < 0$...

Actually, let me recalculate. The correct arbitrage:

* Sell 2-year zero for $P_2 = 0.91$
* Buy 1-year zero for $P_1 = 0.95$
* Enter forward to lock in year-2 rate

If $F < P_2/P_1$, you can arbitrage. Markets prevent this.

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

**Let's extend this example:**

**Part (a): Extract spot rates**

$$
r(0,1) = -\ln(0.95) \approx 0.0513 = 5.13\%
$$
$$
r(0,2) = -\frac{1}{2}\ln(0.90) \approx 0.0527 = 5.27\%
$$
$$
r(0,3) = -\frac{1}{3}\ln(0.85) \approx 0.0542 = 5.42\%
$$

The term structure is upward sloping: longer maturities command higher rates.

**Part (b): Compute forward rate from year 1 to year 2**

$$
f(0,1,2) = \frac{\ln P(0,1) - \ln P(0,2)}{2-1} = \ln(0.95) - \ln(0.90) \approx 0.0541 = 5.41\%
$$

**Part (c): What if the bond traded at $P = 0.95$?**

Then it's mispriced relative to the discount curve.

Arbitrage:
* Sell the bond for $0.95$
* Buy the replicating portfolio for $0.958$
* Lock in $0.95 - 0.958 = -0.008$... wait, that's a loss.

Actually: sell the replicating portfolio, buy the bond.

* Buy bond for $0.95$
* Short $0.04$ units of 1-year zero (receive $0.04 \times 0.95 = 0.038$)
* Short $0.04$ units of 2-year zero (receive $0.04 \times 0.90 = 0.036$)
* Short $1.04$ units of 3-year zero (receive $1.04 \times 0.85 = 0.884$)

Total received: $0.038 + 0.036 + 0.884 = 0.958$

Net today: $0.958 - 0.95 = 0.008$ risk-free profit.

At maturity, bond pays exactly what shorts require. Free money.

</section>

<section class="slide" markdown="1">

## 10. Exercises

### Exercise 1

Compute $P(0,5)$ for a zero-coupon bond under:

1. Simple interest $r=6\%$
2. Annual compounding $r=6\%$
3. Continuous compounding $r=6\%$

Compare results.

**Solution hints:**

1. Simple: $P = 1/(1+rT)$
2. Annual: $P = 1/(1+r)^T$
3. Continuous: $P = e^{-rT}$

Observe how the differences grow with maturity.

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

**Extended parts:**

(a) Compute the spot rates $r(0,1)$, $r(0,2)$, $r(0,3)$.

(b) Compute forward rates: $f(0,1,2)$ and $f(0,2,3)$.

(c) If this bond trades at $P=1.02$, describe the arbitrage strategy.

(d) What coupon rate $c^*$ would make the bond trade at par ($P=1$)?

</section>

<section class="slide" markdown="1">

### Exercise 3

A bond trades at price $0.92$ with:

* $T=2$
* $c=0.06$

Compute its yield to maturity.

Then explain why two bonds with the same YTM may have different prices.

**Solution approach for YTM:**

Solve:
$$
0.92 = \frac{0.06}{1+y} + \frac{1.06}{(1+y)^2}
$$

This requires numerical methods (Newton-Raphson) or financial calculator.

**Answer:** $y \approx 9.23\%$

**Explanation part:**

Two bonds with same YTM but different prices could have:
* Different coupon rates
* Different maturities
* Different credit quality (if not truly risk-free)
* Different liquidity

YTM is not a complete descriptor of a bond.

</section>

<section class="slide" markdown="1">

### Exercise 4: Duration

Given a bond with:
* Face value = 100
* Coupon rate = 5% (annual)
* Maturity = 4 years
* Current price = 95.50

(a) Compute the Macaulay duration.

(b) If yields increase by 1%, estimate the new price using duration.

**Duration formula:**

$$
D = \frac{1}{P} \sum_{t=1}^{T} t \cdot C_t \cdot P(0,t)
$$

where $C_t$ is the cash flow at time $t$.

Duration measures the sensitivity of bond prices to interest rate changes.

It's the "center of mass" of the bond's cash flows.

</section>

<section class="slide" markdown="1">

### Exercise 5: Bootstrapping the Yield Curve

You observe the following par bonds (bonds trading at face value):

| Maturity | Coupon Rate |
| -------- | ----------- |
| 1 year   | 4%          |
| 2 years  | 5%          |
| 3 years  | 5.5%        |

Bootstrap the discount factors $P(0,1)$, $P(0,2)$, $P(0,3)$.

**Hint:** For par bonds, price = 100.

* Year 1: $100 = 4 \cdot P(0,1) + 100 \cdot P(0,1)$
* Year 2: $100 = 5 \cdot P(0,1) + 5 \cdot P(0,2) + 100 \cdot P(0,2)$
* And so on...

Solve recursively.

This is how market practitioners build the term structure from observable bond prices.

</section>

<section class="slide" markdown="1">

### Exercise 6: Arbitrage Detection

Consider three bonds:

**Bond A (1-year zero):** Price = 0.96

**Bond B (2-year zero):** Price = 0.90

**Bond C (2-year coupon bond):** Coupon = 5%, Price = 0.98

Is there an arbitrage opportunity? If yes, describe the strategy.

**Approach:**

1. Compute fair price of Bond C using bonds A and B
2. Compare with market price
3. If different, construct arbitrage

Fair price = $0.05 \times 0.96 + 1.05 \times 0.90 = 0.048 + 0.945 = 0.993$

Market price = $0.98 < 0.993$

**Arbitrage:** Buy Bond C, sell replicating portfolio.

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

<section class="slide" markdown="1">

## Advanced Topic: Convexity

Duration is a linear approximation. For large rate changes, we need **convexity**.

**Taylor expansion of bond price:**

$$
\frac{dP}{P} \approx -D \cdot dy + \frac{1}{2}C \cdot (dy)^2
$$

where:
* $D$ = duration
* $C$ = convexity
* $dy$ = change in yield

**Convexity formula:**

$$
C = \frac{1}{P} \sum_{t=1}^{T} t(t+1) \cdot C_t \cdot P(0,t)
$$

Positive convexity is valuable: bond prices rise more when yields fall than they drop when yields rise.

</section>

<section class="slide" markdown="1">

## Advanced Topic: Forward Rate Agreements (FRA)

An **FRA** is a contract to lock in a borrowing/lending rate for a future period.

**Notation:**
* FRA$(T_1, T_2)$: agreement to borrow/lend between $T_1$ and $T_2$

**No-arbitrage pricing:**

The forward rate $f$ must satisfy:

$$
P(0,T_2) = P(0,T_1) \cdot e^{-f(T_2-T_1)}
$$

Otherwise, you could:
* Borrow short, lend long
* Or vice versa
* Lock in risk-free profit

**Market usage:**

* Hedging future borrowing costs
* Speculation on rate movements
* Constructing synthetic positions

FRAs are the building blocks of interest rate swaps.

</section>

<section class="slide" markdown="1">

## Connection to Future Lectures

Today's foundations enable:

1. **Portfolio theory:** How to combine risky assets with risk-free bonds
2. **CAPM:** Risk-free rate as the baseline return
3. **Options pricing:** Discounting expected payoffs
4. **Risk management:** Term structure models for VaR

Every model we build assumes you understand:
* What a discount factor is
* Why no-arbitrage matters
* How to decompose complex cash flows

If you leave this lecture with nothing else, remember:

> Price every cash flow separately, then add them up.

That's 90% of fixed income in one sentence.

</section>

<section class="slide" markdown="1">

## Further Reading

**Classics:**
* Luenberger, *Investment Science* (Ch. 3-4)
* Hull, *Options, Futures, and Other Derivatives* (Ch. 4)
* Tuckman & Serrat, *Fixed Income Securities* (Ch. 1-3)

**For the mathematically inclined:**
* Björk, *Arbitrage Theory in Continuous Time* (Ch. 1-2)
* Shreve, *Stochastic Calculus for Finance I* (Ch. 1)

**Market perspective:**
* Fabozzi, *Bond Markets, Analysis, and Strategies*

The theory is beautiful. The practice is messy. You need both.

</section>

<section class="slide" markdown="1">

## Summary: Key Formulas

**Zero-coupon bond pricing:**
$$P(0,T) = e^{-r(0,T) \cdot T}$$

**Spot rate extraction:**
$$r(0,T) = -\frac{1}{T} \ln P(0,T)$$

**Forward rate:**
$$f(0,T_1,T_2) = \frac{\ln P(0,T_1) - \ln P(0,T_2)}{T_2-T_1}$$

**Coupon bond pricing:**
$$P = \sum_{t=1}^{T} c \cdot P(0,t) + P(0,T)$$

**Money market account:**
$$B(t) = e^{rt}$$

These five formulas are your toolkit.

Master them, and the money market becomes transparent.

</section>

</div>
