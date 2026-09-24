# while True:
#       name: str = input("please enter your name")
#       if name.isalpha():
#             break
#       else:
#             print("please enter a valid only enter letters")
# while True:
#       age: str = input("How old are you")
#       if age.isdigit():
#             break
#       else:
#             print("please enter a valid only numbers")
# if age is not None and int(age) >= 18:
#       print(f"Hello {name} you are an adult")
# else:
#       print(f"Hello {name} you are not an adult")
      

# project 2
# string = input("Enter a string to reverse: ")
string = "welcome to the land of flower"
print("reversed string", end="")
for word in range(len(string) -1, -1, -1):
    print(string[word], end="")