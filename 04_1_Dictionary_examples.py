"""
Examples - Dictionary data type.
"""
print('-' * 80)
# Example of dict
print("\tExample - of Dictionary data type ")
D = {True:"Hello", 10:2.145, 3.14:[10,20,30], (1,2):{10,20}}
print('-' * 80)

# Get data type, id etc.
print("Get the data type of object D{}, it's id and len")
print("Data type of D{} is -", type(D), "its id", id(D), "and len -", len(D))


print("Dict. Values are, - for key True -", D[True], " for key 10 -", D[10], "for key 3.14-",D[3.14],
      "for key (1,2)", D[(1,2)])
print('-' * 80)

# Example of dict
print("\tExample of Dictionary, get values using for loop ")
print("""
for x in D:
    print(x)

    above method only print keys. (This may be python 2 specific approach).
    In python 3 need to explicity mention keys to get values. so we need to use for loop as,

# First way to get values
for x in D.keys():
    print("For key ", x, "Value is - ", D[x])

#2nd way to get only values.
for x in D.values():
    print("Print only values i.e. - ", x,"and it's type is -", type(x) )

#and 3rd way to get values using items.
Dict. stores data in elements, and within element key:value present.
E.g. first item will be True:Hello   

rs = D.items()
for x in rs:
    print("Vales in rs i.e. D.items() are - ", x)
    print("for each item, it will return tuple, and first part in tuple is key and second is value")

for x in D.items():
    print("Item[0]", x[0], "Item1", x[1])   


""")
for x in D:
    print(x)

for x in D.keys():
    print("For key - ", x, "it's value is - ", D[x], "and type of key is - ", type(x))

for x in D.values():
    print("Print only values i.e. - ", x,"and it's type is -", type(x) )

rs = D.items()
for x in rs:
    print("Vales in rs i.e. D.items() are - ", x)
    print("for each item, it will return tuple, and first part in tuple is key and second is value")

for x in D.items():
    print("Item[0]", x[0], "Item1", x[1])
print('-' * 80)

#
print("\tExample of Dictionary, get values using get method")
print("""
Dict.get method is very popular becuase it will return None when there is no key and user
is tried to access it. 

for x in D.keys():
    print("Using get method", D.get(x))
""")

for x in D.keys():
    print("Using get method", D.get(x))

rs = D.get(100)
print("Trying to access unknown key e.g. 100, which is not available in D \n Return value of rs -",rs, type(rs))
print("It should return None, for above statment")
print('-' * 80)

#
print("\tExample of update, add, delete items in Dictionary")
print("---Update value of key ---")
print("Before update value of key True - ", D[True])
D[True] = -1
print("After update value of key True", D[True])

print("---Add new key. value in Dict ---")
print("Add new key pair by simply adding, key value, e.g. D[1000] = Python")
D[1000] = "Python"
print("Print Dictionary and check newly added key, value e.g. D[1000] = Python - \n", D)

print("---Delete key,value ---")
print("Delete key,value using del method e.g. del (D[(1,2)]")
print("It will not only delete key, but also delete values")
print("Before delete key,values in D are, \n", D)
del (D[(1,2)])
print("After delete key,values in D are, \n", D)
print('-' * 80)

# Update of multiple dict.
print("\tExample of multiple dict. update")
D1 = {10:1,20:2,30:3,40:4}
D2 = {30:300,40:400,50:500,60:600}

print("""
When resultant dictionay update, values of first arg. will be getting updated.
e.g. D1.update(D2) then all values of D1 keys will be update by D2.keys which are the 
common between two sets.
e.g.
D1 = {10:1,20:2,30:3,40:4}
D2 = {30:300,40:400,50:500,60:600}

print("Before update D1 -\n", D1, "and D2 \n", D2)
D1.update(D2)
print("After D1.update(D2), result of D1 are -", D1)

""")
print("Before update D1 -\n", D1, "and D2 \n", D2)
D1.update(D2)
print("After D1.update(D2), result of D1 are -\n", D1)

D1 = {10:1,20:2,30:3,40:4}
D2 = {30:300,40:400,50:500,60:600}
print("Before update D1 -\n", D1, "and D2 \n", D2)
D2.update(D1)
print("After D2.update(D1), result of D1 are -\n", D2)
print('-' * 80)

#
print("\tExample of creating dictionary with different ways")

D = dict(name="abc", city="xyz", role=10)
print("""
When you use this method
dict(name="abc", city="xyz", role=10)
then make sure key name i.e. first variable name is valid supprted name.
""")
print("After create new dict, key,values are -\n",D)

print("""
dict.formekeys method will be used when you don't about key and it's values.
You can just create array of keys and assign None values.
E.g.
L = [10,20,30,40,50]
D = dict.fromkeys(L,None)

IMP - In this scenarios, all keys pointing to same value object i.e. None
""")
L = [10,20,30,40,50]
D = dict.fromkeys(L,None)
print("After using dict.fromkeys(L.None) - \n",D)
print('-' * 80)

#
print("\tExample of creating dict. using 2 diff. list object. e.g. L1 for key and L2 for values")
K = [10,20,30,40]
V = ["a", "b", "c", "d"]

print("You can use zip method to combine L1 and L2 and result of this will be tuple")
rs = zip(K, V)
print("Check type of class, it's zip", type(zip))
print("Get tuple values using for loop")
print("\tzip is collection of tuples of n dimentions")
for x in rs:
    print(x)
print("""
Send zip result to list and then send list to dict.
e.g.
L = list (zip (K, V))
D = dict(L)
Or use in one line as,
D = dict (list(zip(K,V)))
""")
#L = list (zip (K, V))
#D = dict(L)
D = dict (list(zip(K,V)))
print("Resulted dictionary is - \n", D)
print('-' * 80)

#
print("\tExample of set default values when key not found")
D = {10:100, 20:200, 30:300 }
D.setdefault(400)
D.get(400)
print("Try to get unknown key,", D)
print("Try to get known key, e.g. D[10]", D[10])
print('-' * 80)

times = 100

