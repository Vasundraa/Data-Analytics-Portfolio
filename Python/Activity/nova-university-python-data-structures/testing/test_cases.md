# Test Cases – Nova University Student Management System

## 1. Test Execution Summary

| Item | Details |
|---|---|
| Application tested | `student_service_portal.py` in this project folder |
| Execution date | 12 October 2026 |
| Python version | Python 3.13.5 |
| Test method | Automated input-driven function/menu checks, validation boundary checks, syntax compilation, and a complete console workflow in a separate process |
| Assertions executed | 65 |
| Passed | 65 |
| Failed | 0 |
| Overall status | **PASS** for the test scenarios listed in this document |

The tests were executed against the project file in this folder. Menu functions were exercised with controlled console inputs; a separate end-to-end run exercised registration, course registration, marks entry, result viewing, and exit in one program session. The tests use temporary sample records and do not require real student data.

## 2. Test Data

The following sample identifiers and values were used where applicable:

- Student IDs: `ST101`, `ST102`, `ST103`, and `ST301`
- Departments: `CSE`, `IT`, `AI&DS`, `ECE`, and `BBA`
- Courses: `Python`, `SQL`, `Excel`, and `Power BI`
- Valid email examples: `a@example.com`, `valid.name+tag@example.co.in`
- Valid phone example: `1234567890`
- Attendance boundary values: `74`, `75`, and `100`
- Mark boundary values: `0`, `49`, `50`, `60`, `70`, `80`, `90`, and `100`

## 3. Functional Test Cases

Every case below was executed and its result checked against the expected behavior.

| ID | Scenario | Test Input / Steps | Expected Result | Verified Result |
|---|---|---|---|---|
| TC-01 | Register a new student | Enter valid ID and student details. | Record is created and success message appears. | **Passed** |
| TC-02 | Duplicate student ID | Register an ID, then try to register the same ID again. | Duplicate registration is rejected; only one record remains. | **Passed** |
| TC-03 | Blank student ID | Submit a blank or whitespace-only ID. | Registration is rejected with a validation message. | **Passed** |
| TC-04 | Search valid student | Search for an existing student ID. | The matching student's record is displayed. | **Passed** |
| TC-05 | Search unknown student | Search for `ST999`. | Not-found message appears and the menu continues. | **Passed** |
| TC-06 | Invalid department selection | Enter an out-of-range department number, then a valid number. | Invalid choice is rejected; valid selection allows registration to continue. | **Passed** |
| TC-07 | Update student details | Change a student's name. | New name is stored and success message appears. | **Passed** |
| TC-08 | Change student ID | Change an existing ID to an unused ID. | Record is stored under the new ID and removed from the old key. | **Passed** |
| TC-09 | Duplicate new student ID | Change an ID to one already in use. | Change is rejected; both original records remain intact. | **Passed** |
| TC-10 | Register a course | Register a student for Python. | Python is added to the student's course set. | **Passed** |
| TC-11 | Duplicate course registration | Register Python twice for one student. | Duplicate is reported and the set retains one Python entry. | **Passed** |
| TC-12 | Remove a course | Remove a registered course that has a mark. | Course and associated mark are removed; one matching aggregate mark is removed. | **Passed** |
| TC-13 | Invalid course selection | Enter a non-numeric course choice, then a valid choice. | Invalid choice is handled without crashing; valid selection works. | **Passed** |
| TC-14 | Attendance below threshold | Set attendance to 74%. | Student is Not Eligible. | **Passed** |
| TC-15 | Attendance exactly at threshold | Check eligibility at 75%. | Student is Eligible. | **Passed** |
| TC-16 | Attendance upper boundary | Enter 100%. | Value is accepted. | **Passed** |
| TC-17 | Invalid attendance | Enter `-1`, `101`, and text before a valid value. | Invalid values are rejected and the prompt repeats. | **Passed** |
| TC-18 | Enter marks | Enter Python mark 85 for a student registered in Python. | Student mark and subject aggregate list are updated. | **Passed** |
| TC-19 | Invalid marks | Enter `-1`, `101`, and text before a valid mark. | Invalid values are rejected and the prompt repeats. | **Passed** |
| TC-20 | Update marks | Change a Python mark from 80 to 95. | Student mark is updated; one old aggregate occurrence is removed and the new mark is added. | **Passed** |
| TC-21 | Mark for a newly registered course | Add SQL after Python already has a mark, then enter marks. | Only the missing SQL mark is requested and stored. | **Passed** |
| TC-22 | Grade boundary F | Evaluate mark 49. | Grade F is returned. | **Passed** |
| TC-23 | Grade boundary E | Evaluate mark 50. | Grade E is returned. | **Passed** |
| TC-24 | Grade boundary A | Evaluate mark 90. | Grade A is returned. | **Passed** |
| TC-25 | Complete passing result | Give every registered course a mark of at least 50. | Result status is Pass. | **Passed** |
| TC-26 | Failed result | Give one registered course a mark below 50 and complete the other marks. | Result status is Fail. | **Passed** |
| TC-27 | Incomplete result | Register multiple courses but leave at least one mark missing. | Result status is Incomplete. | **Passed** |
| TC-28 | Course overlap intersection | Have one student registered for both Python and SQL. | Intersection includes the student enrolled in both courses only. | **Passed** |
| TC-29 | Course overlap difference | Compare Python students against SQL students. | Python-only student appears in the difference. | **Passed** |
| TC-30 | Course overlap union | Have students in either or both selected courses. | Union includes each matching student once. | **Passed** |
| TC-31 | Symmetric difference | Compare Python and SQL groups with shared and exclusive students. | Only students in exactly one group appear. | **Passed** |
| TC-32 | Disjoint groups | Compare active Python students against active Excel students where there is no overlap. | Application reports the groups are completely different. | **Passed** |
| TC-33 | Withdraw a student | Confirm withdrawal for an active student with a mark. | Status changes to Withdrawn, historical record remains, and its mark is removed from the active aggregate. | **Passed** |
| TC-34 | Withdraw same student again | Attempt to withdraw an already withdrawn student. | Already-withdrawn message appears. | **Passed** |
| TC-35 | Highest and lowest average | Create two students with complete marks and different averages. | Highest and lowest average options identify the correct students and averages. | **Passed** |
| TC-36 | Empty statistics | Open statistics with no student records. | Zero/no-data messages appear without a crash. | **Passed** |
| TC-37 | Department student listing | List a department with students and one without students. | Matching active students are listed, or a no-students message appears. | **Passed** |
| TC-38 | Course participation | Select Python for course participation after registering an active student. | Active student appears and the total count is correct. | **Passed** |
| TC-39 | Invalid main-menu choice | Enter text at the main menu, then select exit. | Invalid-choice message appears; program continues and exits normally. | **Passed** |
| TC-40 | Multiple operations in one session | Register a student, register a course, enter marks, and view the result. | Data persists between menus and the completed result is displayed. | **Passed** |
| TC-41 | Exit | Select main-menu option 10. | Exit message appears and the process terminates successfully. | **Passed** |

## 4. Input Validation Tests

| ID | Field | Inputs Tested | Expected Behavior | Verified Result |
|---|---|---|---|---|
| VAL-01 | Admission year | Text, year below 1900, year above 2100, fewer than four digits, more than four digits, and valid boundary year 1900 | Invalid years are rejected; valid four-digit year in range is accepted. | **Passed** |
| VAL-02 | Email | Missing/invalid address, missing suffix, address containing a space, and valid address with plus sign/subdomain | Invalid email is rejected; valid email is accepted. | **Passed** |
| VAL-03 | Phone number | Too few digits, alphabetic characters, 11 digits, and valid 10-digit number | Invalid phone numbers are rejected; valid 10-digit number is accepted. | **Passed** |
| VAL-04 | Attendance | Negative, above 100, text, and valid value | Invalid values are rejected; valid percentage is accepted. | **Passed** |
| VAL-05 | Marks | Negative, above 100, text, and valid value | Invalid values are rejected; valid whole-number mark is accepted. | **Passed** |
| VAL-06 | Menu choices | Unsupported numeric and text choices | Invalid-choice message appears and menu remains usable. | **Passed** |

## 5. Additional Coverage Checks

These additional assertions supplement the 41 functional cases and validation table above.

| ID | Additional behavior checked | Verified Result |
|---|---|---|
| EXT-01 | All grade bands: A at 90, B at 80, C at 70, D at 60, E at 50, and F below 50 | **Passed** |
| EXT-02 | Blank student name is rejected; a valid name can then be entered | **Passed** |
| EXT-03 | Displaying courses for a student with no registered courses | **Passed** |
| EXT-04 | Invalid course-removal choice leaves course and mark unchanged | **Passed** |
| EXT-05 | Removing one student's mark when two students share the same mark preserves the other student's aggregate occurrence | **Passed** |
| EXT-06 | Cancelling withdrawal preserves active status and aggregate marks | **Passed** |
| EXT-07 | Withdrawn student is excluded from active course-overlap results | **Passed** |
| EXT-08 | Attendance cannot be updated for a withdrawn student | **Passed** |
| EXT-09 | Attendance below-threshold listing and eligible-student summary counts | **Passed** |
| EXT-10 | Individual result and bulk result processing handle complete and incomplete records | **Passed** |
| EXT-11 | Active-student count, department counts, exam eligibility, failed-student count, and unique departments | **Passed** |
| EXT-12 | Attendance update is blocked when a student has no registered courses | **Passed** |
| EXT-13 | Invalid course names and selecting the same course twice are handled | **Passed** |
| EXT-14 | Marks for Python, SQL, Excel, and Power BI update the correct subject aggregate lists | **Passed** |
| EXT-15 | Student record display includes department, year, email, phone, and academic status | **Passed** |
| EXT-16 | Academic summary calculates total marks and average correctly | **Passed** |
| EXT-17 | End-to-end console flow: registration → course registration → marks → result → exit in one process | **Passed** |
| EXT-18 | Python syntax compilation with `py_compile` | **Passed** |
| EXT-19 | Short/long admission years are rejected and lower valid year boundary is accepted | **Passed** |
| EXT-20 | Email with spaces is rejected and a valid plus-address/subdomain is accepted | **Passed** |
| EXT-21 | An 11-digit phone number is rejected | **Passed** |

## 6. Final Verification Notes

- All **65 automated assertions passed** in the test run performed on 12 October 2026 using Python 3.13.5.
- The test run included the 41 functional scenarios, validation checks, additional edge cases, syntax compilation, and a single-process end-to-end workflow.
- The tests verify the scenarios described here; they do not prove that every possible input combination or environment has been tested.
- Sample student data is temporary test data and is not real student information.
