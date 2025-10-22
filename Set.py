

# Creating a Set
fruits = {"apple", "banana", "cherry", "apple"}
print("Original Set:", fruits)

# Adding items
fruits.add("orange")
fruits.update(["grape", "kiwi"])
print("After Adding:", fruits)

# Removing items
fruits.discard("banana")
fruits.remove("apple")
print("After Removing:", fruits)

# Looping
print("Fruits in Set:")
for fruit in fruits:
    print(fruit)

# Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))
print("Symmetric Difference:", A.symmetric_difference(B))

# Membership
print("Is 3 in A?", 3 in A)
print("Is 10 not in A?", 10 not in A)

# Copy
C = A.copy()
print("Copy of A:", C)

# Frozen Set
F = frozenset([10, 20, 30])
print("Frozen Set:", F)
