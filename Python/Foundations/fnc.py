def gradeCalc(marks):
    if(marks<=100 and marks>=0):
        if(marks>=90): return 'O'
        elif(marks>=80): return'A'
        elif(marks>=70): return 'B'
        elif(marks>=60): return 'C'
        elif(marks>=40): return'D'
        else: return'RA'
    else:
        return "Invalid Input"
