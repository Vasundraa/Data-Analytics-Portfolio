class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def displayRole(self):
        return "University Person"

class Student(Person):
    def __init__(self,name,email,dept):
        super().__init__(name,email)
        self.dept=dept

    def displayRole(self):
        return "Student"

class Teacher(Student):
    def __init__(self,name,email,dept,sub):
        super().__init__(name,email,dept)
        self.sub=sub

    def displayRole(self):
        return "Teacher"

persons=[
    Student("Ram","abc@gmail.com","CSE"),
    Teacher("Sheela","cde@gmail.com","IT",["Maths","CS"])
]

for person in persons:
    print(person.displayRole())