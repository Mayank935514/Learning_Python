#Example-1
def sum(*elements):
    res=0
    for x in elements:
        res=res+x
    return res
print(sum(10,20))
print(sum(10))
print(sum())

#Example-2
def sum(init_sum, *element):
    res = init_sum
    for x in element:
        res = res+x
    return res
print(sum(0,50,120))
print(sum(5,50,70))
print()

#Example-3
def printElements(*elements):
    print(elements)
printElements(101,"ddd",300)
printElements(102,"def",400)