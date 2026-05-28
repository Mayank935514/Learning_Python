#Example-1 --> Passing an Integer
def fun(x):
    x=15
x=10
fun(x)
print(x)  ## local variable changes doesn't reflect changes on global variable
print()

#Example-2 --> Passing a List
def fun(l):
    l.append(15)
l=[10,20,30]
fun(l)
print(l)   ## here we are not changing reference, only modifying
print()

#Example-3
def fun(l):
    l=[40,50]
l=[10,20,30]
fun(l)
print(l)