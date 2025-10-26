# ---------------------------------------
# Day 12 - Full Explanation of While Loop
# ---------------------------------------

# 1️⃣ Basic while loop
i = 1
while i <= 5:
    print(i)
    i += 1
print("-" * 30)

# 2️⃣ Infinite loop (commented for safety)
# while True:
#     print("Hello")

# 3️⃣ Using break
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1
print("-" * 30)

# 4️⃣ Using continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
print("-" * 30)

# 5️⃣ While with else
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed successfully ✅")
print("-" * 30)

# 6️⃣ Break + else
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
else:
    print("This will not print ❌")
print("-" * 30)

# 7️⃣ While loop with user input (password)
password = "admin"
attempt = " "
count = 0
while attempt != password and count < 3:
    attempt = input("Enter password: ")
    count += 1
    if attempt == password:
        print("Login successful ✅")
        break
    else:
        print("Wrong password ❌")
else:
    print("Access denied 🚫")
print("-" * 30)

# 8️⃣ Sum of numbers
i = 1
sum = 0
while i <= 5:
    sum += i
    i += 1
print("Sum:", sum)
print("-" * 30)

# 9️⃣ Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1
print("-" * 30)

# 🔟 Reverse counting
i = 5
while i >= 1:
    print(i)
    i -= 1
print("-" * 30)

# 1️⃣1️⃣ Multiplication table
num = 5
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
print("-" * 30)

# 1️⃣2️⃣ Factorial of a number
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
