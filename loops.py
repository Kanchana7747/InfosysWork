# For loop
print("For loop 0–4:")
for i in range(5):
    print(i)

# While loop
print("\nWhile loop 1–5:")
count = 1
while count <= 5:
    print(count)
    count += 1

# Loop with break
print("\nLoop with break:")
for i in range(10):
    if i == 5:
        break
    print(i)

# Loop with continue
print("\nLoop with continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# Right angle triangle pattern
n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    print("*" * i)

# Factorial of a number
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial of", n, "=", fact)

# Count vowels in a string
s = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print("Number of vowels =", count)

# Pattern: x^2, xx^2, xxx^2 ...

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    print("x" * i + "^2")

# Square star pattern

n = int(input("Enter number of rows and columns: "))

for i in range(n):        # rows
    for j in range(n):    # columns
        print("*", end=" ")
    print()
