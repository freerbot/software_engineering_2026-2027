#
# class Toy:
#     def __init__(self, name):
#         self.name = name
#
# class Box:
#     def __init__(self, toy):
#         self.toy = toy
#
#     def show_contents(self):
#         print(f"The box contains a {self.toy.name}.")
#
# # Create a Toy object
# teddy = Toy("Teddy Bear")
#
# # Pass the Toy object to the Box
# gift_box = Box(teddy)
#
# # Show what's inside the box
# gift_box.show_contents()

'''
Expand this program so that there is a Player class.
Instantiate a player object using the Player class.
The Player class should accept two arguments:
1) a name (let's say 'Steve' in this case)
2) a box

And the Player class should have one method, show_toy() which 
says "Steve is holding a box that contains a teddy bear"

The box should contain a toy.
So the player object will contain the box and the box will contain the toy.
'''



class Toy:
    def __init__(self, name):
        self.name = name


class Box:
    def __init__(self, toy):
        self.toy = toy

    def get_toy_name(self):
        return self.toy.name

class Person:
    def __init__(self, name, box):
        self.name = name
        self.box = box

    def show_toy(self):
        print(f"{self.name} has a box containing a {self.box.get_toy_name()}.")


# Create a Toy
robot = Toy("Robot")

# Put the Toy in a Box
toy_box = Box(robot)

# Give the Box to a Person
alice = Person("Alice", toy_box)

# Show what's inside
alice.show_toy()








