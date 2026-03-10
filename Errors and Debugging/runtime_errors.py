"""
HSC Software Engineering – Programming Fundamentals
Topic: Runtime Errors in Python

This file demonstrates common RUNTIME ERRORS that can occur when running Python programs.

In the HSC Software Engineering course, understanding runtime errors is part of:
- Programming Fundamentals
- Testing and debugging code
- Tracing execution to find and fix faults

A RUNTIME ERROR happens while the program is running (after it has passed syntax checking).
The code is syntactically correct, but something goes wrong during execution.

HOW TO USE THIS FILE:
- The FIRST example below is "live" (not commented out) and will cause a runtime error.
- All OTHER examples are commented out.
- Uncomment ONE example at a time, run the file, read the error message, then fix it.
"""

# =========================================================
# EXAMPLE 1 (LIVE): Division by zero (ZeroDivisionError)
# =========================================================
# Description:
# The code below is syntactically correct, so Python will start running it.
# However, dividing by zero is mathematically undefined, so at runtime
# Python raises a ZeroDivisionError.

print("Example 1: Division by zero (this will cause a runtime error)")

numerator = 10
denominator = 0  # This value causes the runtime error below

# The next line will raise: ZeroDivisionError: division by zero
result = numerator / denominator

print("This line will NOT be reached, because the error occurs above.")
print("Result:", result)


# ---------------------------------------------------------
# IMPORTANT:
# After you have seen the error, FIX the code so that it runs:
#
# One possible correction:
#
# print("Example 1: Division by zero (fixed version)")
# numerator = 10
# denominator = 0
#
# if denominator != 0:
#     result = numerator / denominator
#     print("Result:", result)
# else:
#     print("Cannot divide by zero.")
#
# Then you can move on to the next examples.
# ---------------------------------------------------------


# =========================================================
# EXAMPLE 2 (COMMENTED OUT): Using a variable before assigning it (NameError)
# =========================================================
# Description:
# A NameError occurs when you try to use a variable that has not been defined yet.
# The code is syntactically valid, but at runtime Python cannot find the name.

# To test:
# 1. Comment/fix Example 1 so it no longer raises an error.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("\nExample 2: Using a variable before assignment (NameError)")
# total = items_count + 5   # items_count is not defined before use
# print("Total:", total)

# Correct version:
# print("\nExample 2: Using a variable before assignment (fixed)")
# items_count = 10
# total = items_count + 5
# print("Total:", total)


# =========================================================
# EXAMPLE 3 (COMMENTED OUT): Invalid operation between types (TypeError)
# =========================================================
# Description:
# A TypeError often occurs when you try to perform an operation on
# incompatible data types (for example, adding a string and an integer).

# To test:
# 1. Comment/fix any previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("\nExample 3: Invalid operation between types (TypeError)")
# age = 17
# message = "You are " + age + " years old."  # cannot concatenate str and int
# print(message)

# Correct version (convert int to str):
# print("\nExample 3: Invalid operation between types (fixed)")
# age = 17
# message = "You are " + str(age) + " years old."
# print(message)


# =========================================================
# EXAMPLE 4 (COMMENTED OUT): Index out of range (IndexError)
# =========================================================
# Description:
# An IndexError happens when you try to access a position in a list (or string)
# that does not exist. The code is syntactically correct, but the index is invalid.

# To test:
# 1. Comment/fix any previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("\nExample 4: Index out of range (IndexError)")
# numbers = [10, 20, 30]
# print("numbers:", numbers)
# print("Attempting to access element at index 3...")
# print(numbers[3])  # valid indices are 0, 1, 2 only

# Correct version:
# print("\nExample 4: Index out of range (fixed)")
# numbers = [10, 20, 30]
# print("numbers:", numbers)
# print("Last element in the list is:", numbers[2])  # index 2 is valid
#
# # Or use len to protect against invalid indices:
# index = 3
# if 0 <= index < len(numbers):
#     print("Element at index", index, "is", numbers[index])
# else:
#     print("Index", index, "is out of range.")


# =========================================================
# EXAMPLE 5 (COMMENTED OUT): Converting invalid input to int (ValueError)
# =========================================================
# Description:
# A ValueError is raised when a function receives a value of the right type
# but an inappropriate value. For example, converting a non-numeric string
# to an integer using int().

# To test:
# 1. Comment/fix any previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("\nExample 5: Converting invalid input to int (ValueError)")
# user_input = "abc"
# number = int(user_input)  # "abc" cannot be converted to an integer
# print("Number:", number)

# Correct version (validate the input first):
# print("\nExample 5: Converting invalid input to int (fixed)")
# user_input = "123"
# if user_input.isdigit():
#     number = int(user_input)
#     print("Number:", number)
# else:
#     print("Invalid number entered:", user_input)


# =========================================================
# EXAMPLE 6 (COMMENTED OUT): Accessing a missing key in a dictionary (KeyError)
# =========================================================
# Description:
# A KeyError occurs when you try to access a key that does not exist
# in a dictionary.

# To test:
# 1. Comment/fix any previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("\nExample 6: Accessing a missing key in a dictionary (KeyError)")
# student = {
#     "name": "Alex",
#     "year": 12
# }
# print("Student dictionary:", student)
# print("Accessing 'mark' key...")
# print(student["mark"])  # 'mark' key does not exist

# Correct version:
# print("\nExample 6: Accessing a missing key in a dictionary (fixed)")
# student = {
#     "name": "Alex",
#     "year": 12
# }
# print("Student dictionary:", student)
#
# # Use get with a default value:
# print("Mark:", student.get("mark", "No mark recorded"))


# =========================================================
# SUMMARY (FOR STUDENTS)
# =========================================================
# In the HSC Software Engineering – Programming Fundamentals unit,
# you should be able to:
# - Distinguish between SYNTAX ERRORS and RUNTIME ERRORS.
# - Recognise common runtime errors such as:
#     - ZeroDivisionError (e.g. dividing by zero)
#     - NameError (using variables before assignment)
#     - TypeError (invalid operations between data types)
#     - IndexError (list or string index out of range)
#     - ValueError (invalid values for operations or type conversions)
#     - KeyError (missing keys in dictionaries)
# - Use error messages and program tracing to locate and correct faults.
#
# PRACTICE ACTIVITY:
# - For each example above:
#     1. Uncomment the example (one at a time).
#     2. Predict what error will occur and why.
#     3. Run the program and examine the exact error message.
#     4. Modify the code to prevent the error (as shown in the "fixed" versions).
# - Explain, in your own words, how each correction changes the program's behaviour.
#
# This practice supports your understanding of debugging and error handling
# in the HSC Software Engineering course.