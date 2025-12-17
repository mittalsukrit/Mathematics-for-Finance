---

layout: default
title: Value at Risk (VaR)
--------------------------

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

# Value at Risk (VaR)

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Motivation: why downside risk?
2. Quantiles and loss distributions
3. Definition of Value at Risk
4. Measuring downside risk
5. Computing VaR: parametric method
6. VaR with normal returns – examples
7. VaR in the Black–Scholes model
8. Mathematical properties and proofs
9. Limitations of VaR
10. Exercises

</section>

<section class="slide" markdown="1">

## 1. Motivation: Why Downside Risk?

Variance treats upside and downside symmetrically.

Investors do not.

Losses hurt more than gains help.

Risk management therefore focuses on:

> How bad can things get?

VaR is the industry’s first systematic answer.

</section>

<section class="slide" markdown="1">

### From Portfolio Choice to Risk Management

So far:

* We optimized portfolios
* We priced assets

Now:

* We measure losses
* We control exposure

This shift is practical, not philosophical.

</section>

<section class="slide" markdown="1">

## 2. Quantiles and Loss Distributions

Let $L$ denote portfolio loss over a fixed horizon.

$L$ is a random variable.

Risk is encoded in its distribution.

Quantiles summarize extreme outcomes.

</section>

<section class="slide" markdown="1">

### Quantiles

For $\alpha \in (0,1)$, the $\alpha$-quantile $q_\alpha$ satisfies:

$$
\mathbb{P}(L \le q_\alpha) = \alpha
$$

Interpretation:

With probability $\alpha$, losses do not exceed $q_\alpha$.

</section>

<section class="slide" markdown="1">

## 3. Definition of Value at Risk

The **Value at Risk** at level $\alpha$ is:

$$
\text{VaR}_\alpha = \inf { x : \mathbb{P}(L \le x) \ge \alpha }
$$

In words:

> The worst loss not exceeded with probability $\alpha$.

</section>

<section class="slide" markdown="1">

### Interpretation

* Typical levels: 95%, 99%
* Time horizon: 1 day, 10 days, 1 year

VaR answers a narrow question.

It does not describe tail severity beyond the quantile.

</section>

<section class="slide" markdown="1">

## 4. Measuring Downside Risk

VaR focuses on:

* Left tail of returns
* Right tail of losses

It ignores upside outcomes entirely.

This is a feature, not a bug.

</section>

<section class="slide" markdown="1">

### Loss vs Return Convention

Let $R$ be portfolio return.

Define loss as:

$$
L = -R
$$

Quantiles of $L$ correspond to lower-tail quantiles of $R$.

Sign conventions matter.

</section>

<section class="slide" markdown="1">

## 5. Parametric VaR

Assume returns are normally distributed:

$$
R \sim \mathcal{N}(\mu, \sigma^2)
$$

Then losses $L = -R$ are also normal.

VaR becomes analytical.

</section>

<section class="slide" markdown="1">

### Normal VaR Formula

Let $z_\alpha$ be the $\alpha$-quantile of the standard normal.

Then:

$$
\text{VaR}*\alpha = -(\mu + \sigma z*{1-\alpha})
$$

Often written as:

$$
\text{VaR}*\alpha = \sigma z*\alpha - \mu
$$

depending on conventions.

</section>

<section class="slide" markdown="1">

## 6. Numerical Example

Suppose:

* $\mu = 0.1%$ daily
* $\sigma = 1%$ daily
* $\alpha = 99%$

Then $z_{0.99} \approx 2.33$.

$$
\text{VaR}_{0.99} \approx 2.33% - 0.1% = 2.23%
$$

This is a one-day VaR.

</section>

<section class="slide" markdown="1">

## 7. VaR in the Black–Scholes Model

Assume asset price follows:

$$
\frac{dS_t}{S_t} = \mu dt + \sigma dW_t
$$

Log-returns are normally distributed.

This aligns perfectly with parametric VaR.

</section>

<section class="slide" markdown="1">

### Distribution of Log-Returns

Over horizon $T$:

$$
\ln \frac{S_T}{S_0} \sim \mathcal{N}\left((\mu - \tfrac{1}{2}\sigma^2)T, \sigma^2 T\right)
$$

Losses can be expressed explicitly.

Closed-form VaR follows.

</section>

<section class="slide" markdown="1">

### VaR for a Stock Position

For investment value $V_0$:

$$
\text{VaR}*\alpha = V_0 \left(1 - e^{(\mu - \frac{1}{2}\sigma^2)T + \sigma \sqrt{T} z*{1-\alpha}} \right)
$$

This is exact under Black–Scholes assumptions.

</section>

<section class="slide" markdown="1">

## 8. Mathematical Properties and Proofs

### Proposition

VaR is **positively homogeneous**:

$$
\text{VaR}*\alpha(cL) = c,\text{VaR}*\alpha(L), \quad c>0
$$

Proof follows directly from quantile scaling.

</section>

<section class="slide" markdown="1">

### Lack of Subadditivity

In general:

$$
\text{VaR}*\alpha(L_1 + L_2) \nleq \text{VaR}*\alpha(L_1) + \text{VaR}_\alpha(L_2)
$$

VaR may penalize diversification.

This is not a technicality.

It is a fundamental flaw.

</section>

<section class="slide" markdown="1">

## 9. Limitations of VaR

* Ignores tail severity
* Not coherent in general
* Sensitive to distributional assumptions

Yet:

VaR remains a regulatory standard.

History matters.

</section>

<section class="slide" markdown="1">

## 10. Exercises

### Exercise 1

Compute 95% and 99% VaR for a portfolio with:

* $\mu = 5%$ annually
* $\sigma = 20%$ annually

Assume normality.

</section>

<section class="slide" markdown="1">

### Exercise 2

Derive the Black–Scholes VaR formula step by step.

Identify each probabilistic assumption.

</section>

<section class="slide" markdown="1">

### Exercise 3

Construct an example where diversification increases VaR.

Explain the intuition.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* VaR is a quantile-based risk measure
* It focuses exclusively on downside risk
* It is analytically convenient
* It is theoretically imperfect

Next: coherent risk measures.

Because regulators learned the hard way.

</section>

</div>
