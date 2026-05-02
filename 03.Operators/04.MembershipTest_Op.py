# Example-1
s= "geeksforgeeks"
print("g" in s)
print("for" in s)
print("gk" in s)
print()

# Example-2
d={10: "abc", 20: "efg"}
print(10 in d)
print(15 in d)
print("abc" in d)  # only checks keys not value so it will give false
print()

# Example-3
l=[10,20,30,15]
print(30 in l)
print([20,30] in l) # gives false because [20,30] is a sublist but not a member
print()

#Example-4
l=[10,20,30,15]
print(30 not in l)
print(40 not in l)
print([20,30] not in l)