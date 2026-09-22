-- Business Analysis
-- Patients per Hospital
SELECT
    h.hospital_name,
    COUNT(DISTINCT a.patient_id) AS total_patients
FROM Hospitals h
JOIN Appointments a
    ON h.hospital_id = a.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY total_patients DESC;

-- Doctors per Hospital
SELECT
    h.hospital_name,
    COUNT(d.doctor_id) AS total_doctors
FROM Hospitals h
JOIN Doctors d
    ON h.hospital_id = d.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY total_doctors DESC;

-- Departments per Hospital
SELECT
    h.hospital_name,
    COUNT(d.department_id) AS total_departments
FROM Hospitals h
JOIN Departments d
    ON h.hospital_id = d.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY total_departments DESC;

-- Average Appointments per Doctor
SELECT
    ROUND(COUNT(a.appointment_id) / COUNT(DISTINCT d.doctor_id), 2)
    AS avg_appointments_per_doctor
FROM Doctors d
JOIN Appointments a
    ON d.doctor_id = a.doctor_id;
    
-- Doctors with No Appointments
SELECT
    d.doctor_id,
    d.first_name
FROM Doctors d
LEFT JOIN Appointments a
    ON d.doctor_id = a.doctor_id
WHERE a.appointment_id IS NULL;

-- Patient Activity Analysis
-- Patients with Multiple Appointments
SELECT
    patient_id,
    COUNT(*) AS appointment_count
FROM Appointments
GROUP BY patient_id
HAVING COUNT(*) > 1
ORDER BY appointment_count DESC;

-- Patients with Multiple Admissions
SELECT
    patient_id,
    COUNT(*) AS admission_count
FROM Admissions
GROUP BY patient_id
HAVING COUNT(*) > 1
ORDER BY admission_count DESC;

-- Service Utilization Analysis
-- Treatment Status Distribution
SELECT
    treatment_status,
    COUNT(*) AS total_treatments
FROM Treatments
GROUP BY treatment_status
ORDER BY total_treatments DESC;

-- Laboratory Status Distribution
SELECT
    test_status,
    COUNT(*) AS total_tests
FROM Laboratory
GROUP BY test_status
ORDER BY total_tests DESC;

-- Financial KPI Analysis
-- Collection Rate
SELECT
    ROUND(
        (SELECT SUM(total_paid)
         FROM
         (
             SELECT
                 bill_id,
                 SUM(CAST(payment_amount AS DECIMAL(10,2))) AS total_paid
             FROM Payments
             WHERE payment_status = 'Success'
             GROUP BY bill_id
         ) p)
        /
        (SELECT SUM(total_amount)
         FROM Billing)
        * 100,
        2
    ) AS collection_rate_percentage;
    
-- Billing Status Distribution
SELECT
    bill_status,
    COUNT(bill_id) AS total_bills,
    ROUND(SUM(total_amount), 2) AS total_billed_amount
FROM Billing
GROUP BY bill_status
ORDER BY total_billed_amount DESC;

-- Payment Status Distribution
SELECT
    payment_status,
    COUNT(payment_id) AS total_payments,
    ROUND(
        SUM(CAST(payment_amount AS DECIMAL(10,2))),
        2
    ) AS total_amount
FROM Payments
GROUP BY payment_status
ORDER BY total_amount DESC;

-- Hospital Financial Analysis
SELECT
    h.hospital_name,
    ROUND(SUM(b.total_amount), 2) AS total_billed_amount
FROM Billing b
JOIN Admissions a
    ON b.admission_id = a.admission_id
JOIN Departments d
    ON a.department_id = d.department_id
JOIN Hospitals h
    ON d.hospital_id = h.hospital_id
GROUP BY h.hospital_id, h.hospital_name
ORDER BY total_billed_amount DESC;
    
-- Ranking Analysis
-- Rank Doctors by Appointment Workload
SELECT
    d.doctor_id,
    d.first_name,
    COUNT(a.appointment_id) AS appointment_count,
    RANK() OVER (
        ORDER BY COUNT(a.appointment_id) DESC
    ) AS workload_rank
FROM Doctors d
LEFT JOIN Appointments a
    ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id, d.first_name; 