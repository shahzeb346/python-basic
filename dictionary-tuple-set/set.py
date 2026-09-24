# a set is a collection of an unordered unique elememnts and set is mutable
my_set = {1,2,3,"orange","mango","peach"}
print(my_set)
# adding an elelment
my_set.add(4) 
print(my_set)

# removing and element
my_set.remove(4)
print(my_set)

# no guarente of element order
color = {"red","green","blue","white"}
print(color)
# check an element is exist or not
check =  "green" in color
print(check)

# check the set length
length = len(color)
print(length)

# union of two set
seta = {1,2,3}
setb = {3,4,5}

union = seta | setb
print(seta.union(setb))
print(union)

# intersection
print(seta.intersection(setb))

# difference of a set
print(seta.difference(setb))
