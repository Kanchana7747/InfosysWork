# -------------------------
# STRING METHODS
# -------------------------
# Python provides many built-in methods to manipulate strings.

text = "  python programming  "

print("Original:", repr(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Strip spaces:", text.strip())
print("Replace words:", text.replace("python", "java"))
print("Split into list:", text.split())
print("Count of 'm':", text.count("m"))
print("Starts with 'py':", text.startswith("py"))
print("Ends with 'ing':", text.endswith("ing"))

# Print only alphabets from a string

s = input("Enter a string: ")

for ch in s:
    if ch.isalpha():   # checks if character is alphabet
        print(ch, end="")
# Print only uppercase letters from a string

s = input("Enter a string: ")

for ch in s:
    if ch.isupper():   # checks if character is uppercase
        print(ch, end="")
        
# Simple Calculator

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
        print("Error: Division by zero not allowed")
else:
    print("Invalid Operator")

