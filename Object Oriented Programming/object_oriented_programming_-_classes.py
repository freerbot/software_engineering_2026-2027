# This program includes a Dog class that can be used to create Dog objects.
# It's very limited in what it can do, though. We'll improve it soon.
#
class Dog: #this creates a class called Dog
    name = "Kenny" #and these are attributes of that class
    breed = "chihuahua"

my_dog = Dog() #this INSTANTIATES an object called my_dog using the Dog class


print(f"My dog is {my_dog.name} and it is a {my_dog.breed}.")

#
# if my_dog.breed == "chihuahua":
#     print("And he's pretty small.")


#####################################################################################



### This version uses a CONSTRUCTOR to help INSTANTIATE an object based on the class.
### Instantiate just means "create". When you INSTANTIATE an object, you are creating
### an INSTANCE of the class.
### This is better because it allows you to assign values to the attributes when
### you instantiate the object. This can be done by letting the user input() information
### about the object, for example.
#
# class Dog:
#     def __init__(self, name, breed): # this def __init__() section is a CONSTRUCTOR
#         self.name = name
#         self.breed = breed
#
# name = input("What's your dog's name? ")
# breed = input("What's your dog's breed? ")
#
# my_dog = Dog(name, breed)
#
# name = input("What's your dog's name? ")
# breed = input("What's your dog's breed? ")
# my_other_dog = Dog(name, breed)
# print(f"Your dog is {my_dog.name} and it is a {my_dog.breed}.")
# print(f"Your dog is {my_other_dog.name} and it is a {my_other_dog.breed}.")
##################################################################################


### This version includes a method. When that method is called, it will print the word "woof".
#
# class Dog:
#     def __init__(self, name, breed): # this def __init__() section is a constructor
#         self.name = name
#         self.breed = breed
#
#     def bark(self): # this is a method, which is just a function that's part of an object.
#         print("I'm barking! Woof!")
#
#     def eat(self, food_type):
#         if food_type == "pizza":
#             print("Pizza, my favourite food! Thanks!")
#         elif food_type == "dog food":
#             print("Ugh, dog food again. Disappointing!")
#         else:
#             print("I don't even know what this food is. Yuck.")
#
#     def pee(self):
#         print("I'm peeing on the floor, sorry!")
#
# name = input("What's your dog's name? ")
# breed = input("What's your dog's breed? ")
#
# my_dog = Dog(name, breed)
#
# print(f"Your dog is {my_dog.name} and it is a {my_dog.breed}.")
# my_dog.bark()
# my_dog.eat("pizza")
# my_dog.pee()
