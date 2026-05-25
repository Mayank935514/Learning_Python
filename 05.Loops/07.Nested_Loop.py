#Example-1 --> Print Tables of a number from 1 to 10
for  i in range(1,11):
    for j in range(i,i*10+1,i):
        print(j,end=" ")
    print()
print()
#Example-2
ll=[[10,20,30],[40,50,60],[70,80]]
for l in ll:
    for x in l:
        print(x, end=" ")
    print()