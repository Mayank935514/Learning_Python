#Single characters are always pallindrome.
#Code-1
s=input("Enter a string: ")
low=0
high=len(s)-1
while low < high:
    if s[low]!=s[high]:
        print("No")
        break
    low=low+1
    high=high-1
else:
    print("Yes")

#Code-2
s=input("Enter a string: ")
if s==s[::-1]:
    print("Yes")
else:
    print("No")