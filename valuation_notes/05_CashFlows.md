\newpage

# Cash Flows

The two most important cash flows to be computed are the one to the firm and the one to equity. The important quantities are:

* $\mathrm{EBIT}$, operating earnings
* $\mathrm{NI}$, net income, earnings after interest expenses
* $t$, the tax rate
* $i$, reinvestments for future growth
    1.  $i=\mathrm{cap.ex.-depreciation+change\ in\ noncash \ working\ capital}$
    2.  $i=\mathrm{EBIT}(1-i_\mathrm{rate})$
* $d$, net debt cash flow
    $d=\mathrm{new\ debt-repaid\ debt}$

| **FCF to the Firm** | **FCF to Equity** |
|---|---|
| $$ \mathrm{FCFF}=\mathrm{EBIT}(1-t)-i $$ | $$ \mathrm{FCFE}=\mathrm{NI}-i+d $$ |

## Measuring Earnings

Accurate earnings measurement relies on timely cash flow data, typically sourced from accounting records. However, these records may require updates to reflect current financial performance.

#### Updated numbers
To ensure data relevance, prioritize the use of trailing twelve months (TTM) figures. This approach offers a more current snapshot of a company's financial health compared to relying solely on historical data. While consistency is desirable, prioritizing up-to-date information is paramount. Even partial updates can significantly improve the accuracy of earnings analysis.

Manually compiling TTM figures is achievable using a company's 10-K (annual report) and 10-Q (quarterly report) filings, readily available through regulatory databases.

> __Update revenues in the third quarter__
> \vspace{-6pt}
> $$
  \mathrm{r_{updated}=r_{10K}-r_{first\ 3\ q.\ last\ year}+r_{first\ 3\ q.\ this\ year}}
$$


#### Normalize income
When looking at the numbers it is essential to consider if the TTM result is an outlier or not. We can compare to the firm's history and to other comparable firms (it is a shift in the market?). In the outlier is something that won't repeat in the future, then you can average that number in time (i.e., the last 5 years).

#### Clean accounting data
Until a few years ago (2019), operating leases were not treated as debt. But it is a contractual cash flow that should be treated as debt.
In some companies this is a big deal: air companies, retail business, restaurants\dots. Leases are the way there companies are contracting debt.
When converting a lease to debt we are also creating an asset (that the debt bought). The leases expenditures (OLE) have to be subtracted after the operating income computation that in turns must include the depreciation costs. So we have to adjust the operating income.

$$
  AOI = OI+OLE-d
$$

The other aspect to correct is the capitalization of R&D:

* Choose amortizable life (depending on sector)
* Collect R&D expenses for as long as the amortizable life
* Sum to CapEx the unamortized R&D for the period

The CAPEX is subtracted from the earnings to obtain FCF (both to equity and to firm)  so the cash flow results will be the same but the overview of what the company is doing is much better.

> __SAP R&D__
>
> Using data in the table below (numbers in million EUR), we can correct the operating income adding there year R&D expenditures (that we now must consider CapEx) and subtracting this year amortization of research assets.
> 
> $$
\mathrm{AOI=OI+R\&D_{exp}-R\&D_{amm}=OI+1020-903}
  \label{eq:OESAPADJ}
$$
> 
> The value of research asset is 2914.
>
> | Year    | R&D Exp | \% Unamortized | Unamortized | Y. Amortization |
> |---------|---------|----------------|-------------|-----------------|
> | Current | 1020.02 | 5/5=1          | 1020.02     | 0               |
> | -1      | 993.99  | 4/5=0.8        | 795.19      | 198.8           |
> | -2      | 909.39  | 0.6            | 545.63      | 181.88          |
> | -3      | 898.25  | 0.4            | 359.3       | 179.65          |
> | -4      | 969.38  | 0.2            | 193.88      | 193.88          |
> | -5      | 744.67  | 0.0            | 0.0         | 148.93          |
> 
> Table: Amortization of R&D expenses with 5-years life.


\begin{figure}[!ht]
  \begin{center}
\usetikzlibrary {positioning}
\usetikzlibrary {calc}
\begin{tikzpicture}[
final/.style={rectangle, draw=black!100,, text=white, fill=black!100, very thick, minimum size=7mm, rounded corners=.8ex},
input/.style={rectangle, draw=black!60, fill=black!5, very thick, minimum size=5mm, rounded corners=.8ex, align=center}
]
\begin{scope}[node distance=5mm]
%Nodes
\node[input]  (1) {Firm's\\history};
\node[input]  (2) [right=of 1] {Comparable\\Firms};
\node[input]  (3) [right=of 2] {Operating leases\\(Convert into debt)};
\node[input]  (4) [right=of 3] {R\&D Expenses\\(Convert into asset)};
\node[input]  (5) at ($(1)!0.5!(2)+(0,-1.5)$) {Normalize Earnings};
\node[input]  (6) at ($(3)!0.5!(4)+(0,-1.5)$) {Cleanse accounting data};
\node[final]  (7) at ($(5)!0.5!(6)+(0,-1.5)$) {\textbf{Measuring Earnings}};
\end{scope}

%Lines
\draw[->] (1.south) -- (5.north);
\draw[->] (2.south) -- (5.north);
\draw[->] (5.south) -- (7.north);
\draw[->] (6.south) -- (7.north);
\draw[->] (4.south) -- (6.north);
\draw[->] (3.south) -- (6.north);
\end{tikzpicture}
  \end{center}
  \caption{From report to actual earnings}\label{fig:report2earnings}
\end{figure}

### Cash flows of money losing companies
#### Money losing company
The correction that can be done is to average across the last 5 years. This can work only if:

- The company lost money only recently, averaging will yield a positive cash flow.
- The problem that caused the loss has been resolved/was unique.
- The business has not changed

#### Business Losses
Companies with negative OI, high CapEx or high debt payment. You can discount the projected FCFE to today, but the real question is: will the company survive?

If the company is very young you can estimate the profit margin from the mature companies in the same business and use it for long term estimations.

If the company has structural issues, look at the industry average and move towards that margin over time.

#### Recurring vs One-Time Expenses/Losses
If the company is incurring a one-time expense, you should not consider it. $\mathrm{OI = OI_{reported} + Expense}$. If it is recurring (even if not annual), you have to consider it - annualized.

If the loss is cyclical you can average the earnings across one cycle.

### Accounting malfeasance
There is obviously no easy way to be 100\% sure of this, but there are a few warning signals:

- In the operating cash flow section of the cash flow statement of the company, you can get the cash earnings of the company. In the income statement you get the accrual earnings. In a healthy company one is higher than the other alternatively year by year. If the accrual earning is always higher than cash earnings, than there is something wrong (the company may sell stuff for credit to increase the accrual earnings)
- Sudden changes in standard expense items (SG&A, R&D)
- Big difference between tax income and reported income

## Tax Rate
While the tax rate used for the cost of debt calculation is always the marginal rate, the one on OI is a bit more nuance.

The company's effective tax rate on the OI might be different from the country marginal tax rate. The reason for this is that the company might pay taxes in multiple countries or because of tax deferring.

On the other hand, the lower tax rate cannot be maintained forever. In initial years we start from effective tax rate, in the following years we go to the marginal one progressively.

## Free Cash Flow to Equity (FCFE)

Traditionally, FCFE analysis focused solely on actual dividends paid. However, this approach can be misleading because:

* Companies may retain earnings and pay out less than their potential dividends.
* Some companies might overpay dividends, potentially funding them through new equity issuance, leading to undervaluation.

A more accurate approach is to determine the **potential dividend** a company can afford, independent of its actual dividend policy.

### Potential Dividend Calculation

The potential dividend is derived from the residual cash flow available after necessary investments and debt obligations are met.

### Required Data from the Cash Flow Statement (CFS)

To calculate FCFE, we utilize the following data from the CFS:

* **Net Income (NI):** Found in the operating activities section of the CFS.
* **Capital Expenditures (CapEx):** Located in the investing activities section.
* **Depreciation:** Listed in the operating activities section.
* **Changes in Non-Cash Working Capital:** Found within the operating activities section.
* **Debt Repayment/New Debt:** Located in the financing activities section.

The sign of each item in the CFS indicates whether it represents a cash inflow or outflow.

Crucially, projecting the future evolution of these variables is essential for accurate FCFE estimation. A common and useful assumption is that a company will finance its investments with a constant debt-to-equity ratio (DR). This assumption simplifies the calculation by allowing us to determine the portion of capital expenditures and changes in non-cash working capital funded by equity investors.

This assumption leads to the following FCFE equation:

$$
\mathrm{FCFE = NI - (1 - DR) \times i}
\label{eq:FCFE-DR}
$$

> __Disney (1997) FCFE Estimations__
>
> * Net Income = 1533 mln
> * CapEx = 1746 mln
> * Depreciation = 1134 mln
> * Change in non-cash working capital = +477 mln
> * Debt-capital ratio = 0.2383
> * Dividends = 345 mln
> * 
> This allows the computation of the FCFE and a comparison with issued dividends.
> $$
  \mathrm{FCFE}=1533-(1-0.2383)*(1746+1134)+477*(1-0.2383)=704 \mathrm{mln}
$$
> The difference between the dividends payed out and the FCFE is wide.

But this would mean that increasing the DR, so financing investments from debt and not from equity, will lead to higher FCFE. But this is compensated from the levered $\beta$. Net effect will depend on the company.

\begin{figure}[h]
  \begin{center}
\tikzset{every picture/.style={line width=0.75pt}} %set default line width to 0.75pt
\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
%uncomment if require: \path (0,518); %set diagram left start at 0, and has height of 518

%Shape: Axis 2D [id:dp1962786249425823]
\draw [line width=1.5]  (38.5,121.03) -- (490.84,121.03)(65.78,0.7) -- (65.78,178.58) (483.84,116.03) -- (490.84,121.03) -- (483.84,126.03) (60.78,7.7) -- (65.78,0.7) -- (70.78,7.7)  ;
%Curve Lines [id:da39072828440378093]
\draw [color={rgb, 255:red, 74; green, 144; blue, 226 }  ,draw opacity=1 ][line width=3]    (69.23,121.03) .. controls (112.6,121.9) and (242.73,87.02) .. (277.43,69.58) .. controls (312.13,52.14) and (410.16,15.52) .. (479.56,53.89) ;
%Curve Lines [id:da8105400003228049]
\draw [color={rgb, 255:red, 126; green, 211; blue, 33 }  ,draw opacity=1 ][line width=3]    (70.09,144.58) .. controls (113.47,145.45) and (237.52,108.82) .. (278.3,93.13) .. controls (319.07,77.43) and (447.46,24.24) .. (485.63,121.9) ;
%Curve Lines [id:da5924613058776118]
\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=3]    (70.96,166.38) .. controls (114.34,167.25) and (229.72,168.99) .. (296.51,124.52) .. controls (363.31,80.05) and (394.54,44.3) .. (482.16,90.51) ;
%Straight Lines [id:da4453485760121325]
\draw    (308.66,20.67) -- (308.66,330.15) ;
%Shape: Rectangle [id:dp454629159611289]
\draw  [draw opacity=0][fill={rgb, 255:red, 253; green, 0; blue, 0 }  ,fill opacity=1 ] (65.76,218.7) -- (117.81,218.7) -- (117.81,244.86) -- (65.76,244.86) -- cycle ;
%Shape: Rectangle [id:dp436966417746977]
\draw  [draw opacity=0][fill={rgb, 255:red, 253; green, 0; blue, 0 }  ,fill opacity=0.36 ] (117.81,218.7) -- (230.58,218.7) -- (230.58,244.86) -- (117.81,244.86) -- cycle ;
%Shape: Rectangle [id:dp6225219298561413]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=0.39 ] (230.58,218.7) -- (308.66,218.7) -- (308.66,244.86) -- (230.58,244.86) -- cycle ;
%Shape: Rectangle [id:dp2191675972519771]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=0.65 ] (308.66,218.7) -- (378.06,218.7) -- (378.06,244.86) -- (308.66,244.86) -- cycle ;
%Shape: Rectangle [id:dp9344219376801177]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (378.06,218.7) -- (430.11,218.7) -- (430.11,244.86) -- (378.06,244.86) -- cycle ;
%Shape: Rectangle [id:dp4948287318512832]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=0.39 ] (430.11,218.7) -- (482.16,218.7) -- (482.16,244.86) -- (430.11,244.86) -- cycle ;
%Shape: Rectangle [id:dp19534305650850103]
\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=1 ] (65.76,244.86) -- (117.81,244.86) -- (117.81,271.02) -- (65.76,271.02) -- cycle ;
%Shape: Rectangle [id:dp004744387503075265]
\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.7 ] (117.81,244.86) -- (230.58,244.86) -- (230.58,271.02) -- (117.81,271.02) -- cycle ;
%Shape: Rectangle [id:dp6832285124663526]
\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.7 ] (230.58,244.86) -- (308.66,244.86) -- (308.66,271.02) -- (230.58,271.02) -- cycle ;
%Shape: Rectangle [id:dp6115025063739981]
\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.7 ] (308.66,244.86) -- (378.06,244.86) -- (378.06,271.02) -- (308.66,271.02) -- cycle ;
%Shape: Rectangle [id:dp02947556709399146]
\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.37 ] (378.06,244.86) -- (430.11,244.86) -- (430.11,271.02) -- (378.06,271.02) -- cycle ;
%Shape: Rectangle [id:dp41957959650580157]
\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0 ] (430.11,244.86) -- (482.16,244.86) -- (482.16,271.02) -- (430.11,271.02) -- cycle ;
%Shape: Rectangle [id:dp06010100452958822]
\draw  [draw opacity=0][fill={rgb, 255:red, 253; green, 0; blue, 0 }  ,fill opacity=1 ] (65.76,271.02) -- (117.81,271.02) -- (117.81,295.43) -- (65.76,295.43) -- cycle ;
%Shape: Rectangle [id:dp3154806246422521]
\draw  [draw opacity=0][fill={rgb, 255:red, 253; green, 0; blue, 0 }  ,fill opacity=1 ] (117.81,271.02) -- (230.58,271.02) -- (230.58,295.43) -- (117.81,295.43) -- cycle ;
%Shape: Rectangle [id:dp9116325840022357]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=0.39 ] (230.58,271.02) -- (308.66,271.02) -- (308.66,295.43) -- (230.58,295.43) -- cycle ;
%Shape: Rectangle [id:dp3271276805767924]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=0.65 ] (308.66,271.02) -- (378.06,271.02) -- (378.06,295.43) -- (308.66,295.43) -- cycle ;
%Shape: Rectangle [id:dp2890303069342248]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (378.06,271.02) -- (430.11,271.02) -- (430.11,295.43) -- (378.06,295.43) -- cycle ;
%Shape: Rectangle [id:dp34582843621161485]
\draw  [draw opacity=0][fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (430.11,271.02) -- (482.16,271.02) -- (482.16,295.43) -- (430.11,295.43) -- cycle ;
%Curve Lines [id:da35572646123119345]
\draw    (482.16,260.55) .. controls (495.62,265.63) and (487.05,283.83) .. (466.73,286.51) ;
\draw [shift={(464.81,286.71)}, rotate = 355.4] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
%Straight Lines [id:da6235872342341313]
\draw [line width=1.5]    (65.76,177.7) -- (65.76,308.26) ;
%Straight Lines [id:da7611613230767842]
\draw    (117.81,20.95) -- (117.81,295.43) ;
%Straight Lines [id:da29568633870748706]
\draw    (230.58,20.67) -- (230.58,330.15) ;
%Straight Lines [id:da957758117223005]
\draw    (378.06,20.67) -- (378.06,330.15) ;
%Straight Lines [id:da3031612522313216]
\draw    (430.06,20.02) -- (430.11,295.43) ;

% Text Node
\draw (430.06,20.02) node [anchor=north west][inner sep=0.75pt]  [font=\small] [align=left] {\textcolor[rgb]{0.29,0.56,0.89}{\textbf{Revenues}}};
% Text Node
\draw (431.75,49.33) node [anchor=north west][inner sep=0.75pt]  [font=\small] [align=left] {\textbf{\textcolor[rgb]{0.82,0.01,0.11}{FCFE}}};
% Text Node
\draw (429.3,128.47) node [anchor=north west][inner sep=0.75pt]  [font=\small] [align=left] {\textbf{\textcolor[rgb]{0.49,0.83,0.13}{Earnings}}};
% Text Node
\draw (63.78,189.58) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\textbf{Start-up}};
% Text Node
\draw (128.2,190.45) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\textbf{Young Growth}};
% Text Node
\draw (245.56,180.38) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\begin{minipage}[lt]{31.28pt}\setlength\topsep{0pt}
\begin{center}
\textbf{High}\\\textbf{Growth}
\end{center}

\end{minipage}};
% Text Node
\draw (318.29,180.38) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\textbf{Mature}\\\textbf{Growth}};
% Text Node
\draw (380.55,178.64) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\begin{minipage}[lt]{29.47pt}\setlength\topsep{0pt}
\begin{center}
\textbf{Mature}\\\textbf{Stable}
\end{center}

\end{minipage}};
% Text Node
\draw (430.2,189.58) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\begin{minipage}[lt]{31.75pt}\setlength\topsep{0pt}
\begin{center}
\textbf{Decline}
\end{center}

\end{minipage}};
% Text Node
\draw (5.53,224.1) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\textbf{Earnings}};
% Text Node
\draw (5.33,248.62) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\textbf{Reinvest.}};
% Text Node
\draw (243.49,250.13) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {\textcolor[rgb]{1,1,1}{less in \%}};
% Text Node
\draw (318.62,250.26) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {\textcolor[rgb]{1,1,1}{less in \%}};
% Text Node
\draw (428.2,250.26) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {Divestment};
% Text Node
\draw (22.93,275.78) node [anchor=north west][inner sep=0.75pt]  [font=\footnotesize] [align=left] {\textbf{FCFE}};
% Text Node
\draw (308.66,271.02) node [anchor=north west][inner sep=0.75pt]  [font=\scriptsize] [align=left] {{\scriptsize growth more}\\{\scriptsize than earnings}};
% Text Node
\draw (317.16,294.43) node [anchor=north west][inner sep=0.75pt]   [align=left] {\begin{minipage}[lt]{34.07pt}\setlength\topsep{0pt}
\begin{center}
{\scriptsize Buybacks}\\{\scriptsize +}\\{\scriptsize Dividends}
\end{center}

\end{minipage}};
% Text Node
\draw (244.08,294.93) node [anchor=north west][inner sep=0.75pt]   [align=left] {\begin{minipage}[lt]{33.68pt}\setlength\topsep{0pt}
\begin{center}
{\scriptsize Buybacks}
\end{center}

\end{minipage}};


\end{tikzpicture}
  \end{center}
  \caption{FCFE cycle. It is always important to understand in which phase the company is in and that the firm itself understands this.}
  \label{fig:fcfe_cycle}
\end{figure}