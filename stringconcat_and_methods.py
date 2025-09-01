# -------------------------
# STRING CONCATENATION & REPETITION
# -------------------------

str1 = "Hello"
str2 = "World"

# Using + (concatenation)
print("Concatenation:", str1 + " " + str2)   # Hello World

# Using * (repetition)
print("Repetition:", str1 * 3)   # HelloHelloHello

# -------------------------
# STRING SLICING
# -------------------------

text = "PythonProgramming"
print("\nOriginal:", text)

# Basic slicing
print("First 6 chars:", text[:6])        # Python
print("From 7th char:", text[6:])        # Programming
print("Middle part:", text[0:6] + " " + text[6:])  # Python Programming

# Using step in slicing
print("Every 2nd char:", text[::2])      # Pto rgamn
print("Reverse string:", text[::-1])     # gnimmargorPnohtyP

# Negative indexing
print("Last char:", text[-1])            # g
print("Last 5 chars:", text[-5:])        # mming
print("All except last 3:", text[:-3])   # PythonProgrammi

# -------------------------
# REAL-LIFE USE CASES
# -------------------------

# Extract first and last name using slicing
fullname = "Ada Lovelace"
first = fullname[:3]    # 'Ada'
last = fullname[4:]     # 'Lovelace'
print("\nFirst Name:", first)
print("Last Name:", last)

# Reversing can be used to check palindrome
word = "madam"
if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")
