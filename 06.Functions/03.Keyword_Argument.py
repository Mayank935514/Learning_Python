def printDetails(id, name, price):
    print(f"ID is {id}")
    print(f"Name is {name}")
    print(f"Price is {price}")
printDetails(101,"abc",100)  #Positional Argument
print()
printDetails(id=102,name="xyz",price=200)  #keyword argument

# In positional argument, we have to maintain the order while in keyword argument, we don't need to maintain the order.