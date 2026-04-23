
# Parent class (sometimes called a superclass)
class ParentClass:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    #Creates a method
    def parent_method(self):
        print("This is a method in the ParentClass")

# Child class (sometimes called a subclass)
class ChildClass(ParentClass):
    def __init__(self, attribute1, attribute2, attribute3):
    # Call the constructor of the ParentClass
        super().__init__(attribute1, attribute2) #this uses the ParentClass's constructor for the first two attributes
        self.attribute3 = attribute3

    def parent_method(self):
        print("This is the parent method being called from the child object.")

    def child_method(self):
        print("This is a method in the ChildClass")

parent_object = ParentClass("first attribute", "second attribute")
child_object = ChildClass("first attribute", "second attribute", "third attribute")

parent_object.parent_method()
child_object.parent_method() #objects from the ChildClass also include the ParentClass's methods
child_object.child_method()
