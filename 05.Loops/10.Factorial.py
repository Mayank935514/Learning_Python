#Code-1
import math
n=int(input("Enter a number: "))
res=math.factorial(n)
print("Factorial is:",res)
print()

#Code-2
n=int(input("Enter a number: "))
res=1
for i in range(2,n+1):
    res=res*i
print("Factorial is:",res)