a=[10,20,30,40,50]

#to perform a function to each value in the iterables map() is used
mapResult=list(map(lambda x:x+5,a)) #lambda is an anonymous function - single line function
print(mapResult)