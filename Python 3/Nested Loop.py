# * Pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()


# Number Pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Multiplication table (1 to 5)
for i in range(1, 6):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()


# ABC Pattern
for i in range(3):
    for j in ['A', 'B', 'C']:
        print(j, end=" ")
    print()

# Pattern
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
