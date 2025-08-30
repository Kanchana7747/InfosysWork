#arithemetic operator
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponent:", a ** b)       # 1000

#relational operator
x = 5
y = 10

print("Equal:", x == y)       # False
print("Not Equal:", x != y)   # True
print("Greater:", x > y)      # False
print("Less:", x < y)         # True
print("Greater or Equal:", x >= y) # False
print("Less or Equal:", x <= y)    # True

#logical operator
p = True
q = False

print("AND:", p and q)   # False
print("OR:", p or q)     # True
print("NOT:", not p)     # False

#assignment operator
n = 10
print("Initial:", n)

n += 5   # n = n + 5
print("After += :", n)

n -= 3   # n = n - 3
print("After -= :", n)

n *= 2   # n = n * 2
print("After *= :", n)

n /= 4   # n = n / 4
print("After /= :", n)

n %= 3   # n = n % 3
print("After %= :", n)

n **= 2  # n = n ** 2
print("After **= :", n)

n //= 2  # n = n // 2
print("After //= :", n)

#Bitwise operator
a = 6   # 110 in binary
b = 3   # 011 in binary

print("Bitwise AND:", a & b)  # 2 (010)
print("Bitwise OR:", a | b)   # 7 (111)
print("Bitwise XOR:", a ^ b)  # 5 (101)
print("Bitwise NOT:", ~a)     # -7
print("Left Shift:", a << 1)  # 12 (1100)
print("Right Shift:", a >> 1) # 3 (011)

#identity operator
x = [1,2,3]
y = x
z = [1,2,3]

print(x is y)       # True (same object)
print(x is z)       # False (different objects, same content)
print(x is not z)   # True

#Membership operator
nums = [1, 2, 3, 4, 5]

print(3 in nums)        # True
print(7 in nums)        # False
print(7 not in nums)    # True
