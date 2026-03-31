import random

def guess_number():
    secret_number = random.randint(1, 5)
    # print(f"The secret number is {secret_number}.")  <-- this output statement could be useful for debugging the program
    while True:
        guess = int(input("Guess a number between 1 and 5: "))

        if guess == secret_number:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print("Game Over")

# Start the game
guess_number()




# def calculate_average(marks):
#     total = 0
#     count = 0
#
#     for i in range(1, len(marks)):
#         total = total + marks[i]
#         count = count + 1
#
#     average = total / count
#     return average
#
#
# marks_list = [80, 70, 90, 60]
# average_mark = calculate_average(marks_list)
# print("Average mark:", average_mark)
