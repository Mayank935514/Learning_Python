#Example-1
s1="geeksforgeeks"
s2="geeks"
print(s2 in s1)
print(s2 not in s1)
print()

#Example-2
s1="geeks"
s2="forgeeks"
s3=s1+s2
s4="Welcome to "+s1+s2
print(s3)
print(s4)
print()

#Example-3
s1="geeksforgeeks"
s2="geeks"
print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2,0,len(s1)))
print()

#Example-4
s1="geeks"
print(len(s1))
s2=s1.upper()
print(s2)
s3=s1.lower()
print(s3)
print(s1.islower())
print(s2.isupper())
print()

#Example-5
s="GeeksforGeeks Python Course"
print(s.startswith("Geeks"))
print(s.endswith("Course"))
print(s.startswith("Geeks",1))
print(s.startswith("Geeks",8,len(s)))
print()

#Example-6
s1="geeks for geeks"
print(s1.split())
s2="geeks,for,geeks"
print(s2.split(","))
l=["geeksforgeeks","python","course"]
print(" ".join(l))
print(",".join(l))
print()

#Example-7
s="--geeksforgeeks---"
print(s.strip("-"))
print(s.lstrip("-"))
print(s.rstrip("-"))
print()

#Example-8
s1="geeksforgeeks"
s2="geeks"
print(s1.find(s2))
print(s1.find("gfg"))
print(s1.find(s2,1,len(s1)))
print()

#Example-9
s1="geeksforgeeks"
s2="ide"
print(s1<s2)
print(s1<=s2)
print(s1>s2)
print(s1>=s2)
print(s1==s2)
print(s1!=s2)

