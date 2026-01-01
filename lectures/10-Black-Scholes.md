---
layout: default
title: The Black–Scholes Model
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

# The Black–Scholes Model

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Positioning of This Lecture

Students already know:

* One-step binomial model
* Replication and no-arbitrage pricing

This lecture answers:

> What happens when time becomes continuous?

Black–Scholes is not a new idea.

It is the binomial model pushed to its logical limit.

</section>

<section class="slide" markdown="1">

## Outline

1. From binomial trees to continuous time
2. Market model and assumptions
3. Replication strategy in continuous time
4. Self-financing portfolios
5. Derivation of the Black–Scholes PDE
6. Boundary and terminal conditions
7. Black–Scholes formula for European options
8. Interpretation and limitations
9. Exercises

</section>

<section class="slide" markdown="1">

## 1. From Binomial to Black–Scholes

Recall the one-step binomial model:

* Stock moves up or down
* Option is replicated exactly
* Price follows from no-arbitrage

Now increase the number of steps.

Let time steps shrink to zero.

This limit is the Black–Scholes world.

</section>

<section class="slide" markdown="1">

### What Survives the Limit

From the binomial model we keep:

* Replication
* Self-financing strategies
* No-arbitrage pricing

What changes:

* Prices evolve continuously
* Risk is driven by Brownian motion

The logic does not change.

Only the mathematics does.

</section>

<section class="slide" markdown="1">

## 2. Market Model and Assumptions

We assume:

* One risky asset $S_t$
* One risk-free asset $B_t$

Risk-free asset:

$$
\frac{dB_t}{dt} = r B_t
$$

Risky asset follows:

$$
\frac{dS_t}{S_t} = \mu , dt + \sigma , dW_t
$$

These are modeling choices.

Not truths.

</section>

<section class="slide" markdown="1">

### Interpretation of Parameters

* $\mu$: expected return (irrelevant for pricing)
* $\sigma$: volatility (central)
* $r$: risk-free rate

Notice:

> Expected return disappears from option prices.

This is not an accident.

</section>

<section class="slide" markdown="1">

## 3. Derivative Pricing by Replication

Let $V(t,S)$ denote the option price.

Construct a portfolio:

* Hold $\Delta_t$ shares of stock
* Hold $\beta_t$ units of the bond

Portfolio value:

$$
\Pi_t = \Delta_t S_t + \beta_t B_t
$$

Choose $\Delta_t, \beta_t$ to replicate $V$.

</section>

<section class="slide" markdown="1">

### Self-Financing Condition

The portfolio is **self-financing** if:

$$
d\Pi_t = \Delta_t , dS_t + \beta_t , dB_t
$$

No external cash is injected.

Replication relies on this constraint.

This mirrors the binomial model exactly.

</section>

<section class="slide" markdown="1">

## 4. Ito’s Formula (Used, Not Worshipped)

Apply Ito’s lemma to $V(t,S_t)$:

$$
dV = \partial_t V , dt + \partial_S V , dS_t + \tfrac12 \sigma^2 S_t^2 \partial_{SS} V , dt
$$

Ito’s lemma is bookkeeping.

Replication is the idea.

</section>

<section class="slide" markdown="1">

## 5. Derivation of the Black–Scholes Equation

Match the dynamics of $V$ and $\Pi$.

Choose:

$$
\Delta_t = \partial_S V
$$

The stochastic term disappears.

The portfolio becomes locally risk-free.

No-arbitrage implies:

$$
\partial_t V + \tfrac12 \sigma^2 S^2 \partial_{SS} V + r S \partial_S V - r V = 0
$$

This is the **Black–Scholes PDE**.

</section>

<section class="slide" markdown="1">

### What Just Happened

* Risk was eliminated by replication
* Expected return $\mu$ vanished
* Pricing became deterministic

This is no-arbitrage in action.

Not probability magic.

</section>

<section class="slide" markdown="1">

## 6. Boundary and Terminal Conditions

For a European call option:

Terminal condition:

$$
V(T,S) = (S - K)^+
$$

Boundary conditions:

* $V(t,0)=0$
* Linear growth as $S \to \infty$

A PDE without conditions is meaningless.

</section>

<section class="slide" markdown="1">

## 7. Black–Scholes Formula

Solving the PDE yields:

$$
C(t,S) = S \Phi(d_1) - K e^{-r(T-t)} \Phi(d_2)
$$

where:

$$
d_1 = \frac{\ln(S/K) + (r + \tfrac12 \sigma^2)(T-t)}{\sigma \sqrt{T-t}}, \quad d_2 = d_1 - \sigma \sqrt{T-t}
$$

This is a solution—not an assumption.

</section>

<section class="slide" markdown="1">

### Interpretation

* $\Phi(d_1)$: delta-adjusted probability
* $\Phi(d_2)$: risk-neutral exercise probability

Probabilities appear.

But pricing came first.

</section>

<section class="slide" markdown="1">

## 8. Why Risk-Neutral Valuation Works

Replication implies:

> All equivalent martingale measures give the same price.

Risk-neutral pricing is a shortcut.

Replication is the foundation.

Never confuse the two.

</section>

<section class="slide" markdown="1">

## 9. Limitations of Black–Scholes

* Constant volatility
* Continuous trading
* No transaction costs

Markets violate all three.

The model survives anyway.

Structure beats realism.

</section>

<section class="slide" markdown="1">

## 10. Exercises

### Exercise 1

Derive the delta-hedging strategy explicitly for a European call.

</section>

<section class="slide" markdown="1">

### Exercise 2

Show that the Black–Scholes price satisfies the PDE.

</section>

<section class="slide" markdown="1">

### Exercise 3

Explain why $\mu$ does not appear in the pricing formula.

Relate this to no-arbitrage.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* Black–Scholes is the continuous-time binomial model
* Replication, not preferences, drives pricing
* PDEs replace backward induction
* Assumptions are strong—but explicit

Next: Greeks and hedging errors.

Where theory meets practice.

</section>

</div>
