# TrendKart --- Profitability Leakage Analysis Dashboard

## 1. Project Overview

**TrendKart Profitability Leakage Analysis** is an Excel-based business
intelligence project developed for fashion retail management.

The project transforms transactional and master data into an
**interactive management dashboard** focused on a central business
question:

> **Where is TrendKart losing potential profitability despite generating
> sales, and which business areas require management attention?**

The dashboard is designed around the requirements in the supplied
**TrendMart Business Requirements Document (BRD)**, with emphasis on
sales vs. profitability, product/category performance, discount-related
profitability patterns, returns, regional/store performance, channel
performance, and management decision support.

------------------------------------------------------------------------

## 2. Business Problem

TrendKart generates sales across products, stores, regions, customers,
and sales channels. However, revenue alone does not provide a complete
view of business performance.

The analysis therefore focuses on identifying situations where:

-   High sales are not accompanied by proportionate profit.
-   Discount levels are associated with weaker profitability.
-   Certain categories show unusually high return rates.
-   Store/region performance differs in terms of sales and margin.
-   Channel mix influences the overall commercial picture.
-   Specific products or categories require further investigation.

The project follows the BRD principle that observed relationships should
be treated as **associations rather than proven causal effects**.

------------------------------------------------------------------------

## 3. Project Objectives

The dashboard aims to:

1.  Monitor overall sales, profit, profit margin, transaction volume,
    and quantity.
2.  Identify high-performing and comparatively weak products/categories.
3.  Compare sales contribution with profitability.
4.  Investigate discount levels alongside profit margin.
5.  Identify return-rate patterns across categories.
6.  Compare regional performance using sales and profit margin.
7.  Compare Online and Offline sales-channel contribution.
8.  Provide interactive filtering for deeper management investigation.
9.  Convert analytical findings into evidence-based recommendations.

------------------------------------------------------------------------

## 4. Data Used

The workbook contains the following major datasets:

  -----------------------------------------------------------------------
  Dataset                             Business Use
  ----------------------------------- -----------------------------------
  **Sales_Transactions**              Sales, cost, profit, discount,
                                      return, payment, channel, quantity
                                      and transaction analysis

  **Products**                        Product, category, brand, size,
                                      color, material and pricing
                                      attributes

  **Customers**                       Customer demographics and
                                      membership information

  **Stores**                          Store, region and store-type
                                      information

  **Employees**                       Employee/store association

  **Suppliers**                       Supplier context
  -----------------------------------------------------------------------

### Current transaction scope

-   **3,000 sales transaction records**
-   **250 products**
-   **850 customers**
-   **120 stores**
-   Analysis period: **April 2024 -- March 2025**

------------------------------------------------------------------------

## 5. Data Preparation & Quality Handling

The BRD requires data-quality issues to be investigated before analysis.
The project therefore checked transaction identifiers, missing
attributes, data types, relationships, return status, quantity and
profitability fields.

Key observations from the final workbook:

-   **5 duplicate Invoice No values** were identified, representing **10
    transaction rows**.
-   These records were **not automatically deleted**, because the BRD
    requires valid business events to be preserved unless a documented
    reason supports removal.
-   **6 transactions have blank Customer_ID values**.
-   **5 transactions have blank Employee_ID values**.
-   **5 sales transactions do not match a Product_ID in the Products
    table**, resulting in missing product/category attributes for those
    records.
-   **57 transactions have zero quantity** and were retained for
    contextual review rather than automatically removed.
-   **No negative-profit transactions** were found in the current sales
    data.
-   Return Status was checked using the available `Returned` /
    `Not Returned` definition.

### Treatment principle

Data-quality observations were retained or excluded from specific
visuals only where appropriate. The source transaction population was
not arbitrarily reduced simply to improve dashboard appearance.

------------------------------------------------------------------------

## 6. Analytical Methodology

The project follows this workflow:

**Business Requirements → Data Inspection → Data Cleaning & Validation →
Dataset Relationships → Calculated Measures/KPIs → PivotTables →
PivotCharts → Interactive Slicers → Dashboard → Business Insights**

Related datasets were connected using common identifiers such as:

-   `Customer_ID`
-   `Product_ID`
-   `Store_ID`
-   `Employee_ID`

Product, customer and store attributes were used to enrich
transaction-level analysis.

------------------------------------------------------------------------

## 7. Executive KPIs

The dashboard displays five primary KPI cards:

  ------------------------------------------------------------------------
  KPI                                  Current Value Definition
  --------------------- ---------------------------- ---------------------
  **Total Sales**                      ₹9,227,179.96 Total Sales Amount

  **Total Profit**                     ₹1,828,721.60 Total Profit

  **Profit Margin %**                         19.82% Total Profit / Total
                                                     Sales

  **Total Orders**                             3,000 Transaction records
                                                     represented in the
                                                     dashboard

  **Return Rate %**                            4.87% Returned transactions
                                                     / total transactions
  ------------------------------------------------------------------------

### KPI note

The BRD also identifies Total Cost, Total Quantity Sold, Average
Transaction Value, Total Discount and Average Discount % as useful
measures. The current dashboard prioritizes the five KPI cards above;
supporting measures remain available in the analytical workbook where
applicable.

------------------------------------------------------------------------

## 8. Dashboard Visuals

### 1. How are sales and profit changing over time?

Monthly sales and profit trend from April 2024 to March 2025.

**Purpose:** Identify stronger/weaker periods and compare revenue
activity with profitability.

### 2. Which products contribute most to sales and profit?

Top-product comparison using Sales Amount and Profit.

**Purpose:** Identify products that contribute strongly to revenue and
determine whether their profit contribution is proportionate.

### 3. Are higher discounts associated with lower profitability?

Discount percentage compared with Profit Margin %.

**Purpose:** Investigate profitability leakage associated with discount
intensity.

**Interpretation rule:** The chart identifies an association; it does
not establish that discounts cause lower profit.

### 4. Which categories contribute most to sales and profit?

Category-level Sales Amount and Profit comparison.

**Purpose:** Identify commercially strong categories and compare revenue
with profit contribution.

### 5. Which categories have the highest return rates?

Category return-rate analysis.

**Purpose:** Identify categories requiring investigation because of
comparatively high return incidence.

### 6. Which regions are more profitable relative to their sales?

Regional Sales Amount with Profit Margin %.

**Purpose:** Distinguish high sales from high profitability and identify
regions with stronger/weaker margins.

### 7. What share of sales comes from each channel?

Online vs Offline sales contribution.

**Purpose:** Understand channel concentration and commercial
contribution.

------------------------------------------------------------------------

## 9. Interactive Slicers

The final dashboard includes:

-   **Membership**
-   **Brand**
-   **Store Type**
-   **Payment Mode**
-   **Material**
-   **Gender**

These filters allow management to investigate whether performance
patterns change across customer segments, product characteristics, store
formats, payment methods, and customer demographics.

The slicers are connected to the relevant PivotTables so that the
dashboard can be explored interactively.

------------------------------------------------------------------------

## 10. Key Business Findings

### Overall performance

TrendKart generated:

-   **₹92.27 lakh in sales**
-   **₹18.29 lakh in profit**
-   **19.82% overall profit margin**
-   **3,000 transaction records**
-   **6,100 units sold**
-   **4.87% return rate**

### Product performance

The highest-sales product is **GRT Jewellers Sling Bag Olive**,
generating approximately **₹483,225.47** in sales and **₹114,878.08** in
profit.

The product comparison demonstrates that high sales should not
automatically be interpreted as high profitability.

### Category performance

The leading categories by sales are:

1.  **Women Sarees --- ₹1,103,017.82**
2.  **Handbags --- ₹994,021.98**
3.  **Watches --- ₹937,502.18**

Among the larger categories, **Women Dresses** has a comparatively lower
margin of about **17.14%**, indicating an area worth investigating
rather than concluding that the category is inherently underperforming.

### Returns

**Handbags** has the highest category return rate at approximately
**28.29%**, substantially above the overall transaction return rate of
**4.87%**.

This is a strong investigation priority because return incidence is
concentrated rather than evenly distributed across categories.

### Discounting

Profit margin declines as the displayed discount levels increase:

-   0% discount: **28.45%**
-   10% discount: **21.52%**
-   20% discount: **12.84%**
-   30% discount: **3.95%**

This is an **observed association** and should not be presented as proof
that discounting causes lower profitability.

### Regional performance

**South Zone 3** has the highest regional profit margin at approximately
**20.28%**, despite having the lowest sales among the three regions.

This demonstrates why management should evaluate **sales and
profitability together**.

### Channel performance

-   **Offline:** 65.55% of sales
-   **Online:** 34.45% of sales

Profit margins are very similar across channels, so the key insight is
**sales mix/concentration rather than a major channel-margin gap**.

------------------------------------------------------------------------

## 11. Management Recommendations

### 1. Investigate high-return categories

Prioritize **Handbags** for deeper review of return reasons, product
quality, sizing/description accuracy, customer expectations, and
operational handling.

### 2. Review discount strategy

Investigate products/categories/stores where high discount levels
coincide with weaker margins. The objective should be to understand
whether discount intensity is commercially justified.

### 3. Protect high-revenue products with healthy margins

Identify products that combine strong sales with strong margin and
ensure they receive appropriate inventory, merchandising and promotional
attention.

### 4. Investigate high-sales/low-margin areas

Revenue leaders should be reviewed alongside profit and margin to
identify potential profitability leakage.

### 5. Learn from South Zone 3

South Zone 3 demonstrates that lower sales volume can still produce the
strongest margin. Management can investigate which product mix, customer
mix, store characteristics or commercial practices are associated with
this outcome.

### 6. Maintain channel balance

Offline contributes the majority of sales, while Online remains a
substantial secondary channel. Channel-level profitability should
continue to be monitored as the sales mix changes.

------------------------------------------------------------------------

## 12. BRD Alignment

  ------------------------------------------------------------------------
  BRD Requirement                      Dashboard Coverage
  ------------------------------------ -----------------------------------
  Overall                              **Covered** through KPIs and trend
  sales/profit/transactions/quantity   analysis

  Sales vs profitability               **Covered**

  High-sales/low-profit products       **Covered**

  Category/product/brand performance   **Covered**

  Discount vs profitability            **Covered**

  Return patterns                      **Covered** through category
                                       return-rate analysis

  Store/region comparison              **Covered** through regional
                                       analysis and Store Type filtering

  Online vs Offline performance        **Covered**

  Customer/membership analysis         **Partially supported** through
                                       Membership/Gender slicers; no
                                       dedicated customer chart

  Size/color/material patterns         **Partially supported** through
                                       Material filtering; no dedicated
                                       attribute chart

  Employee contribution                **Not directly visualized**

  Supplier context                     **Not directly visualized**

  Store target achievement             **Not concluded**, because
                                       target-period alignment requires
                                       validation
  ------------------------------------------------------------------------

The dashboard follows the BRD requirement to prioritize management
decisions and avoid decorative or redundant visuals.

------------------------------------------------------------------------

## 13. Limitations & Assumptions

-   Duplicate invoice identifiers were identified and retained pending
    business validation.
-   Blank customer/employee identifiers remain part of the source
    transaction population.
-   Five transaction records have unmatched product master attributes
    and are excluded from product/category attribution where no valid
    match exists.
-   Return Rate depends on the available `Return Status` definition.
-   Relationships between discounts and profitability are described as
    associations, not causal effects.
-   Store target comparisons should only be made after validating
    target-period alignment.
-   Customer, employee and supplier analyses are not represented as
    dedicated dashboard visuals.
-   Predictive forecasting and machine learning are outside the current
    scope.

------------------------------------------------------------------------

## 14. Repository Structure

A recommended GitHub repository structure is:

``` text
TrendKart-Excel-Dashboard/
│
├── README.md
├── Trendkart_Dashboard(2).xlsx
├── TrendKart_Business_Insights.pdf
│
└── assets/
    └── dashboard-screenshot.png
```

------------------------------------------------------------------------

## 15. Tools & Skills Demonstrated

-   Microsoft Excel
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

## 16. Conclusion

The TrendKart dashboard provides a consolidated management view of
sales, profitability and potential profitability leakage.

Its main value is that it moves beyond revenue reporting and helps
management ask:

> **Are strong sales translating into strong profitability?**

The dashboard highlights areas requiring further investigation,
particularly discount-related margin patterns, high-return categories,
high-sales/low-margin products and regional differences in
profitability.

The analysis is designed to support **evidence-based management
decisions**, while clearly separating observed patterns from unsupported
causal conclusions.
