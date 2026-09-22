class Student:
    def __init__(self, name, dept, marks, attendance):
        self.name = name
        self.dept = dept

        self.setMarks(marks)
        self.setAttendance(attendance)

        self.setTotalMarks()
        self.setCGPA()

    # Getter and Setter for marks
    def getMarks(self):
        return self._marks

    def setMarks(self, marks):
        for mark in marks:
            if not 0 <= mark <= 100:
                raise ValueError("Invalid marks. Marks should be between 0 and 100")

        self._marks = marks

    # Getter and Setter for attendance
    def getAttendance(self):
        return self._attendance

    def setAttendance(self, attendance):
        if not 0 <= attendance <= 100:
            raise ValueError("Invalid attendance. Attendance should be between 0 and 100")

        self._attendance = attendance

    # Getter and Setter for total marks
    def getTotalMarks(self):
        return self._totalMarks

    def setTotalMarks(self):
        self._totalMarks = sum(self._marks)

    # Getter and Setter for CGPA
    def getCGPA(self):
        return self._cgpa

    def setCGPA(self):
        maximum_marks = len(self._marks) * 100
        self._cgpa = (self._totalMarks / maximum_marks) * 10

    # Display only CGPA
    def displayCGPA(self):
        print("CGPA:", round(self._cgpa, 2))


# Creating object
student1 = Student(
    "Vasundraa",
    "CSE",
    [85, 90, 78, 88, 92],
    95
)

student1.displayCGPA()