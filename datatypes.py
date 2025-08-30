# -------------------------
# DATA TYPES IN PYTHON
# -------------------------
# Python has built-in data types. Some major categories:
# 1. Numeric: int, float, complex
# 2. Sequence: str, list, tuple
# 3. Mapping: dict
# 4. Set Types: set, frozenset
# 5. Boolean: bool
# 6. None Type: None

# Numeric
x = 10         # int
y = 3.14       # float
z = 2 + 3j     # complex

print("x:", x, "| Type:", type(x))
print("y:", y, "| Type:", type(y))
print("z:", z, "| Type:", type(z))

# String
s = "Hello"
print("s:", s, "| Type:", type(s))

# List (mutable, ordered)
lst = [1, 2, 3, "apple"]
print("lst:", lst, "| Type:", type(lst))

# Tuple (immutable, ordered)
tup = (1, 2, 3)
print("tup:", tup, "| Type:", type(tup))

# Dictionary (key-value pairs)
d = {"name": "Alice", "age": 25}
print("d:", d, "| Type:", type(d))

# Set (unordered, unique values)
st = {1, 2, 3, 2}
print("st:", st, "| Type:", type(st))

# Boolean
flag = False
print("flag:", flag, "| Type:", type(flag))

# NoneType
n = None
print("n:", n, "| Type:", type(n))
