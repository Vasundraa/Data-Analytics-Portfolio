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

        choice=input("Enter your choice:")

        match choice:
            case '1':
                studentId=input("Enter student ID:")

                if(studentExist(studentId)):
                    print("Student ID already exists!")
                    continue

                student=getStudentDetails()
                students[studentId]=student
                print("Successfully Added Student Details!")

            case '2':
                displayStudentDetails()

            case '3':
                studentId=input("Enter student ID to update:")

                if(not studentExist(studentId)):
                    print(f"Student Record with {studentId} does not exist")
                    continue

                updateStudentDetails(studentId)

            case '4':
                print("Returning to main menu")
                return
            
            case _:
                print("Invalid choice!")

def studentSearchMenu():
    while(True):
        print("------------ Student Search -------------")

        studentId=input("Enter Student ID to Search:")

        if studentExist(studentId):
            displayStudentRecord(studentId)
            return
        
        print("Student ID does not exist!")

def studentCourseRegistrationMenu():
    while(True):
        print("---------- Course Registration ----------")
        print("1. Register Course")
        print("2. Display Registered Courses")
        print("3. Remove Course")
        print("4. Course Overlap Analysis")
        print("5. Back to Main Menu")

        choice=input("Enter your choice: ")

        match choice:

            case '1':
                studentId=input("Enter Student ID for Course Registration: ")

                if studentExist(studentId):
                    courseList=students[studentId]['coursesRegistered']
                    registerCourse(courseList)
                else:
                    print("Student ID does not exist!")


            case '2':
                studentId=input("Enter Student ID to display courses: ")

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
                studentId=input("Enter Student ID to remove course: ")

                if studentExist(studentId):
                        removeCourse(studentId)
                else:
                    print("Student ID does not exist!")


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

        choice=input("Enter your choice:")

        match choice:
            case '1':
                studentId=input("Enter Student ID to Update Attendance:")

                if studentExist(studentId) and len(students[studentId]['coursesRegistered'])>0:
                    attendance=validateAttendance()
                    students[studentId]['attendance']=attendance
                    print("Attendance Updated Successfully!")
                    return
                
                elif studentExist(studentId) and len(students[studentId]['coursesRegistered'])==0: 
                    print(f"Student {studentId} is not enrolled in any courses. Register course to continue adding attendance details.")
                    return
                
                print("Student ID does not exist!")

            case '2':
                studentId=input("Enter Student ID to Check Semester Exam Eligibilty:")
                if studentExist(studentId) and len(students[studentId]['coursesRegistered'])==0: 
                    print(f"Student {studentId} is not enrolled in any courses. Register course to continue adding attendance details.")
                    return
                if(studentExist(studentId)):
                    eligibilityStatus="Not Eligible"
                    
                    if checkSemesterEligibility(studentId):
                        eligibilityStatus="Eligible"
                    
                    print(f"{studentId} is {eligibilityStatus} for Semester Exam") 
                    return                
               
                print("Student ID does not exist!")

            case '3':
                executed=False
                for student in students:
                    if(not checkSemesterEligibility(student)):
                        print(f"{student:<15}{students[student]['name']:<20}{students[student]['attendance']:<15}{'Not Eligible':<15}")
                        executed=True
                if(not executed): print("No students are below the required attendance.")
                
            case '4':
                eligibleStudents=0
                
                for student in students:
                    if(checkSemesterEligibility(student)):
                        eligibleStudents+=1
                
                print(f"Total Student Count: {len(students)}\nCount of Eligible Students for Semester Examination: {eligibleStudents}")

            case '5':
                print("Returning to main menu.")
                return

            case _:
                print("Invalid Choice!")

def studentsMarksMenu():
    while(True):
        print("------------- Student Marks -------------")

        print("1. Enter student marks\n" \
        "2. Retrieve subject marks\n" \
        "3. Update student marks\n" \
        "4. Display academic summary\n" \
        "5. Calculate average marks\n" \
        "6. Identify highest mark\n" \
        "7. Back to main menu")

        choice=input("Enter your choice: ")

        match choice:
            case '1':
                studentId=input("Enter student ID to enter marks: ")
                if studentExist(studentId):
                    if not len(students[studentId]['coursesRegistered'])==0:
                        if len(students[studentId]['marks'])==0:
                            getMarks(studentId)
                            print("Marks entered successfully!")
                        else:
                            print("Marks are already entered. Update the marks if needed.")
                    else:
                        print("Student is not registered in any course to enter marks.")
                else:
                    print("Students ID does not exist!")

            case '2':
                studentId=input("Enter student ID to display marks: ")
                if studentExist(studentId):
                    if not len(students[studentId]['marks'])==0:
                        print(f"Student name: {students[studentId]['name']}")
                        for course in students[studentId]['marks']:
                            print(f"{course}: {students[studentId]['marks'][course]}")
                    else:
                        print("No marks are entered to display.")
                else:
                    print("Students ID does not exist!")

            case '3':
                studentId=input("Enter student ID to enter updated marks: ")
                if studentExist(studentId):
                    if not len(students[studentId]['marks'])==0:
                        while(True):
                            print("Courses enrolled:")
                            courseList = list(students[studentId]['coursesRegistered'])
                            i = 1
                            for course in courseList:
                                print(f"{i}. {course}")
                                i += 1
                            choice=input("Choose the course to update marks for:")
                            if choice.isdigit() and 1<=int(choice)<=len(students[studentId]['coursesRegistered']):
                                updateMarks(studentId, courseList, int(choice))
                                addMore=input("Want to update more marks? (y/n):") 
                                if addMore=='y':
                                    continue
                                
                                elif addMore=='n':
                                    print("Returning to Main Menu")
                                    return
                                else: 
                                    print("Invalid choice! Returning to main menu.")
                                    return
                            else:
                                print("Invalid choice!")
                    else:
                        print("Marks are not entered. Enter the marks first.")
                else:
                    print("Students ID does not exist!")

            case '4':
                studentId=input("Enter student ID to display academic summary: ")

                if studentExist(studentId):
                    if not len(students[studentId]['marks'])==0:
                        print(f"Student name: {students[studentId]['name']}")

                        totMarks=totalMarks(studentId)
                        failedSubjects=[]

                        print("-" * 40)
                        print(f"{'Subject':<20}{'Mark':<10}")
                        print("-" * 40)

                        for course in students[studentId]['marks']:
                            mark = students[studentId]['marks'][course]
                            print(f"{course:<20}{mark:<10}")
                            if(examResult(mark)=="F"): failedSubjects.append(course)
                        
                        avg=avgMarks(totMarks,studentId)
                        
                        print("-" * 40)
                        print(f"Total Mark: {totMarks}")
                        print(f"Average Mark: {avg}")

                        if not len(failedSubjects)==0:
                            print(f"Failed subjects: {failedSubjects}")

                        else:
                            print("Failed subjects: None")
                    else:
                        print("No marks are entered to display.")
                else:
                    print("Students ID does not exist!")

            case '5':
                print("Overall Average Marks for Each Subject")
                print("-" * 65)
                print(f"{'Subject':<15}{'No. of Students':<20}{'Average Mark':<15}")
                print("-" * 65)

                if len(excelMarks) == 0:
                    print(f"{'Excel':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'Excel':<15}{len(excelMarks):<20}{sum(excelMarks)/len(excelMarks):<15.2f}")

                if len(powerBIMarks) == 0:
                    print(f"{'Power BI':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'Power BI':<15}{len(powerBIMarks):<20}{sum(powerBIMarks)/len(powerBIMarks):<15.2f}")

                if len(pythonMarks) == 0:
                    print(f"{'Python':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'Python':<15}{len(pythonMarks):<20}{sum(pythonMarks)/len(pythonMarks):<15.2f}")

                if len(sqlMarks) == 0:
                    print(f"{'SQL':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'SQL':<15}{len(sqlMarks):<20}{sum(sqlMarks)/len(sqlMarks):<15.2f}")

                print("-" * 65)

            case '6':
                print("Highest Marks for Each Subject")
                print("-" * 65)
                print(f"{'Subject':<15}{'No. of Students':<20}{'Highest Mark':<15}")
                print("-" * 65)

                if len(excelMarks) == 0:
                    print(f"{'Excel':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'Excel':<15}{len(excelMarks):<20}{max(excelMarks):<15}")

                if len(powerBIMarks) == 0:
                    print(f"{'Power BI':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'Power BI':<15}{len(powerBIMarks):<20}{max(powerBIMarks):<15}")

                if len(pythonMarks) == 0:
                    print(f"{'Python':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'Python':<15}{len(pythonMarks):<20}{max(pythonMarks):<15}")

                if len(sqlMarks) == 0:
                    print(f"{'SQL':<15}{'0':<20}{'Not Available':<15}")
                else:
                    print(f"{'SQL':<15}{len(sqlMarks):<20}{max(sqlMarks):<15}")

                print("-" * 65)

            case '7':
                print("Returning to main menu")
                return
            
            case _:
                print(" Invalid choice!")

def studentResultMenu():
    while(True):
            print("------------ Student Result -------------")

            print("1. View student result\n" \
            "2. Process all student results\n" \
            "3. Back to main menu")

            choice=input("Enter your choice:")

            match choice:
                case '1':
                    studentId=input("Enter Student ID to view result:")
            
                    if studentExist(studentId):
                        if not len(students[studentId]['marks'])==0:
                            print(f"Student name: {students[studentId]['name']}")

                            totMarks=totalMarks(studentId)

                            print("-" * 50)
                            print(f"{'Subject':<20}{'Mark':<10}{'Grade':<10}")
                            print("-" * 50)

                            for course in students[studentId]['marks']:
                                mark = students[studentId]['marks'][course]
                                print(f"{course:<20}{mark:<10}{examResult(mark):<10}")

                            print("-" * 50)
                            avg=avgMarks(totMarks,studentId)

                            print(f"Total Mark   : {totMarks}")
                            print(f"Average Mark : {avg:.2f}")
                            print(f"Overall Grade: {examResult(avg)}")

                        else:
                            print("No marks are entered to display.")
                        return
                    
                    print("Student ID does not exist!")

                case '2':
                    if not len(students)==0:
                        print("-" * 120)
                        print(f"{'Student ID':<15}{'Student Name':<20}{'Department':<15}{'Eligibility':<18}{'Average':<12}{'Grade':<10}{'Result':<10}")
                        print("-" * 120)
                        for student in students:
                            if len(students[student]['marks'])==0:
                                noData="No Data"
                                eligibility = "Eligible" if checkSemesterEligibility(student) else "Not Eligible"
                                print(f"{student:<15}"
                                    f"{students[student]['name']:<20}"
                                    f"{students[student]['department']:<15}"
                                    f"{eligibility:<18}"
                                    f"{noData:<12}"
                                    f"{noData:<10}"
                                    f"{noData:<10}")
                            else:
                                totMarks = totalMarks(student)
                                avg = avgMarks(totMarks, student)

                                eligibility = "Eligible" if checkSemesterEligibility(student) else "Not Eligible"
                                grade = examResult(avg)
                                result = "Fail" if grade == "F" else "Pass"

                                print(f"{student:<15}"
                                    f"{students[student]['name']:<20}"
                                    f"{students[student]['department']:<15}"
                                    f"{eligibility:<18}"
                                    f"{avg:<12.2f}"
                                    f"{grade:<10}"
                                    f"{result:<10}")

                        print("-" * 120)
                    else:
                        print("There are no student records stored.")

                case '3':
                    print("Returning to main menu.")
                    break

                case _:
                    print("Invalid choice!")

def departmentInfoMenu():
    while(True):
        print("---------- Department Information ----------")
        print("1. Display Available Departments")
        print("2. Display Students by Department")
        print("3. Back to Main Menu")

        choice=input("Enter your choice: ")

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

                choice=input("Choose a department: ")

                if choice.isdigit():
                    choice=int(choice)

                    if 1 <= choice <= len(depts):
                        selectedDepartment=depts[choice-1]

                        print(f"\n---------- {selectedDepartment} Students ----------")
                        print(f"{'Student ID':<20}{'Student Name':<20}")
                        print("-" * 40)

                        studentsFound=False

                        for studentId in students:
                            if students[studentId]["department"] == selectedDepartment:
                                print(f"{studentId:<20}{students[studentId]['name']:<20}")
                                studentsFound=True

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
    while(True):
        print("---------- Student Statistics ----------")
        print("1. Total Number of Students")
        print("2. Department-wise Student Count")
        print("3. Exam Eligible Students")
        print("4. Failed Students")
        print("5. Highest Average Mark")
        print("6. Lowest Average Mark")
        print("7. Overall Batch Average")
        print("8. Unique Departments Represented")
        print("9. Students Registered for a Course")
        print("10. Back to Main Menu")

        choice=input("Enter your choice: ")

        match choice:
            case '1':
                print(f"Total Number of Students: {len(students)}")

            case '2':
                print("---------- Department-wise Student Count ----------")
                print(f"{'Department':<15}{'Student Count':<15}")
                print("-" * 30)

                for department in depts:
                    count=0

                    for studentId in students:
                        if students[studentId]['department'] == department:
                            count+=1

                    print(f"{department:<15}{count:<15}")

            case '3':
                eligibleStudents=0

                for studentId in students:
                    if checkSemesterEligibility(studentId):
                        eligibleStudents+=1

                print(f"Students Eligible for Semester Examination: {eligibleStudents}")

            case '4':
                failedStudents=0

                for studentId in students:
                    if len(students[studentId]['marks']) == 0:
                        continue

                    studentFailed=False

                    for course in students[studentId]['marks']:
                        mark=students[studentId]['marks'][course]

                        if examResult(mark) == "F":
                            studentFailed=True
                            break

                    if studentFailed:
                        failedStudents+=1

                print(f"Students who failed: {failedStudents}")

            case '5':
                highestAverage=0
                highestStudent=""

                for studentId in students:

                    if len(students[studentId]['marks']) == 0:
                        continue

                    totMarks=totalMarks(studentId)
                    average=avgMarks(totMarks, studentId)

                    if average > highestAverage:
                        highestAverage=average
                        highestStudent=studentId

                if highestStudent=="":
                    print("No student marks are available.")
                else:
                    print("---------- Highest Average Mark ----------")
                    print(f"{'Student ID':<20}{'Student Name':<20}{'Average':<10}")
                    print("-" * 50)
                    print(f"{highestStudent:<20}"
                        f"{students[highestStudent]['name']:<20}"
                        f"{highestAverage:<10.2f}")

            case '6':
                lowestAverage=101
                lowestStudent=""

                for studentId in students:

                    if len(students[studentId]['marks']) == 0:
                        continue

                    totMarks=totalMarks(studentId)
                    average=avgMarks(totMarks, studentId)

                    if average < lowestAverage:
                        lowestAverage=average
                        lowestStudent=studentId

                if lowestStudent=="":
                    print("No student marks are available.")
                else:
                    print("---------- Lowest Average Mark ----------")
                    print(f"{'Student ID':<20}{'Student Name':<20}{'Average':<10}")
                    print("-" * 50)
                    print(f"{lowestStudent:<20}"
                        f"{students[lowestStudent]['name']:<20}"
                        f"{lowestAverage:<10.2f}")

            case '7':
                pass

            case '8':
                pass

            case '9':
                pass

            case '10':
                return

            case _:
                print("Invalid choice!")

# Validation
def validateYear():
    while(True):
        year=input("Enter year of admission:")
        
        if year.isdigit() and len(year)==4:
            return int(year)
        
        print("Invalid Year!")

def validateEmail():
    while(True):
        email=input("Enter email:")
        
        if re.match(r'^[a-zA-Z0-9.]+@[a-zA-Z]+\.[a-zA-Z]{3}$',email):
            return email
        
        print("Invalid Email!")

def validatePhoneNumber():
    while(True):
        phoneNumber=input("Enter phone number:")
        
        if len(phoneNumber)==10 and phoneNumber.isdigit():
            return phoneNumber
        
        print("Invalid phone number!")

def validateAttendance():
    while(True):
        attendance=input("Enter attendance (%):")
        
        if attendance.isdigit() and 0<= int(attendance) <= 100:
            return int(attendance)
        
        print("Invalid attendance range! Enter attendance between 0 to 100.")

def validateMark(course):
    while(True):
        mark=input(f"Enter {course} marks:")
        
        if mark.isdigit() and 0<=int(mark)<=100:
            return int(mark)
        
        print("Invalid mark! Enter mark between 0 to 100")


def getDepartment():   
    while True:
        for i in range(len(depts)):
            print(f"{i + 1}. {depts[i]}: {departments[depts[i]]}")

        choice = input("Choose the department:")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(depts):
                return depts[choice - 1]

        print("Invalid choice!")


def studentExist(studentId):
    return studentId in students

def getMarks(studentId):
    for course in students[studentId]['coursesRegistered']:
        mark=validateMark(course)
        students[studentId]['marks'][course]=mark
        if course == "Python":
            pythonMarks.append(mark)
        elif course == "SQL":
            sqlMarks.append(mark)
        elif course == "Excel":
            excelMarks.append(mark)
        elif course == "Power BI":
            powerBIMarks.append(mark)

def getStudentDetails():
    print("Enter Student Details")
    
    name=input("Enter student name:")
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
        
        choice=input("Enter your choice (1-7):")
        
        match choice:
            case '1':
                newStudentId=input("Enter new student ID:")
                
                if(studentExist(newStudentId)):
                    print("Student ID Already Exists!")
                    continue
                
                students[newStudentId]=students[studentId]
                del students[studentId]
                studentId=newStudentId
                print("Student ID Updated Successfully!")
            
            case '2':
                name=input("Enter name:")
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
    while(True):
        i=1
        
        for course in courses:
            print(f"{i}. {course}")
            i+=1
        
        choice=input(f"Enter your choice to register course (1 - {len(courses)}):")
        
        if(choice.isdigit() and 1<=int(choice)<=len(courses)):
            course=courses[int(choice)-1]
            
            if(course in courseList): 
                print(f"{course} already registered.")
                continue
            
            courseList.add(course)
            print("Course added successfully!")
            addMore=input("Want to add more courses? (y/n):")
            
            if addMore=='y':
                continue
            
            elif addMore=='n':
                sorted(courseList)
                print("Returning to Main Menu")
                return courseList
        
        print("Invalid choice!")

def removeCourse(studentId):
    courseList=students[studentId]['coursesRegistered']

    if len(courseList)==0:
        print("Student is not registered for any course.")
        return

    print("Registered Courses:")

    courseListDisplay=list(courseList)

    for i in range(len(courseListDisplay)):
        print(f"{i + 1}. {courseListDisplay[i]}")

    choice=input("Choose the course to remove: ")

    if choice.isdigit():
        choice=int(choice)

        if 1 <= choice <= len(courseListDisplay):
            course=courseListDisplay[choice - 1]

            courseList.remove(course)

            if course in students[studentId]['marks']:
                oldMark=students[studentId]['marks'][course]
                del students[studentId]['marks'][course]

                if course == "Python":
                    pythonMarks.remove(oldMark)
                elif course == "SQL":
                    sqlMarks.remove(oldMark)
                elif course == "Excel":
                    excelMarks.remove(oldMark)
                elif course == "Power BI":
                    powerBIMarks.remove(oldMark)

            print(f"{course} removed successfully!")
            return

    print("Invalid choice!")


def courseOverlapAnalysis():
    while(True):
        print("---------- Course Overlap Analysis ----------")
        print("1. Students registered for both courses\n" \
        "2. Students registered for first course but not second\n" \
        "3. Students registered for at least one of the courses\n" \
        "4. Students registered for exactly one of the courses\n" \
        "5. Check whether two student groups are completely different\n" \
        "6. Back")

        choice=input("Enter your choice: ")

        match choice:

            case '1':
                firstCourse=input("Enter first course: ")
                secondCourse=input("Enter second course: ")

                firstStudents=set()
                secondStudents=set()

                for studentId in students:
                    if firstCourse in students[studentId]['coursesRegistered']:
                        firstStudents.add(studentId)

                    if secondCourse in students[studentId]['coursesRegistered']:
                        secondStudents.add(studentId)

                commonStudents=firstStudents & secondStudents

                print(f"Students registered for both {firstCourse} and {secondCourse}:")
                print(commonStudents)


            case '2':
                firstCourse=input("Enter first course: ")
                secondCourse=input("Enter second course: ")

                firstStudents=set()
                secondStudents=set()

                for studentId in students:
                    if firstCourse in students[studentId]['coursesRegistered']:
                        firstStudents.add(studentId)

                    if secondCourse in students[studentId]['coursesRegistered']:
                        secondStudents.add(studentId)

                studentsOnlyInFirst=firstStudents - secondStudents

                print(f"Students registered for {firstCourse} but not {secondCourse}:")
                print(studentsOnlyInFirst)


            case '3':
                firstCourse=input("Enter first course: ")
                secondCourse=input("Enter second course: ")

                firstStudents=set()
                secondStudents=set()

                for studentId in students:
                    if firstCourse in students[studentId]['coursesRegistered']:
                        firstStudents.add(studentId)

                    if secondCourse in students[studentId]['coursesRegistered']:
                        secondStudents.add(studentId)

                atLeastOne=firstStudents | secondStudents

                print(f"Students registered for at least one of {firstCourse} or {secondCourse}:")
                print(atLeastOne)


            case '4':
                firstCourse=input("Enter first course: ")
                secondCourse=input("Enter second course: ")

                firstStudents=set()
                secondStudents=set()

                for studentId in students:
                    if firstCourse in students[studentId]['coursesRegistered']:
                        firstStudents.add(studentId)

                    if secondCourse in students[studentId]['coursesRegistered']:
                        secondStudents.add(studentId)

                exactlyOne=firstStudents ^ secondStudents

                print(f"Students registered for exactly one of {firstCourse} and {secondCourse}:")
                print(exactlyOne)

            case '5':
                firstCourse=input("Enter first course: ")
                secondCourse=input("Enter second course: ")

                firstStudents=set()
                secondStudents=set()

                for studentId in students:
                    if firstCourse in students[studentId]['coursesRegistered']:
                        firstStudents.add(studentId)

                    if secondCourse in students[studentId]['coursesRegistered']:
                        secondStudents.add(studentId)

                if firstStudents.isdisjoint(secondStudents):
                    print("The two student groups are completely different.")
                else:
                    print("The two student groups are not completely different.")


            case '6':
                print("Returning to course registration menu.")
                return


            case _:
                print("Invalid choice!")

def checkSemesterEligibility(studentId):
    return students[studentId]['attendance']>=75    

def updateMarks(studentId ,courseList, choice):
    course=courseList[choice-1]
    oldMark=students[studentId]['marks'][course]
    print(f"Current {course} mark: {oldMark}")
    print("Enter updated marks:")
    newMark=validateMark(course)
    students[studentId]['marks'][course]=newMark
    if course == "Python":
        pythonMarks[pythonMarks.index(oldMark)]=newMark
    elif course == "SQL":
        sqlMarks[sqlMarks.index(oldMark)]=newMark
    elif course == "Excel":
        excelMarks[excelMarks.index(oldMark)]=newMark
    elif course == "Power BI":
        powerBIMarks[powerBIMarks.index(oldMark)]=newMark
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
    totalMarks=0

    for course in students[studentId]['marks']:
        totalMarks+=students[studentId]['marks'][course]

    return totalMarks

def avgMarks(marks,studentId):
    return marks/len(students[studentId]['coursesRegistered'])

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
    
    choice=input("Enter your choice (1-10):")
    
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
            pass

        case '10':
            print("Exiting the program. Thank you!")
            break

        case _:
            print("Invalid choice!")