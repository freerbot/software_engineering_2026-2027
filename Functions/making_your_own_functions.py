
#### EXAMPLE OF A VERY BASIC FUNCTION ####

# This defines a function called say_hi.
# It does not take any inputs (no parameters).
def say_hi():
    print("Hi, I'm a computer.")# This line runs when the function is called.

say_hi() # This calls the function so the code inside the function will run.



#### EXAMPLE OF A FUNCTION THAT TAKES 1 INPUT (called a PARAMETER) ####
# # This defines a function that has 1 parameter: name.
# def say_hi(name):
#     print(f"Hi, {name}")
#
# name = "Mr Freer"
# say_hi(name)



#### EXAMPLE OF A FUNCTION THAT HAS 2 PARAMETERS ####

# # This defines a function that expects 2 parameters: name and favourite_food.
# def say_hi(name, favourite_food):
#     # Stores the parameters in local variables (again, showing the process)
#     name = name
#     food = favourite_food
#
#     # Prints a message using both pieces of data.
#     print(f"Hi, {name}. I like {food} also.")
#
# # Creating variables to hold the data to pass to the function.
# name = "Mr Freer"
# favourite_food = "pizza"
#
# # Calling the function with two arguments.
# # An argument is the piece of data you're sending to the function.
# say_hi(name, favourite_food)




#### EXAMPLE OF A FUNCTION THAT HAS 2 PARAMETERS AND USES RANDOM NUMBERS ####

# import random
#
# def calculate_damage(player_strength, player_speed):
#     strength = player_strength
#     speed = player_speed
#     damage = (strength * 2) * (speed / 2) * random.randint(0,3)
#     print(f"You did {damage} points of damage!")
#
# player_strength = 5
# player_speed = 2
# calculate_damage(player_strength, player_speed)

