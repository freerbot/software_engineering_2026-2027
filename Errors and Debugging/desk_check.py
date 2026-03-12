# A desk check is a manual process used to trace through a program step-by-step.
# You write down the values of variables as each line of code runs, showing how
# the program’s state changes over time. This helps verify that the logic works
# as intended, and it is an important skill in HSC Software Engineering for
# understanding algorithms and identifying error


### Example 1. One variable and no loops. This is an easy one.

# value = 8
#
# value = value + 4    # Step 1
# value = value // 3   # Step 2 (integer division)
# value = value * 5    # Step 3
# value = value + 1    # Step 4
#
# print(value)



### Example 2. A little more challenging. Two variables.. but still no loops.

# x = 4
# y = 10
#
# x = x + 3      # Step 1
# y = y - 2      # Step 1
#
# x = x * 2      # Step 2
# y = y + 5      # Step 2
#
# x = x - 1      # Step 3
# y = y // 3     # Step 3
#
# print(x, y)



### Example 3. And this one is more difficult. It involves 2 variables AND it has a loop.

# number = 1
# total = 0
#
# while number <= 5:
#     total = total + number
#     number = number + 1
#
# print(total)
