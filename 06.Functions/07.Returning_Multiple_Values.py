#Example-1
def add_mult(x,y):
    sum=x+y
    mul=x*y
    return sum,mul
s,m=add_mult(10,20)
print(s)
print(m)
print()

#Example-2 
def add_mult_subt(x,y):
    sum=x+y
    mul=x*y
    sub=x-y
    return [sum,mul,sub]
s,m,sb=add_mult_subt(10,20)
print(s)
print(m)
print(sb)
