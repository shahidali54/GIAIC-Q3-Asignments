""" Lesson 09 Exception Handling:
    Exception handling in Python is a mechanism used to handle runtime errors gracefully. 
    It allows the programmer to catch and manage exceptions, preventing the program from 
    crashing unexpectedly. Python provides try, except, else, and finally blocks for
    structured exception handling.
"""

# Step 1: Basic Exception Handling
try:
    result = 10 / 0 # This will raise a ZeroDivisionError
except:
    print("An error occurred: Division by zero is not allowed.") # Handle the exception


# Step 2: Handle specific error types

try:
    result = 10 / 0
except ZeroDivisionError:
    print("An error occurred: Division by zero is not allowed.") # Handle ZeroDivisionError
except Exception as e:
    print(f"An error occurred: {e}") # Handle any other exception


# Step 3: else block runs only when NO error occurs

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!") # Handle ZeroDivisionError
else:
    print(f"Division successful. Result: {result}") # This block runs if no exception occurs


# Step 4: finally block runs NO MATTER WHAT

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!") # Handle ZeroDivisionError
finally:
    print("This will always execute ")  # This block always runs, regardless of exceptions


# Step 5: Combine all four blocks

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.\n")

# Test Cases
divide_numbers(10, 2)       # Valid division
divide_numbers(10, 0)       # Division by zero
divide_numbers(10, "2")     # Invalid input type (string instead of number)
