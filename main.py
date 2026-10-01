# python basic
name: str= "pakistan"
print(name)
print(type(name))
print(id(name))

# integer or number
age: int = 12
print(age)
print(type(age))

# decimal
pi: float= 3.14
print(pi)
print(type(pi))

# boolean
bool: bool= True
print(bool)
print(type(bool))


# operator
a: int =10
b: int =20
# addition
sum= a+b
print(sum)
# subtraction
sub = a-b
print(sub)

# # multiplication
mul = a * b
print(mul)

# # division
divi = a/b
print(divi)

# # floor division
floordivi = a//b
print(floordivi)

# # modulas
modulas = a%b
print(modulas)

# # power
pow = a**b
print(pow)

# Assingment operator
x: int = 10
x+=2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 3
print(x)
x //= 2
print(x)
x %= 2
print(x)
x **= 3
print(x)

#  comparison operator
d = int(input("enter value for d: "))
e = int(input("enter value for e: "))
print("are they equal to ", d == e)
print("are they equal to ", d != e)
print("is d greater than e ", d > e)
print("is d less than e ", d > e)

print("Is d greater than or equal to ", d >= e)
print("Is d less than or equal to ", d <= e)

#  Logical operator and or not
f = int(input("enter the vlaue of f : "))
g = int(input("enter the vlaue of g : "))
# and operator both condition will be true
print("is f less than g and f is equal to g", f<g and f == g)
#  one condition must be true
print("is f less than g or f is equal to g", f<g or f == g)

#  identity operator
# is
# is not
# """
h = 5
i = 6
j = 5

print(h is i)
print(h is j)
print( h is not i)


n = 5
o = 6
p = 7
q = 8

# # * and / have higher precedence than + and -
print(n + o * p)  # 47 (5 + 6 * 7)
print(n + o * p / q)  # 10.25 (5 + 6 * 7 / 8)
print((n + o) * p / q)  # 9.625 (5 + 6) * 7 / 8)









