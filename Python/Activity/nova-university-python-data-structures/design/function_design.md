# Function Design

Functions separate the application into smaller responsibilities. Menu functions manage user interaction; helper functions perform validation, lookups, calculations, and updates.

## 1. Menu Functions

| Function | Responsibility | Main Inputs | Main Effect / Output |
|---|---|---|---|
| `studentRegistrationMenu()` | Add, display, and update student records. | Console choices and student details | Updates `students`; prints messages. |
| `studentSearchMenu()` | Search for a student by ID. | Student ID | Displays the record or a not-found message. |
| `studentCourseRegistrationMenu()` | Manage course registration, display, removal, and overlap analysis. | Student ID and course/menu choices | Updates course sets and displays results. |
| `studentAttendanceMenu()` | Update attendance, check eligibility, list ineligible students, and show counts. | Student ID, attendance, menu choice | Updates attendance or prints eligibility information. |
| `studentsMarksMenu()` | Enter/retrieve/update marks and display academic summaries or subject aggregates. | Student ID and course/mark choices | Updates marks and prints calculations. |
| `studentResultMenu()` | Display an individual result or process all active students. | Student ID or bulk-processing choice | Prints grades, averages, eligibility, and result status. |
| `departmentInfoMenu()` | Display available departments and students by department. | Menu and department choices | Prints department information and matching students. |
| `studentStatisticsMenu()` | Produce counts, averages, failure counts, batch statistics, and course participation. | Statistics option and optional batch/course selection | Prints calculated statistics. |
| `studentWithdrawalMenu()` | Confirm and record student withdrawal. | Student ID and confirmation | Changes academic status and adjusts aggregates. |
| `courseOverlapAnalysis()` | Compare active participant groups for two courses. | Two course names and analysis choice | Prints matching student groups or disjointness status. |

## 2. Student and Course Helpers

| Function | Responsibility | Parameters | Return / Side Effect |
|---|---|---|---|
| `getStudentDetails()` | Collect and validate a new student's details. | None | Returns a student dictionary. |
| `displayStudentDetails()` | Display all stored student records. | None | Prints records. |
| `displayStudentRecord(studentId)` | Display one student record. | `studentId` | Prints a record if called with an existing ID. |
| `updateStudentDetails(studentId)` | Repeatedly offer fields to update. | `studentId` | Mutates the student's record; can change the dictionary key when ID changes. |
| `studentExist(studentId)` | Check whether an ID is in `students`. | `studentId` | Returns a Boolean. |
| `getDepartment()` | Present department choices and validate the selection. | None | Returns a department code. |
| `registerCourse(courseList)` | Add selected courses without duplicates. | A student's course set | Mutates and returns the set. |
| `removeCourse(studentId)` | Remove a registered course and associated mark if present. | `studentId` | Mutates the student's course set, marks, and subject aggregate list. |
| `isActiveStudent(studentId)` | Check whether a stored student has active status. | `studentId` | Returns a Boolean. |

## 3. Marks and Result Helpers

| Function | Responsibility | Parameters | Return / Side Effect |
|---|---|---|---|
| `getMarks(studentId)` | Collect marks for registered courses missing marks. | `studentId` | Updates student's marks and aggregate lists; returns number of courses filled. |
| `addMarkToGlobalList(course, mark)` | Append a mark to the relevant subject aggregate list. | Course name and mark | Mutates one aggregate list. |
| `removeMarkFromGlobalList(course, mark)` | Remove one matching occurrence from a subject aggregate list. | Course name and mark | Mutates one aggregate list when a match exists. |
| `updateMarks(studentId, courseList, choice)` | Replace the selected subject mark. | Student ID, course list, 1-based choice | Updates student's marks and aggregate lists. |
| `totalMarks(studentId)` | Sum marks currently stored for a student. | `studentId` | Returns an integer total. |
| `avgMarks(marks, studentId)` | Divide the supplied total by the number of marks entered. | Total and student ID | Returns a float; returns `0.0` when no marks exist. |
| `examResult(mark)` | Map a mark to its grade. | Numeric mark | Returns A, B, C, D, E, or F. |
| `hasCompleteMarks(studentId)` | Check whether a student has courses and a mark for every registered course. | `studentId` | Returns a Boolean. |
| `studentResultStatus(studentId)` | Determine Pass, Fail, or Incomplete. | `studentId` | Returns a status string. |
| `checkSemesterEligibility(studentId)` | Apply the 75% attendance rule. | `studentId` | Returns a Boolean. |

## 4. Validation Functions

| Function | Responsibility | Return |
|---|---|---|
| `validateYear()` | Accept a four-digit year between 1900 and 2100. | Integer year |
| `validateEmail()` | Check an email against a basic regular expression. | Email string |
| `validatePhoneNumber()` | Require exactly 10 digits. | Phone-number string |
| `validateAttendance()` | Require an integer percentage from 0 to 100. | Integer percentage |
| `validateMark(course)` | Require a whole-number mark from 0 to 100. | Integer mark |

## 5. Function Design Notes

- Menu functions use loops so users can perform multiple operations before returning to the main menu.
- Validation functions repeat prompts until acceptable input is provided.
- `studentExist()` and `isActiveStudent()` centralize repeated checks.
- Calculation functions are reused by individual results, bulk results, and statistics.
- The program is procedural and does not define custom classes, consistent with the project's implementation approach.
