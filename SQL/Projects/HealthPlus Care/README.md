# HealthPlus Care – Healthcare Analytics

## Project Overview

**HealthPlus Care** is a MySQL-based healthcare analytics project developed from a Business Requirements Document (BRD). The project integrates healthcare operational, service, financial, and member-related data to support business analysis and decision-making.

The project focuses on understanding:

- Member and consultation activity
- Specialist and clinic performance
- Telemedicine services
- Chronic care programs
- Health package subscriptions
- Corporate healthcare participation
- Prescriptions and laboratory services
- Claims, billing, and payment collection
- Member feedback and engagement

## Objectives

- Build and manage a structured relational healthcare database.
- Load and validate healthcare data using MySQL.
- Identify and resolve important data quality issues.
- Validate primary keys, foreign keys, and relationships between tables.
- Analyze healthcare operations using SQL queries.
- Answer business questions defined in the BRD.
- Analyze billing, payments, claims, and collection gaps.
- Generate meaningful business insights from the data.

## My Work

### Database Development
- Created and worked with a relational MySQL database containing healthcare operational and financial entities.
- Implemented and validated primary key and foreign key relationships.
- Loaded the source healthcare dataset into the database.

### Data Profiling & Cleaning
Performed detailed data quality checks across the tables, including:

- Duplicate primary key validation.
- NULL value analysis.
- Foreign key integrity checks.
- Email format validation.
- Date validation.
- Categorical value consistency checks.
- Financial value validation.

Applied justified SQL-based corrections, including:
- Standardizing inconsistent gender values.
- Correcting invalid email records where applicable.
- Creating an email status classification.
- Correcting negative payment amounts.
- Filling missing payment modes where appropriate.
- Standardizing missing insurance provider values.
- Recalculating incorrect billing totals.

Data issues that could not be reliably inferred, such as missing relationship values, were retained rather than introducing inaccurate information.

### Business Analysis

Developed SQL queries based on the BRD to analyze:

- Clinic consultation volume.
- Specialist workload.
- Specialization activity.
- Most active members.
- Consultation modes and statuses.
- Reasons for consultation.
- Telemedicine session performance.
- Chronic care program enrollment.
- Health package subscriptions.
- Corporate member participation.
- Prescription activity.
- Laboratory test costs and workload.
- Insurance claim amounts and statuses.
- Billing and payment performance.
- Collection gaps.
- Feedback ratings.
- Members without feedback or consultations.
- Healthcare activity compared with financial and experience indicators.

The analysis uses SQL joins, filtering, aggregation, grouping, subqueries, and analytical calculations to answer business-focused questions.

## Key Skills Demonstrated

**SQL / MySQL:**  
Data Cleaning • Data Validation • Joins • Aggregations • GROUP BY • HAVING • Subqueries • CASE Statements • NULL Handling • Primary & Foreign Keys • Business Analysis

**Database Concepts:**  
Relational Database Design • Referential Integrity • Data Quality • Data Profiling • Financial Data Validation

## Project Outcome

The project transformed raw healthcare data into a structured and validated relational database and prepared it for business-oriented analysis.

The completed analysis provides insights into healthcare service utilization, member engagement, operational workload, financial performance, payment collection, and customer experience.

## Tools Used

- MySQL
- MySQL Workbench
- SQL
- Business Requirements Document (BRD)