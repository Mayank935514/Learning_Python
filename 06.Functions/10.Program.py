def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def primeFactor(n):
    for i in range(2,n+1):
        if isPrime(i):
            while n%i == 0:
                print(i)
                n=n//i
n=int(input("Enter n: "))
print(primeFactor(n))