# CLASS INHERITANCE is one of the fundamental concepts of Object Oriented
# Programming. It allows you to create a PARENT CLASS (with attributes and
# methods) and then create a CHILD CLASS derived from that parent class.
# The child class can include modifications that make it somewhat different
# from the parent class, while retaining many of the attributes/methods from
# the parent class. This is useful because it prevents from needing to
# write multiple classes with (mostly) the same code over and over. Using
# inheritance, you can write one parent class then inherit most of its code
# for a child class while only making minor modifications. This avoids
# the need to re-write basically the same code multiple times.

class Animal: # this is the PARENT CLASS. It has attributes (name, has_dna) and methods (speak(), eat(), and sleep())
    def __init__(self, name):
        self.name = name # takes the name argument and applies it here
        self.has_dna = True # all animals have DNA so the has_dna attribute will automatically be added and set to 'True'

    def speak(self):
        print(f"{self.name} makes a non-specific animal sound.")

    def eat(self):
        print(f"{self.name} eats food.")

    def sleep(self):
        print(f"{self.name} takes a nap.")


class Dog(Animal): # this is a CHILD CLASS. It is derived from the Animal class. The Animal class is the parent of the Dog class.
    def __init__(self, name, furryness): # this class accepts two arguments: name and furryness. it inherits the name from the Animal class but the furryness attribute is unique to the Dog class.
        super().__init__(name) # this line allows the child class to inherit the name attribute from the parent class
        self.furryness = furryness

    def speak(self): # this is an example of METHOD OVERRIDING. the speak() method of this child class will override the speak() method of the parent class.
        print(f"{self.name} barks!") # do if you create a Dog object and use the speak() method, it will bark instead of just making a generic sound.


class Cat(Animal):
    def __init__(self, name, furryness):
        super().__init__(name)
        self.furryness = furryness

    def speak(self):
        print(f"{self.name} meows!")


# let's instantiate an object based on the Animal class..
my_animal = Animal("Steve") # this line INSTANTIATES the my_animal object. It only takes one argument, which is its name.
print(f"{my_animal.name} is a generic animal")
print(f"Does {my_animal.name} have DNA? {my_animal.has_dna}") # the has_dna attribute is automatically included in the Animal class's __init__, no need to send it as an argument when you instantiate an Animal object.
my_animal.speak() # this will output "makes a non-specific animal sound"

# and now instantiate an object based on the Dog class..
my_dog = Dog("Mr Barky", "extremely furry") # this INSTANTIATES my_dog object based on the Dog child class. it takes two arguments (name, furryness) instead of just one argument (name) like an Animal object.
print(f"{my_dog.name} is a dog, which is a type of animal.") # the name attribute is common to the parent and child classes
print(f"{my_dog.name}'s level of furryness is: {my_dog.furryness}.") # the furryness attribute is unique to the child class
print(f"Does {my_dog.name} have DNA? {my_animal.has_dna}") # and the has_dna attribute is also common to both parent and child classes
my_dog.speak() # this will output "barks"
























# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name} makes a sound.")
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def speak(self):
#         print(f"{self.name} barks!")
#
#     def eat(self):
#         print("I'm eating.")
#
#
#
# # Create instances of the classes
# animal = Animal("Generic Animal")
# dog = Dog("Buddy")
#
#
# # Call the speak method on the instances
# animal.speak()
# dog.speak()