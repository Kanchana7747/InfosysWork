#string concat
str1 = "Hello"
str2 = "World"

# Using +
print("Concatenation:", str1 + " " + str2)   # Hello World

# Using * (repeat)
print("Repetition:", str1 * 3)   # HelloHelloHello

#string slicing
text = "PythonProgramming"

print("Original:", text)

# Basic slicing
print("First 6 chars:", text[:6])       # Python
print("From 7th char:", text[6:])       # Programming
print("Middle part:", text[0:6] + " " + text[6:])  # Python Programming

# Using step
print("Every 2nd char:", text[::2])     # Pto rgamn
print("Reverse:", text[::-1])           # gnimmargorPnohtyP

