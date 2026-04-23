
class Toy:
    def __init__(self, name):
        self.name = name

class Box:
    def __init__(self, toy):
        self.toy = toy

    def show_contents(self):
        print(f"The box contains a {self.toy.name}.")

# Create a Toy object
teddy = Toy("Teddy Bear")

# Pass the Toy object to the Box
gift_box = Box(teddy)

# Show what's inside the box
gift_box.show_contents()