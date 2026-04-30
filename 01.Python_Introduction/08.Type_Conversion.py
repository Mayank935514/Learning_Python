# Example-1--> Implicit Type Conversion 
a=10
b=1.5
c=a+b
print(c)
d=True
e=a+d
print(e)
print()

# Explicit Type Conversion Example #
# Example-1
s="135"
i=10+int(s)
f=float(s)
print(i)
print(f)
print()

# Example-2
s="ravi"
print(list(s))
print(tuple(s))
print(set(s))
print()

# Example-3
l=['a','b','c']
print(str(l))
a=10
b=11
print(str(a) + str(b))
c=12.5
print(str(c))
print()

# Example-4
t=(10,20,30)
print(list(t))
s={10,20,30}
print(list(s))
print()

# Example-5
a=20
print(bin(a))
print(hex(a))
print(oct(a))
print()

# Example-6
a="1001"
print(int(a,2))
print(int(a,8))
print(int(a,16))