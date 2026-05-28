#Example-1 --> Without Parameters
def fun():
    print("fun() called")
print("Before calling fun()")
fun()
fun()
print("After calling fun()")
print()

#Example-2 --> With Parameters
def printDates(d,m,y):
    print(d,m,y,sep="-")
printDates("15","08","2000")
print()

#Example-3 --> Function can return Values
def getDate(d,m,y):
    return d+"-"+m+"-"+y
d=getDate("15","2","2001")
print(d)
