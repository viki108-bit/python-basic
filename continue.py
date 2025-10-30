
# Example 1: Basic continue in for loop
# -----------------------------
print("Example 1: Skip number 3")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("-" * 30)

# -----------------------------
# Example 2: Continue in while loop
# -----------------------------
print("Example 2: Skip number 3 using while loop")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

print("-" * 30)

# -----------------------------
# Example 3: Skip even numbers
# -----------------------------
print("Example 3: Print only odd numbers")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

print("-" * 30)

# -----------------------------
# Example 4: Skip specific item in a list
# -----------------------------
print("Example 4: Skip 'banana' from list")
fruits = ["apple", "banana", "mango", "orange"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

print("-" * 30)

# -----------------------------
# Example 5: Nested loop with continue
# -----------------------------
print("Example 5: Nested loop skipping j = 2")
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(f"i = {i}, j = {j}")

print("-" * 30)

# -----------------------------
# Example 6: Real-life example
# -----------------------------
print("Example 6: Skip absent students")
students = ["Viki", "Amit", "None", "Rahul", "Sneha"]

for student in students:
    if student == "None":
        continue
    print("Present:", student)

# -----------------------------
# ✅ Summary:
# continue → Skips current iteration and moves to next one.
# break → Stops the loop completely.
# -----------------------------
