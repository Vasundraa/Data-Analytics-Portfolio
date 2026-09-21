class Student:
    university = "Nova University"

    def __init__ (self, name, id, dept, marks):
        self.name=name
        self.id=id
        self.dept=dept
        self.marks=marks
        self.atd=0
        print("Details Stored!")

    def avg(self):
        return sum(self.marks)/len(self.marks)
    
    def display(self):
        return f"Name:{self.name}\nID:{self.id}\nDepartment:{self.dept}\nMarks:{self.marks}\nUniversity:{self.university}"

def checkRecords(stuNum,stds):
    if(len(stds)!=0):
        if(stuNum>=1 and stuNum<=len(stuNum)):
            return True
        else:
            print(f"Invalid Student Number Choice. Student Number should be between 1 to {len(stds)}")
            return False
    else:
        print("No Student Records Available")
        

stds=[]
num=0
while True:
    print("-------------------------------\n1. Register Student\n2. Display Average mark\n3. Display Details\n4. Exit")
    choice=int(input())

    if(choice>=1 and choice<=4):
        if(choice==1):
            stds.append("")
            print(f"Enter student {num+1} details:")
            name=input("Enter student name:")
            id=input("Enter id:")
            dept=input("Enter department:")
            marks=[]
            for i in range(3):
                mark=int(input(f"Enter mark {i+1}:"))
                marks.append(mark)
            stds[num]=Student(name,id,dept,marks)
            num+=1

        elif(choice==2):
            stuNum=int(input("Enter Student Number:"))
            if(stuNum>=1 and stuNum<=len(stds)):
                print(f"Average of student {stuNum} is {stds[stuNum-1].avg()}")
            else:
                print(f"Invalid Student Number Choice. Student Number should be between 1 to {len(stds)}")

        elif(choice==3):
            stuNum=int(input("Enter Student Number:"))
            if(stuNum>=0 and stuNum<=len(stds)):
                print(f"Details of student {stuNum}:\n {stds[stuNum-1].display()}")
            else:
                print(f"Invalid Student Number Choice. Student Number should be between 1 to {len(stds)}")

        else:
            print("Program Stopped")
            break
    else:
        print("Invalid Choice")