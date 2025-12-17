---

layout: default
title: Risk-Free Asset, Indifference Curves, and Lagrange Multipliers
---------------------------------------------------------------------

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

# Risk-Free Asset, Preferences, and Optimization

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Why add a risk-free asset?
2. Portfolios with a risk-free security
3. Capital allocation line
4. Investor preferences and indifference curves
5. Optimal portfolio choice
6. Mathematical interlude: constrained optimization
7. Lagrange multipliers
8. Proofs and intuition

</section>

<section class="slide" markdown="1">

## 1. Why Add a Risk-Free Asset?

So far, all portfolios involved **only risky assets**.

That world is incomplete.

In reality, investors can always:

* Park money safely
* Borrow or lend at (approximately) risk-free rates

Ignoring this option distorts everything.

</section>

<section class="slide" markdown="1">

### Conceptual Shift

With a risk-free asset:

* Risk becomes optional
* Leverage becomes possible
* Portfolio choice separates into two problems

This separation is not an assumption.

It is a theorem.

</section>

<section class="slide" markdown="1">

## 2. Portfolio with One Risky Asset and One Risk-Free Asset

Let:

* $R_f$ = risk-free return (constant)
* $R$ = return on a risky portfolio
* $w$ = fraction invested in risky asset

Portfolio return:

$$
R_p = wR + (1-w)R_f
$$

This is the simplest mixed portfolio.

</section>

<section class="slide" markdown="1">

### Expected Return

$$
\mathbb{E}[R_p] = w\mathbb{E}[R] + (1-w)R_f
$$

Linear in $w$.

Nothing surprising yet.

</section>

<section class="slide" markdown="1">

### Risk of the Portfolio

Since $R_f$ is constant:

$$
\sigma_p = |w|\sigma
$$

All risk comes from the risky asset.

The risk-free asset contributes none.

</section>

<section class="slide" markdown="1">

## 3. Capital Allocation Line (CAL)

Combining a risky portfolio with a risk-free asset traces a straight line in $(\sigma, \mu)$ space.

Equation:

$$
\mathbb{E}[R_p] = R_f + \frac{\mathbb{E}[R] - R_f}{\sigma} , \sigma_p
$$

This is the **capital allocation line**.

</section>

<section class="slide" markdown="1">

### Interpretation of the CAL

* Intercept: risk-free rate
* Slope: Sharpe ratio

Steeper line = better risk-return trade-off.

Markets reward efficiency, not bravery.

</section>

<section class="slide" markdown="1">

## 4. Many Risky Assets + Risk-Free Asset

When many risky assets exist:

* Investors first form an **optimal risky portfolio**
* Then mix it with the risk-free asset

This is the **two-fund separation theorem**.

Preferences determine *how much* risk, not *which* risk.

</section>

<section class="slide" markdown="1">

## 5. Investor Preferences

To choose among portfolios, we need a model of preferences.

Finance borrows this from economics.

We assume:

* More return is better
* Less risk is better

Nothing exotic.

</section>

<section class="slide" markdown="1">

### Mean–Variance Preferences

Preferences are represented by a utility function:

$$
U(\mu, \sigma) = \mu - \frac{\gamma}{2}\sigma^2
$$

Where $\gamma > 0$ measures risk aversion.

This is not psychology.

It is tractable mathematics.

</section>

<section class="slide" markdown="1">

## 6. Indifference Curves

An **indifference curve** consists of portfolios yielding the same utility.

Holding $U$ constant:

$$
\mu = U + \frac{\gamma}{2}\sigma^2
$$

This is a parabola in $(\sigma, \mu)$ space.

</section>

<section class="slide" markdown="1">

### Properties of Indifference Curves

* Upward sloping
* Increasingly steep
* Do not intersect

Higher curves correspond to higher utility.

Geometry replaces psychology.

</section>

<section class="slide" markdown="1">

## 7. Optimal Portfolio Choice

The investor chooses the portfolio where:

* An indifference curve
* Is tangent to the CAL

This tangency determines the optimal risk exposure.

Different investors, same risky portfolio.

Different mixing proportions.

</section>

<section class="slide" markdown="1">

### Key Result

Risk tolerance affects:

* How much to invest in risky assets

It does *not* affect:

* Which risky portfolio to hold

This result is deep, old, and still misunderstood.

</section>

<section class="slide" markdown="1">

## 8. Mathematical Interlude

So far, we relied on geometry.

Next, we formalize this using **constrained optimization**.

This requires a new mathematical tool.

Enter Lagrange multipliers.

</section>

<section class="slide" markdown="1">

## 9. Motivating Example

Maximize:

$$
f(x,y) = x^2 + y^2
$$

Subject to:

$$
x + y = 1
$$

Unconstrained, this explodes.

The constraint changes everything.

</section>

<section class="slide" markdown="1">

### Geometric Intuition

* Level curves of $f$: circles
* Constraint: straight line

The optimum occurs where:

* A level curve is tangent to the constraint

Gradients align.

</section>

<section class="slide" markdown="1">

## 10. Lagrange Multiplier Method

Define the Lagrangian:

$$
\mathcal{L}(x,y,\lambda) = f(x,y) + \lambda(g(x,y) - c)
$$

First-order conditions:

$$
\nabla f = -\lambda \nabla g
$$

The multiplier enforces the constraint.

</section>

<section class="slide" markdown="1">

### Economic Interpretation of $\lambda$

The Lagrange multiplier measures:

> How much the objective improves if the constraint is relaxed.

In finance, this interpretation will matter.

A lot.

</section>

<section class="slide" markdown="1">

## 11. Constrained Extrema: General Case

Maximize $f(x)$ subject to $g(x)=0$.

Necessary condition:

$$
\nabla f(x^*) = \lambda \nabla g(x^*)
$$

This replaces unconstrained critical points.

</section>

<section class="slide" markdown="1">

### Proof Sketch

At the optimum:

* Movement along the constraint is allowed
* Movement off the constraint is forbidden

Thus, directional derivatives along the constraint vanish.

Gradients must align.

That is the whole proof.

</section>

<section class="slide" markdown="1">

## 12. Why This Matters for Finance

Portfolio optimization is:

* Maximization of expected utility
* Subject to budget constraints

Every serious result ahead relies on this machinery.

Without Lagrange multipliers, modern finance collapses.

</section>

<section class="slide" markdown="1">

## 13. Exercises

### Exercise 1

Derive the optimal weight $w$ for a portfolio combining a risky asset and a risk-free asset under mean–variance utility.

</section>

<section class="slide" markdown="1">

### Exercise 2

Solve the constrained problem:

$$
\max_{x,y} xy \quad \text{s.t.} \quad x^2 + y^2 = 1
$$

Using Lagrange multipliers.

</section>

<section class="slide" markdown="1">

### Exercise 3

Interpret the Lagrange multiplier in the context of a budget constraint.

Explain its economic meaning.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* Adding a risk-free asset changes everything
* Preferences are needed to choose among portfolios
* Indifference curves formalize risk aversion
* Optimal choice is a tangency condition
* Lagrange multipliers are unavoidable

Next, we will unify all of this into full mean–variance optimization.

</section>

</div>
