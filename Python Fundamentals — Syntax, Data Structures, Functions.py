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

# ---------- TUPLES ----------
print("\n--- TUPLES (Immutable, Ordered) ---")
colors = ("red", "green", "blue")
single_item = ("hello",)  # Note the comma!

print(f"Tuple: {colors}")
print(f"First element: {colors[0]}")
print(f"Last element: {colors[-1]}")

# Tuples are faster and use less memory than lists
# Use when data shouldn't change (e.g., days of week)

# ---------- DICTIONARIES ----------
print("\n--- DICTIONARIES (Key-Value Pairs) ---")
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(f"Dictionary: {person}")
print(f"Access by key: {person['name']}")
print(f"Using .get(): {person.get('age')}")
print(f"Using .get() with default: {person.get('country', 'USA')}")

# Adding/updating
person["email"] = "john@email.com"
person["age"] = 31
print(f"After updates: {person}")

# Removing items
del person["city"]
print(f"After deleting 'city': {person}")

removed = person.pop("email")
print(f"After pop (removed '{removed}'): {person}")

# Looping through dictionaries
print("Looping through dictionary:")
for key, value in person.items():
    print(f"  {key}: {value}")

print(f"All keys: {person.keys()}")
print(f"All values: {person.values()}")

# ---------- SETS ----------
print("\n--- SETS (Unordered, No Duplicates) ---")
fruits_set = {"apple", "banana", "cherry", "apple"}  # Duplicate removed
print(f"Set (no duplicates): {fruits_set}")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union (|): {set1 | set2}")
print(f"Intersection (&): {set1 & set2}")
print(f"Difference (-): {set1 - set2}")

# Adding/removing
set1.add(5)
print(f"After add 5: {set1}")
set1.remove(2)
print(f"After remove 2: {set1}")


# ===========================================
# PART 3: FUNCTIONS
# ===========================================

print("\n" + "="*50)
print("PART 3: FUNCTIONS")
print("="*50)

# ---------- BASIC FUNCTIONS ----------
print("\n--- BASIC FUNCTIONS ---")

def greet():
    """Simple function that prints a greeting"""
    print("Hello, World!")

greet()

def greet_person(name):
    """Function with a parameter"""
    print(f"Hello, {name}!")

greet_person("Alice")

def add(a, b):
    """Function that returns a value"""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# ---------- DEFAULT PARAMETERS ----------
print("\n--- DEFAULT PARAMETERS ---")

def greet_with_default(name, greeting="Hello"):
    """Function with default parameter"""
    print(f"{greeting}, {name}!")

greet_with_default("John")        # Uses default greeting
greet_with_default("John", "Hi")  # Overrides default

def calculate(a, b, operation="add"):
    """Calculator function with multiple operations"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"

print(f"Calculate 10 + 5: {calculate(10, 5)}")
print(f"Calculate 10 - 5: {calculate(10, 5, 'subtract')}")
print(f"Calculate 10 * 5: {calculate(10, 5, 'multiply')}")
print(f"Calculate 10 / 5: {calculate(10, 5, 'divide')}")

# ---------- *args AND **kwargs ----------
print("\n--- *args AND **kwargs ---")


# *args - variable number of positional arguments
def sum_all(*args):
    """Sum any number of arguments"""
    return sum(args)

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40): {sum_all(10, 20, 30, 40)}")

# **kwargs - variable number of keyword arguments
def print_info(**kwargs):
    """Print any number of key-value pairs"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("print_info(name='John', age=30, city='NYC'):")
print_info(name="John", age=30, city="NYC")

# ---------- SCOPE (Local vs Global) ----------
print("\n--- SCOPE (Local vs Global) ---")

# Global variable
x = 10
print(f"Global x = {x}")

def my_function():
    # Local variable
    y = 5
    print(f"Inside function - Global x: {x}")
    print(f"Inside function - Local y: {y}")

my_function()
# print(y)  # Error! y is not defined outside the function

# Modifying global variables
count = 0
print(f"Initial count: {count}")

def increment():
    global count  # Need to declare global to modify
    count += 1

increment()
print(f"After increment: {count}")



