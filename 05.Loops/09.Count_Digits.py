# count no. of digits
n=int(input("Enter a digit: "))
res=0
while n>0:
     n=n//10
     res+=1
print("Count od Digits:", res)