#Global variables are the variables which are created outside any function or any class.
#Local variables can't be accessed outside the function.
#Global variable can be accessed inside the local variable.
#Example-1
def fun():
    a=10
    b=20
    print(a,b,c,d)
c=30
d=40
fun()
print(c,d)
print()

#Example-2 --> To change the global variable use 'global' keyword
def fun():
    global x
    x=10
x=15
fun()
print(x)
print()

#Example-3
def fun():
    y=x+5 ##If you see global variable x on right side of local variable then there is no issue or error.
    print(y)
x=15
fun()
print()

#Example-4
def fun():
    x=x+5 ## It raises an error because we are trying to make local variable
    print(x)
x=15
fun()
print()

#Example-5 --> if we have same name of local and global variable, so it hides the global variable.
def fun():
    x=10 #local variable
    globals()['x']=20 #changing global variable
    print(x)
x=15 #global variable
fun()
print(x) #modified global variable
# o/p: 10
#      20