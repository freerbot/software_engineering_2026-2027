"""
HSC Software Engineering – Programming Fundamentals
Topic: Logic Errors in Python

This file demonstrates LOGIC ERRORS — mistakes in the programmer's thinking that
cause a program to run without crashing but produce incorrect results.

In the HSC Software Engineering course, logic errors are closely tied to:
- Tracing execution step-by-step
- Comparing expected output with actual output
- Designing and applying test cases
- Understanding algorithmic reasoning

A LOGIC ERROR:
- Does NOT stop the code from running (unlike syntax/runtime errors)
- Produces the WRONG RESULT
- Must be found through testing, reasoning, or tracing the code

HOW TO USE THIS FILE:
- The FIRST example is “live” and will run, but the output is incorrect.
- All other examples are commented out for controlled student experimentation.
"""

# =========================================================
# EXAMPLE 1 (LIVE): Incorrect calculation (logic error)
# =========================================================
# Description:
# The code BELOW calculates the average of three numbers.
# However, the programmer forgot to divide by 3.
# This produces an incorrect result — a classic logic error.

print("Example 1: Incorrect average calculation (logic error)")

a = 10
b = 20
c = 30

# LOGIC ERROR: Should divide by 3, not 2
average = (a + b + c) / 2

print("Expected average: 20")
print("Actual output:   ", average)
print("This is a logic error because the program RUNS but gives the WRONG result.\n")


# ---------------------------------------------------------
# CORRECT VERSION (AFTER STUDENTS INSPECT OUTPUT):
#
# average = (a + b + c) / 3
# print("Correct average:", average)
#
# ---------------------------------------------------------


# =========================================================
# EXAMPLE 2 (COMMENTED OUT): Wrong loop boundary
# =========================================================
# Description:
# A common logic error occurs when loops iterate too many or too few times.
#
# For example, summing numbers 1–5 but incorrectly looping 1–4.

# print("\nExample 2: Wrong loop boundary (logic error)")
# total = 0
# for i in range(1, 5):   # should be range(1, 6)
#     total += i
#
# print("Expected total of 1+2+3+4+5 = 15")
# print("Actual output:", total)
#
# Correct version:
# total = 0
# for i in range(1, 6):
#     total += i
# print("Correct output:", total)


# =========================================================
# EXAMPLE 3 (COMMENTED OUT): Incorrect condition logic
# =========================================================
# Description:
# Misusing comparison operators results in wrong program behaviour.
#
# Example: Checking whether someone is a teenager.

# print("\nExample 3: Incorrect conditional logic")
# age = 12
#
# if age > 13 and age < 19:   # Teenagers are 13–19 inclusive
#     print("Teenager")
# else:
#     print("Not a teenager (incorrect logic for age 12)")
#
# Correct logic (inclusive):
# if 13 <= age <= 19:
#     print("Teenager")
# else:
#     print("Not a teenager")


# =========================================================
# EXAMPLE 4 (COMMENTED OUT): Incorrect variable update inside loop
# =========================================================
# Description:
# Students often update the wrong variable, leading to incorrect program state.

# print("\nExample 4: Incorrect variable update")
# count = 0
# for n in [2, 4, 6, 8]:
#     count = n   # LOGIC ERROR: Should INCREMENT count, not replace it
#
# print("Expected count: 4")
# print("Actual output:", count)
#
# Correct version:
# count = 0
# for n in [2, 4, 6, 8]:
#     count += 1
# print("Correct output:", count)


# =========================================================
# EXAMPLE 5 (COMMENTED OUT): Misplaced return statement
# =========================================================
# Description:
# A logic error in function design — the return happens too early.

# print("\nExample 5: Misplaced return statement")
#
# def count_even(numbers):
#     count = 0
#     for n in numbers:
#         if n % 2 == 0:
#             count += 1
#         return count      # LOGIC ERROR: Returns on first iteration
#
# print("Expected: 3 even numbers in [2, 3, 4, 6]")
# print("Actual output:", count_even([2, 3, 4, 6]))
#
# Correct version:
# def count_even(numbers):
#     count = 0
#     for n in numbers:
#         if n % 2 == 0:
#             count += 1
#     return count
#
# print("Correct output:", count_even([2, 3, 4, 6]))


# =========================================================
# SUMMARY (FOR STUDENTS)
# =========================================================
# In the Programming Fundamentals unit of HSC Software Engineering,
# you must understand that:
#
# - Logic errors produce incorrect behaviour or results.
# - Programs DO run — no syntax or runtime errors occur.
# - Detecting logic errors relies on:
#     • Expected vs actual output analysis
#     • Careful test case design (including boundary cases)
#     • Tracing program execution (manual or automated)
#     • Reasoning about algorithm design
#
# PRACTICE ACTIVITY:
# - Uncomment each example one at a time.
# - Predict the expected output.
# - Run the code and record the actual output.
# - Identify WHY the logic is wrong.
# - Correct it and retest.
#
# This builds your debugging and algorithmic thinking skills,
# which are essential for HSC Software Engineering.
