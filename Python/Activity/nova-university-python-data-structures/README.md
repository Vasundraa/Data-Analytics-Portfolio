# Nova University – Student Management System

## 1. Application Overview

**Nova University Student Management System** is a console-based application developed using Python to manage student information and academic activities. It supports student registration, course enrollment, attendance tracking, marks management, result processing, department information, and student statistics.

The application uses Python data structures and functions to organize records, perform calculations, validate inputs, and process student information without requiring a database or graphical user interface.

## 2. Problem Statement

Managing student records and academic information manually can lead to duplication, calculation errors, and difficulties in tracking student performance. This application addresses these challenges by providing a centralized, menu-driven system for maintaining student records and performing academic operations efficiently.

It also demonstrates the practical application of Python concepts such as dictionaries, sets, lists, functions, loops, conditional statements, and input validation.

## 3. Features Implemented

- **Student Registration:** Add students and maintain their personal and academic information.
- **Student Search:** Search for students using their unique student ID.
- **Student Information Management:** View and update student details, including name, department, admission year, email, and phone number.
- **Course Registration:** Register students for courses, prevent duplicate enrollment, display registered courses, and remove courses.
- **Course Overlap Analysis:** Identify students enrolled in both courses, only one course, at least one course, or completely separate student groups using set operations.
- **Attendance Management:** Update attendance, check examination eligibility, and identify students below the required attendance percentage.
- **Marks Management:** Enter and update marks for Python, SQL, Excel, and Power BI.
- **Academic Summary:** Calculate total and average marks, display subject-wise marks, and identify failed subjects.
- **Result Processing:** Calculate grades, determine pass/fail status, view individual results, and process results for all active students.
- **Department Information:** Display available departments and list students belonging to a selected department.
- **Student Statistics:** Calculate active student counts, department-wise counts, examination eligibility, failed students, highest and lowest average marks, batch-wise subject averages, unique departments, and course participation.
- **Student Withdrawal:** Mark students as withdrawn while retaining their historical records and excluding them from active student processing.
- **Input Validation:** Validate student details, email addresses, phone numbers, admission years, attendance percentages, marks, and menu selections.

## 4. Business Rules

- Every student must have a unique, non-blank student ID.
- Students can belong to one of the predefined departments: CSE, IT, AI&DS, ECE, or BBA.
- A student cannot register for the same course more than once.
- Only active students can register for courses, update academic details, enter marks, or undergo active academic processing.
- Attendance must be between 0 and 100. Students with attendance of **75% or above** are eligible for semester examinations.
- Marks must be whole numbers between 0 and 100.
- Grades are assigned according to the following scale:

| Marks | Grade |
|---|---|
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| 50–59 | E |
| Below 50 | F |

- A student fails if at least one registered subject has a mark below 50.
- A result is considered incomplete when marks are missing for any registered course.
- Student averages are calculated using the marks actually entered. Incomplete results are not treated as final.
- Withdrawn students are excluded from active student statistics and processing, but their historical information is retained.
- Subject-level aggregate lists are maintained for calculating overall subject averages and highest marks among active students.

## 5. Data Structures Used

| Data Structure | Purpose | Reason for Selection |
|---|---|---|
| Dictionary (`students`) | Stores student records using student IDs as keys. | Provides efficient access, searching, and updating of individual student records. |
| Dictionary (individual student record) | Stores name, department, year, contact details, attendance, courses, marks, and academic status. | Organizes related information into a single student record. |
| Set (`coursesRegistered`) | Stores the courses registered by each student. | Prevents duplicate enrollment and supports set operations for course overlap analysis. |
| Dictionary (`marks`) | Stores subject names and their corresponding marks for each student. | Allows subject-wise mark retrieval and updates. |
| Lists (`pythonMarks`, `sqlMarks`, `excelMarks`, `powerBIMarks`) | Maintain subject-level aggregate marks for active students. | Support calculations such as average and highest marks for each subject. |
| Tuple (`courses`) | Stores the predefined list of available courses. | Keeps the course collection fixed during program execution. |
| Lists and sets created during processing | Store temporary results such as eligible students, failed students, unique departments, and course overlaps. | Simplify filtering, counting, comparison, and reporting operations. |

## 6. Functions and Responsibilities

The application is organized into functions to improve readability, reduce code repetition, and separate individual operations.

### Menu Functions

- `studentRegistrationMenu()` – Handles student registration, information display, and updates.
- `studentSearchMenu()` – Provides student search functionality.
- `studentCourseRegistrationMenu()` – Manages course enrollment and course-related operations.
- `studentAttendanceMenu()` – Handles attendance updates and examination eligibility.
- `studentsMarksMenu()` – Manages marks entry, updates, summaries, and subject-level calculations.
- `studentResultMenu()` – Displays individual results and processes active student results.
- `departmentInfoMenu()` – Displays departments and department-wise student information.
- `studentStatisticsMenu()` – Generates student and academic statistics.
- `studentWithdrawalMenu()` – Handles student withdrawal while retaining records.
- `courseOverlapAnalysis()` – Performs course comparisons using set operations.

### Student and Course Management

- `getStudentDetails()` – Collects and returns validated student information.
- `displayStudentDetails()` – Displays all student records.
- `displayStudentRecord(studentId)` – Displays a specific student's information.
- `updateStudentDetails(studentId)` – Updates selected student details.
- `studentExist(studentId)` – Checks whether a student ID exists.
- `registerCourse(courseList)` – Registers a student for selected courses.
- `removeCourse(studentId)` – Removes a course and its associated mark, when applicable.
- `getDepartment()` – Collects a valid department selection.

### Marks and Result Processing

- `getMarks(studentId)` – Enters marks for registered courses that do not yet have marks.
- `updateMarks(studentId, courseList, choice)` – Updates a student's mark and maintains the subject-level aggregate list.
- `totalMarks(studentId)` – Calculates the total of entered marks.
- `avgMarks(marks, studentId)` – Calculates the average of marks entered for a student.
- `examResult(mark)` – Determines the grade corresponding to a mark.
- `hasCompleteMarks(studentId)` – Checks whether marks are available for all registered courses.
- `studentResultStatus(studentId)` – Determines whether a student's result is Pass, Fail, or Incomplete.
- `addMarkToGlobalList(course, mark)` – Adds a mark to the relevant subject-level aggregate list.
- `removeMarkFromGlobalList(course, mark)` – Removes one occurrence of a mark from the relevant aggregate list.

### Validation and Eligibility

- `validateYear()` – Validates the admission year.
- `validateEmail()` – Checks the email address format.
- `validatePhoneNumber()` – Validates a 10-digit phone number.
- `validateAttendance()` – Validates attendance percentages.
- `validateMark(course)` – Validates subject marks.
- `checkSemesterEligibility(studentId)` – Checks whether attendance meets the examination eligibility requirement.
- `isActiveStudent(studentId)` – Determines whether a student is active and eligible for active processing.

## 7. How to Run the Application

### Prerequisites

- Python 3.10 or later
- A terminal, command prompt, or Python-compatible IDE

### Execution Steps

1. Download or clone the project repository.
2. Open the project directory in your terminal.
3. Run the Python file containing the application:

   ```bash
   python filename.py
   ```

   Replace `filename.py` with the actual name of your Python script.

4. Select an option from the main menu by entering its corresponding number.
5. Follow the prompts to register students, manage courses, update attendance and marks, view results, and generate statistics.
6. Select the exit option to close the application.

The application uses a menu-driven console interface. Users interact with it through numbered options and text inputs. Invalid inputs are handled through validation messages and repeated prompts where applicable.

## 8. Testing Scenarios

| Test Scenario | Expected Outcome |
|---|---|
| Register a student with a valid ID | Student record is created successfully. |
| Register an existing student ID | Duplicate registration is rejected. |
| Enter invalid marks or attendance | Validation prevents out-of-range values. |
| Register the same course twice | Duplicate course registration is prevented. |
| Check attendance at 75% | Student is marked eligible for the semester examination. |
| Enter marks for registered courses | Marks are stored and reflected in subject-level aggregates. |
| Update a student's mark | The individual record and corresponding aggregate list are updated. |
| Remove a registered course | Course registration and its associated mark are removed. |
| Withdraw a student | Historical records remain available, while active processing excludes the student. |
| Test grade boundaries | Marks of 49, 50, and 90 produce grades F, E, and A respectively. |
| Calculate marks and averages | Totals and averages are calculated using entered marks. |
| Start and exit the application | The main menu starts and the program exits correctly. |

These tests cover important functions and boundary conditions. The scenarios listed are not a claim that every possible input sequence has been exhaustively tested.

## 9. Assumptions Made During Development

- Student information is maintained in memory using Python data structures. Records are not permanently stored and are lost when the application terminates.
- Student IDs are treated as unique identifiers and are entered as strings.
- The application supports the predefined departments and four courses: Python, SQL, Excel, and Power BI.
- Attendance is entered as a whole-number percentage.
- Marks are whole numbers between 0 and 100.
- A student must have marks for every registered course before the overall result is considered complete.
- The student fails if any registered subject has a mark below 50.
- The subject-level aggregate lists represent active students' marks rather than identifying individual students. When marks are updated, removed, or withdrawn, the corresponding aggregate values are adjusted.
- Withdrawal changes a student's academic status instead of permanently deleting the record.
- The email validation checks the address format but does not verify whether the address exists.
- The application is intended for learning and demonstration purposes, not as a production-ready university management system.

## 10. Technologies Used

- **Programming Language:** Python
- **Concepts:** Dictionaries, sets, lists, tuples, functions, loops, conditional statements, pattern matching (`match-case`), regular expressions, and input validation
- **Interface:** Command-line / console
- **Storage:** In-memory data structures
- **External Dependencies:** No external packages are required; the application uses Python's built-in `re` module.

## Conclusion

The Nova University Student Management System demonstrates how core Python concepts can be combined to build a structured, menu-driven application for managing student information and academic activities. It applies appropriate data structures, validation rules, set operations, and calculation logic to support student registration, course management, attendance tracking, result processing, and reporting.
