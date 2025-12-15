---
layout: default
title: Overview of Financial Systems
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

  /* Nice-to-have: smoother feel */
  html { scroll-behavior: smooth; }
</style>

<div class="slides">

<section class="slide">

# Overview of Financial Systems

**Sukrit Mittal**  
Franklin Templeton Investments  

</section>

<section class="slide">

## 1. Course Introduction

This course introduces the **mathematical foundations of modern financial systems**.  
The emphasis is not on rules or recipes, but on **structure, abstraction, and rigor**.

Finance today is inseparable from mathematics, computation, and uncertainty.

</section>

<section class="slide">

## What is Quantitative Finance?

Quantitative finance is the **mathematics, statistics, and computing engine** that drives modern financial markets.

It exists because:

- Financial markets have grown too complex for pure intuition.
- Asset prices evolve under uncertainty and randomness — precisely what mathematics formalizes.
- Computers allow simulation, optimization, and testing at massive scale.

</section>

<section class="slide">

## Why Should You Care About Financial Systems?

Finance is no longer a separate industry.  
It is a **mission-critical distributed computing system**.

### Finance Runs on Code

- Banks, hedge funds, payment systems, and exchanges are software-driven.
- Every trade, card swipe, or UPI transaction is executed by code.
- Latency, correctness, and robustness matter as much as capital.

### Algorithms Rule the Battlefield

- High-frequency trading  
- Fraud detection  
- Risk management  
- Portfolio optimization  

Many core computer science innovations—low-latency systems, streaming pipelines, secure computation—were pioneered in finance.

</section>

<section class="slide">

## Financial Literacy as Career Leverage

If you understand **both code and capital**, you are rare—and rarity has value.

Old view:
> Engineers build apps, finance people handle money.

Current reality:
> Those who understand both design the systems that move markets.

</section>

<section class="slide">

## 2. What Is a Financial System?

A **financial system** exists to coordinate economic activity across **time and uncertainty**.

At its core, it performs three fundamental functions.

</section>

<section class="slide">

### 1. Allocation of Capital

Deciding **where money should go**.

Capital is scarce.  
The system must direct it toward projects and assets with the best expected return for the risk taken.

This happens through:
- Investment decisions
- Lending
- Equity financing

</section>

<section class="slide">

### 2. Risk Transfer

Shifting risk from one party to another using financial instruments.

Examples:
- Insurance
- Derivatives
- Hedging contracts

Purpose:
- Allow specialization (a farmer farms, a bank prices risk)
- Spread risk across many participants
- Enable calculated risk-taking instead of existential bets

</section>

<section class="slide">

### 3. Price Discovery

Determining **what an asset is worth right now**.

Markets aggregate:
- Information
- Expectations
- Sentiment

Prices act as **signals**, guiding decisions and allocating resources efficiently.

</section>

<section class="slide">

## An Analogy: Financial System as an Operating System

Think of the financial system as the **operating system of the economy**.

| OS Function                    | Financial Equivalent              |
|--------------------------------|----------------------------------|
| Resource allocation            | Capital allocation               |
| Inter-process communication    | Payments & settlements           |
| Security & access control      | Risk management & regulation     |
| Scheduling                     | Liquidity management             |
| APIs & system calls            | Financial instruments & markets  |
| Monitoring & logs              | Price discovery & reporting      |

Just as a faulty OS crashes applications, a faulty financial system crashes economies.

</section>

<section class="slide">

## 3. Key Components of Financial Systems

</section>

<section class="slide">

## Money Markets vs. Capital Markets

### Money Markets

- Short-term borrowing and lending (maturity ≤ 1 year)
- Primarily regulated by the RBI
- Used to manage liquidity

Characteristics:
- Very low risk
- Returns linked to policy rates
- High liquidity

</section>

<section class="slide">

### Capital Markets

- Long-term securities (maturity > 1 year)
- Regulated by SEBI (and RBI for certain debt)
- Used to fund growth and infrastructure

Characteristics:
- Higher risk
- Higher expected returns
- Sensitive to economic growth and earnings

</section>

<section class="slide">

## Introduction to Financial Markets

### Equity Markets

- **What it is:** Ownership in a company
- **Returns:** Dividends + capital gains
- **Risk:** High, tied to firm performance and market sentiment

Example: Buying shares of Reliance Industries on NSE.

### Debt Markets

- **What it is:** Lending money in exchange for interest
- **Returns:** Fixed interest + principal repayment
- **Risk:** Lower than equity, but subject to default risk

Example: Holding a 10-year Government of India bond.

</section>

<section class="slide">

### Derivatives Markets

- Contracts derived from an underlying asset
- Used for:
  - Hedging
  - Speculation
  - Arbitrage

Types:
- Futures
- Options
- Swaps

Example: A Nifty 50 futures contract.

</section>

<section class="slide">

### Banks

- Accept deposits
- Make loans
- Provide payment services

In India, banks are central to:
- Money markets
- Government securities
- Credit creation

Examples: SBI, HDFC Bank.

</section>

<section class="slide">

### Exchanges

- Organized platforms for buying and selling securities
- Ensure transparency, liquidity, and price discovery

Examples:
- India: NSE, BSE
- US: NYSE, NASDAQ

</section>

<section class="slide">

### Funds

- Pool money from multiple investors
- Invest across asset classes
- Provide diversification and professional management

Examples:
- Mutual funds
- ETFs (e.g., SBI ETF Nifty 50)

</section>

<section class="slide">

## Role of Regulators

### SEBI (Securities and Exchange Board of India)

- Regulates capital markets
- Enforces disclosure and transparency
- Protects investors

US equivalent: SEC.

</section>

<section class="slide">

### RBI (Reserve Bank of India)

- Central bank of India
- Controls monetary policy
- Regulates banks
- Oversees money markets and payment systems

US equivalent: Federal Reserve.

</section>

<section class="slide">

## 4. Takeaways

- **Equity** = ownership  
- **Debt** = lending  
- **Derivatives** = risk transfer or speculation  
- **Banks** = move and create money  
- **Exchanges** = enable trading and price discovery  
- **Funds** = pool and allocate capital  
- **Regulators** = keep the system stable (at least in theory)

A financial system is not just about money.  
It is about **coordination, incentives, and control under uncertainty**.

</section>

<section class="slide">

**Thank you!**

<div style="height:6rem;"></div>

**Any questions?**

</section>

</div>
