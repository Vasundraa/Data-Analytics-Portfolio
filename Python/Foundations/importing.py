from fnc import gradeCalc
studentList=[]
for ct in range(3):
    std={}
    std["name"]=input(f"{ct+1} Enter your name:")
    std["marks"]=int(input("Enter your marks:"))
    std["grade"]=gradeCalc(std["marks"])
    studentList.append(std)
[print(std) for std in studentList] #list comprehension