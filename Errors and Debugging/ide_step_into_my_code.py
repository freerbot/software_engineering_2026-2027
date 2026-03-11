# This is a case where 'Step Into My Code' would be more useful than 'Step Into".

# 'Step Into My Code' steps into functions, but only YOUR functions.

# 'Step Into' steps into your functions AND some functions that are part
# of Python's built-in functions. Or functions that are parts of modules.
# This can get messy.

# In this example, the random module is used. If you use 'Step Into', it will
# step into the code for the random module, which probably isn't very useful when
# you're debugging your own code. So using 'Step Into My Code' would bypass any
# irrelevant functions and only follow the content of your own functions.



import random

print("Guess the number (1–10). You get 3 guesses. Note: The target changes each time!")

for attempt in range(1, 4):
    target = random.randint(1, 10)   # breakpoint here
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == target:
        print("Nice! You guessed it!")
    else:
        print(f"Not this time. The number was {target}.")

print("Game over!")
