num1 = float(input("Enter you first number"))
operator= input("enter your operator (+,-,/,*):")
num2 = float(input("Enter your second number"))


if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    if num2 == "0":
        result = "error: cannot divide by zero"
    else:
        result = num1 / num2
elif operator == "*":
    result = num1 * num2
else:
    result = "error invalid operator"
print(f"Result : {result}")