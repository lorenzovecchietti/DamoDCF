\newpage

# Terminal Value
A company's growth cannot continue indefinitely, and projecting cash flows forever is impractical. Therefore, we use a 'Terminal Value' to represent the firm's worth beyond its explicit forecast period. This value allows us to finalize the discount formula.

$$
    v=\sum_{t=1}^N \frac{CF_t}{(1+r)^t}+\frac{TV}{(1+r)^N}
$$

Three primary approaches exist for calculating Terminal Value:

1.  **Liquidation:** This method assumes the company's assets are sold off. It's suitable for businesses with limited competitive advantages or those heavily reliant on a single individual.
2.  **Stable Growth:** This approach assumes the company will grow at a constant rate in perpetuity.
3.  **Multiple:** This method applies a valuation multiple (e.g., to EBITDA). **Caution:** This approach is generally discouraged for fundamental valuation as it relies on relative valuation rather than intrinsic value.

## Stable Growth

This method posits that the company will grow at a constant, sustainable rate. A crucial condition for this assumption is that the stable growth rate must be lower than the overall economy's growth rate. This raises the question of how to estimate the economy's growth rate. A common proxy is the risk-free rate[^1].

$$
  g_{econ} \approx r_f
$$

The risk-free rate comprises expected inflation and the real interest rate, while economic growth consists of expected inflation and the real growth rate.

In the long run, the real growth rate generally cannot be lower than the real interest rate, as the increase in goods and services must be sufficient to cover the promised returns. While the real growth rate can be higher to compensate for risk-taking, this difference tends to narrow as economies mature. Given that some companies within the economy will still experience growth, assuming the extra growth comes from these companies is a prudent approach.

Determining the point at which a firm reaches stable growth involves considering several factors:

* **Size:** Particularly in relation to its operating market.
* **Current Growth Rate (Revenue):** High current growth is unlikely to be sustained indefinitely.
* **Differential Advantages & Barriers to Entry:** Stronger advantages and barriers suggest a longer period of higher growth.

A company in a stable growth phase typically exhibits characteristics of a mature business:

1.  $\beta \approx 1$ (Beta close to the market average)
2.  Lower cost of debt (Investment-grade credit rating, e.g., BBB or higher)
3.  Higher Debt Ratio (DR)

Finally, the growth rate's significance diminishes as the excess return (Return on Capital - Cost of Capital, or ROC - CoC) decreases. For most companies without long-term competitive advantages, the ROC will gradually converge towards the CoC. Under this scenario, the Terminal Value becomes less dependent on the growth rate, *g*.

$$
    \mathrm{TV=(EBIT_{n+1}(1-t))\frac{1-\frac{g}{ROC}}{CoC-g}}
$$

with:

 - $r_f=\mathrm{inflation+\mathbf{real}\ interest\ rate}$
 - $g=\mathrm{inflation+\mathbf{real}\ growth\ rate}$

In the long term, the real growth rate cannot be lower than the real interest rate, since the growth in goods/services has to be enough to cover the promised rate. In the long term, the real growth rate can be higher than the real interest rate, to compensate risk taking. However, as economies mature, the difference should get smaller and since there will be growth companies in the economy, it is prudent to assume that the extra growth comes from these companies.