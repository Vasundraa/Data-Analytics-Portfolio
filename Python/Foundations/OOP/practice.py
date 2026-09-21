class Student:
    def __init__(self,attendance):
        if(0<=attendance<=100):
            self._attendance=attendance
        else:
            raise ValueError("Invalid Attendance Percentage")

    def get_attendance(self):
        return self._attendance

    def set_attendance(self,attendance):
        if(0<=attendance<=100):
            self._attendance=attendance
        else:
            raise ValueError("Invalid Attendance Percentage")

    

student=Student(15)
student._attendance=150
print(student.get_attendance())