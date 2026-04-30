# Example-1
t=(10,0,"gmp")
print(t)
t=()
print(type(t))
print(t)
t=10
print(type(t))
t=(10,)   #To create a tuple with a single value, then we use comma after the value.
print(type(t))
print()

# Example-2--> In tuple, paranthesis are optional
t=10,20,30,40,10
print(t[2])
print(t[-1])
print(t[1:3])
print(len(t))
print(t.count(10))
print(t.index(20))