#This is a memory game. The player enters 5 words. After this, the player is asked
#to enter the words in reverse order. So they enter word 5 first, word 4 second, etc.
#The game works BUT there are a couple problems:
#1) It's written very inefficiently. It takes almost 50 lines.
#   It could probably be written in half as many lines. Maybe even less.
#   Try to write it in a more efficient way.
#2) The game doesn't keep score. Add a scoring system.

word_list = [] #creates an empty list that we'll be using as a stack

print("I'm going to ask you for five words. \nAfter you input them, I want you to tell \nme the words in reverse order.")

word_list.append(input("Word 1: ")) #let's the user input a word and pushes the user's word onto the top of the stack
word_list.append(input("Word 2: "))
word_list.append(input("Word 3: "))
word_list.append(input("Word 4: "))
word_list.append(input("Word 5: "))


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #this clears the screen, each \n is a new line
print("Ok, now let's play..")

popped_word = word_list.pop() #creates a variable and pops the top of the stack to get the most recently entered word
guess = input("What was word 5? ")
if guess == popped_word:
    print("You're right!")
else:
    print("Sorry, wrong.")

popped_word = word_list.pop()
guess = input("What was word 4? ")
if guess == popped_word:
    print("Correct!")
else:
    print("Sorry, wrong.")

popped_word = word_list.pop()
guess = input("What was word 3? ")
if guess == popped_word:
    print("Correct!")
else:
    print("Sorry, wrong.")

popped_word = word_list.pop()
guess = input("What was word 2? ")
if guess == popped_word:
    print("Correct!")
else:
    print("Sorry, wrong.")

popped_word = word_list.pop()
guess = input("What was word 1? ")
if guess == popped_word:
    print("Correct!")
else:
    print("Sorry, wrong.")

print("Game over! I can't tell you your score because that hasn't been coded yet.. bye!")


# SOLUTION 1:
#
# word_list = [] #creates an empty list that we'll be using as a stack
# score = 0
#
# print("I'm going to ask you for five words. \nAfter you input them, I want you to \ntell me the words in reverse order.")
#
# for x in range(1, 6):
#     word = input(f"Word {x}: ")
#     word_list.append(word)
#
# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #this clears the screen, each \n is a new line
# print("Ok, now let's play..")
#
# for x in range(5, 0, -1):
#     popped_word = word_list.pop()
#     guess = input(f"What was word {x}? ")
#     if guess == popped_word:
#         print("You're right!")
#         score = score + 1
#     else:
#         print("Sorry, wrong.")
#
# print(f"Game over! You got {score} words correct!")



#SOLUTION 2 (user can choose how many words)
#
# word_list = [] #creates an empty list that we'll be using as a stack
# score = 0
#
# print("I'm going to ask you for a series of words. \nAfter you input them, I want you to \ntell me the words in reverse order.")
# how_many_words = int(input("How many words do you think you can remember? "))
#
# for x in range(1, how_many_words + 1):
#     word = input(f"Word {x}: ")
#     word_list.append(word)
#
# print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #this clears the screen, each \n is a new line
# print("Ok, now let's play..")
#
# for x in range(how_many_words, 0, -1):
#     popped_word = word_list.pop()
#     guess = input(f"What was word {x}? ")
#     if guess == popped_word:
#         print("You're right!")
#         score = score + 1
#     else:
#         print("Sorry, wrong.")
#
# print(f"Game over! You got {score} our of {how_many_words} words correct!")