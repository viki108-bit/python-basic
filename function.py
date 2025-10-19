# 1. Simple Function
def greet():
    print("Hello! Welcome to Python Functions.")

greet()

# 2. Function with Parameter
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Viki")

# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# 4. Default Parameter
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()
greet_default("Viki")

# 5. Keyword Arguments
def intro(name, age):
    print(f"My name is {name} and I am {age} years old.")

intro(age=21, name="Viki")

# 6. *args Example
def show_numbers(*nums):
    for n in nums:
        print(n)

show_numbers(1, 2, 3, 4, 5)

# 7. **kwargs Example
def user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

user_info(name="Viki", age=21, city="Pune")

# 8. Recursive Function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))
