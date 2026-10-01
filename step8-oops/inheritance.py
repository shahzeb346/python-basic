# ? Inheritance in Python.
class Parent:
    def __init__(self):
        self.name = "asif"
    def eat(self):
        return "parent is eating"

class   Child(Parent):
    def play(self):
        return "child is playing"

child = Child()
print(child.name)
print(child.eat())
print(child.play())

# multi level inheritance
class Animal:
    def __init__(self, name):
         self.name = name

    def speak(self):
        return "some different sound"
# derived class inheriting from animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} is barknig"


# another class inheriting from the dog
class Puppy(Dog):
    def play(self):
        return f"{self.name} is playing"

# create an object of puppy class
puppy = Puppy("junior")
print(puppy.speak())
print(puppy.play())

# accessing the parent class using super() function
class Vehicle:
    def __init__(self):
        self.brand = "Toyota"

    def start(self):
        return "vehicle is starting"

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.model = "nissan"


car = Car()
print(car.brand)
print(car.model)
print(car.start())

# using super in multiple inheritance
class Animal():
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} dog is barking"

class Walker:
    def __init__(self):
        self.walk_style = "animal is walking on four legs"

class Dog(Animal,Walker):
    def __init__(self, name,breed):
        super().__init__(name)
        Walker.__init__(self)
        self.breed = breed

    def speak(self):
        return super().bark() + " woof"

dog = Dog("tommy","labradar")
print(dog.speak())
print(dog.walk_style)