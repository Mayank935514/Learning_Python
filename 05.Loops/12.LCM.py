#Code-1
import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
gcd=math.gcd(a,b)
lcm=(a*b)/gcd
print("LCM is",lcm)
print()

#Code-2
a=int(input("Enter a: "))
b=int(input("Enter b: "))
res = max(a,b)
while res<=(a*b):
    if res%a == 0 and res%b ==0:
        break
    res+=1
print("LCM is:",res)