\newpage

# Cost of Equity
The discount rate to be utilized is the cost of equity or the cost of capital. Once the right one\footnote{depending on the cash flow considered.} is chosen, it must be estimated.

- **Cost of capital** is the rate at which you would lend the money to the company. This depends on the credit history and on the risk of the company. This allows the computation of the \textit{default spread} with respect to the risk-free rate.
- **Cost of equity** is much more complicated to compute. It is the return that the investors expect to get for their investment.

The estimation of the right discount rate is the only element in the DCF framework that carries the risk concept. Both cost of capital and cost of equity increase if the risk is higher.

To get the risk adjusted discount rate you need:

- risk-free rate
- equity risk premium in the market
- relative risk of the company with respect to the other equity

## Uncertainties
The economic uncertainty is impossible to reduce ($\leftrightarrow$ estimation uncertainty can be reduced with more research). Markets and economies change over time unpredictably.

Uncertainties related to a single firm are *micro* (product release, competition...). Macro uncertainties are those related to the whole economy.

Most common uncertainties are 'continuous' (i.e., the exchange rate). But some risks are discrete (and unpredictable): regulations, nationalizations, wars... cannot be predicted. The continuous risk is well estimated, discrete one is not.

Models assume that the risk that should be rewarded is the risk perceived by the marginal investor who is assumed to be diversified. So it is just the economic, macro, continuous risk that should be incorporated into the cost of equity. **Not all risk counts**.

This is reflected by the market structure: institutional investors are well diversified and they are the ones that have an effect on pricing.

## Expected return models

Expected return models, like CAPM, calculate the return investors require, which is precisely the company's cost of equity (a component of its cost of capital).

### CAPM

CAPM is the model that assumes perfect diversification. It assumes no transaction cost and no private information (the price of the market is the right one, there is no concept of 'cheap' or 'expensive' equity). In the CAPM, the model portfolio is the one with every traded asset in the market $\rightarrow$ market portfolio. The higher or lower risk of a generic portfolio is given by the $\beta$ factor that multiplies the market risk premium.

$$
E(R)=R_f+\beta(R_m-R_f)
$$

### APM

In the APM the higher return of equities with respect to the risk-free rate is justified by the presence of multiple risk factors (micro and macro). Each risk factor is associated with a risk premium ($R_i-R_f$) and a sensitivity ($\beta$) of the portfolio to the specific risk factor.

$$
E(R)=R_f+\sum_i \beta_i (R_i-R_f)
$$

The difficulty of the APM model is that it requires users to quantify multiple factors.

There are a lot of alternatives to the CAPM and APM models:

\begin{tikzpicture}[
node distance=2cm,
input/.style={rectangle, draw=black!60, fill=black!5, rounded corners=.8ex, align=center, very thick},
example/.style={rectangle, draw=black!30,rounded corners=.8ex, align=center}]
% Nodes
\node[input] (start) [align=center] {Do you believe that \\ price makers are diversified?};
\node (yes1) [below of=start, align=center, yshift=0.5cm] {Yes};
\node (no1) [right of=yes1, align=center, xshift=5.5cm] {No};
\node[input] (yes2a) [below of=yes1, align=center, yshift=1cm] {Do you believe in price-based risk?};
\node (yes3a) [below of=yes2a, align=center, yshift=1cm] {Yes};
\node (no2a) [right of=yes3a, align=center, xshift=1.5cm] {No};
\node[example] (result1) [below of=yes3a, align=center, yshift=1cm] {CAPM};
\node[example] (result2) [below of=result1, align=center, yshift=1.4cm] {APM};
\node[example] (result3) [below of=result2, align=center, yshift=1.2cm] {Multi-factor\\models};
\node[example] (result4) [below of=no2a, align=center, yshift=1cm] {Accounting $\beta$s};
\node[example] (result5) [below of=result4, align=center, yshift=1.4cm] {CoD based models};
\node[input] (yes2b) [below of=no1, align=center, yshift=1cm] {Do you believe in price-based risk?};
\node (yes3b) [below of=yes2b, align=center, yshift=1cm] {Yes};
\node (no2b) [right of=yes3b, align=center, xshift=1.5cm] {No};
\node[example] (result11) [below of=yes3b, align=center, yshift=1cm] {Rel. price\\volatility};
\node[example] (result12) [below of=result11, align=center, yshift=1.1cm] {Proxy models};
\node[example] (result13) [below of=result12, align=center, yshift=1.35cm] {CAPM+};
\node[example] (result14) [below of=result13, align=center, yshift=1.35cm] {Implied CoC};
\node[example] (result15) [below of=no2b, align=center, yshift=1cm] {Rel. earnings\\volatility};
\node[example] (result16) [below of=result15, align=center, yshift=0.9cm] {Accounting ratio\\based models};

% Arrows
\draw[->] (start) -- (yes1);
\draw[->] (start) -- (no1);
\draw[->] (yes1) -- (yes2a);
\draw[->] (yes2a) -- (yes3a);
\draw[->] (yes2a) -- (no2a);
\draw[->] (yes3a) -- (result1);
\draw[->] (no2a) -- (result4);
\draw[->] (no1) -- (yes2b);
\draw[->] (yes2b) -- (yes3b);
\draw[->] (yes2b) -- (no2b);
\draw[->] (yes3b) -- (result11);
\draw[->] (no2b) -- (result15);
\end{tikzpicture}

## Inputs for Cost of Equity Estimation
### Risk-Free Rate

The parameter that is present in all these models is the risk-free rate. Hence, it is of paramount importance to estimate it in the best way possible.

For US stocks, the risk-free rate estimation is relatively easy. As the United States are considered reliable enough not to default anytime in the future, their TBill is the risk-free rate for US companies (whose earnings reports are in US dollars).

But what duration of the T-Bills is the right one to choose? Since the cash flows from the equities can persist forever, the right one should be the 30-years T-Bill. This leads to some difficulties down the road $\rightarrow$ it is better to use the 10-years T-Bills.

For a European company (whose earnings reports are in euros) which is the right risk-free rate? Each country's bonds has their rate.

And what about the evaluation of a company in a country which has a non-null default rate? It is possible to subtract from the bond rate a spread dependent on the rating of the country. There is a market where it is possible to buy an 'insurance' (Credit Default Swap) against the default risk. This happens for bond denominated in EUR or USD. When the country is not issuing a foreign-currency bond, an average spread of other countries with the same sovereign-rating should be use.

> **Indian companies risk-free rate**
> India has a local currency sovereign rating\footnote{Ratings are assigned for local currency bond and USD bonds.} of BAA3. The default spread over the risk-free rate for such rating is equal to 2.39\%. So the risk-free rate for Indian companies, considering that the yield to maturity on the 10-year bond is 7.18\%, is 7.18-2.39=4.78\%.

The only important element in evaluating risk-free rates is the currency we are using. The currency is like a unit of measure, we must be coherent to it.

#### Default spreads

To evaluate the default spread there are different ways:

- Compare the bond rate in USD, if the country issues it, with T-Bills. The difference is due to the default risk. The same approach is valid with EUR issued bonds compared with German's bond.
- Check the CDS market
- Average CDS market information to get the default spread associated with a rating

It is also possible to evaluate risk-free rate for currencies, $c$, whose government doesn't issue bonds using the following formula involving expected inflation $i$:
$$
  r_{f_c} = (1+r_{f_\$})\frac{1+i_c}{1+i_\$}
$$

### Equity Risk Premium
The equity risk premium measures the expected added return that the investor expects when investing in equities for their non-free risk nature. The problem is that this premium is not observable, it should be estimated with one of these methods:

- Historical ERP estimation
- Implied ERP estimation

#### Historical risk premium
In order to evaluate the equity risk premium, it's possible to resort to historical data. This data is highly irregular, and a meaningful time frame would be long enough that the data is not representative of the stock market. The other issue is that the standard deviation is really high because of the noisiness of the equity market.

Using an historical risk premium leads also to a contradiction: bad years lower the risk premium, but the investor wants a higher risk premium after those years as he sees the risk as higher.

Finally, there might be a survival bias error: the US market is the one that flourished the most, will still be it? Also, other market have a shorter data history $\rightarrow$ inaccurate.

##### Historical-Country Corrected Risk Premium
As said, many countries do not have a long equity market history. For those, it is possible to correct the US equity risk premium with the default spread of the country.

$$
  \mathrm{ERP}_i=\mathrm{ERP}_\mathrm{US}+\mathrm{DS}_i
$$

But actually one expects equities to be riskier than a government bond. So it is possible to choose a different path. Stocks are more volatile than bonds and that can be considered the results of having different risks. So we measure the two volatility and use them to correct the default spread to get the equity risk spread.

$$
  \mathrm{ERP}_i = \mathrm{ERP}_\mathrm{US}+\mathrm{DS}_i\frac{\sigma_i}{\sigma_{\mathrm{bond}_i}}
$$

But what is the equity risk premium of other AAA countries? It must be the same of the US one, else capitals could move towards the developed market with the higher ERP.

There are also countries that do not have ratings. In this case it is possible to resort the 'Political Risk Service' score and associate the score with a premium.

In case of a company operating in multiple countries it is possible to weight the ERP (as well as the country risk premium) with the geographical revenue distribution. The only problem of this approach is that other risk are not considered (i.e., facilities in emerging market and revenues in developed market)

> **Shell**
> Shell is selling oil in developed countries, but a lot of production is in Oman and Nigeria. There is a risk there that is not accounted for just using revenues for the ERP calculation. In this case is better to use the percentage of oil\&gas production by country.

When companies are particularly exposed to one risky country, another possible weighting is used: $\lambda$.
$$
  \lambda=\frac{\%_{\mathrm{domestic\ rev}}}{\%_{\mathrm{domestic\ rev}_{\mathrm{avg}}}}
$$

$\lambda$ can be then lowered or increased by:

- the usage of risk management products that mitigate country specific risk  $\rightarrow$ lower the $\lambda$
- the firm being of national interest $\rightarrow$ increase the $\lambda$

$\lambda=1$ means that you are exposed as the average company to the market risk, $\lambda<1$ lower risk than average, $\lambda>1$ higher risk than average.

#### Implied Equity Risk Premium
In this case we are trying to evaluate the ERP on the basis of the current market price: given how much the investors are paying for stocks, how much are they expecting? Obviously this is highly affected by age, gender, geographical regions\dots

Given:

- Price paid for the equity ($p$)
- Risk free rate ($r_f$)
- Cash flows to the investor in the previous year ($c_{-1}$) due to dividend and buybacks
- Growth expected by analysts $g$

Assuming that cash flows can keep that growth for 5 years and then will grow at the rate of the economy (at the risk-free rate), we can subdivide the equity risk premium from the risk-free rate:
$$
   \begin{cases}
        p=\underbrace{\sum_{i=1}^5\frac{(1+g)^i \cdot c_{-1} }{(1-r)^i}}_\mathrm{5-year \ constant \ growth}+\underbrace{\frac{\left(\left(1+g\right)^5 \cdot f_{-1}\right)\left(1+r_f\right)}{(1-r_f)(1+r)^5}}_\mathrm{constant\ risk-free\ growth\ forever}\\
        r=r_f+r_e
    \end{cases}
  \label{eq:forwarderp}
$$

The only two unknowns are the expected return, $r$, and the equity risk premium, $r_e$. With a numerical method is possible to move the system and get the equity risk premium expected given the current prices and the current cash flows to equity holders.

The big advantage of using implied risk premium is that it takes in consideration the market phase. During a market crash, the historical risk premium barely change as the weight of the current period is extremely low.

De facto, using implied risk premium is way more effective (positively correlated) in predicting the actual premium.

### Relative risk measures
$\beta$ is the main measure of the relative risk (the one associated with the stock) compared to the market.

**Regression** $\beta$ is typically computed with a regression. Stock returns are compared with market returns computing variance and covariance:

$$
  \beta_i=\frac{\mathrm{Cov}(r_i, r_m)}{\mathrm{Var}(r_m)}
  \label{eq:beta}
$$

Because of this definition, $\beta$ is always backward looking and extremely noisy.

**Relative Price Volatility** In this case we are looking at the total standard deviation of the prices of the equity and not just the portion that is due to the market.
$$
  \beta = \frac{\sigma_p}{\sigma_m}
$$

**Proxy model** For estimating $\beta$, a proxy model considers generic factors such as industry sector or company size and use those to select an appropriate $\beta$ that will be shared with all the companies that shares the same factors.

> **Practical Proxy Model**
> For instance, a large, stable company in the consumer goods sector might have a beta close to 1, indicating its movements closely track the market. Conversely, a smaller, more volatile biotech firm might have a beta greater than 1, reflecting its higher sensitivity to market fluctuations.


It is in general good to have a proxy-model-based approach at least to have a critical evaluation of the $\beta$ that you are using. Something to evaluate is:

- **Service or Product** How discretionary is this service/product? The more it is, the higher the $\beta$, like in the following cases:

  - Cyclical business
  - Luxury goods business
  - High prices goods business
  - Growth firms will
    
- **Operating Leverage** Companies with high fix costs will have higher betas. Scaling up will lead to lower advantages, like in the following cases:
    
  - Firms with high infrastructure need
  - Small and young firms
    
  The only problem with this approach is that it's difficult to split fixed and variable costs just looking at the balance sheet. Most of the time we'll have to assume that in the same sector the cost structure will be similar.
- **Financial Leverage** Debt level influence the $\beta$. You can move from the unlevered to the levered $\beta$, considering the tax discount effect, with:
  $$
    \beta_L=\beta_U\left(1+\frac{D}{E}\underbrace{(1-t)}_{tax}\right)
    \label{eq:betadebt}
  $$


**CAPM+** The proxy model approach is used often even with the classical CAPM. Instead of changing the $\beta$ analysts might do things like increase the cost of equity for small companies.

**Accounting Ratio Based Model** It is possible to use something like debt ratios or cash holdings.

$$
\Downarrow
$$

**Steps to compute $\beta$**

- Select the businesses in which the company is operating.
- Compute the regression $\beta$ for each company (and compute the average).
- Compute the unlevered $\beta$ removing the effect of (average) debt.
- (Compute the average $\beta$.)
- Weight the different $\beta$s with the different operating revenues for different sectors.
- Compute levered $\beta$

$$
  \boxed{
  \mathrm{CoE}=r_f+\beta_L r_e+\lambda r_p
  }
  \label{eq:coeb}
$$
