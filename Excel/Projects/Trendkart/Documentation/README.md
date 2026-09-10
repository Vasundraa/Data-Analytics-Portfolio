# TrendKart --- Profitability Leakage Analysis Dashboard

> **Excel Business Intelligence Project \| Fashion Retail \|
> Profitability Analysis**

TrendKart is an Excel-based business intelligence project developed to
investigate whether strong sales activity is translating into
sustainable profitability.

The project transforms transactional and master data into an interactive
management dashboard focused on the core business question:

> **Where is TrendKart losing potential profitability despite generating
> sales, and which business areas require management attention?**

The project is aligned with the supplied **TrendMart Business
Requirements Document (BRD)**, which requires analysis of sales,
profitability, products, categories, discounts, returns, stores,
regions, channels, customer segments, and relevant fashion attributes.

------------------------------------------------------------------------

## 1. Business Problem

TrendKart generates sales across products, stores, regions, customers,
and sales channels. Revenue alone is not sufficient to evaluate business
performance.

The analysis focuses on identifying situations where:

-   High sales are not accompanied by proportionate profit.
-   Discount levels are associated with weaker profitability.
-   Certain categories show unusually high return rates.
-   Store and regional performance differs in terms of sales and margin.
-   Channel mix influences the overall commercial picture.
-   Specific products or categories require further investigation.

The project follows the BRD principle that observed relationships should
be treated as **associations rather than proven causal effects**.

------------------------------------------------------------------------

## 2. Project Objectives

The dashboard aims to:

1.  Monitor overall sales, profit, profit margin, transaction volume,
    and returns.
2.  Identify high-performing and comparatively weak products and
    categories.
3.  Compare sales contribution with profitability.
4.  Investigate discount levels alongside profit margin.
5.  Identify return-rate patterns across categories.
6.  Compare regional performance using sales and profit margin.
7.  Compare Online and Offline sales-channel contribution.
8.  Provide interactive filtering for deeper management investigation.
9.  Convert analytical findings into evidence-based recommendations.

------------------------------------------------------------------------

## 3. Repository Structure

The following structure matches the final TrendKart project organization used in the GitHub repository.

``` text
Trendkart/
│
├── Dashboard/
│   └── Dashboard_Screenshot.png
│
├── Documentation/
│   ├── README.md
│   └── Business_Insights.pdf
│
└── Source/
    ├── Raw/
    │   └── TrendKart_Fashion_Enterprise_Dataset.xlsx
    │
    └── Cleaned/
        └── TrendKart_Fashion_Enterprise_Dataset_Cleaned.xlsx
```

  Folder              Purpose
  ------------------- -------------------------------------
  `Dashboard/`        Final dashboard screenshot
  `Documentation/`    README and business-insights report
  `Source/Raw/`       Original supplied dataset
  `Source/Cleaned/`   Cleaned analytical dataset

### Source File Handling

The repository keeps the data in two clearly separated folders:

- **Raw** — `TrendKart_Fashion_Enterprise_Dataset.xlsx` is the original source dataset.
- **Cleaned** — `TrendKart_Fashion_Enterprise_Dataset_Cleaned.xlsx` is the cleaned version used for analysis and dashboard development.

The raw dataset is retained for traceability, while the cleaned dataset is used for analytical work. Source records were not blindly deleted; data-quality issues were reviewed and handled according to the business requirements.

------------------------------------------------------------------------

## 4. Data Used

  ------------------------------------------------------------------------
  Dataset                            Approx. Records Business Use
  --------------------- ---------------------------- ---------------------
  Sales Transactions                           3,000 Sales, cost, profit,
                                                     discount, returns,
                                                     payment, channel and
                                                     quantity

  Customers                                      850 Customer demographics
                                                     and membership

  Products                                       250 Category, brand,
                                                     size, color, material
                                                     and product
                                                     attributes

  Stores                                         120 Store, region and
                                                     store-type analysis

  Employees                                      300 Employee/store
                                                     association

  Suppliers                                       90 Supplier context

  Data Quality Log                               --- Data-quality review
                                                     and validation
                                                     guidance
  ------------------------------------------------------------------------

**Analysis period:** April 2024 -- March 2025

### Key dataset relationships

-   `Customer_ID`
-   `Product_ID`
-   `Store_ID`
-   `Employee_ID`
-   `Supplier_ID`

------------------------------------------------------------------------

## 5. Data Preparation & Quality Handling

Data-quality review was an explicit BRD requirement.

The project reviewed duplicate identifiers, missing IDs, dates, numeric
values, inconsistent status/attribute values, negative-profit and
zero-quantity records, dataset relationships, and Return Status.

### Key observations

-   **3,000** sales transaction records.
-   **5 duplicate Invoice No values**, representing 10 transaction rows.
-   Duplicate records were not automatically deleted because duplicate
    identifiers do not by themselves prove invalid business events.
-   **6 transactions** have blank `Customer_ID`.
-   **5 transactions** have blank `Employee_ID`.
-   **5 transactions** have unmatched `Product_ID` values and therefore
    missing product/category attribution.
-   **57 transactions** have zero quantity and were retained for
    contextual review.
-   No negative-profit transactions were identified in the final sales
    data.
-   `Return Status` was reviewed using the available `Returned` /
    `Not Returned` definition.

Valid business events were not removed simply to improve dashboard
appearance.

------------------------------------------------------------------------

## 6. Executive KPIs

  ------------------------------------------------------------------------
  KPI                                          Value Definition
  --------------------- ---------------------------- ---------------------
  **Total Sales**                         ₹92,27,180 Total Sales Amount

  **Total Profit**                        ₹18,28,722 Total Profit

  **Profit Margin %**                         19.82% Total Profit ÷ Total
                                                     Sales

  **Total Orders**                             3,000 Transaction records
                                                     represented in
                                                     dashboard

  **Return Rate %**                            4.87% Returned transactions
                                                     ÷ total transactions
  ------------------------------------------------------------------------

The BRD also identifies Total Cost, Total Quantity Sold, Average
Transaction Value, Total Discount and Average Discount % as useful
measures. The current dashboard prioritizes the five cards above for the
executive view.

------------------------------------------------------------------------

## 7. Dashboard Visuals

### 1. How are sales and profit changing over time?

Monthly Sales Amount and Profit from April 2024 to March 2025.

**Purpose:** Identify stronger/weaker periods and compare revenue
activity with profitability.

### 2. Which products contribute most to sales and profit?

Top products compared using Sales Amount and Profit.

**Purpose:** Determine whether high revenue contribution is accompanied
by proportionate profit.

### 3. Are higher discounts associated with lower profitability?

Discount percentage compared with Profit Margin %.

**Purpose:** Investigate potential profitability leakage associated with
discount intensity.

**Interpretation:** The chart shows an association; it does not prove
that discounts cause lower profit.

### 4. Which categories contribute most to sales and profit?

Category-level Sales Amount and Profit comparison.

**Purpose:** Identify commercially strong categories while
distinguishing revenue from profitability.

### 5. Which categories have the highest return rates?

Category-level return-rate comparison.

**Purpose:** Identify categories requiring further investigation because
of high return incidence.

### 6. Which regions are more profitable relative to their sales?

Regional Sales Amount with Profit Margin %.

**Purpose:** Distinguish sales scale from profitability efficiency.

### 7. What share of sales comes from each channel?

Online versus Offline sales contribution.

**Purpose:** Understand channel concentration and commercial
contribution.

------------------------------------------------------------------------

## 8. Interactive Slicers

The completed dashboard contains six connected slicers:

-   **Membership**
-   **Brand**
-   **Store Type**
-   **Payment Mode**
-   **Material**
-   **Gender**

These filters allow management to investigate customer segments,
demographics, product characteristics, store formats, and payment
patterns.

Category, region, discount, returns and sales channel are represented
directly through dedicated visuals, avoiding unnecessary duplication.

------------------------------------------------------------------------

# 9. Key Business Findings

## Overall Performance

TrendKart generated:

-   **₹92.27 lakh** in sales
-   **₹18.29 lakh** in profit
-   **19.82%** overall profit margin
-   **3,000** transaction records
-   **6,100** units sold
-   **4.87%** return rate

## Product Performance

The highest-sales product in the current ranking is **GRT Jewellers
Sling Bag Olive**, generating approximately **₹4.83 lakh sales** and
**₹1.15 lakh profit**.

High sales should not automatically be interpreted as high
profitability.

## Category Performance

Top categories by sales:

1.  **Women Sarees** --- approximately ₹11.03 lakh
2.  **Handbags** --- approximately ₹9.94 lakh
3.  **Watches** --- approximately ₹9.38 lakh

## Returns

The overall return rate is approximately **4.87%**.

**Handbags** is a major return-rate outlier at approximately **28.29%**,
making it a priority for investigation.

The dashboard identifies the pattern but does not establish the cause.

## Discount & Profitability

    Discount   Profit Margin
  ---------- ---------------
          0%          28.45%
          5%          25.14%
         10%          21.52%
         15%          16.85%
         20%          12.84%
         25%           7.95%
         30%           3.95%

Profit margin declines from **28.45% at 0% discount** to **3.95% at 30%
discount**.

This is an observed **association**, not proof that discounting causes
lower profitability.

## Regional Performance

  Region                 Sales   Profit Margin
  -------------- ------------- ---------------
  South Zone 1     ₹44.63 lakh          19.74%
  South Zone 2     ₹25.55 lakh          19.55%
  South Zone 3     ₹22.09 lakh          20.28%

South Zone 1 contributes the highest sales, while South Zone 3 has the
highest profit margin despite the lowest sales among the three regions.

## Sales Channel Performance

-   **Offline:** approximately ₹60.49 lakh (**65.56%**)
-   **Online:** approximately ₹31.78 lakh (**34.44%**)

Channel margins are very similar, so the dashboard emphasizes sales mix
rather than a redundant channel-margin visual.

------------------------------------------------------------------------

# 10. Management Recommendations

### 1. Investigate Handbags Returns

Review return reasons, product quality, sizing/description accuracy,
customer expectations, and operational handling.

### 2. Review High-Discount Transactions

Investigate products, categories, stores and channels where high
discount levels coincide with weaker margins.

### 3. Protect Profitable High-Volume Products

Identify products combining strong sales and healthy profit and ensure
appropriate inventory, visibility, merchandising and promotional
support.

### 4. Investigate High-Sales / Low-Margin Areas

Review revenue leaders alongside profit and margin to identify potential
profitability leakage.

### 5. Study South Zone 3 Practices

Investigate product mix, store characteristics, customer mix and
commercial practices that may be associated with its stronger margin.

### 6. Validate Transaction Identifiers

The presence of duplicate invoice numbers should be validated before
using invoice numbers as the formal basis for order-count reporting.

### 7. Extend Customer and Product Analysis

Future analysis can expand into customer segments, employee
contribution, size, color, material, store targets and supplier context
where the data supports reliable conclusions.

------------------------------------------------------------------------

# 11. BRD Alignment

  -----------------------------------------------------------------------
  BRD Requirement                     Dashboard Coverage
  ----------------------------------- -----------------------------------
  Overall sales/profit/transaction    ✅ Covered
  performance                         

  Sales vs. profitability             ✅ Covered

  High-sales/low-profit products      ✅ Covered

  Category/product/brand performance  ✅ Covered

  Discount vs. profitability          ✅ Covered

  Return patterns                     ✅ Covered

  Store/region comparison             ✅ Covered

  Online vs. Offline performance      ✅ Covered

  Customer/membership analysis        🟡 Partially supported through
                                      slicers

  Size/color/material patterns        🟡 Partially supported through
                                      Material filtering

  Employee contribution               Not directly visualized

  Supplier context                    Not directly visualized

  Store target achievement            Not concluded; target-period
                                      alignment requires validation
  -----------------------------------------------------------------------

The dashboard follows the BRD requirement to prioritize management
decisions and avoid decorative or redundant visuals.

------------------------------------------------------------------------

# 12. Limitations & Assumptions

-   Duplicate invoice identifiers were identified and retained pending
    business validation.
-   Blank customer/employee identifiers remain part of the source
    transaction population.
-   Five transaction records have unmatched product master attributes
    and are excluded from product/category attribution where no valid
    match exists.
-   Return Rate depends on the available `Return Status` definition.
-   Discount-profitability relationships are described as associations,
    not causal effects.
-   Store target comparisons require target-period alignment validation.
-   Customer, employee and supplier analyses are not represented through
    dedicated dashboard visuals.
-   Predictive forecasting and machine learning are outside the current
    scope.

------------------------------------------------------------------------

# 13. Project Deliverables

-   [Dashboard Screenshot](../Dashboard/Dashboard_Screenshot.png)
-   [Business Insights Report](./Business_Insights.pdf)
-   [Cleaned
    Dataset](../Source/Cleaned/TrendKart_Fashion_Enterprise_Dataset_Cleaned.xlsx)
-   [Raw
    Dataset](../Source/Raw/TrendKart_Fashion_Enterprise_Dataset.xlsx)

------------------------------------------------------------------------

# 14. Tools & Skills Demonstrated

-   Microsoft Excel
-   Power Query / data preparation
-   PivotTables
-   PivotCharts
-   Excel formulas and calculated measures
-   Data cleaning and validation
-   Dataset relationships and lookups
-   KPI design
-   Interactive slicers
-   Business intelligence dashboard design
-   Profitability analysis
-   Return-rate analysis
-   Product/category analysis
-   Regional and channel analysis
-   Business insights and recommendations

------------------------------------------------------------------------

# 15. Conclusion

The TrendKart dashboard provides a consolidated management view of
sales, profitability and potential profitability leakage.

Its main value is that it moves beyond revenue reporting and helps
management answer:

> **Are strong sales translating into strong profitability?**

The analysis highlights discount-related margin patterns, high-return
categories, high-sales/low-margin products and regional differences in
profitability.

The dashboard is designed as a **decision-support tool**: it highlights
meaningful patterns and investigation priorities while clearly
separating observed associations from proven causal relationships.

------------------------------------------------------------------------

## Project Status

**Completed**

-   Data preparation and quality review
-   Dataset relationships
-   KPI calculations
-   Pivot-based analysis
-   Interactive dashboard
-   Connected slicers
-   Business insights
-   Management recommendations
-   Project documentation
