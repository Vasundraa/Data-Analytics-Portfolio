#BRD Questions

# 1. Which clinics receive the highest consultation activity?
SELECT
    c.clinic_id,
    cl.clinic_name,
    COUNT(c.consultation_id) AS consultation_count
FROM Consultations c
JOIN Clinics cl
    ON c.clinic_id = cl.clinic_id
GROUP BY
    c.clinic_id,
    cl.clinic_name
ORDER BY consultation_count DESC;

# 2. Which specialists have the highest consultation workload?
SELECT
    s.specialist_id,
    CONCAT(s.first_name, ' ', s.last_name) AS specialist_name,
    s.specialization,
    COUNT(c.consultation_id) AS consultation_count
FROM Specialists s
JOIN Consultations c
    ON s.specialist_id = c.specialist_id
GROUP BY
    s.specialist_id,
    specialist_name,
    s.specialization
ORDER BY consultation_count DESC;

# 3. Which specializations have the highest activity?
SELECT
    s.specialization,
    COUNT(c.consultation_id) AS consultation_count
FROM Specialists s
JOIN Consultations c
    ON s.specialist_id = c.specialist_id
GROUP BY s.specialization
ORDER BY consultation_count DESC;

# 4. Which members are the most active healthcare users?
SELECT
    m.member_id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.membership_type,
    COUNT(c.consultation_id) AS consultation_count
FROM Members m
JOIN Consultations c
    ON m.member_id = c.member_id
GROUP BY
    m.member_id,
    member_name,
    m.membership_type
ORDER BY consultation_count DESC;

# 5. How do consultation modes compare?
SELECT
    consultation_mode,
    COUNT(*) AS consultation_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Consultations),
        2
    ) AS percentage
FROM Consultations
GROUP BY consultation_mode
ORDER BY consultation_count DESC;

# 6. Which consultation statuses require attention?
SELECT
    status,
    COUNT(*) AS consultation_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Consultations),
        2
    ) AS percentage
FROM Consultations
GROUP BY status
ORDER BY consultation_count DESC;

# 7. How many telemedicine sessions are completed, cancelled, or in other statuses?
SELECT
    session_status,
    COUNT(*) AS session_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Telemedicine_Sessions),
        2
    ) AS percentage
FROM Telemedicine_Sessions
GROUP BY session_status
ORDER BY session_count DESC;

# 8. Which telemedicine platforms and connection-quality categories are most common?
SELECT
    platform,
    connection_quality,
    COUNT(*) AS session_count
FROM Telemedicine_Sessions
GROUP BY
    platform,
    connection_quality
ORDER BY session_count DESC;

# 9. What is the average telemedicine session duration?
SELECT
    ROUND(
        AVG(
            TIMESTAMPDIFF(
                MINUTE,
                session_start_time,
                session_end_time
            )
        ),
        2
    ) AS avg_session_duration_minutes
FROM Telemedicine_Sessions
WHERE session_start_time IS NOT NULL
  AND session_end_time IS NOT NULL;
  
# 10. Which chronic conditions have the highest program enrollment?
SELECT
    condition_name,
    COUNT(*) AS program_enrollment
FROM Chronic_Care_Programs
GROUP BY condition_name
ORDER BY program_enrollment DESC;

# 11. Which specialists manage the most chronic-care programs?
SELECT
    s.specialist_id,
    CONCAT(s.first_name, ' ', s.last_name) AS specialist_name,
    s.specialization,
    COUNT(ccp.program_id) AS chronic_care_programs
FROM Specialists s
JOIN Chronic_Care_Programs ccp
    ON s.specialist_id = ccp.specialist_id
GROUP BY
    s.specialist_id,
    specialist_name,
    s.specialization
ORDER BY chronic_care_programs DESC;

# 12. Which health packages have the highest subscription volume?
SELECT
    hp.package_id,
    hp.package_name,
    hp.package_type,
    COUNT(ps.subscription_id) AS subscription_count
FROM Health_Packages hp
JOIN Package_Subscriptions ps
    ON hp.package_id = ps.package_id
GROUP BY
    hp.package_id,
    hp.package_name,
    hp.package_type
ORDER BY subscription_count DESC;

# 13. Which subscriptions are approaching or have passed expiry?
SELECT
    ps.subscription_id,
    m.member_id,
    hp.package_name,
    ps.subscription_date,
    ps.expiry_date,
    ps.payment_status,
    CASE
        WHEN ps.expiry_date < CURDATE() THEN 'Expired'
        WHEN ps.expiry_date <= DATE_ADD(CURDATE(), INTERVAL 30 DAY)
            THEN 'Expiring within 30 days'
        ELSE 'Active'
    END AS subscription_status
FROM Package_Subscriptions ps
JOIN Members m
    ON ps.member_id = m.member_id
JOIN Health_Packages hp
    ON ps.package_id = hp.package_id
ORDER BY ps.expiry_date;

# 14. Which corporates contribute the most enrolled members?
SELECT
    c.corporate_id,
    c.company_name,
    c.industry,
    c.employee_count,
    COUNT(cm.corporate_member_id) AS enrolled_members
FROM Corporates c
JOIN Corporate_Members cm
    ON c.corporate_id = cm.corporate_id
GROUP BY
    c.corporate_id,
    c.company_name,
    c.industry,
    c.employee_count
ORDER BY enrolled_members DESC;

# 15. Which industries have the greatest corporate healthcare participation?
SELECT
    c.industry,
    COUNT(cm.corporate_member_id) AS enrolled_members
FROM Corporates c
JOIN Corporate_Members cm
    ON c.corporate_id = cm.corporate_id
GROUP BY c.industry
ORDER BY enrolled_members DESC;

# 16. Which medicines are prescribed most frequently?
SELECT
    medicine_name,
    COUNT(*) AS prescription_count
FROM Prescriptions
GROUP BY medicine_name
ORDER BY prescription_count DESC;

# 17. Which specialists generate the highest prescription volume?
SELECT
    s.specialist_id,
    CONCAT(s.first_name, ' ', s.last_name) AS specialist_name,
    s.specialization,
    COUNT(p.prescription_id) AS prescription_count
FROM Specialists s
JOIN Prescriptions p
    ON s.specialist_id = p.specialist_id
GROUP BY
    s.specialist_id,
    specialist_name,
    s.specialization
ORDER BY prescription_count DESC;

# 18. Which lab tests generate the highest total cost?
SELECT
    test_name,
    COUNT(*) AS test_count,
    SUM(test_cost) AS total_test_cost
FROM Lab_Tests
GROUP BY test_name
ORDER BY total_test_cost DESC;

# 19. Which clinics have the highest laboratory workload?
SELECT
    c.clinic_id,
    c.clinic_name,
    COUNT(lt.lab_test_id) AS lab_test_count
FROM Clinics c
JOIN Lab_Tests lt
    ON c.clinic_id = lt.clinic_id
GROUP BY
    c.clinic_id,
    c.clinic_name
ORDER BY lab_test_count DESC;

# 20. Which insurance providers have the highest claim amount?
SELECT
    insurance_provider,
    COUNT(claim_id) AS claim_count,
    SUM(claim_amount) AS total_claim_amount
FROM Claims
GROUP BY insurance_provider
ORDER BY total_claim_amount DESC;

# 21. What is the distribution of claim statuses?
SELECT
    claim_status,
    COUNT(*) AS claim_count,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Claims),
        2
    ) AS percentage
FROM Claims
GROUP BY claim_status
ORDER BY claim_count DESC;

# 22. What is the total billed amount and how is it split among consultation, laboratory, and medicine charges?
SELECT
    ROUND(SUM(consultation_charges), 2) AS total_consultation_charges,
    ROUND(SUM(lab_charges), 2) AS total_lab_charges,
    ROUND(SUM(medicine_charges), 2) AS total_medicine_charges,
    ROUND(SUM(total_amount), 2) AS total_billed_amount
FROM Billing;

# 23. What is the total payment amount by payment status and payment mode?
SELECT
    payment_status,
    payment_mode,
    COUNT(*) AS payment_count,
    ROUND(SUM(payment_amount), 2) AS total_payment_amount
FROM Payments
GROUP BY
    payment_status,
    payment_mode
ORDER BY total_payment_amount DESC;

# 24. What is the validated collection gap?
SELECT
    ROUND((SELECT SUM(total_amount) FROM Billing), 2) AS total_billed_amount,
    ROUND((SELECT SUM(payment_amount) FROM Payments), 2) AS total_payment_amount,
    ROUND(
        (SELECT SUM(total_amount) FROM Billing)
        -
        (SELECT SUM(payment_amount) FROM Payments),
        2
    ) AS collection_gap;
    
# 25. Which clinics or specialists receive the highest and lowest average feedback ratings?
SELECT
    s.specialist_id,
    CONCAT(s.first_name, ' ', s.last_name) AS specialist_name,
    s.specialization,
    COUNT(f.feedback_id) AS feedback_count,
    ROUND(AVG(f.rating), 2) AS average_rating
FROM Specialists s
JOIN Consultations c
    ON s.specialist_id = c.specialist_id
JOIN Feedback f
    ON c.consultation_id = f.consultation_id
GROUP BY
    s.specialist_id,
    specialist_name,
    s.specialization
ORDER BY average_rating DESC;

# 26. Are there members with consultations but no feedback?
SELECT
    m.member_id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    COUNT(DISTINCT c.consultation_id) AS consultation_count
FROM Members m
JOIN Consultations c
    ON m.member_id = c.member_id
LEFT JOIN Feedback f
    ON c.consultation_id = f.consultation_id
WHERE f.feedback_id IS NULL
GROUP BY
    m.member_id,
    member_name
ORDER BY consultation_count DESC;

# 27. Are there registered members with no consultations?
SELECT
    m.member_id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.membership_type
FROM Members m
LEFT JOIN Consultations c
    ON m.member_id = c.member_id
WHERE c.consultation_id IS NULL
ORDER BY m.member_id;

# 28. Which business areas show high activity but weak financial or experience indicators?
SELECT
    cl.clinic_id,
    cl.clinic_name,
    COUNT(DISTINCT c.consultation_id) AS consultation_count,
    ROUND(AVG(f.rating), 2) AS average_rating,
    ROUND(SUM(b.total_amount), 2) AS total_billed_amount
FROM Clinics cl
LEFT JOIN Consultations c
    ON cl.clinic_id = c.clinic_id
LEFT JOIN Feedback f
    ON c.consultation_id = f.consultation_id
LEFT JOIN Billing b
    ON c.consultation_id = b.consultation_id
GROUP BY
    cl.clinic_id,
    cl.clinic_name
ORDER BY consultation_count DESC;

# 29. Which reasons for visit occur most frequently?
SELECT
    reason_for_visit,
    COUNT(*) AS consultation_count
FROM Consultations
GROUP BY reason_for_visit
ORDER BY consultation_count DESC;