#Code-1
def decToBinary(n):
    if n==0:
        return "0"
    res=""
    while n>0:
        res=res+str(n%2)
        n=n//2
    return res[::-1]
n = int(input("Enter a decimal number: "))
print("Binary representation is:", decToBinary(n))

#Code-2
def decToBinary(n):
    res=bin(n)
    return res[2:]
n = int(input("Enter a decimal number: "))
print("Binary representation is:", decToBinary(n))