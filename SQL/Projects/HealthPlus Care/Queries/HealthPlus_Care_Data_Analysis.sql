# ANALYSIS

# How many members are registered - KPI
Select count(*) AS total_members
from Members;

# How many specialists are in each specialization
Select specialization,count(*) as specialist_count
from Specialists
group by specialization
order by specialist_count desc;

# specialists more than 10 years of experience
select *
from Specialists
where experience_years > 10;

# average consultation fee - KPI
select ROUND(AVG(consultation_fee), 2) as avg_consultation_fee
from Specialists;

# highest consultation fee
select max(consultation_fee) as highest_fee
from Specialists;

# top 5 specializations based on specialists - KPI
select specialization,COUNT(*) as specialist_count
from Specialists
group by specialization
order by specialist_count desc
limit 5;

#consultations for each status - KPI
select status,COUNT(*) as consultation_count
from Consultations
group by status
order by consultation_count desc;

# How many consultations does  have each specialist - KPI
select s.specialist_id,s.first_name,COUNT(c.consultation_id) as consultation_count
from Specialists s
LEFT JOIN Consultations c
ON s.specialist_id = c.specialist_id
group by s.specialist_id
order by consultation_count desc;

# Each specialist along with their clinic
select s.first_name,c.clinic_name
from Specialists s
INNER JOIN Clinics c
ON s.clinic_id = c.clinic_id;

# total cost of all laboratory tests - KPI
select SUM(test_cost) AS total_lab_cost
from Lab_Tests;

# total amount of insurance claims - KPI
select SUM(claim_amount) as total_claim_amount
from Claims;

# total claim amount for each insurance provider
select insurance_provider,SUM(claim_amount) as total_claim_amount
from Claims
group by insurance_provider
order by total_claim_amount DESC;