#task - printing even numbers
#method 1
nums=[1,2,3,4,5,6]
even=[]
for n in nums:
    if(n%2==0): even.append(n)
print(f"Result using for loop: {even}")

#method 2 - function
def func(nums):
    even=[]
    for n in nums:
        if(n%2==0): even.append(n)
    return even
print(f"Result using function: {func(nums)}")

#method 3 - lambda function and filter
res=list(filter(lambda x:x%2==0,nums))
print(f"Result using filer: {res}")
