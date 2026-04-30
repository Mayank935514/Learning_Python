"""
Variables are just references to memory locations, they don't have any type information associated with them.
"""
# Swap Two numbers
x=100
y=200
temp=x
x=y
y=temp
print(x)
print(y)

# We can do this using comma assignment
x=100
y=200
x,y=y,x
print(x)
print(y)

# we can multiply values to multiply variables
x,y,z=100,"hello",10.5
print(x)
print(y)
print(z)
x,y=x-5,y+" World"
print(x)
print(y)