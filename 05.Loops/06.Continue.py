#Example-1 --> Print all those numbers in a list that are not a multiple of 5
#Code-1
l=[10,16,17,18,19,15]
for x in l:
    if x%5 == 0:
        continue
    print(x)
print()

#Code-2
l=[10,16,17,18,19,15]
for x in l:
    if x%5 != 0:
        print(x)