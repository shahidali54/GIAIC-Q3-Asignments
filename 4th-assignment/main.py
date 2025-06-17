# Lesson 08: Modules & Functions

# MODULES:
"""A module in Python is basically a separate file or library which can be pre-made (built-in)
   or you can create your own (custom).
   The purpose of modules is to organize and reuse code, like a ready-made toolbox."""

#<================= Here we are using 3 built-in modules: ==========================>
""" 1. math --> For mathematical calculations (sqrt, pow, sin, etc.)
    2. random --> To generate random values (random numbers or random choices)
    3. os --> To work with the Operating System (files/folders handling)"""

#<============================= Importing modules ==================================>
import math    # Importing math module to use math formulas
import random  # Importing random module to generate random values
import os      # Importing os module to work with folders and files


# math module
print("Square root of 64:", math.sqrt(64))  
# math.sqrt(64) means: find the square root of 64 (result will be 8.0)

# random module
print("Random number between 1 and 10:", random.randint(1, 10))  
# random.randint(1, 10) means: print a random number between 1 and 10

print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))  
# random.choice() means: randomly select and print one item from the list

# os module
print("Current working directory:", os.getcwd())  
# os.getcwd() means: print the path of the current working directory

print("List of files/folders in current directory:", os.listdir())  
# os.listdir() means: print the list of all files and folders inside the current directory

#<=========================== CREATING CUSTOM MODULES ================================>

# Importing our custom module (my_module.py)
import my_module

# Using greet() function from custom module
print(my_module.greet("Shahid"))

# Using add() function from custom module
print("Sum of 30 and 40 is:", my_module.add(30, 40))

# Using pi_value from custom module
print("Value of Pi from custom module:", my_module.pi_value)

# Using only single function
from my_module import greet
print(greet("Shahid"))

#<=================== Third-Party Modules (External Libraries) =======================>
"""Third-party modules are those which are not pre-installed with Python.
   We need to install them manually using pip or any package manager.
   requests (used to make HTTP requests)"""

# install the requests library
# pip install requests

""" This is an example of a third-party module.
    We are using 'requests' to fetch data from an external API."""

import requests # third-party module

# Make a request to an API and fetch data
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Check the status code of the API response
print("API Status Code:", response.status_code)

# Print the JSON data received from the API
print("API Response JSON Data:", response.json())


#<================== Different Ways to Import Modules in Python =================>

# Basic Import Method
# This imports the entire module. We will need to use 'module_name.' prefix to access its functions/variables.
import math
print("Value of Pi using basic import:", math.pi)


# Import with Alias
# Giving a short name (alias) to the module for easier access.
import numpy as np
print("Numpy array using alias:", np.array([1, 2, 3]))

# Import Specific Functions or Variables
# Importing only specific parts of a module.
from math import sqrt, pi
print("Square root using specific import:", sqrt(16))
print("Pi value using specific import:", pi)

# Import Specific Functions with Aliases
# Importing specific functions and renaming them for convenience.
from math import sqrt as s, pi as p
print("Square root using alias:", s(25))
print("Pi value using alias:", p)


# Import Everything (Wildcard Import)
"""Imports all functions and variables without using the module name.
   Not recommended for large modules as it clutters the namespace."""
from math import *
print("Sin value using wildcard import:", sin(0))



#<====================== Functions in Python =====================================>
"""A function in Python is a reusable block of code designed to perform a specific task.
Functions help make code modular and DRY (Don't Repeat Yourself)."""

# Defining a simple function

# Built-in Function
# Built-in functions are available by default as soon as Python runs.
print("Hello! World")

# User-Defined Function
# A function we create ourselves is called a user-defined function

# Simple Functions
def my_function():
    print("Hello! Welcome to GIAIC")
my_function()


# Function with parameter
def greet_user(name):
    print(f"Hello, {name}! How are you?")
greet_user("Shahid")


# Function with return value
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 10)
print("Sum is:", result)


# function to checks whether the given number is odd or even.
def check_odd_even(number):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

check_odd_even(7)
check_odd_even(12)


# function to calculates the average of a list of numbers.
def calculate_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print("Average is:", average)

# Functions defined inside built-in modules
# We need to import modules like random to access their functions.
import random  # built-in module
print("Random float using random.random():", random.random())


# Immutable vs Mutable Objects with Functions
def modify_value(x):
    x = 10
    print("Within function:", x)

# Immutable object (integer)
x = 5
print("Original:", x)
modify_value(x)
print("After function:", x)


# Mutable Object (List)
def modify_list(lst):
    lst.append(4)
    print("Within function: ", lst, " - ID:", id(lst))

# Mutable object (list)
lst = [1, 2, 3]
print("Original:", lst, " - ID:", id(lst))
modify_list(lst)
print("After function:", lst, " - ID:", id(lst))


# Function arguments are the values or variables passed into a function when it is called.
def greetings(name):
    "This is docstring of greetings function"
    print ("Hello {}".format(name))
    return

greetings("Shahid")
greetings("Subhan")
greetings("Jawad")

# Keyword Arguments
def printinfo( name, age ):
    print ("Name: ", name)
    print ("Age ", age)
    return

printinfo(name = "Shahid Ali", age = 25)


# Default Arguments
def printinfo(name, age = 20):
    print ("Name: ", name)
    print ("Age ", age)
    return
printinfo(name = "Shahid", age = 25 )   # override the age
printinfo(name = "Shahid")              # default age



#====================== Lesson 09: Exception Handling ================================
"""The try block is used to test a block of code for errors. If an error occurs within the try block, 
   the program will immediately jump to the except block (if provided)."""

# The try Block
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An error occurred!")

"""The except block is used to handle specific errors that occur in the try block. 
    You can specify the type of error to catch, except to catch all errors."""

# The except Block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

"""The else block is executed if no errors occur in the try block. It is optional and 
    is used for code that should only run when the try block is successful"""

# The else Block
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful. Result: {result}")

"""The finally block is executed regardless of whether an error occurred or not. 
It is often used for cleanup operations, such as closing files or releasing resources."""
    
# The finally Block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")


# Putting It All Together
# Here’s an example that combines all four blocks.
def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.")
# Test cases
divide_numbers(10, 2)      # Successful division
divide_numbers(10, 0)      # ZeroDivisionError
divide_numbers(10, "2")    # TypeError


# Practice:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Invalid input. Please enter numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the program!")


# Basic Example of Throwing an Exception:
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")  # Raising an exception
    return a / b

print(divide(10, 2))  # Output: 5.0
print(divide(5, 0))   # Raises: ValueError: Division by zero is not allowed!


# Handling the Exception with try-except
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

try:
    result = divide(5, 0)  # This will raise an exception
    print(result)  # This line won't run if exception occurs
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Division by zero is not allowed!

print("Program continues...")  # This line will always execute


# Throwing Custom Exceptions

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass
def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"

try:
    print(check_positive(-5))  # Raises NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))  # Output: Custom Exception Caught: Negative numbers are not allowed!



#<========================= Lesson 10: I/O File Handling =============================>
"""File handling is essential for reading and writing data to files, enabling persistent storage. 
   Python provides built-in functions and methods to handle files efficiently. 
   This tutorial covers the fundamentals with examples.
   Opening a File

Use the open() function to open a file. Specify the mode (read, write, append, etc.).

Modes:

r: Read (default)

w: Write (Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does.)

a: Append (Opens the file for appending. Creates the file if it doesn't exist, or adds to it if it does.)

x: Exclusive creation (fails if file exists)

b: Binary mode (Used with the other modes (e.g., "rb", "wb") for working with binary files.)

+: Update mode (Can be combined with other modes (e.g., "r+", "w+") to allow both reading and writing.)"""

# w: Write mode. Opens the file for writing. Creates the file if it doesn't exist, or overwrites it if it does.
file = open("new_file.txt", "w")
# Writing to Files:To write to a file, open it in write ("w") or append ("a") mode
file.write("Hello, world!\n")  # \n creates a new line
file.write("This is another line.\n")
file.close()

# writelines(list): Writes a list of strings to the file.
lines = ["Line 1: Shahid\n", "Line 2: Subhan\n", "Line 3: Jawad\n"]
file = open("new_file.txt", "a") # run with mode w, and see the result
file.writelines(lines)
file.close()

file = open("my_file.txt", "r")  # Opens "my_file.txt" in read mode ("r")
file = open("new_file.txt", "r")  # Opens "my_file.txt" in read mode ("r")
content = file.read()
print(content)

line = file.readline()
print(line)
file.seek(0)
print("Position after seek(0):", file.tell())

line = file.readline()
print(line)

# readlines(): Reads all lines into a list.
file.seek(0) # First move the pointer to the start

lines = file.readlines()
for line in lines:
    print(line)

file = open("new_file.txt", "r")
for line in file:  # Iterating directly over the file reads line by line
    print(line.strip()) # .strip() removes leading/trailing whitespace

# Closing Files:
file.close()


# Copying a file
def copy_file(source_path, destination_path):
    try:
        with open(source_path, "r") as source_file, open(destination_path, "w") as dest_file:
            for line in source_file:
                dest_file.write(line)
        print(f"File '{source_path}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file("unique.txt", "unique_copy.txt")


# File Operations Demo
# Create and write to a file
with open('demo.txt', 'w') as file:
    file.write('Python File Handling\n')
    file.write('Line 1\nLine 2\n')

# Read and print content
with open('demo.txt', 'r') as file:
    print("Content:")
    print(file.read())

# Append a new line
with open('demo.txt', 'a') as file:
    file.write('Appended line\n')

# Read lines using seek
with open('demo.txt', 'r+') as file:
    file.seek(0)
    print("First line:", file.readline())


# Conclusion:
"""Python’s file handling is straightforward with open(), read(), write(), and close()
    Always use the with statement for safety and leverage exception handling for robustness.
    Experiment with modes and methods to manage files effectively!"""

# prompt: generate a comprehensive example of file handling using all the functions

# Create a file and write to it
with open('example.txt', 'w') as f:
  f.write("This is line 1.\n")
  f.write("This is line 2.\n")
  f.writelines(["This is line 3.\n", "This is line 4.\n"])

# Read the file and print its content
with open('example.txt', 'r') as f:
  content = f.read()
  print("--- Full Content ---")
  print(content)

# Read the file line by line and print each line
with open('example.txt', 'r') as f:
  print("--- Line by Line ---")
  for line in f:
    print(line, end='')

# Read a single line
with open('example.txt', 'r') as f:
  print("\n--- Readline ---")
  print(f.readline(), end='')

# Read all lines into a list
with open('example.txt', 'r') as f:
  lines = f.readlines()
  print("\n--- Readlines ---")
  for line in lines:
    print(line, end='')

# Append to the file
with open('example.txt', 'a') as f:
  f.write("This is appended line 1.\n")
  f.write("This is appended line 2.\n")

# Reading with seek and tell
with open('example.txt', 'r') as f:
  print("\n--- Seek and Tell ---")
  print("Current position:", f.tell())
  print("First line:", f.readline(), end="")
  print("Current position:", f.tell())
  f.seek(0)
  print("After seek(0):", f.tell())
  print("First line again:", f.readline(), end="")

# Demonstrating 'x' mode (exclusive creation)
try:
    with open('new_file.txt', 'x') as f:
        f.write("This is a new file created in 'x' mode.")
        print("new_file.txt created successfully!")
except FileExistsError:
    print("File 'new_file.txt' already exists!")

# Copy file example
def copy_file(source, destination):
  try:
    with open(source, 'r') as src, open(destination, 'w') as dest:
      for line in src:
        dest.write(line)
      print(f"'{source}' successfully copied to '{destination}'")
  except FileNotFoundError:
    print(f"Error: File not found '{source}'")
  except Exception as e:
    print(f"Error during copying: {e}")

copy_file("example.txt", "example_copy.txt")



#<===================== Lesson 11: The Math & Date Time Calendar =====================>

# The Date & Time
import time # This is required to include time module.
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Getting the Current Time
import time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

# Getting the Current Date
import time
localtime = time.localtime(time.time())
print ("Local current date :", time.strftime("%d-%m-%Y", localtime))

# Getting the Current Time and Date
import time
localtime = time.localtime(time.time())
print ("Local current date and time :", time.strftime("%d-%m-%Y %H:%M:%S", localtime))

# Getting the Formatted Time
import time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


# The Calendar: Getting the Calendar for a Month
import calendar
cal = calendar.month(2025, 3)
print ("Here is the calendar:")
print (cal)

# The Calendar: Getting the Weekday for a Date
import datetime
date_obj = datetime.date(2025, 3, 15)
print("Day of the week:", date_obj.strftime("%A"))


# The Date Time
from datetime import date
date1 = date(2023, 4, 19)
print("Date:", date1)
date2 = date(2023, 4, 30)
print("Date2:", date2)

import datetime
x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)


# The strftime() Method
import datetime
x = datetime.datetime(2025, 3, 26)
print(x.strftime("%f")) #Display Microsecond 000000-999999
print(x.strftime("%A")) #Display the name of the Day
print(x.strftime("%Y")) #Display the Year
print(x.strftime("%B")) #Display the name of the month


# Python Math Module
"""The math module is a built-in module in Python that is used for performing mathematical operations.
   This module provides various built-in methods for performing different mathematical tasks."""

import math

# abs() returns the absolute value of a number
# In Python, abs() is a built-in function, which means it's a global function
# available in the standard library without needing to import any specific modules.
# You can use it directly in your code.
print("abs(-5) = ", abs(-5))  # outputs: 5

# pow() raises a number to a power
print("pow(2, 3) = ", pow(2, 3))  # outputs: 8

# round() rounds a number to a specified number of decimal places
print("round(3.14159, 2) = ", round(3.14159, 2))  # outputs: 3.14

# max() returns the largest of a set of numbers
print("max(1, 2, 3, 4, 5) = ", max(1, 2, 3, 4, 5))  # outputs: 5

# min() returns the smallest of a set of numbers
print("min(1, 2, 3, 4, 5) = ", min(1, 2, 3, 4, 5))  # outputs: 1

# math.sin() returns the sine of an angle in radians
print("math.sin(math.pi/2) = ", math.sin(math.pi/2))  # outputs: 1.0

# math.cos() returns the cosine of an angle in radians
print("math.cos(0) = ", math.cos(0))  # outputs: 1.0

# math.tan() returns the tangent of an angle in radians
print("math.tan(math.pi/4) = ", math.tan(math.pi/4))  # outputs: 1.0

# math.sqrt() returns the square root of a number
print("math.sqrt(9) = ", math.sqrt(9))  # outputs: 3.0

# math.factorial() returns the factorial of a number
print("math.factorial(5) = ", math.factorial(5))  # outputs: 120

# math.log() returns the natural logarithm of a number
print("math.log(10) = ", math.log(10))  # outputs: 2.302585092994046

# math.log10() returns the base-10 logarithm of a number
print("math.log10(100) = ", math.log10(100))  # outputs: 2.0

# math.exp() returns the value of e raised to a power
print("math.exp(2) = ", math.exp(2))  # outputs: 7.38905609893065

# math.ceil() returns the smallest integer greater than or equal to a number
print("math.ceil(4.7) = ", math.ceil(4.7))  # outputs: 5

# math.floor() returns the largest integer less than or equal to a number
print("math.floor(4.7) = ", math.floor(4.7))  # outputs: 4

# math.pi is a constant representing the ratio of a circle's circumference to its diameter
print("math.pi = ", math.pi)  # outputs: 3.14159265359

# math.e is a constant representing the base of the natural logarithm
print("math.e = ", math.e)  # outputs: 2.718281828459045

# math.tau is a constant representing the ratio of a circle's circumference to its radius
print("math.tau = ", math.tau)  # outputs: 6.283185307179586

# math.inf is a constant representing infinity
print("math.inf = ", math.inf)  # outputs: inf

# math.nan is a constant representing "not a number"
print("math.nan = ", math.nan)  # outputs: nan


# NaN: In Python, 
"""NaN stands for "Not a Number".  It's a special floating-point value 
   that represents an undefined or unrepresentable numerical result. It's a way for 
   Python to indicate that a calculation or operation couldn't produce a valid numerical outcome."""

# Uncomment to see error

# result = 0 / 0  # Division by zero
# print(result)      # Output: nan

# result = math.sqrt(-1)  # Square root of a negative number
# print(result)      # Output: nan

result = float('nan')  # Explicitly creating NaN
print(result)      # Output: nan


# Working with NaN:
# Checking for NaN: You can use the math.isnan() function to check if a value is NaN
import math
x = float('nan')
if math.isnan(x):
  print("x is NaN")

# Important Notes:
"""NaN compares unequal to any number, including itself. So, NaN == NaN is False.
   Calculations involving NaN often result in NaN."""

x = float('nan')
y = float('nan')
print( x == y) # Output False


# Infinity In Python, math.inf represents positive infinity, and it is indeed 
# displayed as inf when you print it.
positive_infinity = math.inf
#positive_infinity = -math.inf # Negative infinity
print(positive_infinity)  # Output: inf
print(type(positive_infinity))  # Output: <class 'float'>


#<=================== Key points to remember about math.inf ==========================>
""" Floating-point: math.inf is a floating-point value, not an integer.
    Comparisons: It's greater than any finite number.
    Operations: Many mathematical operations involving infinity will result
    in infinity (or NaN in some cases, like infinity minus infinity).
    Negative Infinity: For negative infinity, you would use -math.inf."""

import math

positive_infinity_1 = math.inf
positive_infinity_2 = math.inf

print(positive_infinity_1 - positive_infinity_2)  # Output: nan
print(positive_infinity_1 * 2)  # Output: inf

positive_infinity = math.inf
print(positive_infinity > 999999999999999999999999) #It's greater than any finite number.

""" Topics covered by Sir Arif Kasim Rozani Google Colabs.
    By Shahid Ali """ 