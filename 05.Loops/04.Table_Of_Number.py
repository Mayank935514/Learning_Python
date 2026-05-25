#Code-1
n=int(input("Enter a number: "))
i=1
while i<11:
    print(i*n)
    i+=1
print()

#Code-2
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n*i)
print()

#Code-3
n=int(input("Enter a n: "))
m=int(input("Enter a m: "))
for i in range(1, m+1):
    print(n*i, end=" ")
