# -------------------------
# STRING METHODS IN PYTHON
# -------------------------
# Strings in Python come with many built-in methods to manipulate and analyze text.

text = "  python programming  "

print("Original:", repr(text))             # repr() shows spaces clearly
print("Uppercase:", text.upper())          # Convert to uppercase
print("Lowercase:", text.lower())          # Convert to lowercase
print("Title Case:", text.title())         # Capitalize each word
print("Strip spaces:", text.strip())       # Remove leading/trailing spaces
print("Replace words:", text.replace("python", "java"))  # Replace substring
print("Split into list:", text.split())    # Split by spaces → list of words
print("Count of 'm':", text.count("m"))    # Count occurrences
print("Starts with 'py':", text.startswith("py"))  # Check prefix
print("Ends with 'ing':", text.endswith("ing"))    # Check suffix
print("Find position of 'pro':", text.find("pro")) # Returns index of substring
print("Is alphabetic?", text.isalpha())    # False → has spaces
print("Is alphanumeric?", text.isalnum())  # False → spaces not allowed
print("Is digit?", "123".isdigit())        # True → only digits

# -------------------------
# PRINT ONLY ALPHABETS
# -------------------------
s = input("\nEnter a string (to print only alphabets): ")

print("Alphabets only:", end=" ")
for ch in s:
    if ch.isalpha():   # checks if character is alphabet
        print(ch, end="")
print()  # new line

# -------------------------
# PRINT ONLY UPPERCASE LETTERS
# -------------------------
s = input("\nEnter a string (to print only uppercase letters): ")

print("Uppercase letters only:", end=" ")
for ch in s:
    if ch.isupper():   # checks if character is uppercase
        print(ch, end="")
print()  # new line

# -------------------------
# SIMPLE CALCULATOR
# -------------------------
a = float(input("\nEnter first number: "))
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
