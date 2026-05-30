# Check whether the list is sorted or not.
#Code-1
def isSorted(l):
    i=1
    while i<len(l):
        if l[i] < l[i-1]:
            return False
        i+=1
    return True
l=[10,20,30,50,40]
if isSorted(l):
    print("Yes")
else:
    print("No")

#Code-2
def isSort(l):
    sl=sorted(l)  #sorted method doesn't modify the list and provides the sorted version of list.
    if sl == l:
        return True
    else:
        return False
l=[10,20,5,30]
if isSort(l):
    print("Yes")
else:
    print("No")