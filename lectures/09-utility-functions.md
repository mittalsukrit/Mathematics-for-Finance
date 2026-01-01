---
layout: default
title: Utility Functions and Risk Aversion
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

# Utility Functions and Risk Aversion

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Why utility?
2. Preferences and rational choice
3. Axioms of expected utility
4. Expected utility maximization
5. Common utility functions
6. Risk aversion
7. Utility, mean–variance, and CAPM
8. Exercises

</section>

<section class="slide" markdown="1">

## 1. Why Utility?

Up to now, we used **mean–variance preferences**.

They were convenient.

They were also restrictive.

Utility theory answers a deeper question:

> What does it mean to choose rationally under uncertainty?

</section>

<section class="slide" markdown="1">

### What Utility Is Not

Utility is not:

* Money
* Happiness
* Psychological satisfaction

Utility is a **numerical representation of preferences**.

Nothing more. Nothing less.

</section>

<section class="slide" markdown="1">

## 2. Preferences and Choice

Consider uncertain outcomes (lotteries).

An investor can rank them:

* $A \succ B$: $A$ preferred to $B$
* $A \sim B$: indifference

Utility assigns numbers consistent with these rankings.

</section>

<section class="slide" markdown="1">

### Rationality as Consistency

Rationality does not mean intelligence.

It means:

* Consistent choices
* Stable preferences

Economics asks for coherence, not wisdom.

</section>

<section class="slide" markdown="1">

## 3. Axioms of Expected Utility

To represent preferences by expected utility, we assume:

1. **Completeness**: choices are comparable
2. **Transitivity**: no preference cycles
3. **Continuity**: no infinite jumps
4. **Independence**: irrelevant alternatives do not matter

These axioms are demanding.

They are also explicit.

</section>

<section class="slide" markdown="1">

### Expected Utility Theorem

If preferences satisfy the axioms, then:

> There exists a utility function $u(\cdot)$ such that preferences are represented by expected utility.

That is:

$$
U = \mathbb{E}[u(W)]
$$

This is a representation result.

Not a psychological claim.

</section>

<section class="slide" markdown="1">

## 4. Expected Utility Maximization

Given wealth $W$ as a random variable:

The investor chooses portfolios to:

$$
\max ; \mathbb{E}[u(W)]
$$

Subject to budget constraints.

This is the most general formulation of choice under uncertainty.

</section>

<section class="slide" markdown="1">

### Utility Is Ordinal

If $u$ represents preferences, so does:

$$
\tilde u = a u + b \quad (a>0)
$$

Only rankings matter.

Levels do not.

This subtle point is often forgotten.

</section>

<section class="slide" markdown="1">

## 5. Common Utility Functions

### Quadratic Utility

$$
u(W) = W - \frac{\gamma}{2}W^2$$

* Leads to mean–variance preferences
* Analytically convenient
* Implies increasing absolute risk tolerance (problematic)

Useful. Not realistic.

</section>

<section class="slide" markdown="1">

### Exponential Utility (CARA)

$$
u(W) = -e^{-\gamma W}$$

* Constant absolute risk aversion
* Wealth-independent risk attitudes
* Tractable under normality

Popular in theory.

</section>

<section class="slide" markdown="1">

### Power Utility (CRRA)

$$
u(W) = \frac{W^{1-\gamma}}{1-\gamma}$$

* Constant relative risk aversion
* Scale-invariant behavior
* Widely used in macro and asset pricing

This one survives contact with data better.

</section>

<section class="slide" markdown="1">

## 6. Risk Aversion

Risk aversion captures dislike for uncertainty.

Formally:

> An investor is risk-averse if she prefers the expected value to the lottery.

Mathematically:

$$
\mathbb{E}[u(W)] \le u(\mathbb{E}[W])
$$

</section>

<section class="slide" markdown="1">

### Concavity and Risk Aversion

Risk aversion is equivalent to:

$$
u''(W) < 0$$

Utility is concave.

This single inequality drives everything.

</section>

<section class="slide" markdown="1">

### Arrow–Pratt Measures

* **Absolute risk aversion**:

$$
A(W) = -\frac{u''(W)}{u'(W)}
$$

* **Relative risk aversion**:

$$
R(W) = -W\frac{u''(W)}{u'(W)}
$$

These quantify attitudes toward risk.

</section>

<section class="slide" markdown="1">

## 7. Utility and Mean–Variance

Under:

* Quadratic utility, or
* Normally distributed returns

Expected utility reduces to:

$$
\mathbb{E}[W] - \frac{\gamma}{2}\text{Var}(W)
$$

Mean–variance is not a heuristic.

It is a special case.

</section>

<section class="slide" markdown="1">

## 8. Utility and CAPM

CAPM assumes:

* Mean–variance behavior
* Homogeneous beliefs

These are justified by:

* Quadratic utility, or
* Normal returns

CAPM rests on fragile foundations.

But foundations nonetheless.

</section>

<section class="slide" markdown="1">

### What Changes with General Utility?

* Market portfolio need not be mean–variance efficient
* Pricing relations become nonlinear

CAPM is elegant.

Reality is not.

</section>

<section class="slide" markdown="1">

## 9. Exercises

### Exercise 1

Show that concavity of $u$ implies risk aversion using Jensen’s inequality.

</section>

<section class="slide" markdown="1">

### Exercise 2

Compute absolute and relative risk aversion for:

$$
u(W) = -e^{-\gamma W}$$

Interpret the result.

</section>

<section class="slide" markdown="1">

### Exercise 3

Explain why mean–variance preferences may fail for skewed return distributions.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* Utility formalizes rational choice under uncertainty
* Risk aversion is concavity
* Mean–variance is a special case of expected utility
* CAPM relies on strong utility assumptions

Next, we move beyond expected utility.

Because investors do.

</section>

</div>
