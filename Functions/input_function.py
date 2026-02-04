# The input() function allows the user to type text into your program.
# Ths most common use of this is for assigning values to variables.
# For example:

user_name = input("Enter your name here: ")
print(f"Hello, {user_name}.")



user_age = int(input("Enter your age here: "))
if user_age > 18:
    print("You are an adult.")
else:
    print("You're not an adult.")