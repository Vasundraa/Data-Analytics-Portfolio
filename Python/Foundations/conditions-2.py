marks=int(input("Enter the marks:"))
print("Result: ")
if(marks<=100 and marks>=90):
    print("Excellent")
elif(marks<90 and marks>=75):
    print("Good")
elif(marks<75 and marks>=50):
    print("Pass")
elif(marks<50 and marks>=0):
    print("Fail")
else:
    print("Invalid Entry")