# Input – Process – Output (IPO)

This document describes the principal inputs, processing steps, and outputs of the Nova University Student Management & Academic Service System.

## 1. Main Menu

| Input | Process | Output |
|---|---|---|
| Main-menu choice (1–10) | Validate the choice and call the corresponding menu function. Repeat until Exit is selected. | Selected service menu or invalid-choice message; exit confirmation when requested. |

## 2. Student Registration and Maintenance

| Input | Process | Output |
|---|---|---|
| Student ID and personal details | Check that the ID is non-blank and unique; validate name, department, year, email, and phone; store the record in `students`. | Success message or validation/duplicate error. |
| Student ID for search | Check whether the ID exists in the dictionary. | Student record or “does not exist” message. |
| Existing student ID and update selection | Confirm the student exists and is active; validate the new value; update the record. If changing ID, check uniqueness and move the record to the new key. | Updated record or error message. |

## 3. Course Registration

| Input | Process | Output |
|---|---|---|
| Student ID and course selection | Confirm student exists and is active; map the numeric selection to a configured course; add to the student's course set only if not already present. | Updated registered-course set or duplicate/invalid-choice message. |
| Student ID and course removal selection | Remove the course from the student's set; if marks exist for that course, remove the mark and adjust the corresponding aggregate list. | Course removal confirmation or error. |
| Two course names and analysis option | Build active-student ID sets for each course and apply the selected set operation. | Matching student IDs and names, or a message that no students match. |

## 4. Attendance and Eligibility

| Input | Process | Output |
|---|---|---|
| Student ID and attendance percentage | Confirm active student and course enrollment; validate 0–100; update attendance. | Attendance update confirmation. |
| Student ID | Compare attendance with the 75% threshold. | Eligible or Not Eligible. |
| Request for students below threshold | Iterate over active students and check eligibility. | Table of students below the threshold or a no-match message. |
| Attendance summary request | Count active students and eligible students. | Active and eligible student counts. |

## 5. Marks and Results

| Input | Process | Output |
|---|---|---|
| Student ID and marks for missing registered courses | Validate each mark; store it under the course key in the student's `marks` dictionary; append it to the relevant subject aggregate list. | Marks-entry confirmation or message that all registered courses already have marks. |
| Student ID and course selection | Retrieve or update the relevant subject mark. For updates, replace the student's mark and adjust the aggregate list. | Subject mark, updated mark, or validation message. |
| Student ID | Sum entered marks, calculate average, assign grade, identify marks below 50, and check completeness. | Academic summary and complete/incomplete result status. |
| Request to process all active students | Iterate over active records; calculate eligibility and result fields; avoid treating incomplete marks as final. | Tabular report for active students. |

## 6. Department Information and Statistics

| Input | Process | Output |
|---|---|---|
| Department selection | Validate the selection and filter active students by department. | Department details and matching students. |
| Statistics option | Count/filter active records or calculate averages and subject-level aggregates as appropriate. | Requested statistic or no-data message. |
| Admission-batch selection | Collect distinct active-student years; validate selected year; average available marks by subject for that batch. | Per-subject counts and averages. |
| Course selection | Filter active students whose course set contains the selected course. | Course participants and count. |

## 7. Student Withdrawal

| Input | Process | Output |
|---|---|---|
| Student ID and confirmation | Confirm the record exists and is not already withdrawn. On confirmation, adjust subject aggregate lists and change academic status to `Withdrawn`; retain the record and marks as history. | Withdrawal confirmation or cancellation message. |

## 8. Important Processing Rules

- Invalid numeric menu choices are handled before indexing a list.
- Missing students are reported instead of being accessed as if present.
- Attendance eligibility is `attendance >= 75`.
- Grade thresholds follow the scale documented in `business_requirements.md`.
- Incomplete records are identified instead of presenting an incomplete average as a final result.
- Withdrawn students remain searchable for historical information but are filtered out of active processing.
