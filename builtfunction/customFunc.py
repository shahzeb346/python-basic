
def input_Name():
    name = input("enter your name")
    print(name)
input_Name()

# print age and name in custom function

name = input("please enter your name")
age = input("How old are you")
def name_and_age(name: str, age: int):
    print("Name = ", name)
    print("Age = ", age)

name_and_age(name,age)
name_and_age(age="22", name="usman")

def Name_And_Age(age: int, name: str = "hassan"):
    print("Name = ", name)
    print("Age = ", age)

Name_And_Age(age="44")


# Lambda function

def square(x:int):
    return x*x
print(square(5))

numbers = [1,2,3,4,5,6]
square = map(lambda x:x * 2, numbers)
print(list(square))

# power rule
number = [2,4,6,8,10]
square = map(lambda x:x ** 2, number)
print(list(square))