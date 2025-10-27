
# 1️ break in for loop
for i in range(1, 10):
    print(i)
    if i == 5:
        break
print("-" * 30)

# 2️ break in while loop
i = 1
while i <= 10:
    print(i)
    if i == 6:
        break
    i += 1
print("-" * 30)

# 3️ break in nested loops
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"({i},{j})")
print("-" * 30)

# 4️ break with else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished ✅")
print("-" * 30)

# 5️ search in list example
names = ["Viki", "Amit", "Sana", "Raj"]
search = "Sana"
for name in names:
    if name == search:
        print(f"{search} found ✅")
        break
else:
    print("Name not found ❌")
print("-" * 30)

# 6️ password check
password = "admin"
attempts = 0
while attempts < 3:
    user = input("Enter password: ")
    if user == password:
        print("Login Successful ✅")
        break
    else:
        print("Wrong password ❌")
    attempts += 1
else:
    print("Access Denied 🚫")
print("-" * 30)

# 7️ prime number check
num = 7
for i in range(2, num):
    if num % i == 0:
        print("Not Prime ❌")
        break
else:
    print("Prime ✅")
print("-" * 30)

# 8️ break in infinite loop
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        print("Stopped by user 👋")
        break
    print("You entered:", num)
print("-" * 30)
