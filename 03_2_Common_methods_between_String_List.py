"""
Examples of Common methods between String and List.
"""
print('-' * 80)
# Example of * + method
print("\tExample of common methods +, *")

print("Exampel of list combincation")
L = [10,20,30,40,50]
L1 = [10,20,30,40,50]
L2 = [60,70,80]
print("Print L1 + L2 - ", L + L1)
print("Print L1 + L2 - ", L1 + L2)
print("Example of multiplication in using list - \n", L1 *10)
print('-' * 80)

# e.g. type, id, len
print("\tExample of common methods print, type, id, len")
L = [10,20,30,40,50]
L1 = [10,20,30,40,50]
L2 = [60,70,80]
print("Common method print -", L)
print("Common method type -", type(L))
print("Common method id -", id(L))
print("Common method length len() -", len(L))
print("Common method len * 2 -", len(L * 2))
print('-' * 80)

# e.g. for
print("\tExample of common methods for loop")
L = [10,20,30,40,50]
for x in L:
    print("Using for loop - version1 - ", x)
print(" -- ")
for i in range(len(L)):
    print("Using for loop - version2 - ", L[i])
    L[i] = L[i] + 5
print("After updating values in list - ", L)
print('-' * 80)

# e.g. reverse list
print("\tExample of common methods reverse")
L = [10,20,30,40,50]
print("Normal list - ", L)
print("Reverse list - ", L[::-1])
print('-' * 80)

# e.g. reverse list
print("\tExample of common methods reverse")
L = [10,20,30,40,50]
print("Normal list - ", L)
print("Reverse list - ", L[::-1])
print('-' * 80)

# e.g. count method for list
print("\tExample of common methods count for list")
L = [10,20,30,40,50, 10, 10, 10]
print("Normal list - ", L)
print("counts in list for search number 10 - ", L.count(10))
print('-' * 80)

# e.g. count method for list
print("\tExample of common methods index for list")
L = [10,20,30,40,50, 10, 10, 10]
print("Normal list - ", L)
print("index in list for search number 10 from index 1- ", L.index(10, 1))
print("find list is not supported by list")
print('-' * 80)