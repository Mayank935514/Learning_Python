#Ques-- Find the smallest divisor of a number such that the divisor is greater than 1
#Code-1
n=int(input("Enter a number: "))
for x in range(2,n+1):
    if(n%x == 0):
        print(x)
        break

#Code-2
n=int(input("Enter a number: "))
x=2
while x<=n:
    if n%x == 0:
        print(x)
        break
    x+=1