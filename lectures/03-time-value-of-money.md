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

### The Indifference Rate

We can solve for the **break-even** interest rate where you'd be indifferent:

$$100(1 + r) = 110 \implies r = 0.10 = 10\%$$

At exactly 10%, both options are equivalent.

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

### Practice Questions

1. If you invest $5,000 at 6% simple interest for 18 months, what is the final amount?
2. How long does it take for $2,000 to grow to $2,500 at 5% simple interest?

*Hint for Q2: Solve $2000(1 + 0.05t) = 2500$ for $t$.*

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

## The Power of Compounding

### Einstein's Alleged Quote
*"Compound interest is the eighth wonder of the world. He who understands it, earns it; he who doesn't, pays it."*

### Illustration: The Rule of 72

**Approximate time to double** your money:

$$t \approx \frac{72}{r\%}$$

where $r\%$ is the annual percentage rate.

**Examples:**
- At 6%: $t \approx 72/6 = 12$ years
- At 8%: $t \approx 72/8 = 9$ years
- At 12%: $t \approx 72/12 = 6$ years

**Verification at 8%:** $(1.08)^9 = 1.999 \approx 2$ ✓

### Derivation

Solve $(1+r)^t = 2$ for $t$:

$$t = \frac{\ln 2}{\ln(1+r)} \approx \frac{0.693}{r}$$

For $r$ as a percentage: $t \approx \frac{69.3}{r\%}$. The rule of 72 is easier to use and quite accurate for rates between 6-10%.

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

### Why Does This Work?

Each period, the amount is multiplied by $\left(1 + \frac{r}{n}\right)$. After $nt$ periods:

$$P \rightarrow P\left(1 + \frac{r}{n}\right) \rightarrow P\left(1 + \frac{r}{n}\right)^2 \rightarrow \cdots \rightarrow P\left(1 + \frac{r}{n}\right)^{nt}$$

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

## Discount Rate and Present Value Relationship

### Inverse Relationship

Present value and discount rate move in **opposite directions**:

$$\frac{\partial PV}{\partial r} = \frac{\partial}{\partial r}\left[\frac{C}{(1+r)^t}\right] = -\frac{tC}{(1+r)^{t+1}} < 0$$

**Interpretation:**
- Higher discount rates → lower present values
- Lower discount rates → higher present values

### Financial Implications

**Bond markets:** When interest rates rise, bond prices fall (and vice versa).

**Equity markets:** Higher discount rates reduce the present value of future earnings, lowering stock prices.

### Example

PV of $1,000 in 10 years at different rates:
- At 5%: $1,000/(1.05)^{10} = $613.91
- At 10%: $1,000/(1.10)^{10} = $385.54
- At 15%: $1,000/(1.15)^{10} = $247.19

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

**Notice:** The difference between monthly and quarterly is $2.00, much smaller than the $8.53 difference between quarterly and annual. This diminishing return pattern continues as $n$ increases.

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

### Why It Matters

Financial institutions often quote **APR** (nominal rate) but compound more frequently. The EAR reveals the **true cost** or **true return**.

**Regulation:** In many jurisdictions, lenders must disclose the EAR (also called APY - Annual Percentage Yield) to help consumers compare products.

### Exercise

A credit card charges 18% APR with daily compounding. What is the effective annual rate?

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

Rewrite the exponent: let $m = \frac{n}{r}$, so $n = mr$ and as $n \to \infty$, we have $m \to \infty$:

$$A = P \lim_{m \to \infty} \left[\left(1 + \frac{1}{m}\right)^m\right]^{rt}$$

Using the fundamental limit $\lim_{m \to \infty} \left(1 + \frac{1}{m}\right)^m = e$:

$$A = P(e)^{rt} = Pe^{rt}$$

### Why $e$?

The number $e$ naturally arises as the base for continuous growth processes.

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

## Real vs. Nominal Interest Rates

### Nominal Rate
The stated interest rate, **not adjusted** for inflation.

### Real Rate
The interest rate **adjusted** for inflation—the actual increase in purchasing power.

### Fisher Equation

$$(1 + r_{\text{nominal}}) = (1 + r_{\text{real}})(1 + \pi)$$

where $\pi$ is the inflation rate.

**Approximation** (for small rates):

$$r_{\text{real}} \approx r_{\text{nominal}} - \pi$$

### Example

You earn 8% on an investment, but inflation is 3%.

**Exact:** $r_{\text{real}} = \frac{1.08}{1.03} - 1 = 0.0485 = 4.85\%$

**Approximate:** $r_{\text{real}} \approx 8\% - 3\% = 5\%$

### Why It Matters

When comparing investments across time or countries, **real rates** provide the true comparison of purchasing power gains.

</section>

<section class="slide" markdown="1">

## Present Value with Continuous Compounding

If $A = Pe^{rt}$, then solving for $P$:

$$P = Ae^{-rt}$$

This is the **present value** of a future amount $A$ under continuous compounding.

**Example:** What is the present value of $1,500 to be received in 5 years at 6% continuous rate?

$$P = 1{,}500 \cdot e^{-0.06 \times 5} = 1{,}500 \cdot e^{-0.3} = \$1{,}109.96$$

### Interpretation

The discount factor $e^{-rt}$ represents the "weight" we assign to future cash. As $t$ or $r$ increases, this weight decreases exponentially.

### Exercise

Verify that $1,109.96$ invested at 6% continuous rate for 5 years yields $1,500.

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

**Derivation:** Set the growth equal over one year:

$$\left(1 + \frac{r_n}{n}\right)^n = e^{r_c}$$

Taking natural log: $n \ln\left(1 + \frac{r_n}{n}\right) = r_c$

### From Continuous to Periodic

Given continuous rate $r_c$, the equivalent periodic rate $r_n$ is:

$$r_n = n\left(e^{r_c/n} - 1\right)$$

**Derivation:** From $e^{r_c} = \left(1 + \frac{r_n}{n}\right)^n$, raise both sides to power $1/n$:

$$e^{r_c/n} = 1 + \frac{r_n}{n} \implies r_n = n(e^{r_c/n} - 1)$$

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

### The Additivity Principle

The present value operator is **linear**:

$$PV(C_1 + C_2) = PV(C_1) + PV(C_2)$$

This allows us to value complex cash flow streams by breaking them into components.

</section>

<section class="slide" markdown="1">

## Present Value of Cash Flow Stream

Consider cash flows $C_1, C_2, \ldots, C_n$ at times $t_1, t_2, \ldots, t_n$.

### Present Value

$$PV = \sum_{k=1}^{n} C_k e^{-rt_k}$$

(using continuous compounding)

Or with periodic compounding at rate $r$:

$$PV = \sum_{k=1}^{n} \frac{C_k}{(1+r)^{t_k}}$$

### Example

Cash flows: $100 at $t=1$, $200 at $t=2$, $150 at $t=3$. Rate: 5% (annual compounding).

$$PV = \frac{100}{1.05} + \frac{200}{(1.05)^2} + \frac{150}{(1.05)^3}$$

$$= 95.24 + 181.41 + 129.58 = \$406.23$$

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

Factor out $\frac{C}{1+r}$:

$$PV = \frac{C}{1+r}\left[1 + \frac{1}{1+r} + \frac{1}{(1+r)^2} + \cdots + \frac{1}{(1+r)^{n-1}}\right]$$

This is a geometric series with first term $a = 1$, ratio $q = \frac{1}{1+r}$, and $n$ terms.

Geometric series sum: $S_n = a \cdot \frac{1-q^n}{1-q} = \frac{1 - (1+r)^{-n}}{1 - \frac{1}{1+r}} = \frac{1-(1+r)^{-n}}{\frac{r}{1+r}}$

Therefore:

$$PV = \frac{C}{1+r} \cdot \frac{1-(1+r)^{-n}}{\frac{r}{1+r}} = C \cdot \frac{1 - (1+r)^{-n}}{r}$$

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

**Derivation:** Relate to present value. If $PV$ grows for $n$ periods:

$$FV = PV \cdot (1+r)^n = C \cdot \frac{1 - (1+r)^{-n}}{r} \cdot (1+r)^n$$

$$= C \cdot \frac{(1+r)^n - 1}{r}$$

**Example:** You save $500 at the end of each year for 5 years at 6%.

$$FV = 500 \cdot \frac{(1.06)^5 - 1}{0.06} = 500 \cdot \frac{1.3382 - 1}{0.06}$$

$$= 500 \times 5.637 = \$2{,}818.50$$

**Verification:** This is $2,106.00 \times (1.06)^5 = 2,818.50$ ✓

</section>

<section class="slide" markdown="1">

## Annuity Due

Payments occur at the **beginning** of each period.

**Present Value of Annuity Due:**

$$PV_{\text{due}} = PV_{\text{ordinary}} \times (1+r)$$

**Future Value of Annuity Due:**

$$FV_{\text{due}} = FV_{\text{ordinary}} \times (1+r)$$

**Intuition:** Each payment earns interest for one additional period.

### Derivation for PV

For an annuity due, the first payment is at $t=0$, not $t=1$:

$$PV_{\text{due}} = C + \frac{C}{1+r} + \frac{C}{(1+r)^2} + \cdots + \frac{C}{(1+r)^{n-1}}$$

$$= (1+r)\left[\frac{C}{1+r} + \frac{C}{(1+r)^2} + \cdots + \frac{C}{(1+r)^n}\right] = (1+r) \cdot PV_{\text{ordinary}}$$

### Example

Using our earlier example ($500/year for 5 years at 6%):
- Ordinary annuity: $2,106.00
- Annuity due: $2,106.00 \times 1.06 = $2,232.36

</section>

<section class="slide" markdown="1">

## Perpetuities

A **perpetuity** is an annuity that continues **forever**.

### Present Value of Perpetuity

As $n \to \infty$ in the annuity formula:

$$PV = \lim_{n \to \infty} C \cdot \frac{1 - (1+r)^{-n}}{r}$$

Since $(1+r) > 1$, we have $(1+r)^{-n} \to 0$ as $n \to \infty$:

$$PV = C \cdot \frac{1 - 0}{r} = \frac{C}{r}$$

**Example:** A bond pays $50 per year forever at 5% interest.

$$PV = \frac{50}{0.05} = \$1{,}000$$

### Intuition

At 5%, a $1,000 investment yields $50 annually forever—exactly matching the perpetuity's cash flows.

</section>

<section class="slide" markdown="1">

## Growing Perpetuity

A **growing perpetuity** has payments that increase at rate $g$ each period.

First payment: $C$  
Second payment: $C(1+g)$  
Third payment: $C(1+g)^2$, etc.

### Present Value

$$PV = \frac{C}{1+r} + \frac{C(1+g)}{(1+r)^2} + \frac{C(1+g)^2}{(1+r)^3} + \cdots$$

$$= \frac{C}{1+r}\left[1 + \frac{1+g}{1+r} + \left(\frac{1+g}{1+r}\right)^2 + \cdots\right]$$

This is a geometric series with ratio $q = \frac{1+g}{1+r}$. For convergence, we need $|q| < 1$, i.e., $r > g$.

Sum: $\frac{1}{1-q} = \frac{1}{1 - \frac{1+g}{1+r}} = \frac{1+r}{r-g}$

Therefore:

$$PV = \frac{C}{1+r} \cdot \frac{1+r}{r-g} = \frac{C}{r - g}$$

**Example:** First payment $100, growing at 3% annually, discount rate 8%.

$$PV = \frac{100}{0.08 - 0.03} = \frac{100}{0.05} = \$2{,}000$$

</section>

<section class="slide" markdown="1">

## 7. Applications

### Bond Valuation

A bond pays periodic coupons plus face value at maturity.

$$\text{Bond Price} = PV(\text{coupons}) + PV(\text{face value})$$

**Example:** A 3-year bond with $1,000 face value pays 6% annual coupons. Market rate is 5%.

Coupons: $60 per year (ordinary annuity)  
Face value: $1,000 at $t=3$

$$\text{Price} = 60 \cdot \frac{1-(1.05)^{-3}}{0.05} + \frac{1{,}000}{(1.05)^3}$$

$$= 60 \times 2.7232 + 863.84 = 163.39 + 863.84 = \$1{,}027.23$$

The bond trades at a **premium** because the coupon rate (6%) exceeds the market rate (5%).

### Loan Amortization

Monthly loan payments form an annuity. Given loan amount $L$, rate $r$, term $n$:

$$\text{Payment} = L \cdot \frac{r}{1 - (1+r)^{-n}}$$

This is derived by solving $L = PV(\text{payments})$.

</section>

<section class="slide" markdown="1">

## Application: Mortgage Example

You borrow $300,000 for 30 years at 4.5% annual rate (compounded monthly).

Monthly rate: $r = 0.045/12 = 0.00375$  
Number of payments: $n = 30 \times 12 = 360$

$$\text{Monthly Payment} = 300{,}000 \cdot \frac{0.00375}{1 - (1.00375)^{-360}}$$

$$= 300{,}000 \cdot \frac{0.00375}{1 - 0.2556} = 300{,}000 \times 0.005067 = \$1{,}520.06$$

### Amortization Insight

**Total paid:** $1,520.06 \times 360 = $547,220.40  
**Interest paid:** $547,220.40 - $300,000 = $247,220.40

Over the loan's life, you pay **82% of the principal** in interest!

**First payment breakdown:**
- Interest: $300,000 \times 0.00375 = $1,125.00
- Principal: $1,520.06 - $1,125.00 = $395.06

Early payments are mostly interest; later payments are mostly principal.

</section>

<section class="slide" markdown="1">

## Net Present Value (NPV)

### Definition

The **Net Present Value** of a project is the sum of all discounted cash flows, including the initial investment (typically negative):

$$NPV = -C_0 + \sum_{t=1}^{n} \frac{C_t}{(1+r)^t}$$

where $C_0$ is the initial investment and $C_t$ are future cash flows.

### Decision Rule

- **NPV > 0**: Accept the project (it adds value)
- **NPV < 0**: Reject the project (it destroys value)
- **NPV = 0**: Indifferent (breaks even)

### Example

A project requires $10,000 investment today and generates $3,000, $4,000, $5,000 over the next 3 years. Discount rate is 8%.

$$NPV = -10{,}000 + \frac{3{,}000}{1.08} + \frac{4{,}000}{(1.08)^2} + \frac{5{,}000}{(1.08)^3}$$

$$= -10{,}000 + 2{,}778 + 3{,}429 + 3{,}969 = \$176$$

**Decision:** Accept (positive NPV).

</section>

<section class="slide" markdown="1">

## Internal Rate of Return (IRR)

### Definition

The **Internal Rate of Return** is the discount rate that makes NPV equal to zero:

$$0 = -C_0 + \sum_{t=1}^{n} \frac{C_t}{(1+IRR)^t}$$

### Interpretation

IRR is the **break-even rate** of return for the project.

### Decision Rule

- If **IRR > hurdle rate**: Accept the project
- If **IRR < hurdle rate**: Reject the project

### Example (continued)

For our earlier project, find IRR where:

$$0 = -10{,}000 + \frac{3{,}000}{(1+IRR)} + \frac{4{,}000}{(1+IRR)^2} + \frac{5{,}000}{(1+IRR)^3}$$

This requires numerical methods (e.g., Newton-Raphson). Solution: **IRR ≈ 8.89%**

Since IRR (8.89%) > discount rate (8%), the project is acceptable—consistent with positive NPV.

### Limitations

- Can have multiple solutions if cash flows change sign more than once
- Assumes reinvestment at IRR (often unrealistic)
- NPV is generally preferred for ranking projects

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

<section class="slide" markdown="1">

## Practice Problems

### Problem 1: Comparing Options

You win a lottery with two payout options:
- Option A: $500,000 today
- Option B: $50,000 per year for 15 years (first payment in 1 year)

At what discount rate are you indifferent between the two options?

*Hint: Set the PV of option B equal to $500,000 and solve for $r$.*

</section>

<section class="slide" markdown="1">

## Practice Problems (continued)

### Problem 2: Retirement Planning

You want $2 million when you retire in 30 years. You plan to invest in an account earning 7% annually (compounded monthly).

(a) If you make a single deposit today, how much do you need?

(b) If you make equal monthly deposits, how much per month?

### Problem 3: Rate Equivalence

What semi-annual compounding rate is equivalent to 6% continuously compounded?

</section>

<section class="slide" markdown="1">

## Practice Problems (continued)

### Problem 4: Growing Annuity

A growing annuity pays $C$ in the first period, $C(1+g)$ in the second, etc., for $n$ periods total.

Derive the present value formula:

$$PV = \frac{C}{r-g}\left[1 - \left(\frac{1+g}{1+r}\right)^n\right]$$

*Hint: Start with the geometric series for the growing perpetuity and subtract the tail.*

### Problem 5: Bond Pricing

A 10-year bond with face value $1,000 pays 8% annual coupons. If the yield is 6%, what is the bond price? What if the yield is 10%?

</section>

<section class="slide" markdown="1">

## Advanced Topic: Duration (Preview)

### Macaulay Duration

The **weighted average time** until cash flows are received:

$$D = \frac{\sum_{t=1}^{n} t \cdot PV(C_t)}{\sum_{t=1}^{n} PV(C_t)} = \frac{\sum_{t=1}^{n} t \cdot \frac{C_t}{(1+r)^t}}{PV}$$

### Why Duration Matters

Duration measures the **sensitivity** of a bond's price to interest rate changes:

$$\frac{\Delta P}{P} \approx -D \cdot \frac{\Delta r}{1+r}$$

### Example Interpretation

A bond with duration 7 years will lose approximately 7% in value if interest rates rise by 1 percentage point.

### Applications

- **Immunization**: Match asset and liability durations to hedge interest rate risk
- **Portfolio management**: Adjust duration to express interest rate views
- **Risk management**: Measure and limit interest rate exposure

*This will be covered in detail in later lectures on fixed income.*

</section>

<section class="slide" markdown="1">

## Hints for Practice Problems

### Problem 1 (Lottery Options)
Set up: $500{,}000 = 50{,}000 \cdot \frac{1-(1+r)^{-15}}{r}$  
Solve numerically: $r \approx 7.23\%$

### Problem 2 (Retirement Planning)
(a) $PV = 2{,}000{,}000 / (1 + 0.07/12)^{360} \approx \$245{,}975$  
(b) Solve: $2{,}000{,}000 = PMT \cdot \frac{(1+0.07/12)^{360}-1}{0.07/12}$, giving $PMT \approx \$1{,}633$

### Problem 3 (Rate Equivalence)
$r_2 = 2(e^{0.06/2} - 1) = 2(e^{0.03} - 1) \approx 6.09\%$

### Problem 5 (Bond Pricing)
At 6% yield: Bond price = $1,147.20 (premium)  
At 10% yield: Bond price = $877.11 (discount)  
When coupon rate > yield, bond trades at premium; when coupon rate < yield, bond trades at discount.

</section>

</div>
