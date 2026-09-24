# loops in python
students = ["ahamd","muhammad","subhan","midrar","noorullah","huzaifa"]

for student in students:
    print(f"{student} is a student")

# conditional loop
for student in students:
     print(f"{student} is a student")
     if student == "subhan":
      break

# the range function in python
x= [1,2,3,4,5,7,8]
# x = range(6)
x= range(3,6)
# print(x)

for n in x:
    print(n)


# while loop in python
i = 1
j = 0
while i <= 6:
    print(i)
    i += 1

while i <= 7:
    print(i)
    if i == 3:
        break
    i += 1


