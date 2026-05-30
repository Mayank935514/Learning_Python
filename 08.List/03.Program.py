#Ques- Separate Even and Odd
def getEvenOdd(l):
    even=[]
    odd=[]
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd
l=[10,12,11,16]
even,odd=getEvenOdd(l)
print(even)
print(odd)
