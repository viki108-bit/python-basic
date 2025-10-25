
# 1️⃣ Basic for loop with range()
print("Basic for loop:")
for i in range(5):
    print(i)
print("-" * 30)

# 2️⃣ for loop with start, stop, step
print("For loop with start, stop, step:")
for i in range(1, 10, 2):
    print(i)
print("-" * 30)

# 3️⃣ Loop through list
print("Looping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("-" * 30)

# 4️⃣ Loop through string
print("Looping through a string:")
for ch in "Viki":
    print(ch)
print("-" * 30)

# 5️⃣ Using else with for loop
print("For loop with else:")
for i in range(5):
    print(i)
else:
    print("Loop finished successfully ✅")
print("-" * 30)

# 6️⃣ Using break
print("Using break in for loop:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("-" * 30)

# 7️⃣ Using continue
print("Using continue in for loop:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("-" * 30)

# 8️⃣ Nested for loop
print("Nested for loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()
print("-" * 30)

# 9️⃣ Reverse loop using range
print("Reverse loop:")
for i in range(10, 0, -1):
    print(i)
print("-" * 30)

# 🔟 List comprehension with for loop
print("List comprehension example:")
squares = [x ** 2 for x in range(1, 6)]
print(squares)
print("-" * 30)

# 1️⃣1️⃣ For loop with if condition
print("For loop with condition:")
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
print("-" * 30)

# 1️⃣2️⃣ For loop with dictionary
print("Loop through dictionary:")
student = {"name": "Viki", "age": 21, "city": "Pune"}
for key in student:
    print(key, ":", student[key])
print("-" * 30)

# 1️⃣3️⃣ Using pass in for loop
print("Using pass statement:")
for i in range(5):
    pass  # placeholder
print("Loop executed but nothing happened with 'pass'")
print("-" * 30)

# 1️⃣4️⃣ Real-life example: Check prime number
print("Check if number is prime:")
num = 11
for i in range(2, num):
    if num % i == 0:
        print("Not Prime ❌")
        break
else:
    print("Prime ✅")
print("-" * 30)

# 1️⃣5️⃣ Nested condition + loop example
print("Multiplication Table (1 to 5):")
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 15)
