#Code-1
def getFirstDigit(x):
    while x>=10:
        x=x//10
    return x
x=int(input("Enter digit: "))
print(getFirstDigit(x))
print()

#Code-2
import math
def getFirstDigit(x):
    d=int(math.log10(x))
    res=x//(10**d)
    return res
x=int(input("Enter digit: "))
print(getFirstDigit(x))