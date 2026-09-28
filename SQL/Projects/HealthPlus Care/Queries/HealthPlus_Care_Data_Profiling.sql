# PROFILING

describe clinics;

describe Specialists;

DESCRIBE Members;

describe Corporates;

describe Corporate_Members;

describe Consultations;

describe Telemedicine_Sessions;

describe Chronic_Care_Programs;

describe Health_Packages;

describe Package_Subscriptions;

describe Prescriptions;

describe Lab_Tests;

describe Claims;

describe Staff;

describe Billing ;

describe Payments;

describe Feedback;

select * from clinics;

select count(*) from clinics;

select * from Specialists;

select count(*) from Specialists;

select * from Members;

select count(*) from Members;

select * from Corporates;

select count(*) from Corporates;

select * from Corporate_Members;

select count(*) from Corporate_Members;

select * from Consultations;

select count(*) from Consultations;

select * from Telemedicine_Sessions;

select count(*) from Telemedicine_Sessions;

select * from Chronic_Care_Programs;

select count(*) from Chronic_Care_Programs;

select * from Health_Packages;

select count(*) from Health_Packages;

select * from Package_Subscriptions;

select count(*) from Package_Subscriptions;

select * from Prescriptions;

select count(*) from Prescriptions;

select * from Lab_Tests;

select count(*) from Lab_Tests;

select * from Claims;

select count(*) from Claims;

select * from Staff;

select count(*) from Staff;

select * from Billing ;

select count(*) from Billing ;

select * from payments;

select count(*) from payments;

select * from Feedback;

select count(*) from Feedback;

# Members data profiling

SELECT distinct gender from Members;

SELECT * from Members where email is null;

SELECT * from Members where email not like '%@%.%';
SELECT *
FROM Members
WHERE email LIKE '%@@%';

# Claims data profiling

SELECT * from Claims where consultation_id is null;

SELECT * from Claims where insurance_provider is null;

SELECT
    COUNT(*) AS missing_consultation_id,
    COUNT(member_id) AS with_member_id,
    COUNT(claim_amount) AS with_claim_amount,
    COUNT(claim_status) AS with_claim_status
FROM Claims
WHERE consultation_id IS NULL;

# Billing data profiling

SELECT * from Billing where consultation_id is null;

SELECT
    bill_id,
    consultation_charges,
    lab_charges,
    medicine_charges,
    total_amount,
    consultation_charges + lab_charges + medicine_charges AS calculated_total
FROM Billing
WHERE total_amount < 0;

SELECT
    COUNT(*) AS missing_consultation_id,
    COUNT(member_id) AS with_member_id,
    COUNT(total_amount) AS with_total_amount,
    COUNT(bill_date) AS with_bill_date
FROM Billing
WHERE consultation_id IS NULL;

# Payments data profiling

SELECT * FROM Payments where payment_mode is null;

SELECT
    p.payment_id,
    p.bill_id,
    p.payment_amount,
    b.total_amount
FROM Payments p
JOIN Billing b
    ON p.bill_id = b.bill_id
WHERE p.payment_amount < 0;

SELECT COUNT(*) AS negative_payments
FROM Payments
WHERE payment_amount < 0;

SELECT COUNT(*) AS nullValues
FROM Payments
WHERE payment_mode IS NULL;
