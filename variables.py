# -------------------------
# VARIABLES IN PYTHON
# -------------------------
# A variable is a reserved memory location to store values.
# In Python, you don’t need to declare type explicitly, it is inferred automatically.
# Syntax: variable_name = value

# Example variables
x = 10          # Integer variable
pi = 3.1416     # Float variable
name = "namess"  # String variable
is_active = True   # Boolean variable

print("Integer:", x)
print("Float:", pi)
print("String:", name)
print("Boolean:", is_active)

# Multiple assignments
a, b, c = 1, 2, 3
print("Multiple assignment → a:", a, "b:", b, "c:", c)

# Reassigning with a different type (Dynamic Typing)
x = "Now I am a string"
print("Dynamic typing →", x, "| Type:", type(x))

#Add 2 integers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum_result = a + b
print("Sum =", sum_result)

# Program to find perimeter of a rectangle

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

perimeter = 2 * (length + width)
print("Perimeter of Rectangle =", perimeter)



