# Operators in Python
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups

# Arithmetic Operators, Assignment Operators, Comparison Operators, Logical Operators, 
# Identity Operators, Membership Operators, Bitwise Operators

# Arithmetic Operators
# + Addition, - Subtraction, * Multiplication, / Division, % Modulus, ** Exponentiation,

#  + Addition
addition1 = 10
addition2 = 20
print(addition1 + addition2)          # 10 + 20 = 30

# -  Subtraction
subtraction1 = 20
subtraction2 = 10  
print(subtraction1 - subtraction2)    # 20 - 10 =

# *  Multiplication
multiplication1 = 4
multiplication2 = 2
print(multiplication1 * multiplication2)  # 4 * 2 = 8

# /  Division
division1 = 20
division2 = 2
print(division1 / division2)    # 10.0

# %  Modulus
modulus1 = 10
modulus2 = 3
print(modulus1 % modulus2)      # 1

# ** Exponentiation
exponentiation1 = 2
exponentiation2 = 3
print(exponentiation1 ** exponentiation2) # 2 ** 3 = 8


# Relational/Comparison Operators
value1 = 11
value2 = 18
print(value1 == value2)  # False
print(value1 != value2)  # True
print(value1 >= value2)  # False
print(value1 <= value2)  # True
print(value1 < value2)  # True
print(value1 > value2)  # False


# Assignment Operators
value3 = 10
value3 += 5    # value3 = value3 + 5
print(value3)  # 15

value4 = 20
value4 -= 5     # value4 = value4 - 5
print(value4)   # 15

value5 = 30
value5 *= 5     # value5 = value5 * 5
print(value5)   # 150

value6 = 40
value6 /= 5     # value6 = value6 / 5
print(value6)   # 8.0

value7 = 2
value7 **= 3   # value7 = value7 ** 3
print(value7)  # 8


# Logical Operators
# and, or, not
value8 = 10
value9 = 20

print(value8 > 5 and value9 > 15)  # False
print(value8 > 5 or value9 > 15)   # True
print(not(value8 > 5 and value9 > 15))  # True

c = 10 
d = 20
print(c > d and d > c)  # False
print(c < d and d > c)  # True

print(c > d or d < c)  # False
print(c < d or d < c)  # True

e = 10
f = 20
print(not e < f)  # False
print(not e > f)  # True


# Identity Operators
# is, is not
a = [1, 2, 3]  
b = [1, 2, 3]  
c = a  
print(a is c)      # True (both refer to the same object in memory)
print(a is b)      # False (both have the same values but different memory locations)
print(a is not b)  # True (because they are different objects)


# Membership Operators
# in, not in

# in
# Check if an item is present in a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print("Banana" in fruits)  # Output: True
print("Grape" in fruits)   # Output: False

# Check in string
text = "Hello World"
print("Hello" in text)  # Output: True
print("Python" in text) # Output: False

# Check in dictionary
student = {"name": "Shahid", "age": 25, "city": "Karachi"}
print("name" in student)  # Output: True
print("salary" in student)  # Output: False

# not in
# Check if an item is not present in a list
fruits1 = ["Apple", "Banana", "Mango"]
print("Grape" not in fruits1)  # Output: True
print("Banana" not in fruits1) # Output: False

# Check not in string
text1 = "Hello World"
print("Python" not in text1) # Output: True
print("Hello" not in text1)  # Output: False

# Check not in dictionary
student1 = {"name": "Shahid", "age": 25, "city": "Karachi"}
print("country" not in student1)  # Output: True
print("name" not in student1)  # Output: False


# Bitwise Operators
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)

# & (AND)
and1 = 10
and2 = 4
print("and1 & and2 = ", and1 & and2)  # 0

# | (OR)
or1 = 10
or2 = 4
print("or1 | or2 = ", or1 | or2)  # 14

# ^ (XOR)
xor1 = 10
xor2 = 10
print("xor1 ^ xor2 = ", xor1 ^ xor2)  # 34

# ~ (NOT)
not1 = 10
not2 = 4
print("~not1 = ", ~not1)  # -11

# << (Left Shift)
left_shift1 = 10
left_shift2 = 2
print("left_shift1 << left_shift2 = ", left_shift1 << left_shift2)  # 40

# >> (Right Shift)
right_shift1 = 10
right_shift2 = 2
print("right_shift1 >> right_shift2 = ", right_shift1 >> right_shift2)  # 2