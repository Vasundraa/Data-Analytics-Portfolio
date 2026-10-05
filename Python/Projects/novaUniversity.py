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
        studentId=input("Enter Student ID for Course Registration:")
        
        if studentExist(studentId):
            courseList=students[studentId]['coursesRegistered']
            registerCourse(courseList)
            return
        
        print("Student ID does not exist!")        

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
                        print(f"{student}\t\t{students[student]['name']}\t\t{students[student]['attendance']}\t\tNot Eligible")
                        executed=True
                if(not executed): print("No students are below the required attendance.")
                
            case '4':
                eligibleStudents=0
                
                for student in students:
                    if(checkSemesterEligibility(student)):
                        eligibleStudents+=1
                
                print(f"Total Student Count: {len(students)}\nCount of Eligible Students for Semester Examination: {eligibleStudents}")

            case '5':
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
                        print("Marks are already entered. Update the marks if needed.")
                else:
                    print("Students ID does not exist!")

            case '4':
                studentId=input("Enter student ID to display academic summary: ")

                if studentExist(studentId):
                    if not len(students[studentId]['marks'])==0:
                        print(f"Student name: {students[studentId]['name']}")

                        totalMarks=0
                        totalCourse=len(students[studentId]['marks'])
                        failedSubjects=[]

                        for course in students[studentId]['marks']:
                            mark=students[studentId]['marks'][course]

                            print(f"{course}: {mark}")

                            if(examResult(mark)=="F"): failedSubjects.append(course)

                            totalMarks+=mark

                        print(f"Total Mark: {totalMarks}\nAverage Mark: {totalMarks/totalCourse}")

                        if not len(failedSubjects)==0:
                            print(f"Failed subjects: {failedSubjects}")

                        else:
                            print("Failed subjects: None")
                    else:
                        print("No marks are entered to display.")
                else:
                    print("Students ID does not exist!")

            case '5':
                print()

            case '6':
                pass

            case '7':
                return
            
            case _:
                print(" Invalid choice!")


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
            pass

        case '7':
            pass

        case '8':
            pass

        case '9':
            pass

        case '10':
            print("Exiting the program. Thank you!")
            break

        case _:
            print("Invalid choice!")