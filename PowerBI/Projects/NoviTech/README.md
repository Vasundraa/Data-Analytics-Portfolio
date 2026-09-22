# Novitech Manufacturing Analytics -- Power BI

## Project Overview

**Novitech Manufacturing Analytics** is an end-to-end Power BI business
intelligence project developed to give management a consolidated view of
manufacturing performance, quality, operational efficiency, cost
exposure, procurement, supplier performance, raw-material dependency,
and workforce performance.

Novitech Manufacturing operates across multiple plants and produces
different products using raw materials purchased from external
suppliers. The Business Requirements Document (BRD) identified a key
business challenge: operational and procurement information existed
across different areas, making it difficult for management to understand
where efficiency was being lost, where cost exposure existed, and which
production or supply-chain factors required attention.

This project converts those business requirements into an interactive
**seven-page management dashboard** that allows users to move from an
overall business view into production, quality, cost, procurement,
supply-chain, and operator-level analysis.

The dashboard is designed around business questions rather than simply
presenting numbers. Each page helps management understand a particular
part of the manufacturing process and then move naturally to the next
question.

------------------------------------------------------------------------

## Business Problem

The central business problem identified in the BRD was the lack of a
centralized view of operational and financial performance.

Management needed visibility into:

-   Production output and production patterns
-   Plant and product performance
-   Defective production and quality losses
-   Downtime and operational efficiency
-   Energy consumption and energy efficiency
-   Product cost exposure
-   Procurement spending
-   Supplier lead time and delivery delays
-   Raw-material cost and dependency
-   Operator and shift performance

The overall business question addressed by the project is:

> **Where is Novitech Manufacturing losing operational efficiency and
> carrying financial or supply-chain exposure, and what production or
> supply-chain factors are contributing to those risks?**

------------------------------------------------------------------------

## Project Objectives

The dashboard was developed to support the following objectives defined
in the BRD:

-   Measure production output and production activity.
-   Compare production performance across plants, products, operators,
    and shifts.
-   Identify areas with higher defective production.
-   Analyze downtime and operational time loss.
-   Understand total energy consumption and energy consumed per unit.
-   Analyze procurement spending and spending concentration.
-   Compare supplier lead time, delay rate, order volume, and purchasing
    spend.
-   Understand product unit-cost exposure.
-   Provide potential price/margin context using available product
    information.
-   Estimate defect-related cost exposure using product unit cost.
-   Analyze raw-material standard cost and product-material
    dependencies.
-   Identify materials shared across multiple products.
-   Compare operator and shift performance.
-   Give management a connected view that can be used to identify areas
    requiring further investigation.

------------------------------------------------------------------------

# Work Completed

## 1. Data Preparation and Validation

The project included data preparation in line with the BRD requirements.

The work included:

-   Validating data types.
-   Reviewing null and blank values.
-   Checking business identifiers and duplicate records.
-   Standardizing categorical values where required.
-   Validating dates.
-   Reviewing quantity, cost, price, downtime, energy, lead-time, and
    related fields.
-   Checking values for consistency before analysis.
-   Handling blank shift values so that production analysis and shift
    comparisons could reconcile correctly.
-   Reviewing procurement delay values and ensuring delayed-order
    analysis used the correct representation in the source data.

The cleaned data was then used for the business analysis and dashboard
development.

------------------------------------------------------------------------

## 2. Business Analysis and KPI Development

The project includes operational, quality, efficiency, procurement,
financial-context, and supply-chain KPIs required by the BRD.

### Production and Operational KPIs

-   Total Production
-   Total Production Runs
-   Total Defects
-   Defect Rate
-   Total Downtime Hours
-   Average Downtime per Run
-   Total Energy
-   Energy per Unit

### Procurement KPIs

-   Total Purchase Orders
-   Total Procurement Spend
-   Delayed Orders
-   Delay Rate
-   Average Lead Time

### Financial Context Measures

-   Potential Unit Margin
-   Estimated Defect Cost
-   Estimated Production Cost
-   Potential Production Value

### Raw Material KPIs

-   Total Raw Materials
-   Average Material Standard Cost
-   Products with Material Dependencies
-   Material Dependencies
-   Critical Materials

For this project, a **critical material** is treated as a material used
by more than one product. This indicates shared product dependency; it
is not automatically classified as an actual supply shortage or
confirmed high-risk material.

### Operator KPI

-   Total Operators

Existing production, defect, downtime, and energy measures are reused to
provide operator-level performance views.

------------------------------------------------------------------------

# Dashboard Structure

The final dashboard contains **seven analytical pages**, each with a
specific business purpose.

------------------------------------------------------------------------

## Page 1 -- Executive Overview

### Purpose

Provide management with a high-level view of overall manufacturing
performance before moving into detailed analysis.

### Key KPIs

-   Total Production
-   Total Defects
-   Defect Rate
-   Total Downtime
-   Total Energy

### Analysis Covered

-   Production trend
-   Production by plant
-   Production by product
-   Plant defect-rate comparison
-   Top operator production

### Business Story

The Executive Overview answers:

> **What is happening overall?**

It establishes the scale of production and highlights the major
operational signals that require deeper investigation.

The page acts as the starting point for the rest of the dashboard.

------------------------------------------------------------------------

## Page 2 -- Production & Plant Performance

### Purpose

Understand where production is happening and how production is
distributed across plants, products, and shifts.

### KPIs

-   Production Output
-   Production Runs
-   Defective Units
-   Defect Rate
-   Downtime Hours

### Analysis Covered

#### Production Trend

**Question:** How is production output changing over time?

A time-based view is used to identify changes and patterns in production
volume.

#### Plant Comparison

**Question:** How does production output compare across plants?

This identifies where production volume is concentrated.

#### Product Category Production

**Question:** How is production distributed across product categories?

This shows which product categories contribute more to overall output.

#### Plant Output and Quality

**Question:** How do plant output and quality performance compare?

Production volume is considered together with defect rate to identify
plants that may require closer operational review.

#### Shift Production

**Question:** How is production distributed across shifts?

This shows how the overall production workload is distributed among
shifts.

### Business Story

The page moves from:

> **How much are we producing?**

to:

> **Where is that production coming from?**

and then:

> **Does higher production also come with acceptable quality and
> balanced shift contribution?**

------------------------------------------------------------------------

## Page 3 -- Quality & Operational Efficiency

### Purpose

Understand quality losses, downtime, and energy usage.

The BRD emphasizes that high production volume alone does not
necessarily mean efficient manufacturing. Production therefore needs to
be considered together with defects, downtime, and energy consumption.

### KPIs

-   Total Defects
-   Defect Rate
-   Total Downtime Hours
-   Average Downtime per Run
-   Energy per Unit

### Analysis Covered

#### Defect Trend

**Question:** How are defective units changing over time?

This identifies changes in quality losses across the production period.

#### Defects by Product Category

**Question:** Which product categories have the most defective units?

This identifies where defective production is concentrated.

#### Downtime by Plant

**Question:** Which plants experience the most downtime?

This identifies plants associated with higher operational time loss.

#### Energy Trend

**Question:** How is energy consumption changing over time?

This provides visibility into overall energy usage patterns.

#### Energy per Unit

**Question:** Which product categories use more energy per unit?

Energy per unit provides a more comparable view across categories with
different production volumes.

### Business Story

The page moves from:

> **Are we producing?**

to:

> **Are we producing efficiently?**

It helps management examine three important forms of operational loss or
exposure:

-   Quality loss
-   Time loss
-   Energy usage

------------------------------------------------------------------------

# Page 4 -- Finance & Cost Analysis

## Purpose

Provide financial and cost context using the manufacturing and
procurement information available in the dataset.

### Important Financial Limitation

The dataset does **not** contain actual sales transactions.

Therefore:

-   Actual revenue cannot be calculated.
-   Actual profit cannot be calculated.
-   Actual discounts, returns, taxes, and customer-level sales are not
    available.
-   Potential production value is not actual revenue.
-   Potential unit margin is not actual profit.
-   Estimated defect cost is a cost-exposure estimate, not confirmed
    scrap or rework cost.
-   Estimated production cost is a comparison context and not a formal
    accounting COGS calculation.

These limitations are explicitly respected throughout the dashboard.

### Analysis Covered

#### Procurement Spend Trend

**Question:** How is procurement spending changing over time?

Shows changes in purchasing expenditure across the available
purchase-order period.

#### Potential Value vs Estimated Production Cost

**Question:** How does potential value compare with estimated cost by
product category?

This provides planning-oriented context using target price and product
unit cost.

#### Estimated Defect Cost

**Question:** Which product categories have the highest estimated defect
cost?

This estimates the product-cost exposure associated with defective
quantities.

#### Supplier Procurement Spend

**Question:** Which suppliers account for the highest procurement spend?

This identifies where purchasing expenditure is concentrated.

#### Delayed Supplier Orders

**Question:** Which suppliers have the most delayed orders?

This connects purchasing activity with delivery reliability.

### Business Story

The page moves from:

> **How much are we spending?**

to:

> **Where is the spending concentrated?**

and then:

> **Where do production defects create additional cost exposure?**

The analysis is intended for business context and management review, not
as a replacement for accounting or financial statements.

------------------------------------------------------------------------

# Page 5 -- Procurement & Supplier Performance

## Purpose

Understand purchasing activity and supplier delivery performance.

### KPIs

-   Purchase Orders
-   Procurement Spend
-   Delayed Orders
-   Delay Rate
-   Average Lead Time

### Key Results

The completed dashboard shows:

-   **1,600 Purchase Orders**
-   **171 Delayed Orders**
-   **10.69% Delay Rate**

### Analysis Covered

#### Supplier Lead Time

**Question:** Which suppliers have the longest average lead time?

Shows how long suppliers typically take to deliver orders.

#### Supplier Delay Rate

**Question:** Which suppliers have the highest delay rate?

Shows delivery reliability differences between suppliers.

#### Procurement Spend Trend

**Question:** How is procurement spend changing month by month?

Shows purchasing expenditure over time.

#### Supplier Spend

**Question:** Which suppliers have the highest procurement spend?

Identifies purchasing concentration.

#### Supplier Lead Time vs Delay Rate

**Question:** How do supplier lead time and delay rate compare?

Brings supplier speed and delivery reliability together for review.

### Business Story

The page moves through:

> **How quickly do suppliers deliver?**

→

> **How reliable are they?**

→

> **How much are we spending?**

→

> **Which suppliers deserve closer review when spend and delivery
> performance are considered together?**

The dashboard identifies patterns for investigation; it does not
independently determine that a supplier is good or bad.

------------------------------------------------------------------------

# Page 6 -- Raw Materials & Supply Chain Risk

## Purpose

Understand raw-material cost, product-material dependency, and shared
material requirements.

### KPIs

-   Total Raw Materials
-   Average Material Standard Cost
-   Products with Material Dependencies
-   Material Dependencies
-   Critical Materials

### Key Results

-   **12 Raw Materials**
-   **₹20.26 Average Material Standard Cost**
-   **10 Products with Material Dependencies**
-   **41 Material Dependencies**
-   **10 Critical Materials**

Critical Materials are defined in this analysis as materials used by
more than one product.

### Analysis Covered

#### Material Standard Cost

**Question:** Which raw materials have the highest standard cost?

Identifies materials with higher standard cost.

#### Shared Material Dependency

**Question:** Which materials are used across the most products?

Identifies materials shared across multiple products.

#### Product Material Complexity

**Question:** Which products depend on the most raw materials?

Shows which products require a larger number of different materials.

#### Cost and Dependency

**Question:** Which materials have high cost and high dependency?

Combines material cost with the number of products using the material.

#### Material Requirement

**Question:** Which raw materials account for the largest share of
requirements?

Shows the relative quantity requirements across materials.

### Business Story

The page moves from:

> **What materials do we use?**

to:

> **Which materials are expensive?**

to:

> **Which materials are shared across products?**

and finally:

> **Where could material dependency require closer supply-chain
> attention?**

The analysis identifies dependency patterns; it does not claim an actual
shortage or supply disruption.

------------------------------------------------------------------------

# Page 7 -- Operator & Shift Performance

## Purpose

Understand differences in production output, defects, downtime, and
energy across operators and shifts.

### KPIs

-   Total Operators
-   Operator Output
-   Operator Defects
-   Downtime Hours
-   Energy Consumption

### Key Results

-   **20 Operators**
-   **1,029,692 Total Operator Output**
-   **17,649 Operator Defects**
-   **1,436 Downtime Hours**
-   **3,205,562 kWh Energy Consumption**

### Analysis Covered

#### Top 10 Operator Production

**Question:** Which operators have the highest production output?

Shows the operators contributing the highest production volumes.

#### Production by Shift

**Question:** How does production output compare across shifts?

Production distribution shown in the completed dashboard:

-   Night: **565,671 (54.94%)**
-   Swing: **254,123 (24.68%)**
-   Day: **209,898 (20.38%)**

#### Top 10 Operator Defects

**Question:** Which operators have the highest defective units?

Identifies operators associated with higher defective-unit counts.

Defect count should be considered alongside production volume rather
than being interpreted as a standalone measure of individual
performance.

#### Downtime vs Production

**Question:** How do operator downtime and production output compare?

Shows the relationship between operator-associated downtime and
production output.

#### Energy by Shift

**Question:** How is energy consumption distributed across shifts?

Shows the distribution of energy consumption across shifts.

### Business Story

The page moves from:

> **Who contributes to production?**

to:

> **How do shifts contribute?**

to:

> **Where are defects concentrated?**

to:

> **How does downtime relate to production?**

and finally:

> **How is energy distributed across shifts?**

The purpose is to identify patterns for operational review, not to label
individual employees as good or poor performers.

------------------------------------------------------------------------

# Key Business Insights

The completed dashboard provides a connected view of several important
business areas.

## 1. Production concentration

Production is distributed differently across plants, products, and
shifts. Understanding this concentration helps management know where the
largest operational workloads are occurring.

## 2. Quality concentration

Defective units are not distributed equally across all products,
categories, plants, or operators. The dashboard helps identify areas
where quality performance deserves closer investigation.

## 3. Downtime visibility

Downtime varies across plants and operators. This provides a starting
point for investigating the operational reasons behind higher time loss.

## 4. Energy visibility

Energy consumption can be viewed both in total and relative to
production. This helps management identify products or shifts where
energy usage deserves further review.

## 5. Cost exposure

Defective production creates estimated product-cost exposure. The
dashboard makes this exposure visible at category and product levels
using available unit-cost information.

## 6. Procurement concentration

Purchasing expenditure is concentrated across suppliers. Understanding
this concentration helps management review supplier relationships and
purchasing exposure.

## 7. Supplier delivery performance

Purchase-order delays and differences in lead time provide visibility
into supplier delivery reliability.

The dashboard shows **171 delayed orders out of 1,600 purchase orders**,
corresponding to a **10.69% delay rate**.

## 8. Shared material dependency

A significant number of materials are shared across multiple products.
This creates a useful visibility point for supply planning because a
shared material can affect more than one product.

## 9. Workforce and shift visibility

Operator and shift analysis allows production, defects, downtime, and
energy to be considered together rather than reviewing workforce output
alone.

------------------------------------------------------------------------

# Business Recommendations

The dashboard is intended to support management investigation and
action.

### 1. Strengthen quality monitoring

Focus quality reviews on products, plants, categories, and operators
showing higher defective-unit levels.

### 2. Investigate higher downtime

Review the operational reasons behind higher downtime at the identified
plants and operators.

### 3. Monitor energy efficiency

Compare energy consumption and energy per unit across products and
shifts to identify areas for further operational review.

### 4. Review supplier delivery reliability

Pay closer attention to suppliers showing higher delay rates or longer
lead times, particularly where purchasing spend is significant.

### 5. Monitor shared materials

Give closer availability and procurement attention to materials used
across multiple products.

### 6. Evaluate production together with quality and efficiency

Production volume should not be viewed in isolation. Management should
consider output together with defects, downtime, and energy consumption.

### 7. Use the dashboard for regular management review

The dashboard can be used as a recurring review tool to:

-   identify changes
-   compare performance
-   investigate unusual patterns
-   assign follow-up actions
-   monitor whether performance improves over time

------------------------------------------------------------------------

# KPI Definitions

  -----------------------------------------------------------------------
  KPI                                 Business Meaning
  ----------------------------------- -----------------------------------
  Total Production                    Total quantity produced

  Total Production Runs               Number of production records/runs

  Total Defects                       Total defective quantity

  Defect Rate                         Defective quantity compared with
                                      production

  Total Downtime Hours                Total recorded downtime converted
                                      to hours

  Average Downtime per Run            Average downtime associated with
                                      each production run

  Total Energy                        Total energy consumed

  Energy per Unit                     Energy consumed relative to
                                      production

  Total Procurement Spend             Purchasing expenditure based on
                                      quantity ordered and unit price

  Total Purchase Orders               Number of purchase orders

  Delayed Orders                      Purchase orders marked as delayed

  Delay Rate                          Delayed orders compared with total
                                      purchase orders

  Average Lead Time                   Average supplier delivery lead time

  Potential Unit Margin               Target price minus unit cost

  Estimated Defect Cost               Defective quantity multiplied by
                                      product unit cost

  Estimated Production Cost           Produced quantity multiplied by
                                      product unit cost

  Potential Production Value          Produced quantity multiplied by
                                      target price

  Products with Material Dependencies Number of products represented in
                                      the product-material dependency
                                      information

  Material Dependencies               Number of product-material
                                      dependency records

  Critical Materials                  Materials used by more than one
                                      product
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Financial Assumptions and Limitations

The financial analysis follows the limitations defined in the BRD.

### Actual revenue

Actual revenue cannot be calculated because sales transactions are not
included in the available dataset.

### Actual profit

Actual profit cannot be calculated because sales, revenue, discounts,
returns, taxes, and other financial transaction information are
unavailable.

### Potential Unit Margin

Potential Unit Margin is calculated as:

**Target Price − Unit Cost**

This represents potential margin context only and must not be
interpreted as actual profit.

### Potential Production Value

Potential Production Value is calculated using:

**Quantity Produced × Target Price**

This represents a planning or target-price scenario and is not actual
revenue.

### Estimated Defect Cost

Estimated Defect Cost is calculated using:

**Defective Quantity × Product Unit Cost**

This is a cost-exposure estimate and should not be described as
confirmed scrap, rework, or accounting loss.

### Estimated Production Cost

Estimated Production Cost is calculated using:

**Quantity Produced × Product Unit Cost**

This provides cost context for comparing production scale and is not a
formal accounting COGS calculation.

------------------------------------------------------------------------

# Dashboard Usage

The dashboard is designed to support a simple management review cycle:

### 1. Understand

Start with the Executive Overview to understand overall production,
defects, downtime, and energy.

### 2. Compare

Move into plant, product, supplier, material, operator, and shift
comparisons.

### 3. Identify

Identify areas showing higher production concentration, defects,
downtime, energy usage, procurement spend, delays, or material
dependency.

### 4. Investigate

Use the relevant dashboard page and filters to examine the area in
greater detail.

### 5. Act

Use the insight as a starting point for operational, quality,
procurement, or supply-chain follow-up.

### 6. Monitor

Return to the dashboard periodically to determine whether the identified
area has changed.

------------------------------------------------------------------------

# Conclusion

The Novitech Manufacturing Analytics project provides a single business
view across production, quality, operational efficiency, finance and
cost context, procurement, suppliers, raw materials, and workforce
performance.

The dashboard does not simply report numbers. It helps management ask
the next business question:

> **Where should we look more closely?**

Production performance leads to quality and efficiency analysis. Quality
and operational losses lead to cost exposure. Production depends on
materials, materials depend on suppliers, and workforce and shifts
contribute to daily operational outcomes.

By connecting these areas, the dashboard gives management a practical
way to identify patterns, investigate areas of concern, and support
better operational and supply-chain decisions.

------------------------------------------------------------------------

## Project Outcome

The completed solution delivers:

-   Cleaned and validated business data
-   Business-focused KPI calculations
-   Seven-page interactive Power BI dashboard
-   Production and plant analysis
-   Quality and operational efficiency analysis
-   Finance and cost-context analysis
-   Procurement and supplier performance analysis
-   Raw-material dependency analysis
-   Operator and shift performance analysis
-   Business insights
-   Management recommendations
-   Clearly documented financial assumptions and limitations

The solution is aligned with the Novitech Manufacturing BRD and is
designed to support evidence-based management review.
