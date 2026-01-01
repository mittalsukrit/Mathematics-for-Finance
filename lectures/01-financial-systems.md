---
layout: default
title: Overview of Financial Systems
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

# Overview of Financial Systems

**Sukrit Mittal**  
Franklin Templeton Investments  

</section>

<section class="slide" markdown="1">

## Course Introduction

This course introduces the **mathematical foundations of modern financial systems**.  
The emphasis is not on rules or recipes, but on **structure, abstraction, and rigor**.

Finance today is inseparable from mathematics, computation, and uncertainty.

**What you'll learn:**
- How to model financial markets mathematically
- How to quantify and manage risk
- How to value assets under uncertainty
- The computational tools that power modern finance

**What you won't learn:**
- How to get rich quick
- Stock tips or market predictions

</section>

<section class="slide" markdown="1">

## What is Quantitative Finance?

Quantitative finance is the **mathematics, statistics, and computing engine** that drives modern financial markets.

It exists because:

- **Financial markets have grown too complex for pure intuition.**  
  With thousands of assets, interdependent risks, and global connections, human intuition alone cannot process the complexity. Mathematical models provide a structured way to understand these systems.

- **Asset prices evolve under uncertainty and randomness — precisely what mathematics formalizes.**  
  We don't know what Apple's stock will be worth tomorrow, but we can model the probability distribution of possible outcomes. This is where stochastic calculus, probability theory, and statistics become essential tools.

- **Computers allow simulation, optimization, and testing at massive scale.**  
  We can backtest strategies on decades of historical data, run Monte Carlo simulations with millions of scenarios, and optimize portfolios across thousands of assets—all in seconds. This computational power has transformed finance from an art to a science.

</section>

<section class="slide" markdown="1">

<div align="center">
<img src="Figures/Line chart of Apple .png" alt="Stock chart" style="width:80%;"/>
</div>

</section>

<section class="slide" markdown="1">

## Why Should You Care About Financial Systems?

Finance is no longer a separate industry.  
It is a **mission-critical distributed computing system**.

### 1. Finance Runs on Code

- Banks, hedge funds, payment systems, and exchanges are software-driven.
- Every trade, card swipe, or UPI transaction is executed by code.
- Latency, correctness, and robustness matter as much as capital.

</section>

<section class="slide" markdown="1">

## Why Should You Care About Financial Systems?

Finance is no longer a separate industry.  
It is a **mission-critical distributed computing system**.

### 2. Algorithms Rule the Battlefield

- **High-frequency trading:** Algorithms execute thousands of trades per second, exploiting tiny price discrepancies.
- **Fraud detection:** Machine learning models analyze transaction patterns in real-time to flag suspicious activity.
- **Risk management:** Complex algorithms calculate Value-at-Risk (VaR), stress test portfolios, and manage collateral requirements.
- **Portfolio optimization:** Algorithms balance risk and return across hundreds or thousands of securities.

Many core computer science innovations—low-latency systems, streaming pipelines, secure computation—were pioneered in finance. The financial industry was building distributed systems and real-time data processing long before "big data" became a buzzword.

</section>

<section class="slide" markdown="1">

## Financial Literacy as Career Leverage

If you understand **both code and capital**, you are rare—and rarity has value.

Old view:
> Engineers build apps, finance people handle money.

Current reality:
> Those who understand both design the systems that move markets.

**Career opportunities at the intersection:**
- Quantitative analyst (quant) at hedge funds and banks
- Algorithmic trading developer
- Risk management technologist
- Fintech entrepreneur
- Blockchain developer

</section>

<section class="slide" markdown="1">

## What is a Financial System?

A **financial system** exists to coordinate economic activity across **time and uncertainty**.

At its core, it performs three fundamental functions.

**Think about it this way:** 
1. You have an idea for a startup but no money (*capital allocation* problem)
2. A farmer worries about crop prices falling next season (*risk transfer* problem)
3. An investor wants to know if Tesla is overvalued (*price discovery* problem)

The financial system provides mechanisms to solve all three.

</section>

<section class="slide" markdown="1">

<div align="center">
<img src="Figures/STI_clean_landscape_thumb.avif" alt="Stock chart" style="width:80%;"/>
</div>

</section>

<section class="slide" markdown="1">

### 1. Capital Allocation Problem

Deciding **where money should go**.

Capital is scarce.  
The system must direct it toward projects and assets with the best expected return for the risk taken.

This happens through:
- **Investment decisions:** Venture capitalists funding startups, institutional investors buying stocks
- **Lending:** Banks providing loans to businesses and consumers
- **Equity financing:** Companies raising capital by issuing shares

**Why it matters:** Efficient capital allocation means productive companies get funded while failing ones don't. This drives economic growth. Misallocation (e.g., real estate bubbles, zombie companies) destroys value and causes crises.

**Example:** When you deposit ₹100,000 in a bank, that money doesn't sit idle. The bank lends it to businesses or homebuyers. Your savings are allocated to productive uses, and you earn interest in return.

</section>

<section class="slide" markdown="1">

### 2. Risk Transfer Problem

Shifting risk from one party to another using financial instruments.

Examples:
- **Insurance:** You pay a premium to transfer risk of loss to an insurance company
- **Derivatives:** A farmer locks in wheat prices using futures contracts, transferring price risk to speculators
- **Hedging contracts:** An airline buys oil futures to protect against rising fuel costs

Purpose:
- **Allow specialization:** A farmer farms, a bank prices risk. Each does what they do best.
- **Spread risk across many participants:** Instead of one person bearing catastrophic loss, risk is distributed across thousands of counterparties.
- **Enable calculated risk-taking:** Businesses can take productive risks (R&D, expansion) while hedging away unproductive ones (currency fluctuations, commodity prices).

**Without risk transfer:** 
- Airlines would face bankruptcy risk from oil price spikes
- Farmers couldn't invest in next season's crop
- International trade would be paralyzed by currency risk

**The mathematical challenge:** How do we price these risk transfers fairly? This is where quantitative finance becomes critical.

</section>

<section class="slide" markdown="1">

### 3. Price Discovery Problem

Determining **what an asset is worth right now**.

Markets aggregate: **Information**, **Expectations**, **Sentiment**. 

Prices act as **signals**, guiding decisions and allocating resources efficiently.

**How it works:**
- If a stock is undervalued, buyers bid it up
- If it's overvalued, sellers drive it down
- The equilibrium price reflects the collective wisdom (or folly) of all market participants

**Example:** When Apple announces record iPhone sales, the stock price rises immediately. The new price incorporates this information without any central authority setting it. Millions of traders, algorithms, and investors update their valuations, and the market finds a new equilibrium in seconds.

**Why it matters:** Price discovery allows resources to flow to their most valued uses. If Tesla's stock price falls, it becomes harder for the company to raise capital—the market is signaling that resources should go elsewhere.

**The dark side:** Price discovery can fail during panics, bubbles, or when markets become illiquid. This is why market microstructure and behavioral finance are important fields.

</section>

<section class="slide" markdown="1">

## Key Components of Financial Systems

- Money Market
- Capital Market
  - Equity Market
  - Debt Market
  - Derivatives Market

</section>

<section class="slide" markdown="1">

## Money Markets vs. Capital Market

### Money Market

- Short-term borrowing and lending (maturity ≤ 1 year)
- Primarily regulated by the RBI
- Used to manage liquidity

**Characteristics:**
- **Very low risk:** Short duration means less exposure to default or interest rate changes
- **Returns linked to policy rates:** Typically close to the repo rate or overnight rates
- **High liquidity:** Easy to buy and sell quickly

**Common instruments:**
- Treasury bills (T-bills)
- Commercial paper (short-term corporate debt)
- Certificates of deposit (CDs)
- Repurchase agreements (repos)

**Purpose:** Money markets are the "working capital" of the financial system. Banks use them to manage day-to-day liquidity, and the RBI uses them to implement monetary policy.

</section>

<section class="slide" markdown="1">

## Money Market vs. Capital Market

### Capital Market

- Long-term securities (maturity > 1 year)
- Regulated by SEBI (and RBI for certain debt)
- Used to fund growth and infrastructure

**Characteristics:**
- **Higher risk:** Longer time horizon means more uncertainty and price volatility
- **Higher expected returns:** Investors demand compensation for taking on more risk
- **Sensitive to economic growth and earnings:** Long-term performance drives valuations

**Common instruments:**
- Stocks (equity)
- Corporate bonds
- Government bonds with maturity > 1 year
- Mutual funds and ETFs

**Purpose:** Capital markets fund long-term investments—building factories, infrastructure projects, R&D. Companies raise capital here to grow, while investors seek returns over years or decades.

**Key difference from money markets:** Capital markets are about **growth and wealth creation**, while money markets are about **liquidity management and safety**.

</section>

<section class="slide" markdown="1">

## Capital Markets

### Equity Market

- **What it is:** Ownership in a company. When you buy a share, you own a piece of that business.
- **Returns:** Dividends (profit sharing) + capital gains (increase in stock price)
- **Risk:** High, tied to firm performance and market sentiment

**Why companies issue equity:** To raise capital without taking on debt. Shareholders bear the risk but also get the upside.

**Why investors buy equity:** Potential for high returns over long periods. Historically, equities outperform bonds and cash over decades.

Example: Buying shares of Reliance Industries on NSE. You become a partial owner of one of India's largest conglomerates.

</section>

<section class="slide" markdown="1">

## Capital Markets

### Debt Market

- **What it is:** Lending money in exchange for interest. You're a creditor, not an owner.
- **Returns:** Fixed interest + principal repayment
- **Risk:** Lower than equity, but subject to default risk (the borrower might not pay back)

**Why companies/governments issue debt:** To raise capital while maintaining control (unlike equity, bondholders don't get ownership or voting rights).

**Why investors buy debt:** Stable, predictable income. Useful for conservative investors or portfolio diversification.

Example: Holding a 10-year Government of India bond paying 7% annual interest. You lend money to the government, and they promise to pay you back with interest.

</section>

<section class="slide" markdown="1">

## Capital Markets

### Derivatives Market

- Contracts derived from an underlying asset (stocks, bonds, commodities, currencies)
- Used for:
  - **Hedging:** Reducing risk (e.g., an airline hedging fuel costs)
  - **Speculation:** Betting on price movements with leverage
  - **Arbitrage:** Exploiting price differences between markets

Types:
- **Futures:** Obligation to buy/sell at a future date at a predetermined price
- **Options:** Right (not obligation) to buy/sell at a predetermined price
- **Swaps:** Exchange of cash flows (e.g., fixed vs. floating interest rates)

**Power and danger:** Derivatives provide leverage—you can control large positions with small capital. This magnifies both gains and losses. The 2008 crisis was partly caused by complex derivatives that few understood.

**Example:** A Nifty 50 futures contract allows you to bet on (or hedge against) the movement of India's benchmark stock index without buying all 50 stocks.

</section>

<section class="slide" markdown="1">

## Financial Institutions

### Banks

- Accept deposits
- Make loans
- Provide payment services

In India, banks are central to:
- **Money markets:** Banks are major participants in overnight lending
- **Government securities:** Major holders of G-Secs
- **Credit creation:** Through fractional reserve banking, banks create money by lending out deposits

**How banks make money:**
- Net interest margin (difference between lending and deposit rates)
- Fees (transaction fees, account maintenance)
- Trading and investment income

**Why banks matter:** They're the plumbing of the financial system. When banks fail, credit freezes, and economies contract. This is why banking regulation is so strict.

Examples: SBI (India's largest public sector bank), HDFC Bank (largest private sector bank).

</section>

<section class="slide" markdown="1">

## Financial Institutions

### Exchanges

- Organized platforms for buying and selling securities
- Ensure transparency, liquidity, and price discovery

**What exchanges provide:**
- **Standardization:** All trades follow the same rules and procedures
- **Clearing and settlement:** Guarantee that trades are completed correctly
- **Market surveillance:** Monitor for manipulation and insider trading
- **Liquidity:** Bring together many buyers and sellers, making it easy to trade

**Electronic vs. physical:** Modern exchanges are almost entirely electronic. Trading happens in microseconds through matching engines.

Examples:
- **India:** NSE (National Stock Exchange - largest by volume), BSE (Bombay Stock Exchange - oldest in Asia)
- **US:** NYSE (New York Stock Exchange - largest by market cap), NASDAQ (tech-heavy, fully electronic)

**Fun fact:** NSE's trading system can handle 40,000 orders per second. This computational infrastructure is what makes modern markets possible.

</section>

<section class="slide" markdown="1">

## Financial Institutions

### Funds

- Pool money from multiple investors
- Invest across asset classes
- Provide diversification and professional management

**Types:**
- **Mutual funds:** Actively or passively managed portfolios of stocks, bonds, or other assets
- **ETFs (Exchange-Traded Funds):** Trade like stocks but hold diversified portfolios
- **Hedge funds:** Private funds using sophisticated strategies (often restricted to wealthy investors)
- **Pension funds:** Long-term investment vehicles for retirement savings

**Why funds matter:**
- **Diversification:** Small investors can own pieces of hundreds of companies
- **Professional management:** Fund managers have expertise and resources individual investors lack
- **Economies of scale:** Lower transaction costs and better access to research

Examples:
- **Mutual funds:** HDFC Top 100 Fund, ICICI Prudential Bluechip Fund
- **ETFs:** SBI ETF Nifty 50 (tracks the Nifty index)

</section>

<section class="slide" markdown="1">

## Financial Regulators

### SEBI (Securities and Exchange Board of India)

- Regulates capital markets (stocks, bonds, mutual funds)
- Enforces disclosure and transparency requirements
- Protects investors from fraud and manipulation

**Key responsibilities:**
- Approving IPOs and ensuring proper disclosure
- Regulating mutual funds and portfolio managers
- Monitoring insider trading and market manipulation
- Setting rules for brokers and exchanges

**Recent actions:** SEBI has cracked down on "pump and dump" schemes, imposed stricter disclosure norms, and pushed for faster settlement (now T+1, meaning trades settle in one day).

US equivalent: SEC (Securities and Exchange Commission).

</section>

<section class="slide" markdown="1">

## Financial Regulators

### RBI (Reserve Bank of India)

- Central bank of India
- Controls monetary policy (interest rates, money supply)
- Regulates banks and financial institutions
- Oversees money markets and payment systems

**Key tools:**
- **Repo rate:** The rate at which RBI lends to banks (affects all other interest rates)
- **Cash Reserve Ratio (CRR):** Fraction of deposits banks must hold with RBI
- **Open market operations:** Buying/selling government bonds to control liquidity

**Why it matters:** The RBI's decisions ripple through the entire economy. When RBI raises rates, borrowing becomes expensive, which slows growth but controls inflation. When it cuts rates, borrowing becomes cheap, stimulating growth.

**Recent focus:** Digital payments (UPI), inflation targeting (maintaining CPI around 4%), and financial stability.

US equivalent: Federal Reserve (The Fed).

</section>

<section class="slide" markdown="1">

## Takeaways

**Financial markets/instruments:**
- **Equity** = ownership (high risk, high potential return)
- **Debt** = lending (lower risk, predictable return)  
- **Derivatives** = risk transfer or speculation (leverage and complexity)

**Financial institutions:**
- **Banks** = move and create money (the plumbing of finance)
- **Exchanges** = enable trading and price discovery (the marketplaces)
- **Funds** = pool and allocate capital (diversification and management)

**Financial Regulators:**
- **SEBI** = protect investors and ensure market integrity
- **RBI** = control monetary policy and banking stability

A financial system is not just about money.  
It is about **coordination, incentives, and control under uncertainty**.

</section>

<section class="slide" markdown="1">

## Thank you!

<div style="height:6rem;"></div>

## Any questions?

</section>

</div>
