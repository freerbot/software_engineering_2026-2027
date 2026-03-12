# A breakpoint is a tool used during debugging that pauses a program at a
# specific line of code. When the program stops, the developer can inspect the
# current values of variables and see exactly what the program is doing at that
# moment. Breakpoints help identify logic errors by allowing the program to run
# step-by-step from the paused point onward.


# Example 1
#
# for x in range(0, 5):
#     print(x) # Try a breakpoint here




# Example 2

# def calculate_total(prices):
#     total = 0
#     for price in prices:
#         total = total + price # try a breakpoint here
#     return total
#
# shopping_cart = [10, 25, 5, 30]
# result = calculate_total(shopping_cart)
# print(f"Total: ${result}")



# Example 3

# import random
# secret_number = random.randint(1,10)
# for x in range(0,3):
#     guess = int(input("What's your guess? "))
#     if guess > secret_number:
#         print("Too low!")
#     elif guess < secret_number:
#         print("Too high!")
#     else:
#         print("Correct!")
#         break
#
# print("Game over")