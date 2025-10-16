
# Example 1: Simple if
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 3: if-elif-else
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")

# Example 4: Nested if
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")

# Example 5: Shorthand if
n = 7
print("Even") if n % 2 == 0 else print("Odd")
