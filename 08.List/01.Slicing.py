#Example-1
l=[10,20,30,40,50]
print(l[0:5:2])
print()

#Example-2
l=[10,20,30,40,50]
print(l[:4])
print()

#Example-3
l=[10,20,30,40,50]
print(l[1:4])
print(l[4:1:-1])
print()

#Example-4
l=[10,20,30,40,50]
print(l[-1:-6:-1])
print(l[::-1])
print()

#Example-5
l=[10,20,30,40,50]
print(l[0:5])
print(l[:])
print()

#Example-6
l=[10,20,30]
l2=l[:]
t1=(10,20,30)
t2=t1[:]
s1="geeks"
s2=s1[:]
print(l is l2)
print(t1 is t2)
print(s1 is s2)