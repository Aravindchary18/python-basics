# Python Classes & Built-in Functions — Quick Notes
# A class is a blueprint; an object is created from a class.
# Animal and Dog are classes, not built-in functions.
# Dog(Animal) means Dog inherits from Animal.
# self is compulsory in class methods and refers to the current object.
# __init__ is a special (magic) method, not a built-in function.
# __init__ runs automatically when an object is created.
# self.variable = value stores data inside the object.
# Methods belong to a class; functions do not.
# Built-in functions come with Python and work everywhere.
# Examples of built-in functions: print(), len(), type(), input(), isinstance()

class animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class dog(animal):
        def bark(self):
            print(self.name +"says woof"+str(self.age))
dog=dog("buddy",45)
dog.bark()