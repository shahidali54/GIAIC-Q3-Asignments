print("Hello, World!")

# Basic Python Practice, Variables & Data Types
name = "Shahid Ali"
age = 25
is_student = True

print("My name is", name, "and I am", age, "years old.", "Is student.", is_student)
print("Is", name, "a student?", is_student)

# get users Input & print Output
name = input("Enter your name:")
age = int(input("Enter your age"))

print(f"Hello {name} you are {age} years old")

# Conditional Statements (if-else) Even/Odd Number Check
num = int(input("Enter a number"))

if num % 2 == 0:
  print(f"{num} is even.")

else:
    print(f"{num} is odd")

# Loops (for & while)
for i in range(1, 11):
  print(i)

# While Loop - Countdown Timer
count = 5
while count > 0:
  print(count)
  count -= 1
  print("Happy Birthday!")

# Functions Sum of Two Numbers
def add_numbers(a, b):
  return a + b
  print(add_numbers(5,10))

# Lists & Loops
fruits = ["Apple", "Banana", "Mango", "Grapes"]
for fruit in fruits:
  print(fruit)

# Find Maximum in a List
numbers = [12, 55, 34, 99, 35]
print(max(numbers))
