"""
HSC Software Engineering – Programming Fundamentals
Topic: Syntax Errors in Python

This file demonstrates common SYNTAX ERRORS that occur when writing Python code.

In the HSC Software Engineering course, understanding syntax errors is part of:
- Programming Fundamentals
- Testing and debugging code
- Recognising and correcting common errors

A SYNTAX ERROR happens when the code breaks the "grammar rules" of the language.
Python then cannot translate (interpret) the code into machine instructions.

HOW TO USE THIS FILE:
- The FIRST example below is "live" (not commented out) and will cause a syntax error.
- All OTHER examples are commented out.
- Uncomment ONE example at a time, run the file, read the error message, then fix it.
"""
#
# ---------------------------------------------------------
# EXAMPLE 1 (LIVE): Missing colon in an if statement
# ---------------------------------------------------------
# This example is intentionally WRONG and will cause a syntax error
# because the if statement is missing a ':' at the end of the line.

# Try running this file as-is. Python should show a SyntaxError
# pointing near the 'if' line.

if 5 > 3    # <-- Syntax error here: missing colon (:) at the end
    print("This line will never run because the code above is invalid")


# ---------------------------------------------------------
# IMPORTANT:
# After you have seen the error, FIX the code so that it runs:
#
# Correct version:
#
# if 5 > 3:
#     print("The condition is True, so this line will run correctly.")
#
# Then you can move on to the next examples one by one.
# ---------------------------------------------------------


# =========================================================
# EXAMPLE 2 (COMMENTED OUT): Unmatched quotation marks
# =========================================================
# Description:
# A common syntax error is forgetting to close a string with a matching
# quotation mark. Python then does not know where the string ends.

# To test:
# 1. Comment out (or fix) Example 1 above.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("This line is fine.")

# print("This line will cause a syntax error)   # missing closing quote


# Correct version:
# print("This line will NOT cause a syntax error.")


# =========================================================
# EXAMPLE 3 (COMMENTED OUT): Incorrect indentation
# =========================================================
# Description:
# Python uses INDENTATION to show which statements belong to a block
# (e.g. inside an if, for, while, function, etc.).
# Inconsistent or incorrect indentation causes a SyntaxError.

# To test:
# 1. Comment/fix previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("Start of example 3")
# if True:
# print("This line is incorrectly indented")  # no indentation -> syntax error


# Correct version:
# print("Start of example 3")
# if True:
#     print("This line is correctly indented")


# =========================================================
# EXAMPLE 4 (COMMENTED OUT): Using a reserved keyword as a variable name
# =========================================================
# Description:
# Python has special words (keywords) that are part of the language syntax,
# such as: if, else, for, while, def, class, return, etc.
# You CANNOT use these words as variable names.

# To test:
# 1. Comment/fix any previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# def = 10      # 'def' is a reserved keyword -> syntax error
# print(def)


# Correct version:
# number = 10
# print(number)


# =========================================================
# EXAMPLE 5 (COMMENTED OUT): Missing closing parenthesis in a function call
# =========================================================
# Description:
# When calling a function (such as print), parentheses must match.
# If you forget a closing parenthesis, Python cannot parse the line.

# To test:
# 1. Comment/fix any previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# print("This will work correctly.")
# print("This will cause a syntax error"   # missing closing parenthesis


# Correct version:
# print("This will work correctly.")
# print("This will also work correctly.")


# =========================================================
# EXAMPLE 6 (COMMENTED OUT): Extra comma in a function definition parameters list
# =========================================================
# Description:
# When defining a function, the parameter list must be valid.
# An extra comma or mis-placed symbol can cause a syntax error.

# To test:
# 1. Comment/fix any previous active example.
# 2. Uncomment the lines below.
# 3. Run the file and observe the error message.

# def add_numbers(a, b,):
#     return a + b
#
# print(add_numbers(3, 4))

# Note:
# In modern Python, a trailing comma in a function definition MAY be allowed
# depending on the version and context, so this may or may not cause a syntax error.
# If it does not, adjust the example to something like:

# def add_numbers(a b):
#     return a + b

# This version is definitely wrong because it is missing a comma between parameters.


# =========================================================
# SUMMARY (FOR STUDENTS)
# =========================================================
# In the HSC Software Engineering – Programming Fundamentals unit,
# you should be able to:
# - Recognise what a SYNTAX ERROR is.
# - Read Python error messages and connect them to the incorrect line.
# - Correct simple syntax errors such as:
