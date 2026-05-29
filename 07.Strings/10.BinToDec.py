#Code-1
def binTodec(n):
    res=0
    p=1
    for x in reversed(n):
        res=res+int(x)*p
        p=p*2
    return res
n = input("Enter a Binary number: ")
print("Decimal is:", binTodec(n))

#Code-2
def binTodec(n):
    res=int(n,2)
    return res
n = input("Enter a Binary number: ")
print("Decimal is:", binTodec(n))
