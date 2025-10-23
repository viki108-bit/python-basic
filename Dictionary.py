# Day 8 - Detailed Explanation of Dictionary in Python

# Creating a Dictionary
student = {"name": "Viki", "age": 21, "course": "Python"}
print("Original Dictionary:", student)

# Accessing Values
print("Name:", student["name"])
print("Age using get():", student.get("age"))

# Adding and Updating
student["city"] = "Pune"
student["age"] = 22
print("After Add & Update:", student)

# Removing Items
student.pop("city")
print("After pop:", student)

# Looping
for key, value in student.items():
    print(key, ":", value)

# Nested Dictionary
students = {
    "student1": {"name": "Viki", "age": 21},
    "student2": {"name": "Amit", "age": 22}
}
print("Nested:", students["student1"]["name"])

# Dictionary Comprehension
squares = {x: x*x for x in range(1, 6)}
print("Squares:", squares)

# Copying Dictionary
copy_student = student.copy()
print("Copy:", copy_student)
