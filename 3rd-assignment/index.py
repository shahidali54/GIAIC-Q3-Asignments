import random 

# lesson_05_control_flow_loops

# If-Else Statement (Checks temperature and prints the weather condition)
temprature = int(input("Enter Temperature: "))  # Taking temperature input from user

if temprature >= 50:
    print("It's a very hot day!")

elif temprature >= 40:
    print("It's a hot day!")

elif temprature >= 30:
    print("It's a moderate day!")

elif temprature >= 20:
    print("It's a cool day!")

else:
    print("It's a cold day!")



# For Loop (Looping through a list of fruits)
fruits = ["Apple", "Banana", "Cherry", "Mango"]
for fruit in fruits:
    print("I like", fruit)


# For Loop with Range (Loops from 0 to 4)
for i in range(5):  
    print("Count:", i)


# For Loop that prints "Hello, World!" 5 times
for i in range(5):
    print("Hello, World!")


# For Loop with Break Statement
for i in range(1, 11):  # Loop to print numbers from 1 to 10
    if i == 5:
        print("Loop stopped at", i)  # Message when loop stops at 5
        break  # Stops the loop when i equals 5
    print(i)


# While Loop with Break Statement
count = 1  # Initial count value
while count <= 10:  # Runs loop while count is 10 or less
    print("Count:", count)
    if count == 8:
        break  # Stops the loop when count reaches 8
    count += 1  # Increments count by 1 in each loop iteration


# lesson_06_lists_tuples_dictionary

# List Operations
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers.append(11)  # Adding an element to the end of the list
numbers.remove(2)   # Removing an element
numbers.reverse()   # Reversing the list
random.shuffle(numbers)  # Shuffling the list randomly
numbers.sort()  # Sorting the list in ascending order
print(numbers)

# List of fruits
fruits = ["Apple", "Banana", "Mango", "Grapes"]

# Loop to print each fruit
for fruit in fruits:
    print(fruit)

# Using 'not in' to check if a fruit is missing in the list
if "Orange" not in fruits:
    print("Orange is not in the list.")


# Find Maximum in a List
numbers = [12, 55, 34, 99, 35]
print(max(numbers))


# # Tuple (Immutable)
# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print("First day of the week:", days[0])

month = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print("First month of the year:", month[0])


# Dictionary (Key-Value Pairs)
student = {
    "name": "Shahid Ali",
    "age": 20,
    "course": "Python"
}
print("Student Name:", student["name"])
print("Student Age:", student.get("age"))
print("Course:", student.get("course"))


info = {
    "name": "Shahid",
    "age": 25,
    "is_student": True,
    "grades": [90, 85, 88],
    "address": {"city": "Karachi", "country": "Pakistan"}
}
print(info)


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
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print("Unique numbers:", unique_numbers)

# Set Operations
A = {1, 2, 3}
B = {3, 4, 5}
print("Union:", A | B)  # Union
print("Intersection:", A & B)  # Intersection
print("Difference:", A - B)  # Difference


# Frozenset (Immutable Set) - This set cannot be changed after creation
frozen_numbers = frozenset([10, 20, 30, 40])
print("Frozenset:", frozen_numbers)  

# Duplicate values are automatically removed in a frozenset
items = frozenset([1, 2, 2, 3, 4, 4, 5])
print(items) 

# Using frozenset as dictionary keys (because normal sets are not allowed as keys)
ferozenset_student = {
    frozenset(["Shahid", "Python"]): 95,
    frozenset(["Jawad", "HTML"]): 88
}
print(ferozenset_student)  

# Another example of a frozenset with fruits
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print(frozen_fruits)

# Trying to add an item to a frozenset (This will cause an error)
frozen_fruits.add("mango")  # ERROR: 'frozenset' object has no attribute 'add'
