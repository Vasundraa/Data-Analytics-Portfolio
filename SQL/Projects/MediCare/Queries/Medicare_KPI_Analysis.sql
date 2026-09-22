-- KPI Analysis
-- Total Patients
SELECT COUNT(*) AS total_patients
FROM Patients;

-- Total Appointments
SELECT COUNT(*) AS total_appointments
FROM Appointments;

-- Total Admissions
SELECT COUNT(*) AS total_admissions
FROM Admissions;

-- Total Treatments
SELECT COUNT(*) AS total_treatments
FROM Treatments;

-- Total Treament Cost
SELECT
    ROUND(SUM(CAST(treatment_cost AS DECIMAL(10,2))), 2)
    AS total_treatment_cost
FROM Treatments;

-- Total Laboratory Activity
SELECT COUNT(*) AS total_lab_activity
FROM Laboratory;

-- Total Laboratory Cost
SELECT
    ROUND(SUM(CAST(test_cost AS DECIMAL(10,2))), 2)
    AS total_lab_cost
FROM Laboratory;

-- Total Pharmacy Activity
SELECT COUNT(*) AS total_pharmacy_activity
FROM Pharmacy;