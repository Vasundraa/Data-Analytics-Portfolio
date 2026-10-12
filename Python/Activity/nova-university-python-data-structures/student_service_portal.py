import re

print("------------ NOVA UNIVERSITY ------------")

students={}

departments={

    "CSE": "Computer Science and Engineering",

    "IT": "Information Technology",

    "AI&DS": "Artificial Intelligence & Data Science",

    "ECE": "Electronics & Communication Engineering",

    "BBA": "Business Administration"

}

depts = list(departments.keys())

courses=("Python", "SQL", "Excel", "Power BI")

pythonMarks = []

sqlMarks = []

excelMarks = []

powerBIMarks = []

# Menus

def studentRegistrationMenu():

    while True:

        print("---------- Student Registration ---------")

        print("1. Add a new student\n" \

        "2. Display student information\n" \

        "3. Update student information\n" \

        "4. Back to main menu")

        choice=input("Enter your choice: ").strip()

        match choice:

            case '1':

                studentId = input("Enter student ID: ").strip()
                if not studentId:
                    print("Student ID cannot be blank!")
                    continue

                if(studentExist(studentId)):

                    print("Student ID already exists!")

                    continue

                student=getStudentDetails()

                students[studentId]=student

                print("Successfully Added Student Details!")

            case '2':

                displayStudentDetails()

            case '3':

                studentId = input("Enter student ID to update: ").strip()

                if(not studentExist(studentId)):

                    print(f"Student Record with {studentId} does not exist")

                    continue

                if not isActiveStudent(studentId):

                    print("Cannot update a withdrawn student's details.")

                    continue

                updateStudentDetails(studentId)

            case '4':

                print("Returning to main menu")

                return

            case _:

                print("Invalid choice!")

def studentSearchMenu():
    while True:
        print("------------ Student Search -------------")
        print("1. Search by Student ID")
        print("2. Back to main menu")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                studentId = input("Enter Student ID to Search: ").strip()
                if studentExist(studentId):
                    displayStudentRecord(studentId)
                else:
                    print("Student ID does not exist!")
            case '2':
                return
            case _:
                print("Invalid choice!")

def studentCourseRegistrationMenu():

    while(True):

        print("---------- Course Registration ----------")

        print("1. Register Course")

        print("2. Display Registered Courses")

        print("3. Remove Course")

        print("4. Course Overlap Analysis")

        print("5. Back to Main Menu")

        choice=input("Enter your choice: ").strip()

        match choice:

            case '1':

                studentId = input("Enter Student ID for Course Registration: ").strip()

                if not studentExist(studentId):

                    print("Student ID does not exist!")

                    continue

                if not isActiveStudent(studentId):

                    print("Cannot register courses for a withdrawn student.")

                    continue

                courseList = students[studentId]['coursesRegistered']

                registerCourse(courseList)

            case '2':

                studentId=input("Enter Student ID to display courses: ").strip()

                if studentExist(studentId):

                    courseList=students[studentId]['coursesRegistered']

                    if len(courseList)==0:

                        print("Student is not registered for any course.")

                    else:

                        print("Registered Courses:")

                        for course in courseList:

                            print(course)

                else:

                    print("Student ID does not exist!")

            case '3':

                studentId=input("Enter Student ID to remove course: ").strip()

                if not studentExist(studentId):

                    print("Student ID does not exist!")

                    continue

                if not isActiveStudent(studentId):

                    print("Cannot modify courses for a withdrawn student.")

                    continue

                removeCourse(studentId)

            case '4':

                courseOverlapAnalysis()

            case '5':

                print("Returning to main menu.")

                return

            case _:

                print("Invalid choice!")      

def studentAttendanceMenu():

    while(True):

        print("----------- Student Attendance ----------")

        print("1. Update student attendance\n" \

        "2. Check exam eligibilty\n" \

        "3. List students below required attendance\n" \

        "4. Attendance details summary\n" \

        "5. Back to main menu")

        choice=input("Enter your choice: ").strip()

        match choice:

            case '1':

                studentId = input("Enter Student ID to Update Attendance: ").strip()

                if not studentExist(studentId):

                    print("Student ID does not exist!")

                    continue

                if not isActiveStudent(studentId):

                    print("Cannot update attendance for a withdrawn student.")

                    continue

                if len(students[studentId]['coursesRegistered']) == 0:

                    print(

                        f"Student {studentId} is not enrolled in any courses. "

                        "Register a course before adding attendance details."

                    )

                    continue

                attendance = validateAttendance()

                students[studentId]['attendance'] = attendance

                print("Attendance Updated Successfully!")

            case '2':

                studentId = input("Enter Student ID to Check Semester Exam Eligibility: ").strip()

                if not studentExist(studentId):

                    print("Student ID does not exist!")

                    continue

                if not isActiveStudent(studentId):

                    print("This student has withdrawn and is not eligible for active exam processing.")

                    continue

                if len(students[studentId]['coursesRegistered']) == 0:

                    print(

                        f"Student {studentId} is not enrolled in any courses."

                    )

                    continue

                eligibilityStatus = (

                    "Eligible"

                    if checkSemesterEligibility(studentId)

                    else "Not Eligible"

                )

                print(

                    f"{studentId} is {eligibilityStatus} "

                    "for Semester Exam"

                )

            case '3':

                executed = False

                print(

                    f"{'Student ID':<15}"

                    f"{'Student Name':<20}"

                    f"{'Attendance':<15}"

                    f"{'Eligibility':<15}"

                )

                for studentId in students:

                    if not isActiveStudent(studentId):

                        continue

                    if not checkSemesterEligibility(studentId):

                        print(

                            f"{studentId:<15}"

                            f"{students[studentId]['name']:<20}"

                            f"{students[studentId]['attendance']:<15}"

                            f"{'Not Eligible':<15}"

                        )

                        executed = True

                if not executed:

                    print("No active students are below the required attendance.")

            case '4':

                eligibleStudents = 0

                activeStudents = 0

                for studentId in students:

                    if not isActiveStudent(studentId):

                        continue

                    activeStudents += 1

                    if checkSemesterEligibility(studentId):

                        eligibleStudents += 1

                print(f"Total Active Students: {activeStudents}")

                print(

                    "Count of Eligible Students for Semester Examination: "

                    f"{eligibleStudents}"

                )

            case '5':

                print("Returning to main menu.")

                return

            case _:

                print("Invalid Choice!")

def studentsMarksMenu():
    while True:
        print("------------- Student Marks -------------")
        print("1. Enter student marks")
        print("2. Retrieve subject marks")
        print("3. Update student marks")
        print("4. Display academic summary")
        print("5. Calculate average marks")
        print("6. Identify highest mark")
        print("7. Back to main menu")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                studentId = input("Enter student ID to enter marks: ").strip()
                if not studentExist(studentId):
                    print("Student ID does not exist!")
                    continue
                if not isActiveStudent(studentId):
                    print("Cannot enter marks for a withdrawn student.")
                    continue
                if not students[studentId]['coursesRegistered']:
                    print("Student is not registered in any course to enter marks.")
                    continue
                entered = getMarks(studentId)
                if entered:
                    print("Marks entered successfully!")
                else:
                    print("All registered courses already have marks.")

            case '2':
                studentId = input("Enter student ID to display marks: ").strip()
                if not studentExist(studentId):
                    print("Student ID does not exist!")
                    continue
                student = students[studentId]
                if not student['marks']:
                    print("No marks are entered to display.")
                    continue
                if not isActiveStudent(studentId):
                    print("Historical marks for withdrawn student:")
                print(f"Student name: {student['name']}")
                for course in courses:
                    if course in student['marks']:
                        print(f"{course}: {student['marks'][course]}")
                missing = student['coursesRegistered'] - student['marks'].keys()
                if missing:
                    print(f"Marks not yet entered for: {', '.join(sorted(missing))}")

            case '3':
                studentId = input("Enter student ID to update marks: ").strip()
                if not studentExist(studentId):
                    print("Student ID does not exist!")
                    continue
                if not isActiveStudent(studentId):
                    print("Cannot update marks for a withdrawn student.")
                    continue
                student = students[studentId]
                courseList = [course for course in courses if course in student['marks']]
                if not courseList:
                    print("No marks are available to update. Enter marks first.")
                    continue
                while True:
                    print("Courses with marks entered:")
                    for i, course in enumerate(courseList, start=1):
                        print(f"{i}. {course}")
                    choice = input("Choose the course to update marks for: ").strip()
                    if not choice.isdigit() or not 1 <= int(choice) <= len(courseList):
                        print("Invalid choice!")
                        continue
                    updateMarks(studentId, courseList, int(choice))
                    addMore = input("Want to update more marks? (y/n): ").strip().lower()
                    if addMore != 'y':
                        if addMore != 'n':
                            print("Invalid response. Returning to marks menu.")
                        break
                    courseList = [course for course in courses if course in student['marks']]
                    if not courseList:
                        print("No marks are available to update.")
                        break

            case '4':
                studentId = input("Enter student ID to display academic summary: ").strip()
                if not studentExist(studentId):
                    print("Student ID does not exist!")
                    continue
                student = students[studentId]
                if not student['marks']:
                    print("No marks are entered to display.")
                    continue
                if not isActiveStudent(studentId):
                    print("Historical academic summary for withdrawn student:")
                print(f"Student name: {student['name']}")
                print("-" * 40)
                print(f"{'Subject':<20}{'Mark':<10}")
                print("-" * 40)
                failedSubjects = []
                for course in courses:
                    if course in student['marks']:
                        mark = student['marks'][course]
                        print(f"{course:<20}{mark:<10}")
                        if examResult(mark) == "F":
                            failedSubjects.append(course)
                total = totalMarks(studentId)
                average = avgMarks(total, studentId)
                print("-" * 40)
                print(f"Total Mark: {total}")
                print(f"Average of entered marks: {average:.2f}")
                missing = student['coursesRegistered'] - student['marks'].keys()
                if missing:
                    print(f"Result incomplete. Marks missing for: {', '.join(sorted(missing))}")
                print(f"Failed subjects: {failedSubjects if failedSubjects else 'None'}")

            case '5':
                print("Overall Average Marks for Each Subject (active students)")
                print("-" * 65)
                print(f"{'Subject':<15}{'No. of Marks':<20}{'Average Mark':<15}")
                print("-" * 65)
                subjectLists = {
                    "Python": pythonMarks,
                    "SQL": sqlMarks,
                    "Excel": excelMarks,
                    "Power BI": powerBIMarks
                }
                for course in courses:
                    subjectMarks = subjectLists[course]
                    if not subjectMarks:
                        print(f"{course:<15}{0:<20}{'Not Available':<15}")
                    else:
                        average = sum(subjectMarks) / len(subjectMarks)
                        print(f"{course:<15}{len(subjectMarks):<20}{average:<15.2f}")
                print("-" * 65)

            case '6':
                print("Highest Marks for Each Subject (active students)")
                print("-" * 65)
                print(f"{'Subject':<15}{'No. of Marks':<20}{'Highest Mark':<15}")
                print("-" * 65)
                subjectLists = {
                    "Python": pythonMarks,
                    "SQL": sqlMarks,
                    "Excel": excelMarks,
                    "Power BI": powerBIMarks
                }
                for course in courses:
                    subjectMarks = subjectLists[course]
                    if not subjectMarks:
                        print(f"{course:<15}{0:<20}{'Not Available':<15}")
                    else:
                        print(f"{course:<15}{len(subjectMarks):<20}{max(subjectMarks):<15}")
                print("-" * 65)

            case '7':
                print("Returning to main menu.")
                return
            case _:
                print("Invalid choice!")

def studentResultMenu():
    while True:
        print("------------ Student Result -------------")
        print("1. View student result")
        print("2. Process all active student results")
        print("3. Back to main menu")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                studentId = input("Enter Student ID to view result: ").strip()
                if not studentExist(studentId):
                    print("Student ID does not exist!")
                    continue
                student = students[studentId]
                if not student['marks']:
                    print("No marks are entered to display.")
                    continue
                if not isActiveStudent(studentId):
                    print("Historical result for withdrawn student:")
                print(f"Student name: {student['name']}")
                print(f"Academic status: {student['academicStatus']}")
                print("-" * 50)
                print(f"{'Subject':<20}{'Mark':<10}{'Grade':<10}")
                print("-" * 50)
                for course in courses:
                    if course in student['marks']:
                        mark = student['marks'][course]
                        print(f"{course:<20}{mark:<10}{examResult(mark):<10}")
                print("-" * 50)
                total = totalMarks(studentId)
                average = avgMarks(total, studentId)
                print(f"Total Mark: {total}")
                print(f"Average of entered marks: {average:.2f}")
                missing = student['coursesRegistered'] - student['marks'].keys()
                if missing:
                    print(f"Overall result: Incomplete (marks missing for {', '.join(sorted(missing))})")
                else:
                    print(f"Overall Grade: {examResult(average)}")
                    print(f"Pass/Fail: {studentResultStatus(studentId)}")
                if isActiveStudent(studentId):
                    print(f"Exam eligibility: {'Eligible' if checkSemesterEligibility(studentId) else 'Not Eligible'}")
                else:
                    print(f"Historical attendance eligibility: {'Eligible' if checkSemesterEligibility(studentId) else 'Not Eligible'}")

            case '2':
                activeStudentIds = [sid for sid in students if isActiveStudent(sid)]
                if not activeStudentIds:
                    print("There are no active student records to process.")
                    continue
                print("-" * 125)
                print(f"{'Student ID':<15}{'Student Name':<20}{'Department':<15}{'Attendance':<12}{'Eligibility':<15}{'Average':<12}{'Grade':<10}{'Result':<12}")
                print("-" * 125)
                for studentId in activeStudentIds:
                    student = students[studentId]
                    eligibility = "Eligible" if checkSemesterEligibility(studentId) else "Not Eligible"
                    missing = student['coursesRegistered'] - student['marks'].keys()
                    if not student['marks']:
                        averageText = gradeText = resultText = "No Data"
                    elif missing:
                        averageText = f"{avgMarks(totalMarks(studentId), studentId):.2f}*"
                        gradeText = resultText = "Incomplete"
                    else:
                        average = avgMarks(totalMarks(studentId), studentId)
                        averageText = f"{average:.2f}"
                        gradeText = examResult(average)
                        resultText = studentResultStatus(studentId)
                    print(f"{studentId:<15}{student['name']:<20}{student['department']:<15}{student['attendance']:<12}{eligibility:<15}{averageText:<12}{gradeText:<10}{resultText:<12}")
                print("* Average is based only on marks entered; incomplete results are not final.")
                print("-" * 125)

            case '3':
                print("Returning to main menu.")
                return
            case _:
                print("Invalid choice!")

def departmentInfoMenu():

    while(True):

        print("---------- Department Information ----------")

        print("1. Display Available Departments")

        print("2. Display Students by Department")

        print("3. Back to Main Menu")

        choice=input("Enter your choice: ").strip()

        match choice:

            case '1':

                print("\n---------- Available Departments ----------")

                print(f"{'Code':<10}{'Department Name'}")

                print("-" * 60)

                for code, name in departments.items():

                    print(f"{code:<10}{name}")

            case '2':

                print("\n---------- Select Department ----------")

                i=1

                for code, name in departments.items():

                    print(f"{i}. {code} - {name}")

                    i+=1

                choice=input("Choose a department: ").strip()

                if choice.isdigit():

                    choice=int(choice)

                    if 1 <= choice <= len(depts):

                        selectedDepartment=depts[choice-1]

                        print(f"\n---------- {selectedDepartment} Students ----------")

                        print(f"{'Student ID':<20}{'Student Name':<20}")

                        print("-" * 40)

                        studentsFound=False

                        for studentId in students:

                            if not isActiveStudent(studentId):

                                continue

                            if students[studentId]["department"] == selectedDepartment:

                                print(

                                    f"{studentId:<20}"

                                    f"{students[studentId]['name']:<20}"

                                )

                                studentsFound = True

                        if not studentsFound:

                            print("No students are registered under this department.")

                    else:

                        print("Invalid department choice!")

                else:

                    print("Invalid choice!")

            case '3':

                return

            case _:

                print("Invalid choice!")

def studentStatisticsMenu():
    while True:
        print("---------- Student Statistics ----------")
        print("1. Total Number of Active Students")
        print("2. Department-wise Student Count")
        print("3. Exam Eligible Students")
        print("4. Failed Students")
        print("5. Highest Average Mark")
        print("6. Lowest Average Mark")
        print("7. Overall Batch Average")
        print("8. Unique Departments Represented")
        print("9. Students Registered for a Course")
        print("10. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                print(f"Total Number of Active Students: {sum(1 for sid in students if isActiveStudent(sid))}")

            case '2':
                print("---------- Department-wise Student Count ----------")
                print(f"{'Department':<15}{'Student Count':<15}")
                print("-" * 30)
                for department in depts:
                    count = sum(1 for sid, student in students.items() if isActiveStudent(sid) and student['department'] == department)
                    print(f"{department:<15}{count:<15}")

            case '3':
                eligible = sum(1 for sid in students if isActiveStudent(sid) and checkSemesterEligibility(sid))
                print(f"Active Students Eligible for Semester Examination: {eligible}")

            case '4':
                failedStudents = []
                for sid, student in students.items():
                    if not isActiveStudent(sid) or not student['coursesRegistered']:
                        continue
                    if student['coursesRegistered'] - student['marks'].keys():
                        continue
                    if studentResultStatus(sid) == "Fail":
                        failedStudents.append(sid)
                print(f"Active Students Who Failed (at least one subject below 50): {len(failedStudents)}")
                if failedStudents:
                    for sid in failedStudents:
                        print(f"{sid}: {students[sid]['name']}")

            case '5' | '6':
                averages = []
                for sid, student in students.items():
                    if not isActiveStudent(sid) or not student['coursesRegistered']:
                        continue
                    if student['coursesRegistered'] - student['marks'].keys():
                        continue
                    averages.append((avgMarks(totalMarks(sid), sid), sid))
                if not averages:
                    print("No active students have complete marks for all registered courses.")
                    continue
                average, sid = (max(averages) if choice == '5' else min(averages))
                label = "Highest" if choice == '5' else "Lowest"
                print(f"---------- {label} Average Mark ----------")
                print(f"{'Student ID':<20}{'Student Name':<25}{'Average':<10}")
                print("-" * 55)
                print(f"{sid:<20}{students[sid]['name']:<25}{average:<10.2f}")

            case '7':
                activeStudents = [(sid, student) for sid, student in students.items() if isActiveStudent(sid)]
                years = sorted({student['year'] for _, student in activeStudents})
                if not years:
                    print("No active student records available.")
                    continue
                print("---------- Available Admission Batches ----------")
                for i, year in enumerate(years, start=1):
                    print(f"{i}. {year}")
                batchChoice = input("Select admission batch: ").strip()
                if not batchChoice.isdigit() or not 1 <= int(batchChoice) <= len(years):
                    print("Invalid batch choice!")
                    continue
                selectedYear = years[int(batchChoice) - 1]
                print(f"Average marks by subject for batch {selectedYear} (active students)")
                print(f"{'Subject':<15}{'Students with Marks':<22}{'Average':<10}")
                print("-" * 47)
                for subject in courses:
                    subjectMarks = [student['marks'][subject] for _, student in activeStudents if student['year'] == selectedYear and subject in student['marks']]
                    if subjectMarks:
                        print(f"{subject:<15}{len(subjectMarks):<22}{sum(subjectMarks) / len(subjectMarks):<10.2f}")
                    else:
                        print(f"{subject:<15}{0:<22}{'No Data':<10}")

            case '8':
                uniqueDepartments = sorted({student['department'] for sid, student in students.items() if isActiveStudent(sid)})
                print(f"Unique Departments Represented: {len(uniqueDepartments)}")
                if uniqueDepartments:
                    for department in uniqueDepartments:
                        print(f"- {department}")
                else:
                    print("No active departments are represented.")

            case '9':
                print("---------- Students Registered for a Course ----------")
                for i, course in enumerate(courses, start=1):
                    print(f"{i}. {course}")
                courseChoice = input("Select a course: ").strip()
                if not courseChoice.isdigit() or not 1 <= int(courseChoice) <= len(courses):
                    print("Invalid course selection!")
                    continue
                selectedCourse = courses[int(courseChoice) - 1]
                matches = [(sid, student['name']) for sid, student in students.items() if isActiveStudent(sid) and selectedCourse in student['coursesRegistered']]
                print(f"\nStudents registered for {selectedCourse}:")
                print(f"{'Student ID':<20}{'Student Name':<25}")
                print("-" * 45)
                for sid, name in matches:
                    print(f"{sid:<20}{name:<25}")
                print("-" * 45)
                print(f"Total active students registered: {len(matches)}")

            case '10':
                return
            case _:
                print("Invalid choice!")

def validateYear():
    while True:
        year = input("Enter year of admission: ").strip()
        if year.isdigit() and len(year) == 4 and 1900 <= int(year) <= 2100:
            return int(year)
        print("Invalid year! Enter a four-digit year between 1900 and 2100.")

def validateEmail():
    while True:
        email = input("Enter email: ").strip()
        if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email):
            return email
        print("Invalid email address!")

def validatePhoneNumber():
    while True:
        phoneNumber = input("Enter phone number: ").strip()
        if len(phoneNumber) == 10 and phoneNumber.isdigit():
            return phoneNumber
        print("Invalid phone number! Enter exactly 10 digits.")

def validateAttendance():
    while True:
        attendance = input("Enter attendance (%): ").strip()
        if attendance.isdigit() and 0 <= int(attendance) <= 100:
            return int(attendance)
        print("Invalid attendance range! Enter attendance between 0 and 100.")

def validateMark(course):
    while True:
        mark = input(f"Enter {course} marks: ").strip()
        if mark.isdigit() and 0 <= int(mark) <= 100:
            return int(mark)
        print("Invalid mark! Enter a mark between 0 and 100.")

def getDepartment():  

    while True:

        for i in range(len(depts)):

            print(f"{i + 1}. {depts[i]}: {departments[depts[i]]}")

        choice = input("Choose the department: ").strip()

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(depts):

                return depts[choice - 1]

        print("Invalid choice!")

def studentExist(studentId):

    return studentId in students

def addMarkToGlobalList(course, mark):
    """Append a mark to its subject-level aggregate list."""
    subjectLists = {
        "Python": pythonMarks,
        "SQL": sqlMarks,
        "Excel": excelMarks,
        "Power BI": powerBIMarks
    }
    subjectLists[course].append(mark)

def removeMarkFromGlobalList(course, mark):
    """Remove one occurrence; global lists are aggregates, not student records."""
    subjectLists = {
        "Python": pythonMarks,
        "SQL": sqlMarks,
        "Excel": excelMarks,
        "Power BI": powerBIMarks
    }
    if mark in subjectLists[course]:
        subjectLists[course].remove(mark)

def hasCompleteMarks(studentId):
    student = students[studentId]
    return bool(student['coursesRegistered']) and not (student['coursesRegistered'] - student['marks'].keys())

def studentResultStatus(studentId):
    """A student fails if any registered subject has a mark below 50."""
    student = students[studentId]
    if not hasCompleteMarks(studentId):
        return "Incomplete"
    if any(mark < 50 for mark in student['marks'].values()):
        return "Fail"
    return "Pass"

def getMarks(studentId):
    """Enter marks for registered courses that do not have marks yet."""
    student = students[studentId]
    missingCourses = [course for course in courses if course in student['coursesRegistered'] and course not in student['marks']]
    if not missingCourses:
        return 0
    for course in missingCourses:
        mark = validateMark(course)
        student['marks'][course] = mark
        addMarkToGlobalList(course, mark)
    return len(missingCourses)

def getStudentDetails():

    print("Enter Student Details")

    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        print("Student name cannot be blank!")

    department=getDepartment()

    year=validateYear()

    email=validateEmail()

    phoneNumber=validatePhoneNumber()

    return {"name":name,

            "department":department,

            "year":year,

            "email":email,

            "phoneNumber":phoneNumber,

            "attendance":0,

            "coursesRegistered":set(),

            "marks":{},

            "academicStatus":"Active",}

def displayStudentDetails():

    if len(students)==0:

        print("No student records found")

        return

    for studentId in students:

        print("-----------------------------------------")

        student=students[studentId]

        print(f"Student ID: {studentId}")

        print(f"Student Name: {student['name']}")

        print(f"Department: {student['department']}")

        print(f"Year: {student['year']}")

        print(f"Email: {student['email']}")

        print(f"Phone number: {student['phoneNumber']}")

        print(f"Attendance: {student['attendance']}")

        print(f"Courses: {student['coursesRegistered']}")

        print(f"Marks: {student['marks']}")

        print(f"Academic Status: {student['academicStatus']}")

def displayStudentRecord(studentId):

    if len(students)==0:

        print("No student records found")

        return

    student=students[studentId]

    print("-----------------------------------------")

    print(f"Student ID: {studentId}")

    print(f"Student Name: {student['name']}")

    print(f"Department: {student['department']}")

    print(f"Year: {student['year']}")

    print(f"Email: {student['email']}")

    print(f"Phone number: {student['phoneNumber']}")

    print(f"Attendance: {student['attendance']}")

    print(f"Courses: {student['coursesRegistered']}")

    print(f"Marks: {student['marks']}")

    print(f"Academic Status: {student['academicStatus']}")

def updateStudentDetails(studentId):

    while(True):

        displayStudentRecord(studentId)

        print("Select Value to Update")

        print("1. Student ID\n" \

        "2. Name\n" \

        "3. Department\n" \

        "4. Year\n" \

        "5. Email\n" \

        "6. Phone Number\n" \

        "7. Back to Student Registration Menu")

        choice=input("Enter your choice (1-7): ").strip()

        match choice:

            case '1':

                newStudentId = input("Enter new student ID: ").strip()
                if not newStudentId:
                    print("Student ID cannot be blank!")
                    continue

                if(studentExist(newStudentId)):

                    print("Student ID Already Exists!")

                    continue

                students[newStudentId]=students[studentId]

                del students[studentId]

                studentId=newStudentId

                print("Student ID Updated Successfully!")

            case '2':

                while True:
                    name = input("Enter name: ").strip()
                    if name:
                        break
                    print("Student name cannot be blank!")

                students[studentId]['name']=name

                print("Student Name Updated Successfully!")

            case '3':

                department=getDepartment()

                students[studentId]['department']=department

                print("Student Department Updated Succefully!")

            case '4':

                year=validateYear()

                students[studentId]['year']=year

                print("Student Year of Joining Updated Successfully!")

            case '5':

                email=validateEmail()

                students[studentId]['email']=email

                print("Student Email Updated Successfully!")

            case '6':

                phoneNumber=validatePhoneNumber()

                students[studentId]['phoneNumber']=phoneNumber

                print("Student Phone Number Updated Successfully!")

            case '7':

                return

            case _:

                print("Invalid choice!")

def registerCourse(courseList):
    while True:
        print("Available courses:")
        for i, course in enumerate(courses, start=1):
            print(f"{i}. {course}")
        choice = input(f"Enter your choice to register course (1 - {len(courses)}): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= len(courses):
            print("Invalid choice!")
            continue
        course = courses[int(choice) - 1]
        if course in courseList:
            print(f"{course} already registered.")
        else:
            courseList.add(course)
            print("Course added successfully!")
        addMore = input("Want to add more courses? (y/n): ").strip().lower()
        if addMore == 'y':
            continue
        if addMore == 'n':
            print("Returning to course registration menu.")
            return courseList
        print("Invalid response. Returning to course registration menu.")
        return courseList

def removeCourse(studentId):
    courseList = students[studentId]['coursesRegistered']
    if not courseList:
        print("Student is not registered for any course.")
        return
    courseListDisplay = [course for course in courses if course in courseList]
    print("Registered Courses:")
    for i, course in enumerate(courseListDisplay, start=1):
        print(f"{i}. {course}")
    choice = input("Choose the course to remove: ").strip()
    if not choice.isdigit() or not 1 <= int(choice) <= len(courseListDisplay):
        print("Invalid choice!")
        return
    course = courseListDisplay[int(choice) - 1]
    courseList.remove(course)
    if course in students[studentId]['marks']:
        oldMark = students[studentId]['marks'].pop(course)
        removeMarkFromGlobalList(course, oldMark)
    print(f"{course} removed successfully!")

def courseOverlapAnalysis():
    while True:
        print("---------- Course Overlap Analysis ----------")
        print("1. Students registered for both courses")
        print("2. Students registered for first course but not second")
        print("3. Students registered for at least one of the courses")
        print("4. Students registered for exactly one of the courses")
        print("5. Check whether two student groups are completely different")
        print("6. Back")
        choice = input("Enter your choice: ").strip()
        if choice == '6':
            print("Returning to course registration menu.")
            return
        if choice not in {'1', '2', '3', '4', '5'}:
            print("Invalid choice!")
            continue
        firstCourse = input("Enter first course (exact name): ").strip()
        secondCourse = input("Enter second course (exact name): ").strip()
        if firstCourse not in courses or secondCourse not in courses:
            print(f"Invalid course name. Choose from: {', '.join(courses)}")
            continue
        if firstCourse == secondCourse:
            print("Choose two different courses for overlap analysis.")
            continue
        firstStudents = {sid for sid, student in students.items() if isActiveStudent(sid) and firstCourse in student['coursesRegistered']}
        secondStudents = {sid for sid, student in students.items() if isActiveStudent(sid) and secondCourse in student['coursesRegistered']}
        if choice == '1':
            result = firstStudents & secondStudents
            label = f"Students registered for both {firstCourse} and {secondCourse}"
        elif choice == '2':
            result = firstStudents - secondStudents
            label = f"Students registered for {firstCourse} but not {secondCourse}"
        elif choice == '3':
            result = firstStudents | secondStudents
            label = f"Students registered for at least one of {firstCourse} or {secondCourse}"
        elif choice == '4':
            result = firstStudents ^ secondStudents
            label = f"Students registered for exactly one of {firstCourse} and {secondCourse}"
        else:
            if firstStudents.isdisjoint(secondStudents):
                print("The two student groups are completely different.")
            else:
                print("The two student groups are not completely different.")
            continue
        print(f"{label}:")
        if result:
            for sid in sorted(result):
                print(f"{sid}: {students[sid]['name']}")
        else:
            print("No matching active students found.")

def checkSemesterEligibility(studentId):

    return students[studentId]['attendance']>=75    

def updateMarks(studentId, courseList, choice):
    course = courseList[choice - 1]
    if course not in students[studentId]['marks']:
        print(f"Marks for {course} have not been entered yet. Use Enter Student Marks first.")
        return
    oldMark = students[studentId]['marks'][course]
    print(f"Current {course} mark: {oldMark}")
    print("Enter updated marks:")
    newMark = validateMark(course)
    students[studentId]['marks'][course] = newMark
    removeMarkFromGlobalList(course, oldMark)
    addMarkToGlobalList(course, newMark)
    print("Marks updated successfully!")

def examResult(mark):

    if mark>=90:

        return "A"

    elif mark>=80:

        return "B"

    elif mark>=70:

        return "C"

    elif mark>=60:

        return "D"

    elif mark>=50:

        return "E"

    else:

        return "F"

def totalMarks(studentId):
    return sum(students[studentId]['marks'].values())

def avgMarks(marks, studentId):
    """Average only the marks actually entered for this student."""
    markCount = len(students[studentId]['marks'])
    if markCount == 0:
        return 0.0
    return marks / markCount

def studentWithdrawalMenu():
    while True:
        print("---------- Student Withdrawal ----------")
        print("1. Search Student for Withdrawal")
        print("2. Back to Main Menu")
        choice = input("Enter your choice: ").strip()
        match choice:
            case '1':
                studentId = input("Enter Student ID: ").strip()
                if not studentExist(studentId):
                    print("Student ID does not exist!")
                    continue
                if students[studentId]['academicStatus'] == "Withdrawn":
                    print("This student has already withdrawn.")
                    continue
                displayStudentRecord(studentId)
                confirm = input("Are you sure you want to withdraw this student? (y/n): ").strip().lower()
                if confirm == 'y':
                    # Global lists contain aggregate marks for active students only.
                    # Remove one occurrence for every mark held by this student.
                    for course, mark in list(students[studentId]['marks'].items()):
                        removeMarkFromGlobalList(course, mark)
                    students[studentId]['academicStatus'] = "Withdrawn"
                    print("Student withdrawn successfully.")
                elif confirm == 'n':
                    print("Withdrawal cancelled.")
                else:
                    print("Invalid response. Withdrawal cancelled.")
            case '2':
                print("Returning to main menu.")
                return
            case _:
                print("Invalid choice!")

def isActiveStudent(studentId):

    return (

        studentId in students

        and students[studentId]['academicStatus'] == "Active"

    )

while(True):

    print("-----------------------------------------")

    print("Please select the following options")

    print("-----------------------------------------")

    print("1. Student Registration\n" \

    "2. Student Search\n" \

    "3. Course Registration\n" \

    "4. Attendance\n" \

    "5. Marks\n" \

    "6. Result\n" \

    "7. Department Information\n" \

    "8. Student Statistics\n" \

    "9. Student Withdrawal\n" \

    "10. Exit")

    choice=input("Enter your choice (1-10): ").strip()

    match choice:

        case '1':

            studentRegistrationMenu()

        case '2':

            studentSearchMenu()

        case '3':

            studentCourseRegistrationMenu()

        case '4':

            studentAttendanceMenu()

        case '5':

            studentsMarksMenu()

        case '6':

            studentResultMenu()

        case '7':

            departmentInfoMenu()

        case '8':

            studentStatisticsMenu()

        case '9':

            studentWithdrawalMenu()

        case '10':

            print("Exiting the program. Thank you!")

            break

        case _:

            print("Invalid choice!")
