# id() function--> It is a built-in function that gives a unique identifier for every object.

print(id(5))
a=10
print(id(a))
b=a
print(id(b))

# In python literals are stored at same location if they have same values.
a=20
b=20
print(id(a))
print(id(b))

# "is" operator in python checks the identity of two objects.
a=30
b=30
print(a is b)
c=40
print(c is b)