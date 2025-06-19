""" Lesson 10: File Handling:
    File handling in Python allows you to read from and write to files. this is important
    when you want to store data permanently or work with large datasets.
    python provides built-in functions and methods to interact with files
    such as open(), read(), write(), append() and close().
"""

# 1. Opening a file in read mode
file = open('example.txt', 'r')  # 'r' for read mode
content = file.readline()  # Read the first line of the file 
print(content)     # Print the first line of the file
file.close()   # Close the file after reading 


# reading the entire data from the file
file = open('example.txt', 'r')  # 'r' for read mode
content = file.read()  # Read the entire content of the file 
print(content)     # Print the content of the file
file.close()   # Close the file after reading 


# reading the file in list format
file = open('example.txt', 'r')  # 'r' for read mode
content = file.readlines()  # Read all lines of the file into a list
print(content)     # Print the list of lines from the file
file.close()   # Close the file after reading 


# 2. Opening a file in write mode overwriting the existing data
file = open('example.txt', 'w')  # 'w' for write mode
file.write('Hello, World!\n')  # Write a line to the file
file.write('This is a new line.\n')  # Write another line to the file
file.close()  # Close the file after writing


# 3. Opening a file in append mode to add data without overwriting
file = open('example.txt', 'a')  # 'a' for append mode
file.write('This line will be appended.\n')  # Append a line to the file
file.close()  # Close the file after appending


# 4. close a file using with statement
with open('example.txt', 'r') as file:  # Automatically closes the file after the block
    content = file.read()  # Read the entire content of the file
    print(content)  # Print the content of the file

# 5. Reading a file using 'with' statement
with open('example.txt', 'r') as file:  # Automatically closes the file after the block
    content = file.readlines()  # Read all lines of the file into a list
    for line in content:
        print(line.strip())  # Print each line without extra newline characters  