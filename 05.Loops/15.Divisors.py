#Code-1 --> Naive Approach 
n=int(input("Enter n: "))
for i in range(1,n+1):
    if n%i == 0:
        print(i)
print()

#Code-2 --> using while loop
n=int(input("Enter n: "))
x=1
while x<=n:
    if n%x == 0:
        print(x)
    x+=1
print()

#Code-3 --> Optimized Solution
n=int(input("Enter n: "))
x=1
while x*x <= n:
    if n%x == 0:
        print(x)
        print(n/x)
    x+=1
if x*x == n:
    print(x)