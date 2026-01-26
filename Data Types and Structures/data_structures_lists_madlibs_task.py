# 0) import random
# 1) Get user to input a string containing multiple names, make this a variable
# 2) USe the .split() method to break string into a list
# 3) find out the length of the list using len()
# 4) select a random item from the list
# 5) print the name as part of the story print(f"My friend {random_name}...")

# syntax:
# my_string = input("Enter some words..")
# my_list = my_string.split()
# my_list_length = len(my_list)
# my_list_random_index = random.randint(smallestnumber, largestnumber)
# my_list_random_element = my_list[my_list_random_number]
# print(f"The random thing is {my_list_random_element}.")

















#Write a Python program that allows the user to enter a
#sets of words for several prompts. After the user has
#entered these words, the program will select a random word
#from each set of words and print it as part of a short
#story.















import random
print("Hi, I need some help writing a story. \nI'm going to ask you to give me some names, foods, places and animals.")
print("When you input these things, separate them with a space. \nAnd only use single-word things, please.\n")
names = input("Type a selection of names here. As many as you like: ")
foods = input("Ok, now give me a few different foods: ")
places = input("And now some places: ")
animals = input("Last, please tell me a few different types of animals: ")

names_list = names.split()
foods_list = foods.split()
places_list = places.split()
animals_list = animals.split()

names_list_length = len(names_list)
foods_list_length = len(foods_list)
places_list_length = len(places_list)
animals_list_length = len(animals_list)

random_names_index = random.randint(0, names_list_length -1)
random_foods_index = random.randint(0, foods_list_length -1)
random_places_index = random.randint(0, places_list_length -1)
random_animals_index = random.randint(0, animals_list_length -1)

random_name = names_list[random_names_index]
random_place = places_list[random_places_index]
random_food = foods_list[random_foods_index]
random_animal = animals_list[random_animals_index]



print("\nOk, thanks. Here's your story: \n")
print(f"Once upon a time in {random_place} there was a person named {random_name}.")
print(f"They had a pet {random_animal} who liked to eat {random_food}.")
print(f"They were best friends and happily lived together forever eating {random_food}. The end.")

# print("\nOk, thanks. Here's your story: \n")
# print(f"Once upon a time in {places_list[random_places_index]} there was a person named {names_list[random_names_index]}.")
# print(f"They had a pet {animals_list[random_animals_index]} who liked to eat {foods_list[random_foods_index]}.")
# print(f"They were best friends and happily lived together forever eating {foods_list[random_foods_index]}. The end.")
