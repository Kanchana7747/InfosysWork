# -------------------------------
# Nested Loops in Python
# -------------------------------
# Definition:
# A nested loop means having one loop inside another loop.
# The inner loop executes completely for each iteration of the outer loop.
# Commonly used in patterns, tables, and matrix problems.

# Example 1: Multiplication Table using Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ---
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ---
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ---

# Example 2: Star Pattern
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Output:
# *
# * *
# * * *
# * * * *

# Example 3: Number Triangle Pattern
n = 4
for i in range(1, n+1):       # rows
    for j in range(1, i+1):   # numbers in each row
        print(j, end="")
    print()

# Output:
# 1
# 12
# 123
# 1234
