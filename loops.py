# -------------------------
# Python Loops Examples
# -------------------------

# For loop definition:
# A for loop is used to iterate over a sequence (like range, list, string).
print("For loop 0–4:")
for i in range(5):
    print(i)   # prints numbers 0 to 4

# While loop definition:
# A while loop repeats a block of code until the condition becomes False.
print("\nWhile loop 1–5:")
count = 1
while count <= 5:
    print(count)   # prints numbers 1 to 5
    count += 1

# Break statement definition:
# Used to exit the loop immediately.
print("\nLoop with break:")
for i in range(10):
    if i == 5:     # stops when i=5
        break
    print(i)

# Continue statement definition:
# Skips the current iteration and moves to the next.
print("\nLoop with continue:")
for i in range(5):
    if i == 2:     # skips 2
        continue
    print(i)

# Nested loop definition:
# A loop inside another loop.
print("\nNested loop (multiplication table 1–3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i*j)
    print()

# Right angle triangle pattern
n = int(input("\nEnter number of rows for triangle: "))
for i in range(1, n+1):
    print("*" * i)

# Factorial of a number
n = int(input("\nEnter a number for factorial: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "=", fact)

# Count vowels in a string
s = input("\nEnter a string: ").lower()
vowels = "aeiou"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Number of vowels =", count)

# Pattern: x^2, xx^2, xxx^2 ...
n = int(input("\nEnter number of rows for x^2 pattern: "))
for i in range(1, n+1):
    print("x" * i + "^2")

# Square star pattern using nested loops
n = int(input("\nEnter number of rows/columns for square pattern: "))
for i in range(n):        # rows
    for j in range(n):    # columns
        print("*", end=" ")
    print()
