# Strings in Python
# -----------------
# Strings are sequences of characters enclosed in single, double, or triple quotes.
# They support various operations: indexing, slicing, concatenation, repetition, and built-in methods.

text = "Hello Python"

# Indexing (accessing characters by position)
print("First char:", text[0])      # 'H'
print("Last char:", text[-1])      # 'n'

# Slicing (extracting substrings)
print("First 5 chars:", text[:5])   # 'Hello'
print("From index 6:", text[6:])    # 'Python'
print("Every 2nd char:", text[::2]) # 'HloPto'

# Concatenation (joining strings)
greet = "Hello" + " " + "World"
print("Concatenated:", greet)       # 'Hello World'

# Repetition (repeating strings)
print("Repetition:", "Hi! " * 3)    # 'Hi! Hi! Hi! '

# Length of string
print("Length:", len(text))         # 12

# Common string methods
print("Uppercase:", text.upper())    # 'HELLO PYTHON'
print("Lowercase:", text.lower())    # 'hello python'
print("Title Case:", text.title())   # 'Hello Python'
print("Replace:", text.replace("Python", "World"))  # 'Hello World'
print("Split:", text.split())        # ['Hello', 'Python']
print("Find 'Python':", text.find("Python"))  # index of substring

# Checking string properties
print("Is alphabetic?", text.isalpha())      # False (because of space)
print("Is alphanumeric?", text.isalnum())    # False (space not allowed)
print("Starts with 'Hello'?", text.startswith("Hello")) # True
print("Ends with 'on'?", text.endswith("on"))           # True

# String formatting
name = "Alice"
age = 20
print("Formatted string: {} is {} years old.".format(name, age))
print(f"Formatted string (f-string): {name} is {age} years old.")
