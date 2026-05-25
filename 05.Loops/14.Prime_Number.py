#Code-1 --> Naive Approach
n=int(input("Enter n: "))
if n<=1:
    print("NO")
else:
    for i in range(2,n):
        if n%i == 0:
            print("NO")
            break
    else:
            print("Yes")
print()

#Code-2 --> Optimized Solution
n=int(input("Enter n: "))
if n<=1:
    print("NO")
else:
     x=2
     while x*x <= n:
          if n%x == 0:
               print("NO")
               break
          x+=1
     else:
          print("Yes")