---
layout: default
title: Forwards and Futures
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

# Forwards and Futures

**Sukrit Mittal**
Franklin Templeton Investments

</section>

<section class="slide" markdown="1">

## Outline

1. Why derivatives? economic purpose
2. Forward contracts: structure and notation
3. No-arbitrage toolkit
4. Forward pricing by replication
5. Pricing with income, yields, and carry costs
6. Value of an existing forward contract
7. From forwards to futures markets
8. Margining, mark-to-market, and default control
9. Futures pricing and the forward-futures link
10. Hedging with futures (commodity and equity index)
11. Basis risk and optimal hedge ratio
12. Exercises

</section>

<section class="slide" markdown="1">

## 1. Why Derivatives?

A **derivative** is a contract whose value is derived from an underlying variable.

Underlying can be:

* an asset price (equity, bond, FX, commodity)
* an index level (S&P 500, VIX)
* a rate (short rate, swap rate)
* even weather, credit events, or power prices

### Economic Roles

Derivatives are used for three distinct functions:

* **Hedging:** Reduce unwanted risk (e.g., a wheat farmer locks in a selling price)
* **Speculation:** Take views with leverage (e.g., a trader buys crude oil futures expecting a supply shock)
* **Price discovery/arbitrage:** Enforce consistency across markets (e.g., if futures and spot diverge, arbitrageurs close the gap)

The mathematics is the same; the intent differs.

### Historical Context

Forward contracting dates back centuries — rice futures in 17th-century Japan (the Dojima Rice Exchange) and grain forwards in 19th-century Chicago. The Chicago Board of Trade (CBOT, founded 1848) standardized these agreements into modern futures contracts. Today, global derivatives notional outstanding exceeds $600 trillion.

</section>

<section class="slide" markdown="1">

### Forward vs Futures in One View

A **forward** is a bilateral OTC promise to trade later at a fixed delivery price.

A **futures** contract is the exchange-traded, standardized, collateralized version of a forward.

| Feature | Forward | Futures |
|---------|---------|---------|
| Trading venue | OTC (bilateral) | Exchange (centralized) |
| Terms | Customized | Standardized |
| Counterparty risk | Bilateral credit risk | Clearinghouse-managed |
| Cash flows | Usually at maturity | Daily mark-to-market |
| Liquidity | Lower (bespoke) | Higher (fungible) |
| Regulation | Less (ISDA-governed) | More (exchange rules, CFTC/SEBI) |
| Typical users | Corporates, banks | Asset managers, CTAs, hedgers |

> The economics are nearly identical; the institutional plumbing differs.

</section>

<section class="slide" markdown="1">

## 2. Forward Contracts: Structure and Notation

Time notation:

* $t=0$: initiation date (contract is negotiated)
* $t=T$: maturity/delivery date

State variables and contract terms:

* $S_t$: spot price of the underlying at time $t$
* $K$: delivery price fixed in the contract
* $F_0(T)$: forward price for maturity $T$ agreed at $t=0$

At inception of a newly negotiated contract, the delivery price is set so that the contract has zero initial value: $K = F_0(T)$.

No money changes hands at $t=0$ — this is a key distinction from options, which require a premium.

### Payoff at Maturity

For one unit of underlying:

* **Long forward payoff:** $S_T - K$
* **Short forward payoff:** $K - S_T$

Zero-sum at maturity: the long's gain is the short's loss.

</section>

<section class="slide" markdown="1">

### Payoff Profile

The long forward payoff is **linear** in $S_T$:

* If $S_T = 120$ and $K = 100$: long gains $+20$, short loses $-20$
* If $S_T = 80$ and $K = 100$: long loses $-20$, short gains $+20$
* If $S_T = 100$ and $K = 100$: both get $0$

Unlike options, **both sides are obligated**. There is no walk-away right.

This linearity is fundamental — it means forward pricing requires no probability model, only arbitrage arguments. We will see in the options lecture that nonlinear payoffs demand a fundamentally different approach.

**Example:** A commodity trader enters a 6-month forward to buy 1,000 barrels of crude oil at $K = \$75$ per barrel.

At maturity, if spot is $S_T = \$82$:
$$
\text{Long payoff} = 1{,}000 \times (82 - 75) = +\$7{,}000
$$

If spot is $S_T = \$68$:
$$
\text{Long payoff} = 1{,}000 \times (68 - 75) = -\$7{,}000
$$

The trader is locked in regardless of where the market goes.

</section>

<section class="slide" markdown="1">

### Long and Short Interpretation

**Long forward:** Agrees to buy later at price $K$.

* Gains when market ends up high: $S_T > K$
* Loses when market ends up low: $S_T < K$
* Motivation: lock in purchase price, or speculate on rising prices

**Short forward:** Agrees to sell later at price $K$.

* Gains when market ends up low: $S_T < K$
* Loses when market ends up high: $S_T > K$
* Motivation: lock in selling price, or speculate on falling prices

Forwards require no initial premium in the plain-vanilla case, but they create future contingent gains/losses. This is why counterparty credit risk is a central concern for OTC forwards — both sides may owe money at maturity.

> The direction of the forward tells you whose risk you are managing.

</section>

<section class="slide" markdown="1">

## 3. No-Arbitrage Toolkit

Everything in this lecture follows three principles. These are not assumptions about markets being "efficient" — they are consequences of traders actively seeking profit.

### Principle A: Law of One Price

If two strategies deliver identical cash flows in every state and date, they must have the same price today.

*Violation example:* If portfolio X and portfolio Y have the same payoff in all scenarios but $\text{Price}(X) < \text{Price}(Y)$, then buy X and sell Y for riskless profit.

### Principle B: Replication

Price a hard-to-trade claim by constructing a portfolio of traded assets with identical payoff.

*Application:* We will price forwards by constructing a "synthetic forward" from the spot asset and risk-free borrowing.

### Principle C: Arbitrage Contradiction

If the market price differs from the replication cost, a trader can lock in riskless profit.

Competitive trading removes such gaps quickly. The no-arbitrage price is the only price consistent with equilibrium.

</section>

<section class="slide" markdown="1">

### Cash-and-Carry Arbitrage

This is the core arbitrage trade for forwards/futures.

**When the forward is overpriced:** $F_0(T) > S_0 e^{rT}$

| Time | Action | Cash Flow |
|------|--------|-----------|
| $t=0$ | Borrow $S_0$ at rate $r$ | $+S_0$ |
| $t=0$ | Buy asset spot | $-S_0$ |
| $t=0$ | Short forward at $F_0(T)$ | $0$ |
| $t=T$ | Deliver asset into forward | $+F_0(T)$ |
| $t=T$ | Repay loan | $-S_0 e^{rT}$ |

**Net at $T$:** $F_0(T) - S_0 e^{rT} > 0$ — riskless profit.

No initial investment, no risk, positive payoff. This is a **Type A arbitrage** (money machine).

</section>

<section class="slide" markdown="1">

### Reverse Cash-and-Carry Arbitrage

**When the forward is underpriced:** $F_0(T) < S_0 e^{rT}$

| Time | Action | Cash Flow |
|------|--------|-----------|
| $t=0$ | Short-sell asset | $+S_0$ |
| $t=0$ | Invest $S_0$ at rate $r$ | $-S_0$ |
| $t=0$ | Long forward at $F_0(T)$ | $0$ |
| $t=T$ | Collect investment | $+S_0 e^{rT}$ |
| $t=T$ | Buy asset via forward | $-F_0(T)$ |
| $t=T$ | Return asset to close short | $0$ |

**Net at $T$:** $S_0 e^{rT} - F_0(T) > 0$ — riskless profit.

**Key assumption:** Short-selling must be feasible. For investment assets (stocks, bonds, gold), this usually holds. For consumption commodities (oil, wheat), short-selling may be impractical, which is why forward prices for commodities can deviate from the simple formula.

</section>

<section class="slide" markdown="1">

## 4. Forward Pricing by Replication

**The Replication Argument**: Consider an investment asset with no income and no storage cost.

**Strategy 1 (Synthetic forward):** At $t=0$, borrow $S_0$ and buy the asset. At $T$, you own the asset and owe $S_0 e^{rT}$.

**Strategy 2 (Forward contract):** At $t=0$, enter a long forward at delivery price $K$. At $T$, you pay $K$ and receive the asset.

Both strategies give you the asset at time $T$. By the Law of One Price, the cost must be the same:
$$
K = S_0 e^{rT}
$$

This gives the no-arbitrage forward price:
$$
\boxed{F_0(T) = S_0 e^{rT}}
$$

where $r$ is the continuously compounded risk-free rate for maturity $T$.

> The forward price is *not* a forecast of where the spot will be. It is the cost of *carrying* the asset to maturity.

</section>

<section class="slide" markdown="1">

### Derivation by Contradiction

Suppose $F_0(T) > S_0 e^{rT}$.

**Arbitrageur executes cash-and-carry:**

1. Borrow $S_0$ at rate $r$
2. Buy asset at spot
3. Short forward at $F_0(T)$

At $T$: deliver asset into forward: receive $F_0(T)$. Repay borrowing: pay $S_0 e^{rT}$

Riskless profit:
$$
\Pi_T = F_0(T) - S_0 e^{rT} > 0
$$

Now suppose $F_0(T) < S_0 e^{rT}$.

**Arbitrageur executes reverse cash-and-carry:**

1. Short-sell asset: receive $S_0$
2. Invest $S_0$ at rate $r$
3. Long forward at $F_0(T)$

At $T$: collect $S_0 e^{rT}$, pay $F_0(T)$, return asset. Profit: $S_0 e^{rT} - F_0(T) > 0$.

Both directions lead to free money. Thus the only no-arbitrage equilibrium is $F_0(T) = S_0 e^{rT}$.

</section>

<section class="slide" markdown="1">

### Discrete Compounding and Numerical Example

If the annual compounding rate is $R$:

$$
F_0(T) = S_0(1+R)^T
$$

(With non-integer $T$, use the corresponding money-market convention.)

**Example:** A non-dividend stock trades at $S_0 = 50$. The 6-month continuously compounded risk-free rate is $r = 6\%$.

$$
F_0(0.5) = 50 \times e^{0.06 \times 0.5} = 50 \times e^{0.03} = 50 \times 1.03045 = 51.52
$$

**Interpretation:** The forward premium of $\$1.52$ over spot reflects the financing cost. If you buy the stock today, you tie up $\$50$ for 6 months. The forward lets you defer that capital outlay, and $F_0$ compensates for the interest you would have earned.

**What if the market quotes $F = 52.00$?**

The forward is overpriced by $52.00 - 51.52 = 0.48$. Cash-and-carry arbitrage locks in $\$0.48$ per share.

</section>

<section class="slide" markdown="1">

## 5. Pricing with Income and Carry Costs

Different underlyings modify the cost of carry. The general principle is the same: the forward price reflects the net cost of holding the asset to maturity.

### (i) Known Cash Income

If the asset pays known income before maturity with present value $PV(I)$:

$$
\boxed{F_0(T) = (S_0 - PV(I))\,e^{rT}}
$$

**Intuition:** Holding the asset gives you income that the forward holder misses. Subtract the present value of that income from the spot price before applying the carry cost.

**Example:** A stock trading at $S_0 = 40$ will pay a dividend of $\$1.50$ in 3 months. The 9-month forward price with $r = 5\%$ is:

$$
PV(I) = 1.50 \times e^{-0.05 \times 0.25} = 1.50 \times 0.9876 = 1.48
$$

$$
F_0(0.75) = (40 - 1.48) \times e^{0.05 \times 0.75} = 38.52 \times 1.0382 = 39.99
$$

Notice: the forward price is *below* spot. The dividend income more than offsets the financing cost.

</section>

<section class="slide" markdown="1">

### (ii) Continuous Income Yield

For equities/indices with a continuous dividend yield $q$:

$$
\boxed{F_0(T) = S_0\, e^{(r-q)T}}
$$

Higher $q$ lowers the forward price because the holder of the forward does not receive interim income. The spot holder collects dividends; the forward holder does not.

**Example:** An equity index is at 5,200 with continuous dividend yield $q = 1.8\%$, risk-free rate $r = 4.6\%$, and $T = 0.5$:

$$
F_0 = 5{,}200 \times e^{(0.046 - 0.018) \times 0.5} = 5{,}200 \times e^{0.014} = 5{,}200 \times 1.01410 = 5{,}273.3
$$

**What if the yield rises to $q = 3\%$?**

$$
F_0 = 5{,}200 \times e^{(0.046 - 0.03) \times 0.5} = 5{,}200 \times e^{0.008} = 5{,}200 \times 1.00803 = 5{,}241.7
$$

Higher yield $\Rightarrow$ lower forward. The gap between $r$ and $q$ is what drives the forward premium or discount.

</section>

<section class="slide" markdown="1">

### (iii) Commodities: Storage and Convenience Yield

For commodities, we must account for physical costs and benefits of holding inventory.

Include storage cost rate $u$ and convenience yield $y$:

$$
\boxed{F_0(T) = S_0\, e^{(r + u - y)T}}
$$

**Interpretation of each component:**

* $r$: financing cost of holding inventory (opportunity cost of capital)
* $u$: physical storage, insurance, and transport costs
* $y$: non-monetary benefit of physical ownership — having the commodity on hand avoids production shutdowns or delivery delays

### Contango vs Backwardation

* **Contango:** $F_0(T) > S_0$ — futures above spot. Occurs when $r + u > y$.
* **Backwardation:** $F_0(T) < S_0$ — futures below spot. Occurs when $y > r + u$.

If $y$ is high (scarcity, supply disruption), futures may trade below spot despite positive rates. This is **normal backwardation** — common in energy and agricultural markets during supply stress.

</section>

<section class="slide" markdown="1">

### Commodity Example: Gold Forward

Gold spot is $S_0 = 2{,}050$ USD/oz. Annualized storage cost rate $u = 1.2\%$, convenience yield $y = 0.7\%$, risk-free rate $r = 4.5\%$.

$$
F_0(1) = 2{,}050 \times e^{(0.045 + 0.012 - 0.007) \times 1} = 2{,}050 \times e^{0.05}
$$

$$
= 2{,}050 \times 1.05127 = 2{,}155.10
$$

**Net cost of carry:** $r + u - y = 4.5\% + 1.2\% - 0.7\% = 5.0\%$

Gold is in **contango** — the forward is above spot because carry costs exceed convenience yield. This is typical: gold has low convenience yield (it is not consumed in production) but tangible storage and insurance costs.

**Contrast with crude oil during scarcity:** If supply is tight, $y$ can spike above $r + u$, pushing futures below spot. This happened during the 2022 energy crisis when near-term oil was far more valuable than deferred delivery.

</section>

<section class="slide" markdown="1">

### (iv) Foreign Exchange Forwards

Treat foreign currency as an asset with "income" equal to the foreign risk-free rate $r_f$.

If the domestic rate is $r_d$:

$$
\boxed{F_0(T) = S_0\, e^{(r_d - r_f)T}}
$$

This is **covered interest rate parity (CIP)** in continuous form. It is one of the most precisely enforced arbitrage relationships in finance.

**Example:** USD/EUR spot is 1.1000 USD per EUR. Domestic USD rate $r_d = 5\%$, EUR rate $r_f = 3\%$, $T = 1$ year:

$$
F_0 = 1.1000 \times e^{(0.05 - 0.03) \times 1} = 1.1000 \times e^{0.02} = 1.1000 \times 1.02020 = 1.1222
$$

**Interpretation:** The dollar has a higher interest rate, so the USD/EUR forward is above spot — the dollar is at a *forward discount* relative to the euro. Why? If you hold euros, you earn 3%; holding dollars earns 5%. The forward adjusts so that borrowing in one currency, converting, investing in the other, and covering with a forward yields zero profit.

</section>

<section class="slide" markdown="1">

### Summary of Forward Pricing Formulas

| Underlying | Forward Price | Key Parameter |
|-----------|--------------|---------------|
| No income | $S_0 e^{rT}$ | Risk-free rate $r$ |
| Known cash income $I$ | $(S_0 - PV(I))e^{rT}$ | Dividend amount |
| Continuous yield $q$ | $S_0 e^{(r-q)T}$ | Dividend yield |
| Commodity | $S_0 e^{(r+u-y)T}$ | Storage $u$, convenience $y$ |
| FX | $S_0 e^{(r_d - r_f)T}$ | Interest rate differential |

All formulas share the same structure:

$$
F_0(T) = S_0 \times e^{(\text{net cost of carry}) \times T}
$$

The **net cost of carry** = financing cost + storage costs $-$ income/benefits of holding the asset.

</section>

<section class="slide" markdown="1">

## 6. Value of an Existing Forward Contract

**Pricing** answers: what delivery price $K$ makes a new contract have zero value?

**Valuation** answers: what is an existing contract worth when the market has moved?

These are different questions. Students often confuse them.

### Valuation Formula

For a long forward with delivery price $K$, at time $t < T$:

$$
\boxed{V_t^{\text{long}} = S_t - K\,e^{-r(T-t)}}
$$

**Derivation:** At maturity, the long receives $S_T - K$. At time $t$, the present value of $K$ at maturity is $K e^{-r(T-t)}$. The spot asset is worth $S_t$ today. So the contract value is the difference between what you will receive ($S_t$ growing to $S_T$) and what you must pay (the present value of $K$).

If the underlying has continuous yield $q$, use the market forward price $F_t(T)$:

$$
V_t^{\text{long}} = e^{-r(T-t)}\big(F_t(T) - K\big)
$$

Short value is always the negative: $V_t^{\text{short}} = -V_t^{\text{long}}$.

</section>

<section class="slide" markdown="1">

### Valuation Example

At $t=0$, you entered a 1-year long forward on a non-dividend stock with $K=105$.

After 4 months ($t = 4/12$):

* Spot is $S_t = 112$
* Risk-free rate remains $r = 5\%$
* Remaining time: $T - t = 8/12$

**Step 1:** Present value of delivery price:
$$
K\,e^{-r(T-t)} = 105 \times e^{-0.05 \times 8/12} = 105 \times e^{-0.0333} = 105 \times 0.9672 = 101.56
$$

**Step 2:** Contract value:
$$
V_t^{\text{long}} = 112 - 101.56 = 10.44
$$

The contract has positive value to the long (you could sell this contract for approximately $\$10.44$) and negative value to the short.

**Verification via forward price method:**
$$
F_t(T) = 112 \times e^{0.05 \times 8/12} = 112 \times 1.0339 = 115.80
$$

$$
V_t^{\text{long}} = e^{-0.05 \times 8/12}(115.80 - 105) = 0.9672 \times 10.80 = 10.45 \quad \checkmark
$$

</section>

<section class="slide" markdown="1">

### Forward Price vs Forward Value

> These are the two most commonly confused concepts in derivatives.

* **Forward price** $F_t(T)$: the delivery price that makes a *new* contract at time $t$ have zero value. It changes continuously as markets move.

* **Forward value** $V_t$: the mark-to-market value of an *existing* contract struck at the old delivery price $K$. It starts at zero and fluctuates.

**Key identity:**

$$
V_t^{\text{long}} = e^{-r(T-t)}(F_t(T) - K)
$$

The value is the **discounted difference** between the current fair delivery price and the locked-in delivery price.

**Analogy:** Think of $K$ as the price you agreed to pay for a house 6 months ago. The forward price $F_t$ is what a comparable house sells for today. Your contract's value is the discounted difference — if houses appreciated, your contract is worth money.

### At Inception

When the contract is first written: $K = F_0(T)$, so $V_0 = 0$.

As time passes and $S_t$ moves, $F_t(T)$ changes but $K$ stays fixed. The wedge between them creates value.

</section>

<section class="slide" markdown="1">

## 7. From Forwards to Futures Markets

A futures contract is a standardized forward with institutional risk controls that solve the credit problem of bilateral OTC contracts.

### Standardization Dimensions

Exchanges specify:

* **Contract size (multiplier):** e.g., 1 S&P 500 E-mini = $50 \times \text{index level}$
* **Delivery months:** typically quarterly (Mar, Jun, Sep, Dec) or monthly
* **Quality grade:** for commodities (e.g., WTI crude light sweet, #2 soft red winter wheat)
* **Delivery location:** Cushing, OK for WTI; COMEX vaults for gold
* **Last trading day / notice day:** standardized calendar

Standardization creates **fungibility**: any buyer's contract is identical to any other buyer's, enabling secondary market trading and position netting.

### Open Interest and Volume

* **Volume:** number of contracts traded per day (measures activity)
* **Open interest:** total number of outstanding contracts (measures market size)

Open interest rises when new positions are created and falls when existing positions are closed.

</section>

<section class="slide" markdown="1">

### Clearinghouse Role

The clearinghouse performs **novation**: it becomes the counterparty to every trade.

After a trade between A and B:

* Buyer A faces the clearinghouse (not B)
* Seller B faces the clearinghouse (not A)

**Why this matters:**

1. **Credit risk is mutualized:** If B defaults, the clearinghouse absorbs the loss using margin, default fund, and its own capital — A is protected
2. **Position netting:** A can close a long position by selling to any counterparty, not just the original seller
3. **Transparency:** The clearinghouse monitors all positions and can intervene before losses accumulate

This centralization plus margining is why futures credit risk is far lower than forward credit risk. The 2008 financial crisis demonstrated the value of central clearing — no major futures clearinghouse has ever failed, while bilateral OTC markets saw cascading defaults.

</section>

<section class="slide" markdown="1">

## 8. Margining and Mark-to-Market

### Daily Settlement Mechanics

Let:

* $M$: contract multiplier (e.g., 50 for E-mini S&P 500)
* $N$: number of contracts (positive for long)
* $F_t$: settlement price at end of day $t$

**Daily variation margin cash flow:**

$$
\boxed{\Delta \text{VM}_t = N \cdot M \cdot (F_t - F_{t-1})}
$$

The margin account is credited (if positive) or debited (if negative) each day.

**Cumulative P&L from day 0 to day $t$:**

$$
\text{P\&L}_{0 \to t} = N \cdot M \cdot (F_t - F_0)
$$

Same total economics as a forward at maturity, but **realized pathwise over time**. This is the fundamental difference between forwards and futures.

> Futures convert a single terminal cash flow into a stream of daily cash flows. The path matters because each day's gain or loss must be financed or can be invested.

</section>

<section class="slide" markdown="1">

### Initial and Maintenance Margin

Two margin levels control default risk:

* **Initial margin:** collateral deposited to open a position. Set by the exchange based on contract volatility. Typically 5-15% of notional value.

* **Maintenance margin:** minimum balance below which a **margin call** is triggered. Usually 70-80% of initial margin.

**Margin call process:**

1. End of day: margin balance falls below maintenance level
2. Exchange/broker issues a margin call
3. Trader must deposit cash to restore balance to **initial margin level** (not just maintenance)
4. If not met promptly (usually by next morning), broker can liquidate positions

**Why top up to initial, not maintenance?** This creates a buffer. If you only topped up to maintenance, a single bad day could trigger another margin call immediately. The initial margin provides breathing room.

</section>

<section class="slide" markdown="1">

### Margin Example

Long 3 contracts, multiplier $M = 100$ units. Entry futures price $F_0 = 250$.

Initial margin = $9{,}000$ total, maintenance = $6{,}750$.

| Day | Settlement Price | Daily P&L | Margin Balance | Margin Call? |
|-----|-----------------|-----------|----------------|--------------|
| 0 | 250 | — | 9,000 | — |
| 1 | 247 | $3 \times 100 \times (247-250) = -900$ | 8,100 | No |
| 2 | 244 | $3 \times 100 \times (244-247) = -900$ | 7,200 | No |
| 3 | 242 | $3 \times 100 \times (242-244) = -600$ | 6,600 | **Yes** |
| | | Deposit $+2{,}400$ to restore | 9,000 | |
| 4 | 245 | $3 \times 100 \times (245-242) = +900$ | 9,900 | No |
| 5 | 249 | $3 \times 100 \times (249-245) = +1{,}200$ | 11,100 | No |

**Day 3:** Balance $6{,}600 < 6{,}750$ (maintenance). Margin call requires $9{,}000 - 6{,}600 = 2{,}400$ to restore initial margin.

**Cumulative P&L at day 5:** $3 \times 100 \times (249 - 250) = -300$. Despite the margin call drama, the net loss is small because the price partially recovered.

</section>

<section class="slide" markdown="1">

### Funding Cost of Daily Settlement

Daily mark-to-market creates a subtle cost: you must **finance losses immediately** but can only **invest gains at prevailing rates**.

Consider two scenarios for a long position:

**Scenario A (Steady rise):** Price goes from 100 to 105 in 5 equal daily steps.
* Each day's gain is reinvested at the overnight rate.
* Total slightly exceeds 5 because of reinvestment.

**Scenario B (Volatile path to same endpoint):** Price swings wildly but ends at 105.
* Losses on down days must be financed (borrowing cost).
* Gains on up days earn interest.
* Net funding cost is path-dependent.

This is why the futures price can differ from the forward price when interest rates are stochastic — the daily settlement interacts with rate movements. We formalize this next.

</section>

<section class="slide" markdown="1">

## 9. Futures Pricing and Forward-Futures Link

### The Equivalence Result

Under idealized assumptions:

* **Deterministic** (non-random) interest rates
* No transaction costs, taxes, or margin funding frictions
* Same underlying and maturity

Then:

$$
\boxed{\text{Futures price} = \text{Forward price}}
$$

for the same maturity and underlying.

**Proof sketch:** With deterministic rates, the daily settlement cash flows can be perfectly reinvested/financed at known rates. The total accumulated value of daily settlements exactly matches the terminal forward payoff. This result is due to Cox, Ingersoll, and Ross (1981).

**In practice:** For most equity index and commodity futures with maturities under 1-2 years, the difference is negligibly small (typically a few basis points).

</section>

<section class="slide" markdown="1">

### Why They Can Differ: The Convexity Adjustment

When interest rates are **stochastic**, the daily reinvestment/financing creates a bias.

**The mechanism:** Suppose the underlying price is positively correlated with interest rates (e.g., stock indices tend to rise when rates rise).

* When futures price rises $\rightarrow$ you receive margin gains
* But rates are also high $\rightarrow$ those gains are reinvested at attractive rates
* When futures price falls $\rightarrow$ you pay margin losses
* But rates are low $\rightarrow$ financing those losses is cheap

This asymmetry makes long futures *more attractive* than a long forward. To restore zero value at inception, the futures price must be set **slightly higher** than the forward price.

**Magnitude:** For Eurodollar futures (now SOFR futures), the convexity adjustment can be several basis points for long-dated contracts (5+ years). For equity index futures with 3-month maturities, it is negligible.

**Formal result:**

$$
\text{Futures price} \approx \text{Forward price} + \text{Cov}(\text{daily gains}, \text{rate changes})
$$


The formal convexity adjustment result arises from analyzing how daily settlement interacts with stochastic interest rates.

</section>

<section class="slide" markdown="1">

**Setup:** Let $r_t$ be the spot rate at time $t$. The cumulative P&L from a long futures position with $N$ contracts (notional $M$) is:
$$
\text{P\&L}_T = N \cdot M \cdot (F_T - F_0) = N \cdot M \cdot (S_T - S_0)
$$

For a forward, this payoff is received in a lump sum at $T$. For futures, it is realized as daily increments:
$$
\text{Futures P\&L} = \sum_{i=1}^{T} N \cdot M \cdot (F_i - F_{i-1})
$$

**Key difference:** Each daily gain $N \cdot M \cdot (F_i - F_{i-1})$ received on day $i$ can be reinvested from day $i$ to day $T$ at the then-prevailing rate $r_i$. Each daily loss must be financed at rate $r_i$.

**Accumulated value at $T$:**
$$
\text{Futures P\&L}_{\text{accumulated}} = \sum_{i=1}^{T} [N \cdot M \cdot (F_i - F_{i-1})] \cdot e^{r_i(T-i)}
$$

Taking expectations and assuming $F_{i-1}$ is a [martingale](https://en.wikipedia.org/wiki/Martingale_(probability_theory)) (no trend to prices), the expectation of this produces a cross-term:
$$
\mathbb{E}[\text{Futures P\&L}_{\text{accumulated}}] - \mathbb{E}[\text{Forward P\&L}] \propto \mathbb{E}[\text{Cov}(\Delta F_i, r_i)]
$$

If $\Delta F > 0$ (price rises) tends to occur when $r$ is high, then reinvestment rates are attractive, making futures more valuable. To equate the expected payoff at inception, the futures price must be set higher:
$$
F_0^{\text{futures}} = F_0^{\text{forward}} + \text{Convexity bias}
$$

where the bias is proportional to the correlation between price and rate changes.


</section>

<section class="slide" markdown="1">

### Convergence at Maturity

For both deliverable and cash-settled futures: $F_T = S_T$

If $F_T > S_T$: sell futures at $F_T$, buy spot at $S_T$, deliver immediately. Riskless profit.

If $F_T < S_T$: buy futures at $F_T$, take delivery, sell spot at $S_T$. Riskless profit.

Arbitrage forces convergence. For cash-settled contracts, convergence is built into the settlement rule by definition.

### Basis

Define the **basis** at time $t$:
$$
\text{Basis}_t = S_t - F_t
$$

**Properties:**

* At maturity: $\text{Basis}_T = S_T - F_T = 0$
* Before maturity: basis reflects cost of carry
* For a contango market: basis is negative ($F > S$)
* For a backwardated market: basis is positive ($S > F$)

As maturity approaches, basis converges to zero — this is a deterministic feature, not a forecast.

</section>

<section class="slide" markdown="1">

## 10. Hedging with Futures

> A hedge transfers unwanted price risk from someone who has it to someone willing to bear it.

**Producer/Inventory Hedge (Short Hedge):** If you hold or will produce the physical asset, **falling prices hurt you**.

* Wheat farmer with 100,000 bushels at harvest
* Gold miner with quarterly production
* Oil producer with reserves

Hedge by **shorting futures**. If spot falls, the futures gain offsets the inventory loss.

**Consumer/Input Hedge (Long Hedge):** If you will need to buy the asset in the future, **rising prices hurt you**.

* Airline buying jet fuel
* Cereal manufacturer buying wheat
* Jeweler buying gold

Hedge by **going long futures**. If spot rises, the futures gain offsets the higher purchase cost.

The direction of the hedge is determined by **which spot move is harmful**.

</section>

<section class="slide" markdown="1">

### Short Hedge Example

A wheat farmer expects to harvest 100,000 bushels in 3 months. Current spot is $\$5.80$/bushel. The 3-month futures price is $F_0 = \$5.90$/bushel. Each futures contract covers 5,000 bushels.

**Hedge:** Short $100{,}000 / 5{,}000 = 20$ contracts.

**Scenario 1: Spot falls to $\$5.20$**

| Component | Cash Flow |
|-----------|-----------|
| Sell wheat at spot | $100{,}000 \times 5.20 = \$520{,}000$ |
| Futures P&L | $20 \times 5{,}000 \times (5.90 - 5.20) = +\$70{,}000$ |
| **Total revenue** | **$\$590{,}000$** |

**Scenario 2: Spot rises to $\$6.40$**

| Component | Cash Flow |
|-----------|-----------|
| Sell wheat at spot | $100{,}000 \times 6.40 = \$640{,}000$ |
| Futures P&L | $20 \times 5{,}000 \times (5.90 - 6.40) = -\$50{,}000$ |
| **Total revenue** | **$\$590{,}000$** |

In both cases, the effective selling price is approximately $\$5.90$/bushel (the initial futures price). The hedge locks in revenue regardless of spot movements — but it also eliminates upside.

</section>

<section class="slide" markdown="1">

### Minimum-Variance Hedge Ratio

When the spot and futures exposures are not identical (different commodity, different grade, different timing), a 1:1 hedge is not generally optimal.

**Setup:** Let $\Delta S$ and $\Delta F$ be changes in spot and futures prices over the hedge horizon. The hedged P&L for a long spot position with $h$ units of short futures per unit of spot exposure is:
$$
\Delta \text{P\&L} = \Delta S - h \cdot \Delta F
$$

**Objective:** Choose $h$ to minimize $\text{Var}(\Delta \text{P\&L})$.
$$
\text{Var}(\Delta S - h \cdot \Delta F) = \sigma_S^2 - 2h\,\text{Cov}(\Delta S, \Delta F) + h^2 \sigma_F^2
$$

Take the derivative with respect to $h$ and set to zero:
$$
\frac{\partial}{\partial h}\text{Var} = -2\,\text{Cov}(\Delta S, \Delta F) + 2h\,\sigma_F^2 = 0
$$
$$
\boxed{h^* = \frac{\text{Cov}(\Delta S, \Delta F)}{\text{Var}(\Delta F)} = \rho_{SF}\frac{\sigma_S}{\sigma_F}}
$$

This is simply the **regression coefficient** of $\Delta S$ on $\Delta F$.

</section>

<section class="slide" markdown="1">

### Interpreting the Hedge Ratio

The optimal hedge ratio $h^* = \rho_{SF}\frac{\sigma_S}{\sigma_F}$ has two components:

* $\rho_{SF}$: **correlation** between spot and futures — if correlation is low, hedge less aggressively
* $\sigma_S / \sigma_F$: **volatility ratio** — if spot is more volatile than futures, hedge more than 1:1

**Special cases:**

* $\rho_{SF} = 1$ and $\sigma_S = \sigma_F$: perfect hedge, $h^* = 1$
* $\rho_{SF} = 0$: no hedging benefit at all, $h^* = 0$
* $\rho_{SF} = 0.85$, $\sigma_S > \sigma_F$: cross-hedge with $h^* > 0.85$

**Number of futures contracts:**
$$
N^* = h^* \times \frac{N}{M}
$$

where $N$ is the position size (in units of the underlying) and $M$ is the contract multiplier (notional value per contract). Round to the nearest integer.

**Hedge effectiveness:** The fraction of variance eliminated is $R^2 = \rho_{SF}^2$. With $\rho = 0.85$, the hedge removes $72\%$ of variance.

</section>

<section class="slide" markdown="1">

### Cross-Hedge Example: Airline Fuel

Jet fuel buyer needs 2,000,000 gallons in 4 months. No liquid jet fuel futures exist, so uses heating-oil futures (proxy hedge):

* Contract size $Q_F = 42{,}000$ gallons
* Estimated $\sigma_S = 0.12$ (jet fuel volatility), $\sigma_F = 0.10$ (heating oil volatility), $\rho_{SF} = 0.85$

**Step 1: Optimal hedge ratio**
$$
h^* = 0.85 \times \frac{0.12}{0.10} = 1.02
$$

The ratio exceeds 1 because jet fuel is more volatile than heating oil.

**Step 2: Number of contracts**
$$
N^* = 1.02 \times \frac{2{,}000{,}000}{42{,}000} = 48.6 \approx 49 \text{ contracts (long)}
$$

**Step 3: Hedge effectiveness**
$$
R^2 = 0.85^2 = 0.7225
$$

The hedge removes about $72\%$ of price variance. The remaining $28\%$ is **basis risk** — the risk that jet fuel and heating oil prices diverge.

</section>

<section class="slide" markdown="1">

### Index Futures Hedge for Equity Portfolios

For a portfolio with value $V_P$ and beta $\beta_P$ relative to the index:
$$
\boxed{N = \frac{(\beta_P - \beta^*)\,V_P}{F_0 \cdot M}}
$$
where:

* $\beta^*$ is the **target beta** after hedging
* $F_0 \cdot M$ is the notional value per futures contract
* $N > 0$ means short futures (reducing beta); $N < 0$ means long futures (increasing beta)

**Example:** Portfolio value $V_P = \$50$ million, $\beta_P = 1.3$, target $\beta^* = 0.5$.

Index futures at $F_0 = 5{,}000$, multiplier $M = 50$, so notional per contract $= \$250{,}000$.
$$
N = \frac{(1.3 - 0.5) \times 50{,}000{,}000}{250{,}000} = \frac{0.8 \times 50{,}000{,}000}{250{,}000} = 160 \text{ contracts short}
$$
**Special case: Market-neutral** ($\beta^* = 0$):
$$
N = \frac{1.3 \times 50{,}000{,}000}{250{,}000} = 260 \text{ contracts short}
$$
This is a common strategy for equity long-short hedge funds that want stock-picking alpha without market exposure.

</section>

<section class="slide" markdown="1">

## 11. Basis Risk and Rolling Hedges

### Sources of Basis Risk

A **perfect hedge** requires exact match in:

* Underlying quality (same commodity grade, same stock)
* Quantity (exact multiple of contract size)
* Maturity (hedge expiry matches exposure timing)

Usually at least one mismatch exists. The residual risk comes from **basis changes**:

$$
\Delta \text{Basis} = (S_{t+\Delta t} - F_{t+\Delta t}) - (S_t - F_t)
$$

**Three types of basis risk:**

1. **Cross-commodity basis:** Hedging jet fuel with heating oil futures (different product)
2. **Location basis:** Hedging Brent crude with WTI futures (different delivery point)
3. **Calendar basis:** Hedging a 7-month exposure with 6-month futures (maturity mismatch)

Even a "perfect" hedge with the correct underlying has calendar basis risk if the hedge is lifted before contract expiry.

</section>

<section class="slide" markdown="1">

### Rolling Hedges

Long-dated exposures are often hedged using **nearby (short-dated) futures** and **rolled forward** as each contract approaches expiry.

**Rolling process:**

1. Open hedge with nearest liquid contract (e.g., March futures)
2. Before March expiry, close March position and open June position
3. Before June expiry, close June and open September
4. Continue until exposure date

**Roll yield:** The P&L from closing one contract and opening the next at a different price. In contango markets, rolling is costly (sell low, buy high). In backwardated markets, rolling generates income.

**Real-world example:** Metallgesellschaft (1993) hedged long-term oil delivery commitments with short-dated futures. When oil markets moved against them, massive margin calls on the rolling hedge forced them to liquidate at a $\$1.3$ billion loss — even though the long-term position may have been sound.

> Rolling hedges transform price risk into **funding risk**. The economics may be correct at maturity, but you must survive the margin calls along the way.

</section>

<section class="slide" markdown="1">

### Limitations of Futures Hedging

No hedge is perfect. Key limitations include:

**1. Basis risk is irreducible in cross-hedges**

Even with optimal $h^*$, the hedge only removes $\rho^2$ of variance. If $\rho = 0.80$, you still bear $36\%$ of the original variance.

**2. Hedge ratio estimation error**

$h^*$ depends on estimates of $\sigma_S$, $\sigma_F$, and $\rho$, which change over time. A hedge ratio estimated from historical data may be wrong for the current regime.

**3. Discrete contract sizes**

You cannot trade fractional contracts. If $N^* = 48.6$, you trade 49, introducing a small over-hedge.

**4. Margin funding costs**

Daily mark-to-market requires cash. In volatile markets, margin calls can force liquidation before the hedge horizon (the Metallgesellschaft problem).

**5. Tailing the hedge**

Because futures P&L is realized daily while the spot exposure is at maturity, a precise hedge should be "tailed" — slightly reduced to account for the time value of daily settlements.

</section>

<section class="slide" markdown="1">

## Final Takeaways

* **Forward pricing is a no-arbitrage replication result, not a forecast**
  * $F_0(T) = S_0 e^{rT}$ for a simple investment asset
  * Carry components ($r, q, u, y$) determine forward levels for different underlyings

* **Forward price and forward value are different objects**
  * Forward price $F_t(T)$: delivery price that makes a new contract have zero value
  * Forward value $V_t$: mark-to-market value of an existing contract struck at old $K$
  * $V_t^{\text{long}} = e^{-r(T-t)}(F_t(T) - K)$

* **Futures reduce credit risk via clearing and daily variation margin**
  * Clearinghouse becomes counterparty to every trade
  * Daily mark-to-market prevents loss accumulation
  * Margin calls enforce collateralization

* **Futures and forwards are close, but not always identical**
  * Equal under deterministic interest rates
  * Stochastic rates introduce convexity adjustment
  * Basis converges to zero at maturity: $F_T = S_T$

* **Hedging quality depends on basis behavior and hedge ratio estimation**
  * Minimum-variance hedge ratio: $h^* = \rho_{SF}\frac{\sigma_S}{\sigma_F}$
  * Cross-hedging introduces basis risk from underlying mismatch
  * Index futures hedging uses portfolio beta to size the position

**Key insight:** Forward and futures prices are not forecasts—they are no-arbitrage consequences of the cost of carry. Understanding the replication argument is more important than memorizing formulas.

Next lecture: **Options**—where asymmetric payoffs and nonlinearity demand a fundamentally different pricing approach.

</section>

<section class="slide" markdown="1">

## 12. Exercises

### Exercise 1: Basic Forward Price

A non-dividend stock has $S_0=80$. The continuously compounded risk-free rate is $r=4\%$.

**Tasks:**
1. Compute the 9-month forward price
2. If the market quotes the forward at 82.50, describe the arbitrage strategy
3. What is the arbitrage profit per unit?

</section>

<section class="slide" markdown="1">

### Exercise 2: Index Forward with Dividend Yield

A stock index has current level 5,200 and continuous dividend yield $q=1.8\%$. The risk-free rate is $r=4.6\%$ and $T=0.5$.

**Tasks:**
1. Compute the fair forward price
2. Explain why higher dividend yield lowers the forward price
3. If the index yield increases to $q=3\%$, recompute the forward price

</section>

<section class="slide" markdown="1">

### Exercise 3: Forward Contract Valuation

You entered a long forward 6 months ago with delivery price $K=102$ on a non-dividend asset. Contract maturity is 1 year, current spot is 108, and $r=5\%$ (continuous, flat).

**Tasks:**
1. What is the current contract value to the long?
2. What is the current forward price $F_t(T)$ for a new contract?
3. Verify that $V_t^{\text{long}} = e^{-r(T-t)}(F_t(T) - K)$ gives the same answer

</section>

<section class="slide" markdown="1">

### Exercise 4: Commodity Forward with Carry Costs

Gold spot is 2,050 USD/oz. Annualized storage cost is 1.2% of spot, convenience yield is 0.7%, and $r=4.5\%$.

**Tasks:**
1. Compute the 1-year forward price under the continuous carry model
2. Identify the net cost of carry
3. If convenience yield rises to 5%, is the market in backwardation or contango?

</section>

<section class="slide" markdown="1">

### Exercise 5: FX Forward and Covered Interest Parity

USD/EUR spot is 1.1000 USD per EUR. Domestic USD rate is 5%, EUR rate is 3%, continuous compounding.

**Tasks:**
1. Compute the 1-year forward exchange rate
2. Explain the economic intuition: should the USD/EUR forward be above or below spot?
3. If the market quotes 1.1150, describe the arbitrage

</section>

<section class="slide" markdown="1">

### Exercise 6: Futures Variation Margin

You are long 4 futures contracts. Multiplier is 50. Prices over three days are 300, 296, 301, 298.

**Tasks:**
1. Compute the daily variation margin cash flows
2. Compute the cumulative P&L after three days
3. Compare with the equivalent forward P&L at the final price

</section>

<section class="slide" markdown="1">

### Exercise 7: Margin Call Mechanics

Initial margin is \$60,000, maintenance margin is \$45,000. Starting from initial margin, daily losses are \$8,000, \$5,000, \$4,000.

**Tasks:**
1. Track the margin account balance day by day
2. On which day is a margin call triggered?
3. How much cash is required to restore initial margin?

</section>

<section class="slide" markdown="1">

### Exercise 8: Naive Commodity Hedge

A wheat producer expects 250,000 bushels in 5 months. Each futures contract is 5,000 bushels.

**Tasks:**
1. If using a naive 1:1 hedge, how many contracts are needed?
2. Should the producer go long or short? Explain.
3. What is the main source of residual risk in this hedge?

</section>

<section class="slide" markdown="1">

### Exercise 9: Minimum-Variance Cross-Hedge

For a cross-hedge, estimated $\rho_{SF}=0.78$, $\sigma_S=0.16$, $\sigma_F=0.20$. Exposure size is 12,000 units and each futures contract covers 1,000 units.

**Tasks:**
1. Compute the optimal hedge ratio $h^*$
2. Compute the optimal number of contracts $N^*$
3. Explain why $h^* \neq 1$ even though the hedge is meant to offset the exposure

</section>

<section class="slide" markdown="1">

### Exercise 10: Index Futures Beta Hedge

Equity portfolio value is $V_P=75$ million with beta $1.25$. Index futures are at 5,000 with multiplier $50$.

**Tasks:**
1. How many contracts are needed to reduce beta to 0.60?
2. Should you go long or short the futures?
3. How many contracts would make the portfolio market-neutral ($\beta^*=0$)?

</section>

</div>
