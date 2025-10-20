
# 1. Creating a Tuple
colors = ("red", "green", "blue")
print("Tuple:", colors)

# 2. Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# 3. Looping
for c in colors:
    print("Color:", c)

# 4. Length
print("Total colors:", len(colors))

# 5. Single-element tuple
single = ("apple",)
print(type(single))

# 6. Slicing
numbers = (10, 20, 30, 40, 50)
print("Slice:", numbers[1:4])

# 7. Joining tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
print("Joined:", tuple1 + tuple2)

# 8. Repeating tuple
print("Repeated:", tuple1 * 2)

# 9. Tuple to list conversion
temp = list(colors)
temp.append("yellow")
colors = tuple(temp)
print("Modified Tuple:", colors)

# 10. Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))
