---
layout: default
title: Time Value of Money
---

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

# Time Value of Money

**Sukrit Mittal**  
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Introduction and motivation
2. Simple interest
3. Periodic compounding
4. Continuous compounding
5. Comparing compounding methods
6. Streams of payments
7. Applications

</section>

<section class="slide" markdown="1">

## 1. Introduction and Motivation

### Why Is Money Time-Dependent?

A dollar today is worth **more** than a dollar tomorrow. Why?

* **Opportunity cost**: Money today can be invested to earn returns
* **Inflation**: Purchasing power erodes over time
* **Risk**: Future payments are uncertain

### Core Question

How do we compare cash flows occurring at different points in time?

The answer: **discount** future cash flows to their present value, or **compound** present values to future equivalents.

</section>

<section class="slide" markdown="1">

## The Fundamental Trade-Off

Consider two offers:

* Receive $100 today
* Receive $110 one year from now

Which is better?

**Answer:** It depends on the interest rate.

* If you can invest at 12% annually: $100 today grows to $112 next year → take $100 today
* If you can only invest at 8%: $100 today grows to $108 next year → take $110 next year

The interest rate is the **bridge** between present and future values.

</section>

<section class="slide" markdown="1">

## 2. Simple Interest

### Definition

Under **simple interest**, the interest earned is proportional to:
* Principal amount $P$
* Interest rate $r$ (per period)
* Time $t$

### Formula

$$A(t) = P(1 + rt)$$

where:
* $A(t)$ = amount at time $t$
* $P$ = principal (initial investment)
* $r$ = interest rate per period
* $t$ = number of periods

</section>

<section class="slide" markdown="1">

## Simple Interest: Example

You invest $1,000 at 8% simple interest per year.

**How much will you have after 3 years?**

$$A(3) = 1{,}000(1 + 0.08 \times 3) = 1{,}000 \times 1.24 = \$1{,}240$$

### Key Feature

Interest is earned **only on the principal**, not on accumulated interest.

This is a **linear** growth model:

$$A(t) = 1{,}000 + 80t$$

</section>

<section class="slide" markdown="1">

## Limitations of Simple Interest

Simple interest ignores the fact that interest earned can itself earn interest.

**Example:** With $1,000 at 8% simple interest:

* Year 1: earn $80
* Year 2: earn $80
* Year 3: earn $80
* Total: $1,240

But what if you could reinvest the $80 earned in Year 1?

This leads us to **compound interest**.

</section>

<section class="slide" markdown="1">

## 3. Periodic Compounding

### Definition

With **compound interest**, interest is added to the principal periodically, and subsequent interest is earned on the new total.

### Formula

$$A = P\left(1 + \frac{r}{n}\right)^{nt}$$

where:
* $n$ = number of compounding periods per year
* $t$ = number of years
* $r$ = annual interest rate (APR)

</section>

<section class="slide" markdown="1">

## Compounding Frequencies

| Frequency | Value of $n$ |
|-----------|--------------|
| Annual | $n = 1$ |
| Semi-annual | $n = 2$ |
| Quarterly | $n = 4$ |
| Monthly | $n = 12$ |
| Daily | $n = 365$ |

**Key insight:** As $n$ increases, the final amount $A$ increases, but with diminishing returns.

</section>

<section class="slide" markdown="1">

## Example: Periodic Compounding

Invest $1,000 at 8% annual interest for 3 years under different compounding frequencies.

**Annual compounding ($n=1$):**

$$A = 1{,}000\left(1 + 0.08\right)^{3} = 1{,}000(1.08)^3 = \$1{,}259.71$$

**Quarterly compounding ($n=4$):**

$$A = 1{,}000\left(1 + \frac{0.08}{4}\right)^{12} = 1{,}000(1.02)^{12} = \$1{,}268.24$$

**Monthly compounding ($n=12$):**

$$A = 1{,}000\left(1 + \frac{0.08}{12}\right)^{36} = \$1{,}270.24$$

</section>

<section class="slide" markdown="1">

## Effective Annual Rate (EAR)

The **effective annual rate** is the actual annual return accounting for compounding within the year.

### Formula

$$\text{EAR} = \left(1 + \frac{r}{n}\right)^n - 1$$

**Example:** 8% APR compounded quarterly

$$\text{EAR} = \left(1 + \frac{0.08}{4}\right)^4 - 1 = (1.02)^4 - 1 = 0.0824 = 8.24\%$$

The EAR exceeds the stated rate (APR) whenever $n > 1$.

</section>

<section class="slide" markdown="1">

## 4. Continuous Compounding

### What Happens as $n \to \infty$?

As compounding becomes more frequent, we approach **continuous compounding**.

### Derivation

Starting from periodic compounding:

$$A = P\left(1 + \frac{r}{n}\right)^{nt}$$

Take the limit as $n \to \infty$:

$$A = P \lim_{n \to \infty} \left(1 + \frac{r}{n}\right)^{nt}$$

Using the fact that $\lim_{n \to \infty} \left(1 + \frac{r}{n}\right)^n = e^r$:

$$A = Pe^{rt}$$

</section>

<section class="slide" markdown="1">

## Continuous Compounding Formula

$$A = Pe^{rt}$$

where:
* $e \approx 2.71828$ (Euler's number)
* $r$ = annual interest rate
* $t$ = time in years

### Example

Invest $1,000 at 8% continuously compounded for 3 years:

$$A = 1{,}000 \cdot e^{0.08 \times 3} = 1{,}000 \cdot e^{0.24} = \$1{,}271.25$$

</section>

<section class="slide" markdown="1">

## Present Value with Continuous Compounding

If $A = Pe^{rt}$, then solving for $P$:

$$P = Ae^{-rt}$$

This is the **present value** of a future amount $A$ under continuous compounding.

**Example:** What is the present value of $1,500 to be received in 5 years at 6% continuous rate?

$$P = 1{,}500 \cdot e^{-0.06 \times 5} = 1{,}500 \cdot e^{-0.3} = \$1{,}109.96$$

</section>

<section class="slide" markdown="1">

## 5. Comparing Compounding Methods

### Comparison Table

Invest $1,000 at 8% for 3 years:

| Method | Formula | Amount |
|--------|---------|---------|
| Simple interest | $P(1+rt)$ | $1,240.00 |
| Annual compounding | $P(1+r)^t$ | $1,259.71 |
| Quarterly | $P(1+r/4)^{4t}$ | $1,268.24 |
| Monthly | $P(1+r/12)^{12t}$ | $1,270.24 |
| Daily | $P(1+r/365)^{365t}$ | $1,271.22 |
| Continuous | $Pe^{rt}$ | $1,271.25 |

**Observation:** More frequent compounding yields higher returns, but the gains diminish.

</section>

<section class="slide" markdown="1">

## Converting Between Compounding Frequencies

### From Periodic to Continuous

Given periodic rate $r_n$ with frequency $n$, the equivalent continuous rate $r_c$ is:

$$r_c = n \ln\left(1 + \frac{r_n}{n}\right)$$

### From Continuous to Periodic

Given continuous rate $r_c$, the equivalent periodic rate $r_n$ is:

$$r_n = n\left(e^{r_c/n} - 1\right)$$

</section>

<section class="slide" markdown="1">

## Example: Rate Conversion

**Question:** What continuous rate is equivalent to 8% compounded quarterly?

$$r_c = 4 \ln\left(1 + \frac{0.08}{4}\right) = 4 \ln(1.02) = 4 \times 0.0198 = 0.0792 = 7.92\%$$

**Verification:**

* Quarterly: $1{,}000(1.02)^{12} = 1{,}268.24$
* Continuous: $1{,}000e^{0.0792 \times 3} = 1{,}268.24$ ✓

</section>

<section class="slide" markdown="1">

## 6. Streams of Payments

So far: single payment at time 0.

In practice, many financial instruments involve **multiple cash flows** over time:

* Bond coupons
* Loan payments
* Dividend streams
* Retirement income

How do we value these?

**Answer:** Sum the present values of each individual payment.

</section>

<section class="slide" markdown="1">

## Present Value of Cash Flow Stream

Consider cash flows $C_1, C_2, \ldots, C_n$ at times $t_1, t_2, \ldots, t_n$.

### Present Value

$$PV = \sum_{k=1}^{n} C_k e^{-rt_k}$$

(using continuous compounding)

Or with periodic compounding at rate $r$:

$$PV = \sum_{k=1}^{n} \frac{C_k}{(1+r)^{t_k}}$$

</section>

<section class="slide" markdown="1">

## Annuities

An **annuity** is a sequence of **equal** payments at **regular** intervals.

Two types:

* **Ordinary annuity**: payments at the **end** of each period
* **Annuity due**: payments at the **beginning** of each period

### Notation

* $C$ = payment per period
* $r$ = interest rate per period
* $n$ = number of periods

</section>

<section class="slide" markdown="1">

## Present Value of Ordinary Annuity

**Formula:**

$$PV = C \cdot \frac{1 - (1+r)^{-n}}{r}$$

**Derivation:**

$$PV = \frac{C}{1+r} + \frac{C}{(1+r)^2} + \cdots + \frac{C}{(1+r)^n}$$

This is a geometric series with first term $\frac{C}{1+r}$ and ratio $\frac{1}{1+r}$.

Sum: 

$$PV = \frac{C/(1+r) \cdot [1 - (1+r)^{-n}]}{1 - 1/(1+r)} = C \cdot \frac{1 - (1+r)^{-n}}{r}$$

</section>

<section class="slide" markdown="1">

## Example: Ordinary Annuity

You will receive $500 at the end of each year for 5 years. The interest rate is 6%.

**What is the present value?**

$$PV = 500 \cdot \frac{1 - (1.06)^{-5}}{0.06}$$

$$= 500 \cdot \frac{1 - 0.7473}{0.06} = 500 \cdot \frac{0.2527}{0.06}$$

$$= 500 \times 4.212 = \$2{,}106.00$$

</section>

<section class="slide" markdown="1">

## Future Value of Ordinary Annuity

**Formula:**

$$FV = C \cdot \frac{(1+r)^n - 1}{r}$$

**Example:** You save $500 at the end of each year for 5 years at 6%.

$$FV = 500 \cdot \frac{(1.06)^5 - 1}{0.06} = 500 \cdot \frac{1.3382 - 1}{0.06}$$

$$= 500 \times 5.637 = \$2{,}818.50$$

</section>

<section class="slide" markdown="1">

## Annuity Due

Payments occur at the **beginning** of each period.

**Present Value of Annuity Due:**

$$PV_{\text{due}} = PV_{\text{ordinary}} \times (1+r)$$

**Future Value of Annuity Due:**

$$FV_{\text{due}} = FV_{\text{ordinary}} \times (1+r)$$

**Intuition:** Each payment earns interest for one additional period.

</section>

<section class="slide" markdown="1">

## Perpetuities

A **perpetuity** is an annuity that continues **forever**.

### Present Value of Perpetuity

As $n \to \infty$ in the annuity formula:

$$PV = \lim_{n \to \infty} C \cdot \frac{1 - (1+r)^{-n}}{r} = \frac{C}{r}$$

**Example:** A bond pays $50 per year forever at 5% interest.

$$PV = \frac{50}{0.05} = \$1{,}000$$

</section>

<section class="slide" markdown="1">

## Growing Perpetuity

A **growing perpetuity** has payments that increase at rate $g$ each period.

First payment: $C$  
Second payment: $C(1+g)$  
Third payment: $C(1+g)^2$, etc.

### Present Value

$$PV = \frac{C}{r - g}$$

where $r > g$ (otherwise the value is infinite).

**Example:** First payment $100, growing at 3% annually, discount rate 8%.

$$PV = \frac{100}{0.08 - 0.03} = \frac{100}{0.05} = \$2{,}000$$

</section>

<section class="slide" markdown="1">

## 7. Applications

### Bond Valuation

A bond pays periodic coupons plus face value at maturity.

$$\text{Bond Price} = PV(\text{coupons}) + PV(\text{face value})$$

### Loan Amortization

Monthly loan payments form an annuity. Given loan amount $L$, rate $r$, term $n$:

$$\text{Payment} = L \cdot \frac{r}{1 - (1+r)^{-n}}$$

</section>

<section class="slide" markdown="1">

## Application: Mortgage Example

You borrow $300,000 for 30 years at 4.5% annual rate (compounded monthly).

Monthly rate: $r = 0.045/12 = 0.00375$  
Number of payments: $n = 30 \times 12 = 360$

$$\text{Monthly Payment} = 300{,}000 \cdot \frac{0.00375}{1 - (1.00375)^{-360}}$$

$$= 300{,}000 \cdot \frac{0.00375}{1 - 0.2556} = 300{,}000 \times 0.005067 = \$1{,}520.06$$

</section>

<section class="slide" markdown="1">

## Summary Formulas

| Concept | Formula |
|---------|---------|
| Simple interest | $A = P(1+rt)$ |
| Compound interest | $A = P(1+r/n)^{nt}$ |
| Continuous compounding | $A = Pe^{rt}$ |
| PV of ordinary annuity | $PV = C \cdot \frac{1-(1+r)^{-n}}{r}$ |
| FV of ordinary annuity | $FV = C \cdot \frac{(1+r)^n-1}{r}$ |
| Perpetuity | $PV = \frac{C}{r}$ |
| Growing perpetuity | $PV = \frac{C}{r-g}$ |

</section>

<section class="slide" markdown="1">

## Key Takeaways

1. **Time value of money** is fundamental to all financial decisions
2. **Compound interest** dominates simple interest in practice
3. **Continuous compounding** is the mathematical limit of periodic compounding
4. **Annuities and perpetuities** provide closed-form valuation formulas
5. All valuations reduce to: **sum of discounted cash flows**

These tools form the foundation for:
* Bond pricing
* Stock valuation (dividend discount models)
* Derivatives pricing
* Capital budgeting

</section>

</div>
