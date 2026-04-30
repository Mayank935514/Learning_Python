# Example-1
s1={10,20,30}
print(s1)
s2=set([20,30,40])
print(s2)
s3={} #It compares empty dictionary
print(type(s3))
s4=set() #for empty set, we need to create by constructor style
print(type(s4))
print(s4)
print()

# Example-2
s={10,20}
s.add(30)
print(s)
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update({60,70},[80,90])
print(s)
print()

# Example-3--> Removal Operations
s={10,30,20,40}
s.discard(30) # discard() function doesn't do anything if you provide an item that doesn't present in the set
print(s)
s.remove(20) # It raises an error if the element is not present in the set
print(s)
s.clear()
print(s)
s.add(50)
del s
print()

# Example-4
s={10,20,30,40}
print(len(s))
print(20 in s)
print(50 in s)
print()

# Example-5--> Operations on two sets
s1={2,4,6,8}
s2={3,6,9}
print(s|s2)  # s1.union(s2)
print(s1&s2) # s1.intersection(s2)
print(s1-s2) # s1.difference(s2)
print(s1^s2) # s1.symmetric_difference(s2)
s1.issubset(s2)
s1.issuperset(s2)
print()

# Example-6
s1={2,4,6,8}
s2={4,8}
print(s1.isdisjoint(s2))   
print(s1<=s2)    # subset 
print(s1<s2)     # properSubset
print(s1>=s2)    # superset
print(s1>s2)     # properSuperset