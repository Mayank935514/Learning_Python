#Example-1 --> Square Pattern
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print()

#Example-2 --> Triangular Pattern
n=int(input("Enter n: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
print()

#Example-3 --> Inverted Triangle
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
print()

#Example-4 --> Pyramid Pattern
n=int(input("Enter n: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()