# Example-1
# Arithmetic Progression of nth term
a=int(input("Enter a: "))
d=int(input("Enter d: "))
n=int(input("Enter n: "))
res=a+(n-1)*d
print(res)
print()

# Example-2 
#Geometric Progression of nth term
a=int(input("Enter a: "))
r=int(input("Enter r: "))
n=int(input("Enter n: "))
res=a*r**(n-1)
print(res)
print()

# Example-3
# Sum of Natural Numbers
n=int(input("Enter n: "))
Sum=n*(n+1)/2
print("Sum is",Sum)
print()

# Example-4
# Find Last Digit of a Number
x=int(input("Enter x: "))
ld = abs(x)%10
print("Last Digit is: ",ld)
print()

# Example-5
# Day Before N Days 
d=int(input("Enter d: "))
n=int(input("Enter n: "))
print((d-n)%7)