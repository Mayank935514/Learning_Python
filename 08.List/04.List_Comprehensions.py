# List Comprehensions --> provides us a shortcut syntax to create a list from another iterable.
l1=[x for x in range(11) if x%2 == 0]
print(l1)
print()

#Example-1 --> Get Smaller Elements
def getSmaller(l,x):
    return [e for e in l if e<x]
l=[9,15,12,3,7,11]
x=10
print(getSmaller(l,x))
print()

#Example-2 --> Separate even odd
def getEvenOdd(l):
    even=[x for x in l if x%2 == 0]
    odd=[x for x in l if x%2!= 0]
    return even,odd
l=[10,3,20,5,12]
even,odd=getEvenOdd(l)
print(even)
print(odd)
print()

#Example-3
l1=["geeks","for","geeks","gfg","idle"]
l2=[x.upper() for x in l1 if x.startswith("g")]
print(l2)

