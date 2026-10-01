# ? Create a simple class
class human:
    name= "saad"


# create the instance of this class
human_1 = human()
print(human_1.name)

# constructor  the _init_mehtod is also known for constructor
class human:
    def __init__(self):
        print("hello world")
human_2 = human()

# create a newclass
class car:
    company = "bmw",
    model= 2007,
    color= "red"

class car:
    def __init__(this, color,model):
        print(f"this car color is {color}and model is {model}")

car_1 = car("blue",2003)

# waht are attributes 
class car:
    def __init__(this, company, color, model):
        this.company = company
        this.color = color
        this.model = model
        this.wheel = 4
        print(this.company)
        print(this.color)
        print(this.model)
        


car_2 = car("ferrari","white",2026)

car_3 = car("bmw","red",2012)
print(car_3.wheel)

#  Define and Call a method of a class
class human:
    def __init__(this,name):
        this.name= name
        print(f"Hello my name is {name} and I am a Human.")

    def greet(this):
        print("this is demo human function")

human_3 = human("shahzeb")

human_3.greet()

# ? Class Methods in a Python class
class Example:
    class_variable = 10

    def __init__(self, value):
        self.instance_variable = value

    @staticmethod
    def static_method(a, b):
        # Does not access class or instance variables
        return a + b
    @classmethod
    def class_method(cls, increment):
        # Operates on class level, can access class_variable
        cls.class_variable += increment
        return cls.class_variable
    
# Using @staticmethod
print(Example.static_method(5, 3))  
# # Using @classmethod
print(Example.class_method(5))  