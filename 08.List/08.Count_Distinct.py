#Code-1
def distinct(l):
    res = 1
    for i in range(1, len(l)):
        if l[i] not in l[:i]:
            res += 1
    return res

l = [10, 20, 10, 30, 20, 30]
print(distinct(l))

#Code-2
def distinct(l):
    s=set(l)
    return len(s)
l = [10, 20, 10, 30, 20, 30]
print(distinct(l))