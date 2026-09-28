# CLEANING

# Members data cleaning

UPDATE Members
set gender=
CASE
WHEN lower(trim(gender)) in ('male','m')
THEN 'Male'
WHEN lower(trim(gender)) in ('female','f')
THEN 'Female'
ELSE gender
END;

set sql_safe_updates=0;

update Members 
set email=
CASE
WHEN email like '%gmail' and email not like '%@%'
THEN REPLACE(email,'gmail','@gmail')
END
where email not like '%@%.%';

UPDATE Consultations
SET status =
CASE
    WHEN LOWER(TRIM(status)) = 'completed' THEN 'Completed'
    WHEN LOWER(TRIM(status)) = 'cancelled' THEN 'Cancelled'
    WHEN LOWER(TRIM(status)) = 'scheduled' THEN 'Scheduled'
    WHEN LOWER(TRIM(status)) = 'no-show' THEN 'No-Show'
    ELSE status
END;

ALTER TABLE Consultations
MODIFY consultation_date DATE NOT NULL;

UPDATE Billing
SET total_amount =
    consultation_charges
    + lab_charges
    + medicine_charges
WHERE total_amount < 0;

UPDATE Payments
SET payment_amount = ABS(payment_amount)
WHERE payment_amount < 0;

SELECT
    payment_mode,
    COUNT(*) AS frequency
FROM Payments
WHERE payment_mode IS NOT NULL
GROUP BY payment_mode
ORDER BY frequency DESC
LIMIT 1;
UPDATE Payments
SET payment_mode = 'Cash'
WHERE payment_mode IS NULL;

UPDATE Claims
SET insurance_provider = 'Unknown'
WHERE insurance_provider IS NULL;

ALTER TABLE Members
ADD COLUMN email_status VARCHAR(10);
UPDATE Members
SET email_status =
CASE
    WHEN email IS NULL THEN 'Invalid'
    WHEN email NOT LIKE '%@%.%' THEN 'Invalid'
    WHEN email LIKE '%@@%' THEN 'Invalid'
    ELSE 'Valid'
END;

UPDATE Claims
SET insurance_provider = 'Unknown'
WHERE insurance_provider IS NULL;