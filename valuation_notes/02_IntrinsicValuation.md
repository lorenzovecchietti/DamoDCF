\newpage
# Intrinsic Valuation

## Introduction

Intrinsic valuation is a method of valuing an asset based on its fundamental characteristics, such as its earnings, cash flows, and overall financial health. The core principle is that an asset's true value is determined by its ability to generate future cash flows. The greater the expected cash flow and the lower the uncertainty surrounding it, the higher the intrinsic value.

Currently, the most widely used technique for intrinsic valuation is the Discounted Cash Flow (DCF) analysis.

The fundamental equation for DCF analysis states that the intrinsic value of an asset, denoted as $V$, is the sum of all its expected future cash flows, discounted back to the present using a risk-adjusted discount rate.

$$V=\sum_{y=1}^{n} \frac{\mathrm{E}(CF_y)}{(1+r)^y}$$

Where:

* $V$ is the intrinsic value of the asset.
* $\mathrm{E}(CF_y)$ is the expected cash flow in year $y$.
* $r$ is the risk-adjusted discount rate, reflecting the riskiness of the cash flows.
* $n$ is the number of years in the projection period.

Alternatively, a more conservative approach involves using a subset of cash flows that can be estimated with higher certainty and discounting them at the risk-free rate. This results in the certainty equivalent cash flow (CE). Dividends are a common example of cash flows that might be treated as certainty equivalents. In this case, the valuation equation becomes:

$$V=\sum_{y=1}^{n} \frac{\mathrm{CE}(CF_y)}{(1+r_f)^y}$$

Where:

* $\mathrm{CE}(CF_y)$ is the certainty equivalent cash flow in year $y$.
* $r_f$ is the risk-free rate of return.

### Time Horizon

Both DCF equations require projecting cash flows for a specific number of years, $n$. While the lifespan of a bond is typically well-defined, estimating the lifespan of a company's equity presents a unique challenge, as it theoretically can exist indefinitely.

Despite this indefinite potential, it is possible to conclude the DCF analysis by incorporating the concept of stable growth. A company is considered mature when its growth rate stabilizes at a level that is sustainable in the long term, typically below the overall economic growth rate[^2].

[^2]: It is fundamentally impossible for a single company to consistently outpace the growth of the entire economy over an infinite period.

### Firm vs. Equity Valuation

The DCF model can be applied to value either the entire firm or just the equity portion. The key difference lies in the cash flows used and the discount rate applied.

* **Firm Valuation:** When valuing the entire firm, the relevant cash flow is the Free Cash Flow to the Firm (FCFF), which represents the cash flow available to all investors (both debt and equity holders). The appropriate discount rate in this case is the Weighted Average Cost of Capital (WACC), which reflects the overall risk of the firm's assets.

* **Equity Valuation:** When valuing only the equity, the relevant cash flow is the Free Cash Flow to Equity (FCFE), which represents the cash flow available to equity holders after all debt obligations and reinvestments are met. The appropriate discount rate here is the Cost of Equity, which reflects the riskiness of the company's equity.

Furthermore, the growth rates used in the projections must align with the chosen valuation approach. For firm valuation, the growth in operating earnings should be estimated, while for equity valuation, the growth in net income or Earnings Per Share (EPS) is required.

It's important to note that these growth rates are typically different. They tend to increase as you move from operating income to net income due to the impact of fixed costs like interest expenses.

## DCF Models

There are several variations of the DCF model, each focusing on a different definition of cash flow:

**Dividend Discount Model (DDM):** This model values equity based on the present value of its expected future dividends. The challenge with this approach is that dividend payouts are discretionary and determined by the company's management. A company might choose to retain cash for reinvestment or other purposes, resulting in lower or no dividends, even if it has the capacity to pay them.

**Free Cash Flow to Equity (FCFE) Model:** This model estimates the potential dividends a company could pay by calculating the cash flow available to equity holders after accounting for taxes, reinvestments, and debt payments. It provides a more comprehensive view of the cash flow available to shareholders than just the actual dividends paid.

**Free Cash Flow to Firm (FCFF) Model:** This model values the entire firm by discounting the cash flow available to all its investors (both debt and equity holders). It is often used as a starting point for equity valuation, where the value of debt is then subtracted to arrive at the equity value.

> **Example: DDM and Tech Companies**
> 
> Many technology companies, such as Google (now Alphabet), historically did not pay dividends, despite having the financial capacity to do so. These companies often prioritize reinvesting their earnings for growth. Applying a DDM model to such companies might lead to an undervaluation, as it doesn't capture the potential value creation from reinvested earnings.

|                | **DDM** | **FCFE** | **FCFF** |
|----------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Cash flow** | Dividends                                                                  | Potential dividends = FCFE                                                                                             | FCFF                                                                                                             |
| **Expected growth** | In equity income and dividends                                                 | In equity income and FCFE                                                                                           | In operating income and FCFF                                                                                     |
| **Discount rate** | Cost of equity                                                               | Cost of equity                                                                                                       | Cost of capital                                                                                                  |
| **Steady state** | When dividends grow at a constant rate forever                               | When FCFE grows at a constant rate forever                                                                         | When FCFF grows at a constant rate forever                                                                       |

Table: Summary of the different DCF approaches.

### The Process

The general process for conducting a DCF analysis involves the following steps:

1.  **Gather Data:** Collect historical and current financial data for the company being valued. This includes analyzing (1) profitability trends, (2) past growth rates, and (3) the capital expenditures required to support growth.
2.  **Analyze and Cluster Data:** Examine the historical data to identify different phases of the company's development and performance. This helps in understanding past trends and forming assumptions about the future.
3.  **Forecast the Future:** Project the company's future financial performance, including revenues, expenses, and investments.

If a company has historically maintained stable profit margins, forecasting its future performance primarily involves estimating its revenue growth. However, this is often not the case, as margins can fluctuate due to various factors.

A common approach to estimate future growth is based on the relationship between the percentage of revenue reinvested in growth ($i_\%$) and the return on capital ($r_{capital}$). The arithmetic relationship between these factors and the growth rate ($g_\%$) is given by:

$$g_\%=i_\% \times r_{capital}$$
\label{eq:growth-roc}

The challenge lies in accurately forecasting how these key quantities ($i_\%$ and $r_{capital}$) will evolve over the projection period.