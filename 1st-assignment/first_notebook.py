# Special Keywords explain in Readme.md file

# 1st program
print("Hello, World!")

# Variables
name = "Shahid"  # string
age = 25  # integer
is_student = True  # boolean
value = 44.45444  # float

print(name, age, is_student, value)

# Data types in python
print(type(name))  # string
print(type(age))  # integer
print(type(is_student))  # boolean
print(type(value))  # float

# Basic Python Practice, Variables & Data Types
name = "Shahid Ali"
age = 25
is_student = True

print("My name is", name, "and I am", age, "years old.", "Is student:", is_student)
print("Is", name, "a student?", is_student)

# Get user's input & print output
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old")

# Conditional Statements (if-else) Even/Odd Number Check
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Loops (for & while)
for i in range(1, 11):
    print(i)

# While Loop - Countdown Timer
count = 5
while count > 0:
    print(count)
    count -= 1
print("Happy Birthday!")

# Functions - Sum of Two Numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 10))

# Lists & Loops
fruits = ["Apple", "Banana", "Mango", "Grapes"]
for fruit in fruits:
    print(fruit)

# Find Maximum in a List
numbers = [12, 55, 34, 99, 35]
print(max(numbers))

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Mixed data types tuple
mixed_tuple = (10, "Hello", 3.14, True)
print(mixed_tuple)

# Nested tuple
nested_tuple = ((1, 2, 3), ("a", "b", "c"))
print(nested_tuple)

# Dictionary
student = {
    "name": "Shahid",
    "age": 25,
    "city": "Karachi"
}
print(student)
print(student["name"])
print(student.get("age"))

info = {
    "name": "Shahid",
    "age": 25,
    "is_student": True,
    "grades": [90, 85, 88],
    "address": {"city": "Karachi", "country": "Pakistan"}
}
print(info)

student["grade"] = "A"
print(student)

# Nested Dictionary
employees = {
    "emp1": {"name": "Shahid", "age": 25, "position": "Manager"},
    "emp2": {"name": "Subhan", "age": 25, "position": "Developer"}
}
print(employees["emp1"]["name"])

# Set
my_set = {1, 2, 3, 4, 5}
print(my_set)  

# Remove duplicate values automatically
my_set1 = {1, 2, 2, 3, 4, 4, 5}
print(my_set1)