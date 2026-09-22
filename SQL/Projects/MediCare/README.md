# MediCare Healthcare Operations & Revenue Analytics

**Project Type:** SQL / MySQL Database & Business Analytics  
**Industry:** Healthcare  
**Tool:** MySQL Workbench

## 1. Project Overview

MediCare Healthcare Operations & Revenue Analytics is a MySQL project developed from a Business Requirements Document (BRD). The project integrates healthcare operational and financial data to analyze patient activity, hospital operations, healthcare services, billing, and payment collection.

The intended business flow is:

**Patient → Appointment → Admission → Treatment / Laboratory / Pharmacy → Billing → Payment**

The project combines relational database design, data cleaning, data validation, SQL analysis, KPI calculation, and business insights.

## 2. Business Problem

Healthcare information is distributed across multiple related entities. Management needs a consolidated SQL-based view of:

- Patient activity
- Hospital activity
- Department workload
- Doctor workload
- Admissions and length of stay
- Room utilization
- Treatment activity and cost
- Laboratory activity and cost
- Pharmacy activity and revenue
- Billing performance
- Payment collection
- Billing/payment gaps
- Payment methods and statuses

## 3. Objectives

1. Create a structured relational healthcare database.
2. Implement primary and foreign key relationships.
3. Load and validate source data.
4. Profile NULL values, duplicates, inconsistent formats and invalid records.
5. Clean data using controlled SQL operations.
6. Validate referential integrity.
7. Analyze hospitals, departments, doctors, patients and admissions.
8. Analyze treatments, laboratory services and pharmacy activity.
9. Analyze billing and payment performance.
10. Calculate operational and financial KPIs.
11. Use joins, aggregations, subqueries and window functions.
12. Answer the 16 BRD business questions.
13. Convert SQL results into meaningful business insights.

## 4. Database Tables

| Table | Purpose |
|---|---|
| `Hospitals` | Hospital-level information |
| `Departments` | Department and hospital information |
| `Doctors` | Doctor, hospital and department information |
| `Patients` | Patient master information |
| `Rooms` | Room information and status |
| `Appointments` | Patient-doctor appointment activity |
| `Admissions` | Admission and discharge information |
| `Treatments` | Treatment/service activity and cost |
| `Laboratory` | Diagnostic test activity and cost |
| `Employees` | Hospital workforce information |
| `Insurance` | Patient insurance information |
| `Medicines` | Medicine master information |
| `Pharmacy` | Pharmacy transactions, quantity and revenue |
| `Billing` | Healthcare charges and billed amounts |
| `Payments` | Payment collection, mode and status |

## 5. Folder Structure

```text
MediCare/
│
├── Queries/
│   └── Medicare.sql
│
├── Source/
│   └── Hospital_Analytics_DB_dataset.xlsx
│
└── README.md
```

### `Queries/Medicare.sql`

The complete SQL work for the project is maintained in a **single SQL file**. The file contains the end-to-end MediCare implementation, including database setup, table creation, constraints, data preparation, cleaning and validation queries, analytical queries, KPI calculations, and BRD business-question analysis.

Keeping the project work in one SQL file makes it easy to execute, review, and trace the complete SQL workflow from database creation through final analysis.

### `Source/`

The `Source/` folder contains the original source workbook used for the MediCare project:

```text
Source/
└── Hospital_Analytics_DB_dataset.xlsx
```

This source dataset provides the healthcare and financial data required by the BRD and forms the foundation for the MySQL database and subsequent SQL analysis.

The dataset covers the major business entities required for the project, including:

- Hospitals
- Departments
- Doctors
- Patients
- Appointments
- Admissions
- Rooms
- Treatments
- Laboratory services
- Employees
- Insurance
- Medicines
- Pharmacy
- Billing
- Payments

These entities support the BRD's analytical flow:

**Patient → Appointment → Admission → Treatment / Laboratory / Pharmacy → Billing → Payment**

The source workbook was used as the starting point for:

1. Reviewing the available healthcare entities and fields.
2. Designing the relational MySQL database.
3. Creating the required tables and relationships.
4. Loading the source data into MySQL.
5. Profiling NULL values, duplicates, inconsistent values and invalid records.
6. Cleaning and validating the data using SQL.
7. Performing the 16 BRD business-question analyses.
8. Calculating operational and financial KPIs.
9. Analyzing billing, payments and collection gaps.

The source data therefore acts as the **data foundation** of the project, while `Queries/Medicare.sql` contains the complete SQL implementation and analytical work.

> The source workbook is retained as the original project input. Data-quality corrections and analytical transformations were performed in the MySQL environment through documented SQL operations rather than treating the source workbook as the final analytical database.

## 6. Database Design

Major primary keys include:

| Table | Primary Key |
|---|---|
| Hospitals | `hospital_id` |
| Departments | `department_id` |
| Doctors | `doctor_id` |
| Patients | `patient_id` |
| Rooms | `room_id` |
| Appointments | `appointment_id` |
| Admissions | `admission_id` |
| Treatments | `treatment_id` |
| Billing | `billing_id` |
| Payments | `payment_id` |

Important relationships include:

- Departments → Hospitals
- Doctors → Hospitals
- Doctors → Departments
- Appointments → Patients
- Appointments → Doctors
- Appointments → Hospitals
- Admissions → Patients
- Admissions → Hospitals
- Admissions → Departments
- Admissions → Rooms
- Treatments → Admissions
- Treatments → Patients
- Treatments → Doctors
- Payments → Billing

## 7. Data Profiling & Cleaning

The project included:

### NULL Analysis
NULL values were investigated individually rather than automatically converting them to zero.

### Duplicate Analysis
Potential duplicates were checked, especially payment records. Repeated business transactions were distinguished from genuine duplicate errors.

### Gender Standardization
Inconsistent gender representations such as `M`, `Male`, `F`, and `Female` were standardized where required.

### Date Validation
Joining, appointment, admission, discharge, treatment and payment dates were reviewed for consistency.

### Email Validation
Invalid email formats were identified for data-quality review.

### Payment Mode
Missing payment-mode values were reviewed and populated using the appropriate value identified from the dataset.

### Billing Validation
Billing amounts and charge components were reviewed for numeric consistency and decimal precision.

### Payment Amount
Negative payment values were identified and converted to positive values through a controlled SQL update so they would not distort collection calculations.

## 8. Billing & Payment Analysis

Financial analysis was handled carefully because Billing and Payments may have different levels of detail.

Key measures:

```text
Total Billed Amount = Sum of billing totals

Total Payment Collected = Sum of valid successful payments

Collection Gap = Total Billed Amount - Total Payment Collected

Collection Rate % =
(Total Payment Collected / Total Billed Amount) × 100
```

The project also uses `payment_condition` classifications such as:

- Fully Paid
- Partially Paid
- Overpaid
- Refunded
- Failed

### Avoiding Double Counting

If one bill has multiple payment records, a direct Billing-to-Payments join can repeat the bill amount. Billing and payment amounts therefore need to be aggregated carefully before comparison.

## 9. BRD Business Questions Completed

The SQL analysis covers these 16 questions:

1. Which hospitals have the highest patient and operational activity?
2. Which departments have the highest appointment and admission workload?
3. How is doctor workload distributed?
4. Which patients have the highest healthcare service activity?
5. Which hospitals and departments have the highest admissions?
6. What are the admission type and status patterns?
7. What is the average patient length of stay?
8. How are rooms distributed by type and status?
9. Which treatments have the highest activity and cost?
10. Which laboratory tests/services have the highest volume and cost?
11. Which medicines have the highest pharmacy activity or revenue?
12. How much revenue is billed?
13. How do room, doctor, medicine, laboratory and other charges contribute to billing?
14. How much of the billed amount has been collected?
15. Where are the largest billing/payment gaps?
16. How do payment methods and payment statuses affect collection?

## 10. KPI Analysis

The project includes:

| KPI | Meaning |
|---|---|
| Total Patients | Number of patients |
| Total Appointments | Appointment activity |
| Total Admissions | Admission activity |
| Average Length of Stay | Average valid completed admission duration |
| Total Treatments | Treatment activity |
| Total Treatment Cost | Treatment expenditure |
| Total Laboratory Activity | Laboratory/test volume |
| Total Laboratory Cost | Laboratory expenditure |
| Total Pharmacy Activity | Pharmacy transaction volume |
| Total Billed Amount | Total amount billed |
| Total Payment Collected | Successful payment collection |
| Collection Gap | Billed amount minus collected amount |
| Collection Rate % | Percentage of billed amount collected |
| Hospital Activity | Comparative hospital activity |
| Department Workload | Comparative department workload |
| Doctor Workload | Measurable doctor activity |

## 11. Additional Business Analysis

Supporting analyses include:

- Patients per hospital
- Doctors per hospital
- Departments per hospital
- Average appointments per doctor
- Doctors with no appointment activity
- Patients with multiple appointments
- Patients with multiple admissions
- Treatment status analysis
- Billing status analysis
- Payment status analysis
- Hospital-wise billing
- Doctor workload ranking

Example: Doctors per Hospital

```sql
SELECT
    h.hospital_name,
    COUNT(d.doctor_id) AS total_doctors
FROM Hospitals h
JOIN Doctors d
    ON h.hospital_id = d.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY total_doctors DESC;
```

Example: Patients per Hospital

```sql
SELECT
    h.hospital_name,
    COUNT(DISTINCT a.patient_id) AS total_patients
FROM Hospitals h
JOIN Appointments a
    ON h.hospital_id = a.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY total_patients DESC;
```

# 12. Detailed Work Completed

The project work was carried out as an end-to-end SQL analytics workflow aligned with the MediCare BRD.

## 12. Detailed Work Completed

### Phase 1 — Business Requirement Understanding

The MediCare BRD was reviewed to identify the required operational and financial analysis.

The project was structured around the BRD's core requirement:

> Understand healthcare operations and evaluate how delivered healthcare services are converted into billed and collected revenue.

The BRD requirements covered:

- Hospital operations
- Department workload
- Doctor workload
- Patient activity
- Admissions
- Room utilization
- Treatment services
- Laboratory services
- Pharmacy activity
- Billing
- Payments
- Operational KPIs
- Financial KPIs
- Business insights

### Phase 2 — Source Data Review

The source file:

```text
Hospital_Analytics_DB_dataset
```

was reviewed before creating the final database.

The source data was used as the foundation for the relational MediCare database.

The review focused on:

- Available tables/entities
- Column names
- Identifier fields
- Relationships between entities
- Date fields
- Categorical fields
- Monetary fields
- NULL values
- Duplicate records
- Data-format inconsistencies

### Phase 3 — Database Creation

A dedicated MediCare MySQL database was created.

The SQL implementation includes database and table creation for the healthcare entities required by the BRD.

The major tables include:

- Hospitals
- Departments
- Doctors
- Patients
- Rooms
- Appointments
- Admissions
- Treatments
- Laboratory
- Employees
- Insurance
- Medicines
- Pharmacy
- Billing
- Payments

### Phase 4 — Primary and Foreign Key Implementation

Primary keys were implemented for major entities so records can be uniquely identified.

Foreign-key relationships were established between related healthcare entities.

Examples include:

```text
Departments → Hospitals
Doctors → Hospitals
Doctors → Departments
Appointments → Patients
Appointments → Doctors
Appointments → Hospitals
Admissions → Patients
Admissions → Hospitals
Admissions → Departments
Admissions → Rooms
Treatments → Admissions
Treatments → Patients
Treatments → Doctors
Payments → Billing
```

These relationships support the healthcare flow defined in the BRD.

### Phase 5 — Data Loading

The source dataset was loaded into the MySQL database.

The data-loading stage ensured that the source records were available in relational tables before data profiling and analytical queries were performed.

### Phase 6 — Data Profiling

Data profiling was performed before final analysis.

### NULL Checks

NULL values were checked across relevant tables and columns.

The project followed the BRD principle that NULL values should be investigated before deciding how they should be handled.

Missing values were not automatically converted to zero because a missing value can have a legitimate business meaning.

### Duplicate Checks

Duplicate records were investigated.

Special attention was given to payment records because multiple payment transactions can legitimately belong to the same bill.

The analysis distinguished potential duplicate errors from legitimate repeated business events.

### Categorical Value Checks

Categorical fields were reviewed for inconsistent representations.

Examples included gender, payment mode, payment status, admission type and admission status.

### Date Validation

Relevant date fields were reviewed for consistency, including:

- Joining dates
- Appointment dates
- Admission dates
- Discharge dates
- Treatment dates
- Payment dates

### Numeric and Monetary Validation

Financial and cost-related columns were reviewed for:

- Numeric validity
- Decimal precision
- Negative values
- Text-based numeric fields
- Aggregation readiness

### Phase 7 — Data Cleaning

Controlled SQL updates were used to correct identified data-quality issues.

### Gender Standardization

Inconsistent gender values were standardized so that grouping and aggregation would produce consistent results.

### Joining Date Cleaning

Doctor joining dates were reviewed and standardized for consistent date analysis.

### Date Cleaning

Inconsistent date representations were reviewed and standardized where required.

### Email Validation

Incorrect or invalid email values were identified during profiling.

The project did not blindly replace questionable source values without justification.

### Payment Mode Cleaning

Missing payment-mode values were investigated.

The available payment data was used to identify the appropriate mode value, and missing values were populated accordingly.

### Billing Amount Validation

Billing totals and charge components were reviewed for consistency and appropriate numeric precision.

### Payment Amount Cleaning

Negative payment amounts were identified.

The negative payment values were converted to positive values through a controlled SQL update so they would not distort payment-collection analysis.

### Phase 8 — Healthcare Operational Validation

Operational tables were checked for valid relationships and business consistency.

### Admissions

Admission records were reviewed for:

- Patient IDs
- Hospital IDs
- Department IDs
- Doctor IDs
- Room IDs
- Admission dates
- Discharge dates
- Admission types
- Admission statuses

Discharge dates were not treated as automatically missing errors because a NULL discharge date can represent an ongoing admission.

### Length of Stay

Average length of stay was calculated only for records where valid admission and discharge dates were available.

The calculation uses the difference between discharge and admission dates.

### Rooms

Room type and room status were analyzed to understand resource distribution.

### Treatments

Treatment activity and treatment cost were analyzed.

### Laboratory

Laboratory test volume and cost were analyzed.

### Pharmacy

Medicine-level transactions, quantities and revenue were analyzed where supported by the source fields.

### Phase 9 — Billing and Payment Validation

The Billing and Payments tables received additional validation because they represent financial activity at potentially different grains.

The project checked:

- Billing identifiers
- Patient relationships
- Billing amounts
- Bill status
- Payment identifiers
- Payment amounts
- Payment status
- Payment mode
- Payment dates
- Matching bills and payments
- Duplicate payment records

The project also created/used `payment_condition` to classify payment records into categories such as:

- Fully Paid
- Partially Paid
- Overpaid
- Refunded
- Failed

### Phase 10 — Financial Analysis

Financial analysis was aligned directly with the BRD.

### Total Billed Amount

Calculated the total amount billed across the healthcare network.

### Billing Charge Contribution

Analyzed the contribution of:

- Room charges
- Doctor charges
- Medicine charges
- Laboratory charges
- Other charges

### Total Payment Collected

Calculated successful payment collection.

### Collection Gap

Analyzed the difference between billed and collected amounts.

```text
Collection Gap = Total Billed Amount - Total Payment Collected
```

### Collection Rate

Calculated the proportion of billed revenue represented by collected payments.

```text
Collection Rate % =
(Total Payment Collected / Total Billed Amount) × 100
```

The resulting rate is interpreted together with payment status, overpayments, refunds and multiple-payment records.

### Payment Method and Status

Payment activity was grouped by:

- Payment mode
- Payment status
- Number of payments
- Payment amount

### Phase 11 — BRD Business Question Analysis

All 16 primary business questions defined in the BRD were addressed through SQL analysis.

The completed analysis covers:

1. Hospital patient and operational activity
2. Department appointment and admission workload
3. Doctor workload distribution
4. Patient healthcare service activity
5. Hospital and department admissions
6. Admission type and status patterns
7. Average length of stay
8. Room type and status distribution
9. Treatment activity and cost
10. Laboratory volume and cost
11. Pharmacy/medicine activity and revenue
12. Total billed revenue
13. Billing charge contribution
14. Payment collection
15. Billing/payment gaps
16. Payment methods and payment status

### Phase 12 — KPI Analysis

The BRD KPI framework was implemented through SQL analysis.

KPIs include:

- Total Patients
- Total Appointments
- Total Admissions
- Average Length of Stay
- Total Treatments
- Total Treatment Cost
- Total Laboratory Activity
- Total Laboratory Cost
- Total Pharmacy Activity
- Total Billed Amount
- Total Payment Collected
- Collection Gap
- Collection Rate %
- Hospital Activity
- Department Workload
- Doctor Workload

### Phase 13 — Additional Business Analysis

Additional supporting analyses were performed to extend the BRD analysis.

Examples include:

- Patients per hospital
- Doctors per hospital
- Departments per hospital
- Average appointments per doctor
- Doctors with no appointments
- Patients with multiple appointments
- Patients with multiple admissions
- Treatment status analysis
- Billing status analysis
- Payment status analysis
- Hospital-wise billing
- Doctor workload ranking

For example, because `Doctors` contains `hospital_id`, doctor distribution was analyzed directly between Hospitals and Doctors rather than using an unnecessary intermediate join through Departments.

### Phase 14 — Window Function Analysis

The BRD requires meaningful use of window functions.

The project includes business-oriented applications for:

- `ROW_NUMBER()` — sequential ranking/numbering
- `RANK()` — ranking hospitals, doctors or other business entities
- `LAG()` — comparing a value with a previous record/period
- `LEAD()` — comparing a value with a following record/period

Window functions are used for analytical purposes rather than only demonstrating SQL syntax.

### Phase 15 — Financial Grain and Duplicate-Counting Awareness

One of the important analytical considerations in the project is that Billing and Payments can have different grains.

For example:

```text
One Bill
   ↓
Multiple Payment Records
```

If billing totals are summed after directly joining to multiple payment rows, the same bill can be counted more than once.

Therefore, the project treats billing and payment aggregation carefully when calculating:

- Total billed amount
- Total collected amount
- Collection gap
- Collection rate

This is particularly important for reliable financial analysis.

### Phase 16 — Business Insight Preparation

The SQL results are structured to support management-oriented interpretation.

The analysis can be used to identify:

- Hospitals with higher operational activity
- Departments with higher workload
- Doctor workload distribution
- High-service-utilization patients
- Admission patterns
- Resource distribution
- High-volume/high-cost treatments
- High-volume/high-cost laboratory services
- High-activity medicines
- Major billing components
- Payment collection patterns
- Payment gaps
- Payment-method/status patterns

All insights are restricted to what can be supported by the available dataset and relationships.

---

## 13. SQL Concepts Demonstrated

### DDL
- `CREATE DATABASE`
- `CREATE TABLE`
- `ALTER TABLE`
- `DROP TABLE` where appropriate

### DML
- `INSERT`
- Controlled `UPDATE`

### Querying
- `SELECT`
- `WHERE`
- `ORDER BY`
- `LIMIT`

### Aggregation
- `COUNT()`
- `SUM()`
- `AVG()`
- `GROUP BY`
- `HAVING`

### Joins
- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`

### Other SQL
- `CASE`
- Subqueries
- `CAST()`
- Date functions such as `DATEDIFF()`

### Window Functions
The project includes meaningful analytical use cases for:

- `ROW_NUMBER()`
- `RANK()`
- `LAG()`
- `LEAD()`

These support ranking and comparison rather than being used only to demonstrate syntax.

## 14. Data Quality Principles

The project follows these principles:

- Profile before cleaning.
- Do not automatically convert NULL to zero.
- Distinguish duplicate errors from repeated legitimate transactions.
- Validate foreign-key relationships.
- Preserve business meaning during cleaning.
- Document significant data modifications.
- Avoid duplicate financial aggregation.
- Convert text-based monetary fields to numeric values before calculations.

## 15. Project Workflow

```text
Business Requirements
        ↓
Source Data Review
        ↓
Database Design
        ↓
Table Creation
        ↓
Primary & Foreign Keys
        ↓
Data Loading
        ↓
Data Profiling
        ↓
Data Cleaning
        ↓
Data Validation
        ↓
Business Queries
        ↓
KPI Analysis
        ↓
Business Insights
```

## 16. Skills Demonstrated

`MySQL` `SQL` `Data Cleaning` `Data Validation` `Relational Database` `Primary Keys` `Foreign Keys` `Joins` `Aggregations` `Subqueries` `Window Functions` `KPI Analysis` `Healthcare Analytics` `Revenue Analysis` `Payment Analysis`

## 17. How to Run

1. Install MySQL Server and MySQL Workbench.
2. Open the SQL scripts from `Queries/`.
3. Create and select the MediCare database.
4. Create the required tables and constraints.
5. Load the source data from `Source/`.
6. Run profiling and validation queries.
7. Run documented data-cleaning queries where required.
8. Execute the 16 BRD business-question queries.
9. Execute KPI and supporting business-analysis queries.
10. Review the SQL outputs and document business insights.

## 18. Project Outcome

The MediCare project establishes a structured SQL-based analytical foundation for healthcare operations and revenue analysis.

It demonstrates an end-to-end workflow:

**Database Design → Data Loading → Data Cleaning → Data Validation → SQL Analysis → KPI Calculation → Business Insights**

The resulting analysis provides a consolidated way to understand patient activity, hospital and department workload, doctor activity, healthcare service utilization, billing performance, and payment collection.

## 19. Project Scope Limitation

This is a healthcare analytics project. It is not intended for:

- Medical diagnosis
- Clinical decision-making
- Predictive healthcare modeling unless separately requested
- Claims about healthcare quality or clinical outcomes not supported by the dataset
- External data integration beyond the supplied project data

All business conclusions are limited to the available dataset, relationships and fields.

---

**Project:** MediCare Healthcare Operations & Revenue Analytics  
**Technology:** MySQL / SQL  
**Status:** Database, cleaning, validation, BRD analysis and KPI work completed; repository documentation maintained in this README.
