l1=[1,3,4,2,5]
d1={x:x**3 for x in l1}
print(d1)

d2={x:f"ID{x}" for x in range(5)}
print(d2)

#Zip Functions-->It creates mapping of items in these iterables.
# d3=dict(zip(l2,l3))
l2=[101,103,102]
l3=["gfg","ide","Courses"]
d3={l2[i]:l3[i] for i in range(len(l2))}
print(d3)
print()

#Inserting a Dictionary--> Key becomes value and value becomes key.
d4={101:"gfg",103:"practice",102:"ide"}
d5={v:k for(k,v) in d4.items()}
print(d5)