# Simple if-else
age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print(" Not eligible to vote")

# if-elif-else
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# Nested if
num = -5
if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Number is positive")
else:
    print("Number is negative")

#task
meghana=input()
if(meghana=="died"):
    print("surya weds priya")
else:
    print("surya weds meghana")

#even or odd
a = int(input("Enter first number: "))

if a % 2 == 0:
    print("The num is Even")
else:
    print("The num is Odd")


# Simple calculator program

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Enter operator: ")

if op == '+':
    print("Result =", a + b)
elif op == '-':
    print("Result =", a - b)
elif op == '*':
    print("Result =", a * b)
elif op == '/':
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid Operator")

