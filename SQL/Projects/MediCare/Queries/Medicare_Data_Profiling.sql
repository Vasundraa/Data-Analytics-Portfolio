-- Data Profiling
-- Number of records in each table
SELECT COUNT(*) AS total_hospitals
FROM Hospitals;

SELECT COUNT(*) AS total_departments
FROM Departments;

SELECT COUNT(*) AS total_doctors
FROM Doctors;

SELECT COUNT(*) AS total_patients
FROM Patients;

SELECT COUNT(*) AS total_appointments
FROM Appointments;

SELECT COUNT(*) AS total_admissions
FROM Admissions;

SELECT COUNT(*) AS total_treatments
FROM Treatments;

SELECT COUNT(*) AS total_lab_records
FROM Laboratory;

SELECT COUNT(*) AS total_pharmacy_records
FROM Pharmacy;

SELECT COUNT(*) AS total_bills
FROM Billing;

SELECT COUNT(*) AS total_payments
FROM Payments;