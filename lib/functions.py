# 1. Method to greet the programmer
def greet_programmer():
    print("Hello, programmer!")

# 2. Method to greet with a name
def greet(name):
    print(f"Hello, {name}!")

# 3. Method to greet with a default value
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# 4. Method to add two numbers
def add(num1, num2):
    return num1 + num2

# 5. Method to halve a number
def halve(number):
    return number / 2

greet_programmer()            # Outputs: Hello, programmer!
greet("Alice")                # Outputs: Hello, Alice!
greet_with_default()           # Outputs: Hello, programmer!
greet_with_default("Bob")      # Outputs: Hello, Bob!
print(add(3, 5))               # Outputs: 8
print(halve(10))               # Outputs: 5.0
