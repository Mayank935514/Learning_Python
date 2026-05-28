# It is dictionary based
#Example-1
def printDetails(**details):
    for d,v in details.items():
        print(f"{d} is {v}")
printDetails(id=101,name="abs",price=100)
print()

#Example-2
def printDetails(id,**details):
    print(f"Details of {id}:")
    for d,v in details.items():
        print(f"{d} is {v}")
printDetails(id=101,name="abs",price=100)
print()
printDetails(id=102,name="erbs",price=200)
