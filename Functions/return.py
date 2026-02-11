# If you want to use a function to generate a value to be used elsewhere in your program,
# you can use 'return'. Let's see how that works.

def say_hi(name): # creates a function that takes 1 argument
    greeting = "Hi, " + name # creates a variable and assigns it a value
    return greeting # this sends the value back to where the function was called

print(say_hi("Mr Freer"))


#
# def cube_number(number_to_cube):
#     cubed_number = number_to_cube * number_to_cube * number_to_cube # calculates the cubed number
#     return cubed_number # and this sends that number back to where the function was called
#
# print(cube_number(5)) # this will print the value that the function returns
#
# print(f"5 cubed is {cube_number(5)}")



