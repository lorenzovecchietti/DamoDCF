\newpage

# Growth

Estimating growth requires careful consideration, as the compounding effect significantly impacts future cash flows. Additionally, different growth rates for various balance sheet items have distinct meanings.

\begin{figure}[ht]
\centering
\begin{tikzpicture}[node distance=2cm,auto]
    
% Define block styles
\tikzstyle{block} = [rectangle, draw, fill=black!20, text width=5em, text centered, rounded corners, minimum height=4em]

% Nodes
\node [block] (A) {Revenue Growth};
\node [block, below of=A] (B) {Operating Income Growth};
\node [block, below of=B] (C) {Net Income Growth};
\node [block, below of=C] (D) {EPS Growth};
\node [below right=0.45cm and 0.5cm of A, text=black!50, font=\scriptsize] (aa) {Fixed cost};
\node [below right=0.45cm and 0.5cm of B, text=black!50, font=\scriptsize] (bb) {Fixed interest expenditures};
\node [below right=0.45cm and 0.5cm of C, text=black!50, font=\scriptsize] (cc) {Buybacks};

% Arrow
\path[draw=black,solid,line width=1mm,fill=black, preaction={-triangle 90,thin,draw,shorten >=-1mm}] 
  ($(A.north)+(-1.5,0)$) -- ($(D.south)+(-1.5,0)$) 
  node[pos=0.5,left] {\rotatebox{90}{Higher Growth}};
\draw[->] (A) to[bend left=15] (aa);
\draw[->] (B) to[bend left=15] (bb);
\draw[->] (C) to[bend left=15] (cc);
\draw[->] (aa) to[bend left=15] (B);
\draw[->] (bb) to[bend left=15] (C);
\draw[->] (cc) to[bend left=15] (D);
\end{tikzpicture}
\caption{Difference in growth rates. Growth rates for revenues will be the lower. As fixed costs don't scale up with revenues, OI growth will be larger. Also interest expenditures are fixed, so net income growth will be even larger. Finally EPS is subject to firms buyback.}
\label{fig:growthrate}
\end{figure}


It's crucial to avoid using an incorrect growth rate, especially an analyst's EPS (Earnings Per Share) growth rate, when projecting revenue growth. Doing so will almost certainly lead to an overvaluation of the company.

## Historical Growth

Two primary methods for estimating growth involve analyzing historical data and considering analysts' forecasts.

However, relying solely on historical data is often a weak predictor of future growth. Growth is inherently more forward-looking than backward-looking.

Furthermore, historical growth rates are sensitive to the specific time period chosen for analysis. The selected period should align with the company's current phase and may not be relevant if the company has undergone significant operational changes.

Growth rates can be estimated using regression models or simple averages. Importantly, growth rates should always be calculated using the **geometric average** rather than the arithmetic average to accurately account for compounding.

### Arithmetic Growth Rate:

The arithmetic growth rate represents a constant rate of growth over a specific period. Given a series of values (revenues, EBITDA, EBIT, etc.) for $N$ years, denoted as ${v_i}_{0}^N$, the arithmetic growth rate ($g_a$) is calculated as:


$$
g_a = \frac{\sum_{i=1}^N \frac{v_i - v_{i-1}}{v_{i-1}}}{N-1}
$$


### Geometric Growth Rate:

The geometric growth rate, also known as the Compounded Annual Growth Rate (CAGR), explicitly considers the effect of compounding. Given a starting value ($s$) in the first year and an ending value ($e$) after $N$ years, the geometric growth rate ($g_g$) is:


$$
g_g = \left(1 + \frac{e - s}{s}\right)^{\frac{1}{N-1}} - 1
$$


The arithmetic and geometric growth rates will be equal only when the growth is perfectly steady. Greater volatility (higher standard deviation) in growth rates will lead to a larger divergence between the two, highlighting the importance of using the geometric growth rate for accuracy.

### Negative Earnings

Calculating growth rates based on historical earnings becomes problematic for companies experiencing losses. A negative denominator in the growth rate calculation will invariably result in a negative growth rate, even if the company has recently become profitable or is successfully reducing its losses.

While some may attempt to address this by using the absolute value of the denominator or using the last profitable year's earnings as the base, these methods are generally unreliable. It is often best to disregard these numbers and focus on alternative methods for estimating growth in such situations.

### Extrapolation Danger

When valuing a company experiencing rapid growth, it is unrealistic to project such high growth rates indefinitely into the future. Market limitations and the increasing difficulty of maintaining high growth as a company scales make this unsustainable.

Extensive research suggests that a typical stock's future growth is not strongly correlated with its past growth. While exceptions might exist for dominant companies like the "Magnificent Seven," this general principle holds.

The primary value of historical growth data lies in providing **context**. Significant deviations between estimated future growth and historical growth should prompt critical questions: What fundamental changes are driving this difference? If a company is undergoing a transformation, and the historical growth rate persists, why isn't the transformation yielding different results?

## Analyst Forecasts

The primary focus for analysts is on earnings per share (EPS) growth. Historical data suggests that analyst predictions tend to be slightly closer to actual EPS compared to time series predictions, although the difference is minimal.

These modest results occur even though analysts typically concentrate their efforts on a limited number of companies and their EPS.

"All-America Analyst" teams often exhibit marginally better performance due to:

* **Superior Information:** They may have access to more comprehensive or timely data.
* **Market Influence:** Their analyses, particularly sell ratings, can significantly impact market behavior as investors react to their recommendations.

**The Analysts' Problems:**

1.  **Tunnel Vision:** Analysts often specialize in a single industry sector, potentially limiting their broader perspective.
2.  **Lemmingitis:** There's a tendency for analysts to converge on similar opinions and forecasts.
3.  **Stockholm Syndrome:** Analysts may develop an affinity for the management of the companies they cover, leading them to prioritize protecting the company's interests over those of other stakeholders. This can explain why sell ratings have a stronger impact.
4.  **Factophobia:** Analysts may cling to a narrative or story, even when contradictory evidence or facts emerge.

## Fundamental Forecast

Fundamental forecasting relies on two key components:

* **How much are you investing?** (Reinvestment Rate)
* **How well are you investing?** (Return on Investment - ROI)

The specific metrics used to answer these questions vary depending on the earnings measure being considered, as outlined in Table 1. The expected growth rate is then calculated as the product of the reinvestment rate and the corresponding ROI.

Table 1: Reinvestment measure and return on investment for different earnings measures.

| Earnings Measure         | Reinvestment             | ROI            |
| :----------------------- | :----------------------- | :------------- |
| **EPS** | Retention Ratio          | ROE            |
| **Net Income from Op.** | Equity reinvestment rate | Non-cash ROE   |
| **OI** | Reinvestment Rate        | ROC            |

This approach is most effective when the return on capital (ROC) and margins are relatively stable, as is typical for mature companies. However, if the ROC changes independently of reinvestment (e.g., due to efficiency improvements), the company can experience growth (\textit{efficiency growth}) even if the product of the reinvestment rate and initial ROC is zero.

It's also crucial to recognize that generating value from growth requires earning a return on invested capital that exceeds the cost of that capital.

### EPS Growth Estimation

The **Retention Ratio** indicates the proportion of earnings that are reinvested back into the company:

## Efficiency Growth

The change in Return on Capital (ROC) or Return on Equity (ROE) significantly influences expected growth, even without new investments. The percentage change in ROC/ROE contributes directly to growth. This component is termed 'Efficiency Growth'.

$$
g_{\text{additional,efficiency}} = \frac{RO^*_{t+1} - RO^*_t}{R^*C_t}
$$

This efficiency growth rate, $g_{\text{additional,efficiency}}$, should be added to other growth estimations and calculated using the relevant return metric (ROE or ROC).

It's important to note that efficiency growth is generally sustainable only for a limited period.

> **Efficiency Growth Effect on OI Growth Rate**
>
> If the firm has a reinvestment rate of 0.5 and a ROC that increases (in the next year) from 0.08 to 0.1, the baseline growth of Operating Income (OI) will be only 5\%. However, due to the ROC increase (of 25\%), the actual growth rate will be 0.05 + 0.25 = 30\%.

## Estimating Growth in a General Case

How can we estimate growth when the return on equity or capital is changing? A three-step process can be employed:

1.  **Estimate Growth Rate:**
    1.  Estimate the total addressable market size. Begin with the current market size (considering geographical factors) and project its future growth.
    2.  Estimate the firm's potential market share. This will depend on the company's size, the size of its competitors, and any competitive advantages it possesses.

    After determining the target market share, apply an appropriate growth rate to reach it over time. Realistically, consider a higher growth rate in the initial stages, gradually slowing down as the company becomes larger.

2.  **Estimate Operating Margins:**
    1.  Set target operating margins. These margins are influenced by:
        * Unit economics
        * Economies of scale
        * Competition
    2.  Define the path to achieve these target margins. Some companies prioritize growth over immediate margin improvement, while others may need to focus on business model enhancements.

3.  **Estimate Capital Needed for Growth:** The Sales to Invested Capital ratio indicates how much capital is required to generate revenue increases.

    $$
    \text{Sales to Capital} = \frac{\text{Revenues}}{\text{BV Equity} + \text{BV Debt} - \text{Cash}} = \frac{\Delta \text{Revenues}}{\text{Reinvestment}}
    $$

    This ratio is often determined based on historical data. However, it's a simplified metric that doesn't account for:

    * The time lag between investments and revenue generation (e.g., in the pharmaceutical industry).
    * Potential economies of scale in capital deployment.

> **AirBnB**
> 
> #### Market Size \& Share
> The hospitality market (the relevant market even though AirBnB operates as an internet software platform) has an addressable size of \$650 billion. AirBnB's disruptive potential could expand this market to \$800 trillion. Given AirBnB's dominance model (network effects benefiting both hosts and guests), it could capture a 30\% market share. After payouts to homeowners, AirBnB retains 14\% of the booking value as revenue.
>
> #### Margins
> Based on competitors like Booking and Expedia, an estimated 25\% operating margin is reasonable.
>
>   | Year      | Bookings | Revenue | Growth   | Op. Margin |
>   | :-------- | :------- | :------ | :------- | :--------- |
>   | **LTM** | 26.5     | 3.71    |          |            |
>   | **1** | 37.68    | 5.28    | 42.2\%   | -10.0\%    |
>   | **2** | 52.75    | 7.39    | 40.0\%   | -3.0\%     |
>   | **3** | 71.21    | 9.97    | 35.0\%   | 5.0\%      |
>   | **4** | 96.14    | 13.46   | 35.0\%   | 4.0\%      |
>   | **5** | 124.98   | 17.50   | 30.0\%   | 7.5\%      |
>   | **6** | 156.22   | 21.87   | 25.0\%   | 10.0\%     |
>   | **7** | 187.47   | 26.25   | 20.0\%   | 13.0\%     |
>   | **8** | 215.59   | 30.18   | 15.0\%   | 17.0\%     |
>   | **9** | 230.68   | 32.30   | 7.0\%    | 21.0\%     |
>   | **10** | 235.29   | 32.94   | 2.0\%    | 25.0\%     |
>   | **Terminal** | 240.00   | 33.60   | 2.0\%    | 25.0\%     |
>
>   *Table: Grey cells represent fixed values: market share multiplied by market volume yields booking volume, the terminal operating margin is 25\%, and the first row contains known revenues.*
>
> #### Sales to Capital
> Historical data can be used to estimate the Sales to Capital value.
>
>   | Year      | $\Delta$ Revenue | Sales to Capital | Reinvestment |
>   | :-------- | :--------------- | :--------------- | :----------- |
>   | **LTM** |                  | 1.92             |              |
>   | **1** | 1.57             | 2.00             | 3.13         |
>   | **2** | 2.11             | 2.00             | 4.22         |
>   | **3** | 2.58             | 2.00             | 5.17         |
>   | **4** | 3.49             | 2.00             | 6.98         |
>   | **5** | 4.04             | 2.00             | 8.08         |
>   | **6** | 4.37             | 2.00             | 8.75         |
>   | **7** | 4.37             | 2.00             | 8.75         |
>   | **8** | 3.94             | 2.00             | 7.87         |
>   | **9** | 2.11             | 2.00             | 4.23         |
>   | **10** | 0.65             | 2.00             | 1.29         |
>   | **Term.** | 0.66             | 2.00             | 1.32         |
>
>   *Table Grey cells represent fixed values*
 With this data, it becomes possible to calculate key financial metrics such as EBIT, net EBIT, Invested Capital, and ROIC.

## Accounting Fixes

The accuracy of these calculations heavily relies on accounting practices. Therefore, it's crucial to address potentially misleading aspects in financial statements.

* **Normalization:** Adjusting for unusually positive or negative years to reflect a more typical performance.

* **Misclassification:** Reclassifying items like operating leases as debt and capitalizing R\&D expenses (treating them as assets) to avoid understating invested capital.

* **Write-Offs:** Recognizing that writing off a failed project reduces the book value of equity, which can artificially inflate the return on invested capital and growth rate. The poor investment decision should actually lead to a decrease in ROC.

* **Acquisitions:** Analyzing the 'goodwill'\footnote{Goodwill is an intangible asset that arises when one company acquires another for a price in excess of the net fair value of the acquiree's identifiable assets and liabilities.} recorded on the balance sheet. It's important to identify the portion of goodwill that represents a genuine competitive advantage versus the amount paid in excess of the fair value of the acquired business. The latter should be scrutinized.