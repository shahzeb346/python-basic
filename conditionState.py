name: str = input("What is your name? ")
age : int = int(input("How old are you?"))

if(age) >= 18:
    print("you are an adult")
else:
    print("you are not an adult")

#  elif statement 
if(age) >= 60:
    print("you are a senior a man")
elif(age) < 60 and age >=18 and age< 25:
    print("you are an adult or young")
else:
    print("please enter a valid age")

# switch statement
day = input("Please enter your day in the menu: ")

match day.lower():
    case "monday":
        print("Today in the menu is Biryani")

    case "tuesday":
        print("Today in the menu is Haleem")

    case "wednesday":
        print("Today in the menu is Chicken")

    case "thursday":
        print("Today in the menu is Mutton")

    case "friday":
        print("Today in the menu is Vegetable")

    case "saturday":
        print("Today in the menu is Turkish")

    case "sunday":
        print("Today is an off day")

    case _:
        print("Invalid day. Please enter a valid day.")