# Business Requirements

## 1. Application Name
**Nova University – Student Management & Academic Service System**

## 2. Business Purpose
Provide university administration staff with a single console-based application to maintain student records and perform common academic service activities.

## 3. Problem Statement
Student details, course registrations, attendance, marks, and results need to be managed consistently. A menu-driven application can reduce repetitive manual work, prevent common data-entry errors, and make basic academic information easier to retrieve and summarize.

## 4. Scope

### In scope
- Student registration, search, display, and update.
- Department selection and department-wise student listing.
- Course registration, display, removal, and overlap analysis.
- Attendance updates and examination eligibility checks.
- Marks entry, retrieval, updates, totals, averages, grades, and result processing.
- Student statistics and course participation reports.
- Student withdrawal while retaining historical information.
- Input validation and a persistent menu loop during one run.

### Out of scope
- Graphical interface or web/mobile application.
- Database or permanent file-based storage.
- Authentication, roles, and access control.
- Sending email or SMS notifications.
- Integration with external university systems.

## 5. Functional Requirements

| ID | Requirement |
|---|---|
| BR-01 | Register a student using a unique, non-blank student ID. |
| BR-02 | Store and display name, department, admission year, email, phone number, attendance, courses, marks, and academic status. |
| BR-03 | Search for a student by ID and report when the ID is unknown. |
| BR-04 | Update student information, including the student ID when the new ID is unused. |
| BR-05 | Offer only the configured departments: CSE, IT, AI&DS, ECE, and BBA. |
| BR-06 | Register multiple courses for a student without duplicate course enrollment. |
| BR-07 | Display and remove a student's registered courses. |
| BR-08 | Compare course participant groups using intersection, difference, union, symmetric difference, and disjointness. |
| BR-09 | Store attendance and allow attendance updates. |
| BR-10 | Determine semester examination eligibility from the attendance threshold. |
| BR-11 | Enter and update marks for Python, SQL, Excel, and Power BI for courses registered by the student. |
| BR-12 | Display marks and academic summaries, including totals, averages, grades, and failed subjects. |
| BR-13 | Process an individual result or the results of all active students. |
| BR-14 | Generate active-student, department, eligibility, failure, average, batch, and course participation statistics. |
| BR-15 | Withdraw a student without permanently deleting the student's record. |
| BR-16 | Validate menu choices and user-provided data. |
| BR-17 | Allow multiple operations in the same program session and provide an exit option. |

## 6. Business Rules

1. Student IDs must be unique and cannot be blank.
2. The supported departments are CSE, IT, AI&DS, ECE, and BBA.
3. The supported courses are Python, SQL, Excel, and Power BI.
4. A student cannot register for the same course twice.
5. Attendance must be a whole number from 0 through 100.
6. Attendance of 75% or more qualifies a student for semester examination eligibility.
7. Marks must be whole numbers from 0 through 100.
8. Grade boundaries are A: 90–100, B: 80–89, C: 70–79, D: 60–69, E: 50–59, and F: below 50.
9. A student is considered to have failed if any registered subject mark is below 50.
10. A result is incomplete if the student has no registered courses or is missing a mark for any registered course.
11. Averages are calculated from marks entered. Incomplete results are not treated as final.
12. Withdrawn students are excluded from active-student operations and statistics; their historical record remains accessible.
13. Subject-level mark lists are aggregate lists, not student-to-mark mappings. Updating/removing a mark or withdrawing a student adjusts the aggregate list.
14. Data is stored in memory only and is lost when the program ends.

## 7. Data Validation Rules

| Field | Rule |
|---|---|
| Student ID | Non-blank and unique |
| Name | Cannot be blank |
| Department | Must be selected from the configured department list |
| Admission year | Four-digit year from 1900 to 2100 |
| Email | Must match the application's basic email pattern |
| Phone number | Exactly 10 digits |
| Attendance | Whole number from 0 to 100 |
| Marks | Whole number from 0 to 100 |
| Menu/course/batch choices | Must be a valid listed option |

## 8. Assumptions and Limitations

- A single user operates the console application.
- Student data does not persist between program runs.
- Email validation checks format only, not whether an address exists.
- Phone validation assumes a 10-digit number and does not validate country codes.
- Aggregate subject lists are maintained for calculations; they do not independently identify which student owns each mark.
- The grade is based on the average of entered marks when the result is complete.
- The implementation uses whole-number marks and attendance percentages.
