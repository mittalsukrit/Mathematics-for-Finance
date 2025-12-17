---

layout: default
title: Introduction to Portfolios
---------------------------------

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

# Introduction to Portfolios

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Risk and return: the core trade-off
2. Measuring return
3. Measuring risk: variance
4. Downside risk and semi-variance
5. Portfolios and diversification
6. Two-asset portfolios
7. Attainable set
8. Special cases
9. Minimum variance portfolio
10. Exercises

</section>

<section class="slide" markdown="1">

## 1. Risk and Return: The Core Trade-Off

Finance is not about maximizing return.

It is about choosing **how much risk you are willing to tolerate** for a given return.

No risk, no reward — but also no free lunches.

This trade-off has been understood for centuries.

The mathematics came later.

</section>

<section class="slide" markdown="1">

### What Do We Mean by Return?

Return answers a simple question:

> How much did my investment change in value?

But even simple questions deserve precise definitions.

Ambiguity here infects everything downstream.

</section>

<section class="slide" markdown="1">

## 2. Measuring Return

Let:

* $V_0$ = initial value
* $V_1$ = value at the end of the period

The **simple return** is:

$$
R = \frac{V_1 - V_0}{V_0}
$$

This is the object we will work with throughout this lecture.

</section>

<section class="slide" markdown="1">

### Random Nature of Returns

Future returns are unknown today.

Hence, return is modeled as a **random variable**.

This is not pessimism.

It is intellectual honesty.

</section>

<section class="slide" markdown="1">

## 3. Expected Return

The **expected return** summarizes the center of the return distribution.

If $R$ takes values $r_i$ with probabilities $p_i$:

$$
\mathbb{E}[R] = \sum_i p_i r_i
$$

It is a weighted average of possible outcomes.

</section>

<section class="slide" markdown="1">

### Interpretation of Expected Return

* Not a guaranteed outcome
* Not the most likely outcome
* A long-run average under repeated trials

Markets do not promise outcomes.

They only offer distributions.

</section>

<section class="slide" markdown="1">

## 4. Measuring Risk: Variance

Risk is about **dispersion**, not direction.

The classical measure of risk is **variance**.

Definition:

$$
\text{Var}(R) = \mathbb{E}[(R - \mathbb{E}[R])^2]
$$

Large deviations — up or down — increase variance.

</section>

<section class="slide" markdown="1">

### Standard Deviation

The square root of variance is the **standard deviation**:

$$
\sigma = \sqrt{\text{Var}(R)}
$$

It has the same units as return.

This makes it easier to interpret and compare.

</section>

<section class="slide" markdown="1">

### Criticism of Variance

Variance treats:

* Upside surprises
* Downside disasters

as equally undesirable.

Investors rarely agree with that philosophy.

This criticism is old — and justified.

</section>

<section class="slide" markdown="1">

## 5. Downside Risk and Semi-Variance

To focus on losses, we define **semi-variance**.

Let $m$ be a benchmark (often 0 or the mean).

$$
\text{SemiVar}(R) = \mathbb{E}[\max(0, m - R)^2]
$$

Only downside deviations matter.

</section>

<section class="slide" markdown="1">

### Why Semi-Variance Is Less Popular

* Harder to compute
* Harder to optimize
* Breaks some elegant mathematics

But conceptually, it is closer to how humans think about risk.

Beauty and realism rarely coexist.

</section>

<section class="slide" markdown="1">

## 6. Portfolios and Diversification

A **portfolio** is a weighted combination of assets.

Let:

* $w_i$ = weight of asset $i$
* $R_i$ = return of asset $i$

Portfolio return:

$$
R_p = \sum_i w_i R_i
$$

Diversification is the only free lunch finance ever offered.

</section>

<section class="slide" markdown="1">

### Expected Return of a Portfolio

Expectation is linear:

$$
\mathbb{E}[R_p] = \sum_i w_i \mathbb{E}[R_i]
$$

No interaction terms.

Risk behaves very differently.

</section>

<section class="slide" markdown="1">

## 7. Two-Asset Portfolios

We now restrict attention to two assets.

Let:

* weights: $w$ and $1-w$
* returns: $R_1$, $R_2$

This simple case already contains all the essential geometry.

</section>

<section class="slide" markdown="1">

### Return of a Two-Asset Portfolio

$$
R_p = wR_1 + (1-w)R_2
$$

Expected return:

$$
\mathbb{E}[R_p] = w\mu_1 + (1-w)\mu_2
$$

This is a straight line in $w$.

Risk will not be.

</section>

<section class="slide" markdown="1">

### Variance of a Two-Asset Portfolio

Let:

* variances: $\sigma_1^2, \sigma_2^2$
* covariance: $\sigma_{12}$

Then:

$$
\sigma_p^2 = w^2\sigma_1^2 + (1-w)^2\sigma_2^2 + 2w(1-w)\sigma_{12}
$$

This single equation explains diversification.

</section>

<section class="slide" markdown="1">

### Role of Correlation

Define correlation:

$$
\rho = \frac{\sigma_{12}}{\sigma_1\sigma_2}
$$

* $\rho = 1$: no diversification
* $\rho < 1$: risk reduction
* $\rho = -1$: perfect hedging

Correlation is more important than volatility.

</section>

<section class="slide" markdown="1">

## 8. Attainable Set

As $w$ varies, the pair:

$$
(\sigma_p, \mathbb{E}[R_p])
$$

traces a curve.

This curve is the **attainable set** of portfolios.

It summarizes all feasible risk-return combinations.

</section>

<section class="slide" markdown="1">

### Geometry of the Attainable Set

* A straight line in return space
* A curve in risk-return space

The shape depends entirely on correlation.

This is geometry, not economics.

</section>

<section class="slide" markdown="1">

## 9. Special Cases

### Case 1: Perfect Positive Correlation ($\rho=1$)

No diversification benefit.

Portfolio risk is a weighted average.

</section>

<section class="slide" markdown="1">

### Case 2: Zero Correlation ($\rho=0$)

Risk is reduced, but not eliminated.

Diversification works quietly.

</section>

<section class="slide" markdown="1">

### Case 3: Perfect Negative Correlation ($\rho=-1$)

There exists a **risk-free portfolio**.

Variance can be driven to zero.

This is rare — and powerful.

</section>

<section class="slide" markdown="1">

## 10. Minimum Variance Portfolio

We now minimize $\sigma_p^2$ with respect to $w$.

The solution:

$$
w^* = \frac{\sigma_2^2 - \sigma_{12}}{\sigma_1^2 + \sigma_2^2 - 2\sigma_{12}}
$$

This portfolio has the lowest possible risk.

Regardless of expected returns.

</section>

<section class="slide" markdown="1">

### Interpretation

* Depends only on variances and covariance
* Independent of investor preferences
* Forms the base of the efficient frontier

Optimization comes later.

Structure comes first.

</section>

<section class="slide" markdown="1">

## 11. Exercises

### Exercise 1

Two assets have:

* $\mu_1=10%$, $\sigma_1=20%$
* $\mu_2=6%$, $\sigma_2=10%$
* $\rho=0.3$

Compute the expected return and variance for $w=0.5$.

</section>

<section class="slide" markdown="1">

### Exercise 2

For the same assets, vary $w$ from 0 to 1.

Sketch the attainable set in $(\sigma, \mu)$ space.

Identify the minimum variance portfolio.

</section>

<section class="slide" markdown="1">

### Exercise 3

Construct an example where semi-variance ranks two portfolios differently than variance.

Explain which ranking you find more intuitive, and why.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* Risk and return are inseparable
* Expected return is linear, risk is not
* Variance is convenient, not perfect
* Diversification emerges from correlation
* Even two assets generate rich structure

From here, modern portfolio theory begins in earnest.

</section>

</div>
