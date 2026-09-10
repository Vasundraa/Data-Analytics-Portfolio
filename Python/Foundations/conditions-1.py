marks=int(input("Enter the marks:"))
print("Grade: ")
if(marks<=100 and marks>=90):
    print("A")
elif(marks<90 and marks>=75):
    print("B")
elif(marks<75 and marks>=50):
    print("C")
elif(marks<50 and marks>=0):
    print("Fail")
else:
    print("Invalid Entry")