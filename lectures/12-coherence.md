---
layout: default
title: Coherent Risk Measures and Average Value at Risk
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

# Coherent Risk Measures and Average Value at Risk

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Why coherence?
2. Axioms of coherent risk measures
3. Quantiles revisited
4. Average Value at Risk (AVaR)
5. Representation of AVaR
6. AVaR vs VaR
7. AVaR in the Black–Scholes model
8. Coherence proofs
9. Exercises

</section>

<section class="slide" markdown="1">

## 1. Why Coherence?

VaR answered a practical question.

It failed a theoretical one.

Specifically:

> Diversification should not increase risk.

Coherent risk measures enforce this principle.

</section>

<section class="slide" markdown="1">

### From Heuristics to Axioms

Risk is not just a number.

It is a functional:

$$
\rho : L \to \mathbb{R}
$$

mapping random losses to capital requirements.

Axioms discipline this mapping.

</section>

<section class="slide" markdown="1">

## 2. Axioms of Coherent Risk Measures

A risk measure $\rho(L)$ is **coherent** if it satisfies:

1. **Monotonicity**
   If $L_1 \le L_2$, then $\rho(L_1) \le \rho(L_2)$

2. **Translation invariance**
   $\rho(L + c) = \rho(L) + c$

3. **Positive homogeneity**
   $\rho(\lambda L) = \lambda \rho(L)$ for $\lambda > 0$

4. **Subadditivity**
   $\rho(L_1 + L_2) \le \rho(L_1) + \rho(L_2)$

These axioms formalize diversification.

</section>

<section class="slide" markdown="1">

### Economic Meaning

* Monotonicity: worse losses imply more risk
* Translation: cash reduces risk one-for-one
* Homogeneity: scaling portfolios scales risk
* Subadditivity: diversification helps

If one axiom fails, interpretation collapses.

</section>

<section class="slide" markdown="1">

## 3. Quantiles Revisited

Let $L$ denote loss.

Define VaR again:

$$
\text{VaR}_\alpha(L) = \inf {x : \mathbb{P}(L \le x) \ge \alpha }
$$

VaR is a quantile.

Quantiles are not averages.

</section>

<section class="slide" markdown="1">

## 4. Average Value at Risk (AVaR)

The **Average Value at Risk** at level $\alpha$ is defined as:

$$
\text{AVaR}*\alpha(L) = \frac{1}{1-\alpha} \int*\alpha^1 \text{VaR}_u(L) , du
$$

AVaR averages the worst losses.

This single change fixes VaR.

</section>

<section class="slide" markdown="1">

### Interpretation

AVaR answers:

> Given that things are bad, how bad are they on average?

It measures tail severity.

This is what risk managers actually want.

</section>

<section class="slide" markdown="1">

## 5. Representation of AVaR

An equivalent formulation:

$$
\text{AVaR}*\alpha(L) = \inf*{m \in \mathbb{R}} \left{ m + \frac{1}{1-\alpha} \mathbb{E}[(L - m)^+] \right}
$$

This is a convex optimization problem.

This representation is fundamental.

</section>

<section class="slide" markdown="1">

### Why This Representation Matters

* Convexity becomes explicit
* Numerical computation becomes tractable
* Dual representations emerge naturally

VaR has none of these properties.

</section>

<section class="slide" markdown="1">

## 6. AVaR vs VaR

Key contrasts:

* VaR: quantile, ignores tail shape
* AVaR: tail average, tail-sensitive

VaR may penalize diversification.

AVaR never does.

This difference is structural.

</section>

<section class="slide" markdown="1">

## 7. AVaR in the Black–Scholes Model

Assume log-returns are normal.

Loss $L$ is log-normal.

AVaR admits closed-form expressions.

The math is heavier—but honest.

</section>

<section class="slide" markdown="1">

### Normal Loss Approximation

If losses are normal:

$$
L \sim \mathcal{N}(\mu_L, \sigma_L^2)
$$

Then:

$$
\text{AVaR}*\alpha = \mu_L + \sigma_L \frac{\varphi(z*\alpha)}{1-\alpha}
$$

where $\varphi$ is the standard normal density.

</section>

<section class="slide" markdown="1">

### Interpretation

Compared to VaR:

* Same quantile cutoff
* Larger risk value

AVaR prices tail thickness.

Markets ignore it at their peril.

</section>

<section class="slide" markdown="1">

## 8. Coherence of AVaR

### Theorem

AVaR is a coherent risk measure.

Proof outline:

* Monotonicity: inherited from expectation
* Translation invariance: linearity
* Positive homogeneity: scaling inside expectation
* Subadditivity: convexity of $(x)^+$ and Jensen’s inequality

Each axiom can be proven rigorously.

</section>

<section class="slide" markdown="1">

### Why VaR Fails Subadditivity

VaR focuses on a single quantile.

Combining distributions can move mass.

Averages smooth.

Quantiles jump.

This is not a technicality.

</section>

<section class="slide" markdown="1">

## 9. Exercises

### Exercise 1

Show that AVaR is monotone and translation invariant.

</section>

<section class="slide" markdown="1">

### Exercise 2

Derive the infimum representation of AVaR.

Explain why convexity matters.

</section>

<section class="slide" markdown="1">

### Exercise 3

Compare VaR and AVaR numerically for a heavy-tailed distribution.

Discuss implications for regulation.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* Risk measures must respect diversification
* VaR fails coherence
* AVaR repairs this failure
* Coherence is not philosophy—it is structure

Next: optimization under coherent risk.

Where finance meets convex analysis.

</section>

</div>
