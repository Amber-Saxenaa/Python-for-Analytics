# ===========================================
#PYTHON SYNTAX 
# ===========================================

print("\n" + "="*50)
print("PART 1: PYTHON SYNTAX BASICS")
print("="*50)

# ---------- INDENTATION ----------
print("\n--- INDENTATION ---")
# Correct indentation
if 5 > 2:
    print("✅ Five is greater than two!")
    print("✅ This is inside the if block")

# ---------- VARIABLES ----------
print("\n--- VARIABLES ---")
# Valid variable names
my_name = "John"
age25 = 25
_private = "secret"

print(f"Name: {my_name}")
print(f"Age: {age25}")
print(f"Private: {_private}")

# ---------- ARITHMETIC OPERATORS ----------
print("\n--- ARITHMETIC OPERATORS ---")
print(f"10 + 3  = {10 + 3}")   # 13 (addition)
print(f"10 - 3  = {10 - 3}")   # 7  (subtraction)
print(f"10 * 3  = {10 * 3}")   # 30 (multiplication)
print(f"10 / 3  = {10 / 3}")   # 3.333... (division)
print(f"10 // 3 = {10 // 3}")  # 3  (floor division)
print(f"10 % 3  = {10 % 3}")   # 1  (modulus)
print(f"10 ** 3 = {10 ** 3}")  # 1000 (exponent)

# ---------- COMPARISON OPERATORS ----------
print("\n--- COMPARISON OPERATORS ---")
print(f"5 > 3  = {5 > 3}")    # True
print(f"5 < 3  = {5 < 3}")    # False
print(f"5 == 5 = {5 == 5}")   # True
print(f"5 != 3 = {5 != 3}")   # True
print(f"5 >= 5 = {5 >= 5}")   # True
print(f"5 <= 3 = {5 <= 3}")   # False

# ---------- STRING OPERATIONS ----------
print("\n--- STRING OPERATIONS ---")
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Concatenation: {full_name}")

print(f"String multiplication: {'Ha' * 3}")  # HaHaHa

# String methods
text = "  Hello World  "
print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Strip: '{text.strip()}'")
print(f"Replace: '{text.replace('World', 'Python')}'")
print(f"Length: {len(text)}")

# f-strings (BEST WAY!)
name = "Alice"
age = 25
print(f"f-string: My name is {name} and I'm {age} years old")


# ===========================================
# PART 2: DATA STRUCTURES
# ===========================================

print("\n" + "="*50)
print("PART 2: DATA STRUCTURES")
print("="*50)

# ---------- LISTS ----------
print("\n--- LISTS (Mutable, Ordered) ---")
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

print(f"Original list: {fruits}")
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Slicing [1:3]: {fruits[1:3]}")

# List operations
fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "grape")
print(f"After insert: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

popped = fruits.pop()
print(f"After pop (removed '{popped}'): {fruits}")

print(f"Length: {len(fruits)}")

# Looping through lists
print("Looping through fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

