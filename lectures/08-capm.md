---

layout: default
title: Capital Asset Pricing Model (CAPM)
-----------------------------------------

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

# Capital Asset Pricing Model (CAPM)

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Why CAPM?
2. Assumptions and market setting
3. From portfolio choice to equilibrium
4. Derivation of CAPM
5. Security Market Line (SML)
6. Systematic vs idiosyncratic risk
7. Characteristic line
8. Empirical interpretation and limits
9. Exercises

</section>

<section class="slide" markdown="1">

## 1. Why CAPM?

Up to now we solved **investor problems**.

CAPM answers a different question:

> How are assets priced *in equilibrium*?

This is not about optimal portfolios.

It is about consistency across the entire market.

</section>

<section class="slide" markdown="1">

### What CAPM Is—and Is Not

CAPM is:

* A logical consequence of mean–variance optimization
* An equilibrium restriction

CAPM is not:

* A law of nature
* A trading strategy

It is a benchmark.

Benchmarks can be wrong—and still useful.

</section>

<section class="slide" markdown="1">

## 2. Market Setting and Assumptions

We assume:

* All investors are mean–variance optimizers
* Homogeneous expectations
* A single risk-free rate $R_f$
* Frictionless markets (no taxes, no transaction costs)

These assumptions are strong.

They are also transparent.

</section>

<section class="slide" markdown="1">

### Why These Assumptions?

Not because they are realistic.

But because they allow us to isolate:

> The pricing role of risk.

CAPM is a *controlled experiment* in theory.

</section>

<section class="slide" markdown="1">

## 3. From Portfolio Choice to Equilibrium

From Lecture 07:

* All investors hold the same risky portfolio
* Differences arise only via leverage

In equilibrium:

> The risky portfolio held by everyone must be the market portfolio.

This is the critical step.

</section>

<section class="slide" markdown="1">

### The Market Portfolio

The **market portfolio** contains:

* All risky assets
* In proportion to their market values

No asset can escape the market.

If it exists, it is priced.

</section>

<section class="slide" markdown="1">

## 4. Risk Decomposition

Consider an asset $i$ with return $R_i$.

Decompose its risk relative to the market $R_M$.

Only part of this risk matters.

The rest is diversifiable noise.

</section>

<section class="slide" markdown="1">

### Beta: Measuring Systematic Risk

Define **beta**:

$$
\beta_i = \frac{\text{Cov}(R_i, R_M)}{\text{Var}(R_M)}
$$

Beta measures:

> Sensitivity to market movements.

This is the only risk investors are paid for.

</section>

<section class="slide" markdown="1">

## 5. Derivation of CAPM

Consider the market portfolio $M$.

For any asset $i$:

* Adding $i$ to $M$ must not improve the Sharpe ratio

Otherwise, $M$ would not be optimal.

This restriction pins down expected returns.

</section>

<section class="slide" markdown="1">

### Mathematical Statement

The equilibrium condition yields:

$$
\mathbb{E}[R_i] - R_f = \beta_i\big( \mathbb{E}[R_M] - R_f \big)
$$

This is the **CAPM equation**.

Nothing mystical happened.

</section>

<section class="slide" markdown="1">

## 6. Security Market Line (SML)

Plot expected return against beta.

The CAPM predicts a straight line:

$$
\mathbb{E}[R] = R_f + \beta (\mathbb{E}[R_M] - R_f)
$$

This line is the **Security Market Line**.

</section>

<section class="slide" markdown="1">

### Interpretation of the SML

* Intercept: risk-free rate
* Slope: market risk premium

Assets:

* Above the line: underpriced
* Below the line: overpriced

In theory.

</section>

<section class="slide" markdown="1">

## 7. Systematic vs Idiosyncratic Risk

Total risk decomposes into:

* Systematic risk (market-related)
* Idiosyncratic risk (asset-specific)

Diversification eliminates only the latter.

Markets pay only for what cannot be diversified.

</section>

<section class="slide" markdown="1">

## 8. Characteristic Line

The **characteristic line** relates an asset’s return to the market return:

$$
R_i - R_f = \alpha_i + \beta_i (R_M - R_f) + \varepsilon_i
$$

This is a regression equation.

</section>

<section class="slide" markdown="1">

### Interpretation

* $\beta_i$: systematic exposure
* $\alpha_i$: abnormal return
* $\varepsilon_i$: idiosyncratic noise

In CAPM:

$$
\alpha_i = 0
$$

Nonzero alpha is a claim.

Extraordinary claims require extraordinary evidence.

</section>

<section class="slide" markdown="1">

## 9. Empirical Reality

CAPM is elegant.

Reality is less cooperative.

Empirically:

* Betas are unstable
* Many anomalies exist

But CAPM survives as a benchmark.

Bad models die.

Useful models endure.

</section>

<section class="slide" markdown="1">

## 10. Exercises

### Exercise 1

Given:

* $R_f = 4%$
* $\mathbb{E}[R_M] = 10%$
* $\beta_i = 1.2$

Compute $\mathbb{E}[R_i]$ under CAPM.

</section>

<section class="slide" markdown="1">

### Exercise 2

Estimate $\beta$ for a stock using historical returns.

Discuss limitations of this approach.

</section>

<section class="slide" markdown="1">

### Exercise 3

An asset lies persistently above the SML.

List three possible explanations.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* CAPM links risk to expected return
* Only systematic risk is priced
* The SML is an equilibrium restriction
* The characteristic line connects theory to data

Next, we move beyond CAPM.

Because markets did.

</section>

</div>
