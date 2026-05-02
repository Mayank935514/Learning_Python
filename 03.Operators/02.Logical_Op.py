# Example-1
a=9
b=20
c=30
print(a<b and b<c)
print(a<b or b>c)
print(not a>b)
print()

# Example-2--> Expressions that are treated as false: None, Empty, list, tuple, Dictionary,etc.
s1=" "
s2=s1 or "Defaulter"
print(s2)
print()

# Example-3
x=10
print(x or 20)
y=0
print(y or 30)
z=40
print(z and 50) # z is no-zero value so it will give last evaluated value 

