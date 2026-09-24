# dictionary is a mutable key value pair same like object
my_dic = {"name": "shahzeb", "age":22, "city":"mohmand"}
print(my_dic)
print(my_dic["name"])

# add item
my_dic["email"] = "muhammad1122@gmail.com"
my_dic["age"] = 33
print(my_dic)

# can delete item
del my_dic["city"]
print(my_dic)

# check the item is exist 
if "name" in my_dic:
    print("name is present in distionary")
if "city" not in my_dic:
    print("city is not presnet in dictionary")

# key vlaue pair
my_value = my_dic.items()
print(my_value)

# iterate over value
for key,value in my_value:
    print(f"key: {key}, value: {value}")
    