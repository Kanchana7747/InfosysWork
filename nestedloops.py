# Multiplication table using nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Printing a pattern
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Number triangle pattern

n = int(input("Enter number of rows: "))

for i in range(1, n+1):       # rows
    for j in range(1, i+1):   # numbers in each row
        print(j, end="")
    print()
