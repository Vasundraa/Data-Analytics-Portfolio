# Application Pseudocode

This pseudocode describes the overall logic of the console application and its main services. It is language-independent in structure but reflects the current Python implementation.

## 1. Program Startup and Main Menu

```text
IMPORT regular-expression support
DISPLAY application heading

INITIALIZE empty students dictionary
INITIALIZE department-code-to-name dictionary
INITIALIZE ordered department-code list
INITIALIZE fixed tuple of courses
INITIALIZE empty aggregate mark lists for Python, SQL, Excel, and Power BI

REPEAT
    DISPLAY main menu:
        1. Student Registration
        2. Student Search
        3. Course Registration
        4. Attendance
        5. Marks
        6. Result
        7. Department Information
        8. Student Statistics
        9. Student Withdrawal
        10. Exit

    READ and trim choice

    MATCH choice
        1: OPEN student registration menu
        2: OPEN student search menu
        3: OPEN course registration menu
        4: OPEN attendance menu
        5: OPEN marks menu
        6: OPEN result menu
        7: OPEN department information menu
        8: OPEN statistics menu
        9: OPEN withdrawal menu
        10: DISPLAY exit message and stop loop
        OTHERWISE: DISPLAY invalid choice
UNTIL exit is selected
```

## 2. Register a Student

```text
READ student ID and trim whitespace

IF student ID is blank
    DISPLAY validation message
ELSE IF student ID already exists
    DISPLAY duplicate-ID message
ELSE
    CALL getStudentDetails
        REPEAT until name is not blank
        CALL getDepartment
        CALL validateYear
        CALL validateEmail
        CALL validatePhoneNumber
        INITIALIZE attendance to 0
        INITIALIZE coursesRegistered as empty set
        INITIALIZE marks as empty dictionary
        INITIALIZE academicStatus as Active
    STORE returned student record under student ID
    DISPLAY success message
END IF
```

## 3. Update Student Details

```text
READ student ID
IF student does not exist
    DISPLAY not-found message
ELSE IF student is not active
    DISPLAY cannot-update message
ELSE
    REPEAT
        DISPLAY current student record
        DISPLAY fields available for update
        READ choice

        IF choice is Student ID
            READ new ID
            IF blank OR already exists
                DISPLAY validation message
            ELSE
                MOVE record from old dictionary key to new key
        ELSE IF choice is Name
            REPEAT until non-blank name is entered
            UPDATE name
        ELSE IF choice is Department
            UPDATE using validated department
        ELSE IF choice is Year
            UPDATE using validated year
        ELSE IF choice is Email
            UPDATE using validated email format
        ELSE IF choice is Phone
            UPDATE using validated phone number
        ELSE IF choice is Back
            EXIT update loop
        ELSE
            DISPLAY invalid choice
    UNTIL user chooses Back
END IF
```

## 4. Register or Remove a Course

```text
READ student ID
IF student does not exist OR is withdrawn
    DISPLAY appropriate error
ELSE
    DISPLAY available courses
    READ numeric selection
    VALIDATE selection

    IF registering
        IF course already exists in student's set
            DISPLAY duplicate course message
        ELSE
            ADD course to student's set
            DISPLAY success
        END IF

    IF removing
        DISPLAY registered courses
        READ and validate removal selection
        REMOVE selected course from student's set

        IF student has a mark for the course
            REMOVE mark from student's marks dictionary
            REMOVE one occurrence from the subject aggregate list
        END IF
        DISPLAY success
    END IF
END IF
```

## 5. Course Overlap Analysis

```text
READ analysis choice
IF choice is Back
    RETURN to course menu

READ first course and second course
VALIDATE that both are supported and different

CREATE firstStudents set containing active student IDs registered for first course
CREATE secondStudents set containing active student IDs registered for second course

IF choice is intersection
    result = firstStudents INTERSECTION secondStudents
ELSE IF choice is first-only
    result = firstStudents DIFFERENCE secondStudents
ELSE IF choice is at-least-one
    result = firstStudents UNION secondStudents
ELSE IF choice is exactly-one
    result = SYMMETRIC DIFFERENCE of both sets
ELSE IF choice is disjointness
    DISPLAY whether firstStudents and secondStudents have no common members
    RETURN to analysis menu
END IF

DISPLAY result IDs and names
IF result is empty
    DISPLAY no-match message
END IF
```

## 6. Attendance and Eligibility

```text
READ student ID
CHECK that student exists, is active, and has at least one registered course

IF updating attendance
    CALL validateAttendance
    STORE attendance
    DISPLAY confirmation
ELSE IF checking eligibility
    IF attendance >= 75
        DISPLAY Eligible
    ELSE
        DISPLAY Not Eligible
    END IF
ELSE IF listing students below threshold
    FOR each student
        SKIP withdrawn students
        IF attendance < 75
            DISPLAY student ID, name, attendance, and Not Eligible
        END IF
    END FOR
END IF
```

## 7. Enter Marks and Maintain Aggregates

```text
GET student's registered courses that do not yet have marks

IF no courses are missing marks
    DISPLAY all marks already entered
ELSE
    FOR each missing course
        CALL validateMark(course)
        STORE mark in student's marks dictionary
        APPEND mark to the corresponding subject aggregate list
    END FOR
    DISPLAY success message
END IF
```

## 8. Update a Mark

```text
BUILD list of student's courses that already have marks
IF list is empty
    DISPLAY enter-marks-first message
ELSE
    DISPLAY numbered list of courses with marks
    READ and validate selected number
    oldMark = student's current mark
    READ and validate newMark
    REPLACE mark in student's marks dictionary
    REMOVE one occurrence of oldMark from subject aggregate list
    APPEND newMark to subject aggregate list
    DISPLAY success
END IF
```

## 9. Calculate a Result

```text
IF student has no marks
    DISPLAY no-marks message
ELSE
    total = SUM of entered marks
    average = total / number of entered marks
    DISPLAY subject marks and grades
    IDENTIFY subjects with marks below 50
    CHECK whether any registered course lacks a mark

    IF any registered course lacks a mark OR no course is registered
        overall result = Incomplete
    ELSE
        overall grade = grade for average
        IF any registered subject mark is below 50
            pass/fail status = Fail
        ELSE
            pass/fail status = Pass
        END IF
    END IF

    CHECK examination eligibility using attendance >= 75
    DISPLAY result information
END IF
```

## 10. Student Withdrawal

```text
READ student ID
IF student does not exist
    DISPLAY not-found message
ELSE IF student is already withdrawn
    DISPLAY already-withdrawn message
ELSE
    DISPLAY student record
    ASK for confirmation

    IF confirmation is yes
        FOR each stored subject mark
            REMOVE one occurrence from corresponding aggregate list
        SET academicStatus to Withdrawn
        RETAIN student record and historical marks
        DISPLAY withdrawal confirmation
    ELSE
        DISPLAY cancellation message
    END IF
END IF
```

## 11. Statistics

```text
FOR each statistics request
    CONSIDER active students only

    Depending on selected option:
        COUNT active students
        COUNT students by department
        COUNT students with attendance >= 75
        IDENTIFY complete-mark students who failed
        FIND highest average among complete-mark students
        FIND lowest average among complete-mark students
        SELECT an admission batch and calculate each subject average
        FIND unique departments represented
        LIST active students registered for a selected course

    IF the required collection is empty
        DISPLAY a no-data message
    ELSE
        DISPLAY calculated result
    END IF
END FOR
```

## 12. Program Exit

```text
WHEN main-menu choice is Exit
    DISPLAY thank-you message
    STOP main menu loop
    END PROGRAM
```
