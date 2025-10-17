
# 1. Simple for loop
for i in range(5):
    print("Hello", i)

print("\n--- List Loop ---")
# 2. Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

print("\n--- String Loop ---")
# 3. Loop through a string
for letter in "VIKI":
    print(letter)

print("\n--- Range with step ---")
# 4. Range with start, stop, step
for i in range(1, 11, 2):
    print(i)

print("\n--- While Loop ---")
# 5. While loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\n--- Break and Continue ---")
# 6. Break and Continue example
for i in range(10):
    if i == 5:
        break
    print("Break Example:", i)

for i in range(10):
    if i == 5:
        continue
    print("Continue Example:", i)

print("\n--- Nested Loops ---")
# 7. Nested Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})")
