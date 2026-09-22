DESCRIBE Hospitals;

-- to select duplicate values from Hospitals
SELECT hospital_id, count(*)
FROM Hospitals
GROUP BY hospital_id
HAVING count(*)>1;

-- to check for null values
SELECT department_id
FROM Departments
WHERE head_doctor_id IS NULL;

-- to check distinct values 
SELECT DISTINCT gender
FROM Doctors;

-- to get count of distinct values
SELECT gender, count(*)
FROM Doctors
GROUP BY gender;

-- to preview the standardized column
SELECT gender,
CASE
WHEN LOWER(TRIM(gender)) IN ('male','m')
THEN 'Male'
WHEN LOWER(TRIM(gender)) IN ('female','f')
THEN 'Female'
ELSE gender
END
FROM Doctors;

-- to update the standardized column in the table
UPDATE Doctors
SET gender = CASE
WHEN LOWER(TRIM(gender)) IN ('male','m')
THEN 'Male'
WHEN LOWER(TRIM(gender)) IN ('female','f')
THEN 'Female'
ELSE gender
END;

-- cleaning date value
-- listing the incorrect formats
SELECT doctor_id, joining_date
FROM Doctors
WHERE joining_date NOT REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$';

-- changing / to -
UPDATE Doctors
SET joining_date = REPLACE(joining_date, '/', '-')
WHERE joining_date LIKE '%/%';

-- identifying dates of not yyyy-mm-dd format 
SELECT doctor_id, joining_date
FROM Doctors
WHERE joining_date NOT REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$';

-- finding actual dd-mm-yyyy without ambiguity
SELECT doctor_id, joining_date
FROM Doctors
WHERE joining_date REGEXP '^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
AND CAST(SUBSTRING_INDEX(joining_date,'-',1) AS UNSIGNED) >12;

UPDATE Doctors
SET joining_date = DATE_FORMAT(
STR_TO_DATE(joining_date,'%d-%m-%Y'),
'%Y-%m-%d')
WHERE joining_date REGEXP '^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
AND CAST(SUBSTRING_INDEX(joining_date,'-',1) AS UNSIGNED) >12;

-- finding actual mm-dd-yyyy
SELECT doctor_id, joining_date
FROM Doctors
WHERE joining_date REGEXP '^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
AND CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(joining_date,'-',2),'-',-1) AS UNSIGNED) >12;

UPDATE Doctors
SET joining_date = DATE_FORMAT(
STR_TO_DATE(joining_date,'%m-%d-%Y'),
'%Y-%m-%d')
WHERE joining_date REGEXP '^[0-9]{2}-[0-9]{2}-[0-9]{4}$'
AND CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(joining_date,'-',2),'-',-1) AS UNSIGNED) >12;

-- identifying remaining dates of not yyyy-mm-dd format - cannot be formatted as they are ambiguous
SELECT doctor_id, joining_date
FROM Doctors
WHERE joining_date NOT REGEXP '^[0-9]{4}-[0-9]{2}-[0-9]{2}$';

-- to get count of distinct values
SELECT gender, count(*)
FROM Patients
GROUP BY gender;

-- to update the standardized column in the table
UPDATE Patients
SET gender = CASE
WHEN LOWER(TRIM(gender)) IN ('male','m')
THEN 'Male'
WHEN LOWER(TRIM(gender)) IN ('female','f')
THEN 'Female'
ELSE gender
END;

-- find null values
SELECT * FROM Admissions;
SELECT admission_id, discharge_date
FROM Admissions
WHERE discharge_date IS NULL;

-- to get count of distinct values
SELECT gender, count(*)
FROM Employees
GROUP BY gender;

-- to update the standardized column in the table
UPDATE Employees
SET gender = CASE
WHEN LOWER(TRIM(gender)) IN ('male','m')
THEN 'Male'
WHEN LOWER(TRIM(gender)) IN ('female','f')
THEN 'Female'
ELSE gender
END;

-- filling blank values
SELECT * FROM Payments;
SELECT payment_mode, COUNT(*) AS freq
FROM Payments GROUP BY payment_mode
ORDER BY freq DESC;
UPDATE Payments
SET payment_mode = 'Net Banking'
WHERE payment_mode IS NULL;

-- checking incorrect email
SELECT doctor_id, email
FROM Doctors
WHERE email IS NOT NULL
AND email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';
ALTER TABLE Doctors
ADD COLUMN email_validation VARCHAR(10);
UPDATE Doctors
SET email_validation =
CASE
    WHEN email IS NULL THEN 'Missing'
    WHEN email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
        THEN 'Valid'
    ELSE 'Invalid'
END;

SELECT patient_id, email
FROM Patients
WHERE email IS NULL
   OR email NOT REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';
ALTER TABLE Patients
ADD COLUMN email_validation VARCHAR(10);
UPDATE Patients
SET email_validation =
CASE
    WHEN email IS NULL THEN 'Missing'
    WHEN email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'
        THEN 'Valid'
    ELSE 'Invalid'
END;

-- discharge date issues
SELECT admission_status, COUNT(*) AS frequency
FROM Admissions
WHERE discharge_date IS NULL
GROUP BY admission_status;
SELECT admission_id, discharge_date, admission_status
FROM Admissions
WHERE discharge_date IS NULL
  AND admission_status = 'Discharged';
SELECT *
FROM Admissions
WHERE discharge_date IS NOT NULL
  AND admission_status IN ('Admitted', 'Under Observation');
ALTER TABLE Admissions
ADD COLUMN discharge_validation VARCHAR(30);
UPDATE Admissions
SET discharge_validation =
CASE
    WHEN discharge_date IS NOT NULL
         AND admission_status <> 'Discharged'
        THEN 'Requires Review'
    ELSE 'Valid'
END;

-- incorrect total bill amount
SELECT bill_id,
       total_amount,
       (
           room_charges
         + doctor_charges
         + medicine_charges
         + lab_charges
         + other_charges
       ) AS calculated_total
FROM Billing
WHERE ABS(
    total_amount -
    (
        room_charges
      + doctor_charges
      + medicine_charges
      + lab_charges
      + other_charges
    )
) > 0.01;
UPDATE Billing
SET total_amount = ROUND(
      room_charges
    + doctor_charges
    + medicine_charges
    + lab_charges
    + other_charges,
    2
)
WHERE ABS(
    total_amount -
    (
        room_charges
      + doctor_charges
      + medicine_charges
      + lab_charges
      + other_charges
    )
) > 0.01;
ALTER TABLE Billing
MODIFY total_amount DECIMAL(10,2);
DESCRIBE Billing;

-- negative values in payment_amount
UPDATE Payments
SET payment_amount = ABS(CAST(payment_amount AS DECIMAL(10,2)))
WHERE CAST(payment_amount AS DECIMAL(10,2)) < 0;
ALTER TABLE Payments
ADD payment_condition VARCHAR(30);
UPDATE Payments p
JOIN Billing b
    ON p.bill_id = b.bill_id
SET p.payment_condition =
    CASE
        WHEN p.payment_status = 'Success'
             AND CAST(p.payment_amount AS DECIMAL(10,2)) = b.total_amount
            THEN 'Fully Paid'

        WHEN p.payment_status = 'Success'
             AND CAST(p.payment_amount AS DECIMAL(10,2)) < b.total_amount
            THEN 'Partially Paid'

        WHEN p.payment_status = 'Success'
             AND CAST(p.payment_amount AS DECIMAL(10,2)) > b.total_amount
            THEN 'Overpaid'

        WHEN p.payment_status = 'Refunded'
            THEN 'Refunded'

        WHEN p.payment_status = 'Failed'
            THEN 'Failed'
    END;
    
-- null values in treatments
SELECT treatment_status, COUNT(*) AS frequency
FROM Treatments
WHERE admission_id IS NULL
GROUP BY treatment_status;

-- duplicate paymenyt records
SELECT
    bill_id,
    COUNT(*) AS payment_count
FROM Payments
GROUP BY bill_id
HAVING COUNT(*) > 1;