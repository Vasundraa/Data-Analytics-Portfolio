def func(n):
    return n*n
n=int(input("Enter a number:"))
res=func(n)
print("Square of number",n,"is",res)

#using lambda function
n=int(input("Enter a number:"))
sqrNum=lambda x:x*x
print(sqrNum(n))