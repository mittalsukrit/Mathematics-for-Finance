---
layout: default
title: Portfolios of Multiple Assets
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

# Portfolios of Multiple Assets

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. From two assets to many
2. Portfolio return and risk (general case)
3. Geometry of diversification
4. Three risky securities
5. Minimum variance portfolio (MVP)
6. Minimum variance set and line
7. Introducing the market portfolio
8. Exercises

</section>

<section class="slide" markdown="1">

## 1. From Two Assets to Many

The two-asset case taught us geometry.

The multi-asset case teaches us **structure**.

Nothing fundamentally new appears.

What changes is notation—and discipline.

</section>

<section class="slide" markdown="1">

### Why This Matters

Real portfolios:

* Contain many assets
* Are constrained by budgets
* Must be optimized systematically

Guesswork does not scale.

Linear algebra does.

</section>

<section class="slide" markdown="1">

## 2. Portfolio Return: General Case

Let:

* $n$ risky assets
* returns $R = (R_1, \dots, R_n)^\top$
* weights $w = (w_1, \dots, w_n)^\top$

Portfolio return:

$$
R_p = w^\top R
$$

Budget constraint:

$$
\sum_{i=1}^n w_i = 1
$$

</section>

<section class="slide" markdown="1">

### Expected Return

Let $\mu = \mathbb{E}[R]$.

Then:

$$
\mathbb{E}[R_p] = w^\top \mu
$$

Linearity survives dimension.

Risk will not be so polite.

</section>

<section class="slide" markdown="1">

## 3. Portfolio Risk: Variance

Let $\Sigma$ be the covariance matrix:

$$
\Sigma_{ij} = \text{Cov}(R_i, R_j)
$$

Portfolio variance:

$$
\sigma_p^2 = w^\top \Sigma w
$$

This single quadratic form drives modern portfolio theory.

</section>

<section class="slide" markdown="1">

### Properties of the Covariance Matrix

* Symmetric
* Positive semi-definite

These are not technicalities.

They guarantee meaningful optimization problems.

</section>

<section class="slide" markdown="1">

## 4. Geometry of Diversification

Expected return is linear in $w$.

Variance is quadratic in $w$.

This asymmetry creates:

* Curvature
* Trade-offs
* Efficient frontiers

Diversification is geometry in disguise.

</section>

<section class="slide" markdown="1">

## 5. Three Risky Securities

With three risky assets:

* The weight space is two-dimensional
* The attainable set fills an area

Yet the efficient set collapses to a curve.

More choice does not mean more freedom.

</section>

<section class="slide" markdown="1">

### Return and Risk

For three assets:

$$
R_p = w_1R_1 + w_2R_2 + w_3R_3
$$

$$
\sigma_p^2 = w^\top \Sigma w
$$

With $w_1 + w_2 + w_3 = 1$.

Same equations. Higher dimension.

</section>

<section class="slide" markdown="1">

## 6. Minimum Variance Portfolio (MVP)

The **minimum variance portfolio** solves:

$$
\min_w ; w^\top \Sigma w
$$

subject to:

$$
\mathbf{1}^\top w = 1
$$

Expected returns play no role here.

Risk comes first.

</section>

<section class="slide" markdown="1">

### Solution via Lagrange Multipliers

Lagrangian:

$$
\mathcal{L}(w,\lambda) = w^\top \Sigma w + \lambda(\mathbf{1}^\top w - 1)
$$

First-order condition:

$$
2\Sigma w + \lambda \mathbf{1} = 0
$$

This is linear algebra, not magic.

</section>

<section class="slide" markdown="1">

### Closed-Form Expression

Solving yields:

$$
w^{\text{MVP}} = \frac{\Sigma^{-1}\mathbf{1}}{\mathbf{1}^\top \Sigma^{-1}\mathbf{1}}
$$

This formula appears everywhere for a reason.

</section>

<section class="slide" markdown="1">

## 7. Minimum Variance Set and Line

As we vary expected return constraints:

$$
w^\top \mu = \mu_p
$$

we obtain a family of portfolios.

Their image in $(\sigma, \mu)$ space forms the **minimum variance frontier**.

</section>

<section class="slide" markdown="1">

### Minimum Variance Line

Without a risk-free asset:

* The efficient set is a curve
* Only the upper branch is relevant

Below the MVP, portfolios are dominated.

Efficiency is selective.

</section>

<section class="slide" markdown="1">

## 8. Adding the Risk-Free Asset (Recap)

Once a risk-free asset is available:

* The efficient frontier becomes a straight line
* Only one risky portfolio matters

This line dominates all others.

Geometry collapses again.

</section>

<section class="slide" markdown="1">

## 9. Market Portfolio

The **market portfolio** is:

* The tangency portfolio
* The risky portfolio with the highest Sharpe ratio

It solves:

$$
\max_w \frac{w^\top \mu - R_f}{\sqrt{w^\top \Sigma w}}
$$

Subject to $\mathbf{1}^\top w = 1$.

</section>

<section class="slide" markdown="1">

### Characterization of the Market Portfolio

The solution satisfies:

$$
w^{\text{M}} \propto \Sigma^{-1}(\mu - R_f\mathbf{1})
$$

Preferences disappear.

Markets choose the risky portfolio.

</section>

<section class="slide" markdown="1">

### Interpretation

* Everyone holds the same risky portfolio
* Differences arise only through leverage

This result is fragile empirically.

But foundational theoretically.

</section>

<section class="slide" markdown="1">

## 10. Exercises

### Exercise 1

Given three assets with returns $\mu$ and covariance matrix $\Sigma$:

* Compute the minimum variance portfolio
* Compute its variance

</section>

<section class="slide" markdown="1">

### Exercise 2

Show that the MVP weights sum to one.

Explain why this matters economically.

</section>

<section class="slide" markdown="1">

### Exercise 3

Given a risk-free rate $R_f$, derive the market portfolio.

Explain why it does not depend on risk aversion.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* Multi-asset portfolios require linear algebra
* Expected return is linear, risk is quadratic
* The MVP anchors the efficient frontier
* The risk-free asset collapses the frontier
* The market portfolio emerges naturally

Next, we will turn these results into asset pricing.

</section>

</div>
