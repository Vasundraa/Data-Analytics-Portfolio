# Test Cases – Nova University Student Management System

## 1. Purpose

This document defines functional and validation test scenarios for the console application. **“Expected result” describes the intended behavior.** A case should only be marked Passed after it has been run against the final `student_service_portal.py` version.

## 2. Test Data

Use disposable test records such as:

- Student A: `ST101`, department `CSE`, year `2025`
- Student B: `ST102`, department `IT`, year `2024`
- Student C: `ST103`, department `CSE`, year `2025`
- Courses: Python, SQL, Excel, Power BI

Use valid test email addresses and 10-digit phone numbers. These are sample records, not real student data.

## 3. Functional Test Cases

| ID | Scenario | Test Input / Steps | Expected Result | Status |
|---|---|---|---|---|
| TC-01 | Register a new student | Register `ST101` with valid details. | Record is created and success message appears. | Not yet verified |
| TC-02 | Duplicate student ID | Register `ST101`, then attempt to register `ST101` again. | Second registration is rejected. | Not yet verified |
| TC-03 | Blank student ID | Submit spaces or an empty ID. | Registration is rejected and asks for a valid ID. | Not yet verified |
| TC-04 | Search valid student | Search for `ST101`. | Correct student's details are displayed. | Not yet verified |
| TC-05 | Search unknown student | Search for `ST999`. | A not-found message appears; application continues. | Not yet verified |
| TC-06 | Invalid department selection | Enter a number outside the listed department range. | Invalid selection message and another prompt. | Not yet verified |
| TC-07 | Update student details | Change a student's name or department. | Updated value is stored and displayed. | Not yet verified |
| TC-08 | Change student ID | Change `ST101` to an unused ID. | Record is moved to the new ID and remains accessible. | Not yet verified |
| TC-09 | Duplicate new student ID | Attempt to change `ST101` to an ID already in use. | Change is rejected; original record remains intact. | Not yet verified |
| TC-10 | Register a course | Register a student for Python. | Python appears in the student's course set. | Not yet verified |
| TC-11 | Duplicate course registration | Register Python twice for the same student. | Duplicate is reported and the set contains one Python entry. | Not yet verified |
| TC-12 | Remove a course | Remove a registered course. | Course is removed; associated mark and one aggregate occurrence are removed if present. | Not yet verified |
| TC-13 | Invalid course selection | Enter a letter or out-of-range number. | Invalid selection is handled without crashing. | Not yet verified |
| TC-14 | Attendance below threshold | Set attendance to 74. | Student is Not Eligible. | Not yet verified |
| TC-15 | Attendance exactly at threshold | Set attendance to 75. | Student is Eligible. | Basic helper test passed previously; retest final file |
| TC-16 | Attendance upper boundary | Enter 100. | Value is accepted. | Not yet verified |
| TC-17 | Invalid attendance | Enter -1, 101, or alphabetic input. | Value is rejected and prompt repeats. | Not yet verified |
| TC-18 | Enter marks | Register Python and enter a mark such as 85. | Mark is stored and aggregate list is updated. | Basic helper test passed previously; retest final file |
| TC-19 | Invalid marks | Enter -1, 101, or alphabetic input. | Mark is rejected and prompt repeats. | Not yet verified |
| TC-20 | Update marks | Change a student's Python mark from 80 to 95. | Student record changes; one old aggregate occurrence is removed and new mark appended. | Basic helper test passed previously; retest final file |
| TC-21 | Enter marks for newly registered course | Add a course after entering other marks; enter missing course mark. | Only the missing course mark is requested and stored. | Basic helper test passed previously; retest final file |
| TC-22 | Grade boundary F | Evaluate mark 49. | Grade F. | Basic helper test passed previously; retest final file |
| TC-23 | Grade boundary E | Evaluate mark 50. | Grade E. | Basic helper test passed previously; retest final file |
| TC-24 | Grade boundary A | Evaluate mark 90. | Grade A. | Basic helper test passed previously; retest final file |
| TC-25 | Complete passing result | Enter marks of at least 50 for every registered course. | Result is complete and Pass. | Not yet verified |
| TC-26 | Failed result | Enter a mark below 50 for one registered course and complete all marks. | Result status is Fail and failed subject is identified. | Not yet verified |
| TC-27 | Incomplete result | Register multiple courses but leave at least one without a mark. | Result is labelled Incomplete, not a final pass/fail. | Not yet verified |
| TC-28 | Course overlap intersection | Enroll two students in both Python and SQL. | Both student IDs appear in the intersection. | Not yet verified |
| TC-29 | Course overlap difference | Enroll a student in Python but not SQL. | Student appears in Python-minus-SQL output. | Not yet verified |
| TC-30 | Course overlap union | Have students in either or both courses. | All IDs in either course appear once. | Not yet verified |
| TC-31 | Symmetric difference | Have students in only one of the two courses. | Only exclusive members are shown. | Not yet verified |
| TC-32 | Disjoint groups | Ensure no active student is enrolled in both selected courses. | Application reports the groups are completely different. | Not yet verified |
| TC-33 | Withdraw a student | Confirm withdrawal for an active student. | Status changes to Withdrawn; historical record remains; active processing excludes the student. | Basic helper test passed previously; retest final file |
| TC-34 | Withdraw same student again | Attempt to withdraw an already withdrawn student. | Already-withdrawn message appears. | Not yet verified |
| TC-35 | Highest and lowest average | Create at least two students with complete marks and different averages. | Correct student/average is displayed for each option. | Not yet verified |
| TC-36 | Empty statistics | Open statistics before registering any students. | No-data or zero-count output; no crash. | Not yet verified |
| TC-37 | Department student listing | Select a department with and without active students. | Matching active students appear, or a no-students message. | Not yet verified |
| TC-38 | Course participation | Select a course. | Only active students registered for that course are listed. | Not yet verified |
| TC-39 | Invalid main-menu choice | Enter an unsupported choice. | Invalid-choice message appears; menu repeats. | Not yet verified |
| TC-40 | Multiple operations in one session | Register student, add course, enter marks, view result, return to menu. | Each operation works without restarting the application. | Not yet verified |
| TC-41 | Exit | Select main-menu option 10. | Exit message appears and program terminates. | Main-menu startup/exit test passed previously; retest final file |

## 4. Input Validation Tests

| Field | Invalid Inputs | Expected Behavior |
|---|---|---|
| Admission year | Letters, fewer/more than four digits, below 1900, above 2100 | Reject input and prompt again. |
| Email | Missing `@`, missing domain suffix, spaces | Reject input and prompt again. |
| Phone number | Letters, fewer/more than 10 digits | Reject input and prompt again. |
| Attendance | Negative number, greater than 100, text | Reject input and prompt again. |
| Marks | Negative number, greater than 100, text | Reject input and prompt again. |
| Menu choice | Unsupported number or text | Show invalid-choice message and continue. |

## 5. Previously Performed Checks

During development, the following focused checks were reported as performed on a prior corrected version:

- Python syntax compilation.
- Main-menu startup and exit.
- Aggregate list consistency for a mark update where two students shared the same mark.
- Adding a mark for a newly registered course.
- Removing a course and its associated mark.
- Retaining a withdrawn student's historical mark while excluding it from active records.
- Grade boundary checks for 49, 50, and 90.
- Eligibility at exactly 75% attendance.

**Important:** Re-run these checks against the exact `student_service_portal.py` included in this submission before marking the corresponding cases Passed. The full set of cases above has not been exhaustively executed.

## 6. Test Execution Record

When testing the final submission, record the date, Python version, actual output, and result for each case. Replace “Not yet verified” with “Passed” or “Failed” only after execution. For failures, include the observed behavior and the correction made.
