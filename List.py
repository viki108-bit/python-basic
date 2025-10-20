# 1. List Example
fruits = ["apple", "banana", "cherry", "apple"]
print("Original List:", fruits)

# 2. Accessing
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Changing
fruits[1] = "mango"
print("After Change:", fruits)

# 4. Adding
fruits.append("grape")
fruits.extend(["kiwi", "orange"])
print("After Adding:", fruits)

# 5. Removing
fruits.remove("apple")
fruits.pop()
print("After Removing:", fruits)

# 6. Looping
print("Fruits List:")
for fruit in fruits:
    print(fruit)

# 7. Slicing
numbers = [10, 20, 30, 40, 50, 60]
print("Sliced List:", numbers[1:4])
