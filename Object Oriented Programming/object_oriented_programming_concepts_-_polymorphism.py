# This program is an example of POLYMORPHISM.
# Polymorphism in object-oriented coding refers to the
# ability of objects of different classes to be treated
# as objects of a common parent class. It enables METHOD
# OVERRIDING for code flexibility and reuse.
#
# In this example, there is a
# parent class for Person that has a say_hello() method
# that prints "The person grunts at you" because they
# don't have a language. There are two child classes
# (French and HongKonger) derived from that parent class.
# Each of those child classes has its own say_hello() method.
# When a child class has its own method with the same name
# as a method in the parent class, the child class's method
# is used instead of the parent class's method.
# This is called METHOD OVERRIDING.
#
#
#
# More explanation here: https://www.youtube.com/watch?v=tIWm3I_Zu7I
# or here: https://www.youtube.com/watch?v=pii3hAksya0

class Person:
    def __init__(self, name, age):
        self.name = name # takes the name argument and applies it here
        self.age = age
    def say_hello(self):
        print(f"{self.name} grunts at you")

class French(Person):
    def say_hello(self): # When a French or Hongkonger object is instantiated, its say_hello() method will override the say_hello() method from the Person class
        print(f"{self.name} is {self.age} says Bonjour")

class HongKonger(Person):
    def say_hello(self):
        print(f"{self.name} is {self.age} says 你好")

def introduce(person):
    person.say_hello()

leighton = Person("Team Rocket", 10)
steve = French("steve", 90)
katie = HongKonger("katie", 500)

introduce(leighton)
introduce(steve) # Because the objects/classes are so similar, they can be controlled using the same introduce() function.
introduce(katie)




# Although polymorphism usually involves class inheritance, you can also show
# polymorphism without class inheritance. I've made an example of that below.
# It's similar to the example above but the objects are not derived from a parent
# class. Instead, they are seperate classes with similar methods. Because they
# are so similar, they can be treated as if they were from the same parent
# class.

# class French():
#     def say_hello(self): # When a French or Hongkonger object is instantiated, its say_hello() method will override the say_hello() method from the Person class
#         print("Bonjour")
#
# class HongKonger():
#     def say_hello(self):
#         print("你好")
#
# def introduce(person):
#     person.say_hello()
#
# steve = French()
# katie = HongKonger()
#
# introduce(steve)
# introduce(katie)