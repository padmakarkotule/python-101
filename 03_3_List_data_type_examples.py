"""
Examples of List data type.
"""
print('-' * 80)
# Example of list data type
print("\tExample of list data type")

L = []
print("Empty list", L)
L.append(10)
print("list after append value 10 -", L)
L.append("Hello")
L.append((10,20,30,40,50))
print("After appending couple of other data types - ", L)
print('-' * 80)

#
print("\tExample of list append of tuple data type")
T = (100, 200, 300)
print("Adding tuple values - using for loop")
for x in T:
    L.append(x)
print("After adding tuple value using for loop, L (list) will be - ", L)
print('-' * 80)

#
print("\tExample of list extend method e.g. tuple data type")
T = (1000, 2000, 3000)
print("Adding tuple values - using extend method")
print("Before extend values of L -", L)
L.extend(T)
print("After adding tuple value using extend method, L (list) will be - ", L)
print('-' * 80)

#
print("\tExample of list to update data")
print("Before update values in list \n", L)
L[1] = 100
print("After update values in list L[1], values Hello to 100 ", L[1])
print(L)
print('-' * 80)

#
print("\tExample of list to update data using index")
print("Before update values in list \n", L)
L[L.index(200): L.index(2000) + 1] = ["a", "b", "c", "d"]
print("After update using index")
print(L)
print('-' * 80)

#
print("\tExample of list delete")
print("Before delete values in list \n", L)
del L[L.index("a"): L.index("d") + 1]
print("After delete using index")
print(L)

print("\tExample of list delete of tuple")
print("Before delete values in list \n", L)
del L[2]
print("After delete - deleting tuple")
print(L)
print('-' * 80)

print("\tExample of list delete using empty list")
print("Before delete values in list \n", L)
L[3:4] = []
print("After delete - deleting using range with empty list")
print(L)
print('-' * 80)

print("\tExample of list delete slices")
print("Before delete values in list \n", L)
del L[2:3]
print("After delete - delete slices")
print(L)
print('-' * 80)

print("\tExample of remove data by element")
L = [10,20,30,40]
print("Before delete values in list \n", L)
L.remove(20)
print("After remove value 20 - ")
print(L)
print('-' * 80)

print("\tExample of insert data in list")
L = [10,20,30,40,50,60,70]
print("Before delete values in list \n", L)
L.insert(2, "Hello")
print("After inserting string data Hello at index 2 - ")
print(L)
print('-' * 80)

#
print("\tExample of sort data in list")
L = [234, 23, 4, 23, 345,462]
print("Before sort \n", L)
L.sort()
print("After sort - sort will happen in place in memory ")
print(L)
print('-' * 80)

print("\tExample of sort data in list")
L = [234, 23, 4, 23, 345,462]
print("Before sort \n", L)
x = L.sort()
print("After sort - inplace method, x will return None")
print(x)
print('-' * 80)

#Using sorted
print("\tExample of sorted data in list")
L = [234, 23, 4, 23, 345,462]
print("Before sort, If you don't want to change org. List then use sorted method \n", L)
for x in sorted(L):
    print (x)
print("After sorted method List wiil be same unsorted  - ", L)
print('-' * 80)

#Using sorted
print('-' * 80)
L = [234, 23, 4, 23, 345,462]
print("Before sort, If you don't want to change org. List then use sorted method \n", L)
for x in sorted(L):
    print (x)
print("After sorted method List wiil be same unsorted  - ", L)
print('-' * 80)

# example of list clear
print("\tExample of clear list")
L = [10,20,30,40,50,60,70]
print("Before clear list \n", L)
L.clear()
print("After clear list - ", L)
print('-' * 80)

# example of pop in list
print("\tExample of pop (remove last value) from list")
L = [10,20,30,40,50,60,70]
print("Before using pop (remove last value) from list \n", L)
L.pop()
print("After using pop, - ", L)
print('-' * 80)