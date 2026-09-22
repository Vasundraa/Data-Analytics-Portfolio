from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,email):
        self.name=name
        self.email=email

    @abstractmethod
    def displayRole(self):
        return "University Person"

    @abstractmethod
    def display_dashboard(self):
        pass

class Student(Person):
    def __init__(self,name,email,dept):
        super().__init__(name,email)
        self.dept=dept

    def displayRole(self):
        return "Student"

    def display_dashboard(self):
        return "Student Dashboard"

class Teacher(Student):
    def __init__(self,name,email,dept,sub):
        super().__init__(name,email,dept)
        self.sub=sub

    def displayRole(self):
        return "Teacher"

    def display_dashboard(self):
        return "Teacher Dashboard"

persons=[
    Student("Ram","abc@gmail.com","CSE"),
    Teacher("Sheela","cde@gmail.com","IT",["Maths","CS"])
]

persons[1].display_dashboard()