""" Lesson 11: The Math & Date Time Calendar:
    In this lesson, we explore two important Python modules: math and datetime.
    The math module provides a wide range of mathematical functions such as square root, 
    power, trigonometry, and constants like pi. It is useful for performing advanced 
    mathematical calculations.
    The datetime module provides classes for working with dates and times in Python. 
    It allows you to handle current and custom dates, times, and time intervals easily. 
    Common classes include datetime, date, time, and timedelta.
"""
import math
import time 
import datetime
import calendar
from datetime import date

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Getting the Current Time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

# Getting the Current Date
localtime = time.localtime(time.time())
print ("Local current date :", time.strftime("%d-%m-%Y", localtime))

# Getting the Current Time and Date
localtime = time.localtime(time.time())
print ("Local current date and time :", time.strftime("%d-%m-%Y %H:%M:%S", localtime))

# Getting the Formatted Time
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


# The Calendar: Getting the Calendar for a Month
cal = calendar.month(2025, 4)
print ("Here is the calendar:")
print (cal)

# The Calendar: Getting the Weekday for a Date
date_obj = datetime.date(2025, 4, 16)
print("Day of the week:", date_obj.strftime("%A"))

# The Date Time
date1 = date(2023, 4, 19)
print("Date:", date1)
date2 = date(2023, 4, 30)
print("Date2:", date2)

# Using timedelta to add days
from datetime import timedelta
today = date.today()
future_date = today + timedelta(days=7)
print("Today's date:", today)
print("Date after 7 days:", future_date)


x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)


# The strftime() Method
x = datetime.datetime(2025, 4, 16)
print(x.strftime("%f")) #Display Microsecond 000000-999999
print(x.strftime("%A")) #Display the name of the Day
print(x.strftime("%Y")) #Display the Year
print(x.strftime("%B")) #Display the name of the month



# ======================= MATH MODULE =======================
# Use math.sqrt() to calculate square root
number = 25
sqrt_result = math.sqrt(number)
print(f"The square root of {number} is {sqrt_result}")

# Use math.pow() to calculate power
base = 2
exponent = 3
power_result = math.pow(base, exponent)
print(f"{base} raised to the power {exponent} is {power_result}")

# Use math.pi and math.ceil/floor
print(f"Value of PI is: {math.pi}")
print(f"Ceiling of 3.7 is: {math.ceil(3.7)}")
print(f"Floor of 3.7 is: {math.floor(3.7)}")

# Use math.factorial() to calculate factorial
number = 5
factorial_result = math.factorial(number)
print(f"The factorial of {number} is {factorial_result}")


# new math functions
# Use math.gcd() to calculate greatest common divisor
num1 = 48
num2 = 18
gcd_result = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd_result}")
