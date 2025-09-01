# ===============================
# 1. Simple if-else
# ===============================
# Definition: if-else checks a condition and executes one block if true, 
# another block if false.

age = 20
if age >= 18:
    print("Eligible to vote")   # Output: Eligible to vote
else:
    print("Not eligible to vote")


# ===============================
# 2. if-elif-else
# ===============================
# Definition: Used when we have multiple conditions to check.

marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")           # Output: Grade: B
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


# ===============================
# 3. Nested if
# ===============================
# Definition: When an if statement is written inside another if block.

num = -5
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")  # Output: Number is negative


# ===============================
# 4. Task Program
# ===============================
# Example of simple string comparison using if-else

meghana = input("Enter Meghana's status: ")
if meghana == "died":
    print("surya weds priya")
else:
    print("surya weds meghana")


# ===============================
# 5. Even or Odd Program
# ===============================
# Definition: Checks whether a number is divisible by 2 or not.

a = int(input("Enter a number: "))
if a % 2 == 0:
    print("The num is Even")      # Example: input=4 → Output: Even
else:
    print("The num is Odd")       # Example: input=5 → Output: Odd


# ===============================
# 6. Simple Calculator Program
# ===============================
# Definition: Performs arithmetic operations using if-elif-else.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter operator: ")

if op == '+':
    print("Result =", a + b)      # Example: 5 + 3 = 8
elif op == '-':
    print("Result =", a - b)      # Example: 7 - 2 = 5
elif op == '*':
    print("Result =", a * b)      # Example: 4 * 2 = 8
elif op == '/':
    if b != 0:
        print("Result =", a / b)  # Example: 10 / 2 = 5.0
    else:
        print("Division by zero not allowed")
else:
    print("Invalid Operator")
