"""
Branching and looping

"""
print('-' * 80)
"""print string in iterable"""
print("print string in iterable")
list1 = [1, 2, 3, 4]
s6 = str(list1)  # list to String
for c in s6:  # String is an iterable
    print(c)
print('-' * 80)

# Range Function
print("For loop using range function - for loop version 1")
L1 = [1, 2, 3]
# for loop version 1
for x in L1:
    print(x)
print('-' * 80)
# for loop version 2
print("for loop version 2")
for i in range(len(L1)):
    print(L1[i])

print('-' * 80)
# Diff Between for loop v1 and v2 and decide when to use which method.
# for loop version 1
L = [True, 10, 3.14,"Hello"]
print ("----for loop version1 extended -- printing object from list obj.")
for x in L:
    print(x, type(x))
print ("----for loop version1 extended -- using index.")
for i in range(len(L)):
    #i = i + 3
    print(L[i], type(L[i]))
print(L)  # does not change

# for loop version 2
print ("for loop version2 extended")
for i in range(len(L1)):
    L1[i] = L1[i] + 3
print(L1)  # Change
print('-' * 80)

# for loop for Set
print("For loop for Set")
S = {10,20,30,40}
help = """
for i in range(len(S)):
    print(S[i])
This will not work and it will show error as,
For loop for Set
Traceback (most recent call last):
  File "02_2_Branching_and_loops.py", line 45, in <module>
    print(S[i])
TypeError: 'set' object is not subscriptable

To print index in Set, use element option while using for loop
e.g.
for element in S:
    print(element)
"""
print(help)
print("To print index in Set, use element option while using for loop")

for element in S:
    print(element)
print(" Out put may not be sequentional because Set obj. is not sequentional container")
print('-' * 80)

# for loop version - version1
print ("============ for loop version1 ========")
print("More e.g. for version1")
L1 = [10,20,30,40,50]
for x in L1:
    print("---------id(address in memory of L1 = ", id(L1), "---------")
    print("Value =",x, "Type =", type(x), "and id (address in memory)=", id(x))

print ("============ for loop version2 ========")
for i in range(len(L1)) :
    print("---------id(address in memory of L1 = ", id(L1), "---------")
    print("Value =",L1[i], "Type =", type(L1[i]), "and id (address in memory)=", id(L1[i]))
print('-' * 80)

# If you have sequentional container object and do not want update values then use
# for loop version 1.
L = [10,20,30,40,50]
print("______ IMP - version1 - (Useful when to use ver.1 and ver.2 of for loop) ______")
for x in L:
    #print("Not updating list values - ",x, type(x), id(x))
    #print ("adding +5 in list object, it will not get updated values")
    print(" Before - type and id of", x, "=", type(x), ',', id(x))
    x = x + 5
    print(" After - type and id of ",x, "=", type(x), ',', id(x))
print("Printing L values after adding +5 in for loop using ver.1 = \n", L, "\nIt doesn't changed")

print("______ IMP - version2 - (Useful when to use ver.1 and ver.2 of for loop) ______")
for x in range(len(L)):
    #print("Updating list values - ", x, type(x), id(x))
    #print("adding +5 in list object, it will updated values")
    print(" Before - type and id of", x, "=", type(x), ',', id(x))
    L[x] = L[x] + 5
    print(" After - type and id of",x, "=", type(x), ',', id(x))
print("Printing L values after adding +5 in for loop using ver.2 = \n", L, "\nIt changed", )

# While loop examples
print('=' * 30, "Example of While loop", '=' * 30)
i = 0
while i < 10:
    i = i+1
    print("In while loop", i)
print(
"""
You can do whatever you want using for loop but there are some cases where you have to use while loop.
E.g. You want to print “Hello” work continues, then it may not be 
possible using for loop because there you have to give range as its inerrable 
object but using while it possible e.g.
While TRUE:
Print ("Hello")

""")

print('=' * 30, "Example of Break, Continue, pass in for loop", '=' * 30)
# Break statement : to exit out of a loop when an external
# condition is triggered.

print("Example of break statement")
number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        break  # break here
    print('Example of Break - Number is ' + str(number))
print('-' * 80)

# continue: to skip over the part of a loop where an external
# condition is triggered.
print("Example of continue statement")
number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        continue  # continue here
    print('Example of Continue - Number is ' + str(number))
print('-' * 80)

# Pass : When an external condition is triggered, the pass
# statement allows you to handle the condition without the
# loop being impacted in any way.
print("Example of pass statement")
number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        pass  # pass here
    print('Example of pass statment - Number is ' + str(number))

# The pass statement tells the program to disregard that
# condition and continue to run the program as usual.
print('-' * 80)

print("Example of break using for loop - using search string and once match use break")
L = [10,20,30,40,50]
se = 20
for i in range(len(L)):
    if L[i] == se:
        print("String matches, using break statement and quit the program")
        break
print('-' * 80)
print(" -- for else example --")
for i in range(len(L)):
    if L[i] == se:
        print("String matches, using break statement and quit the program - ", L[i])
        print("- Element found - for else example - ")
        break
else:
    print("Element not found")



print('-' * 80)

"""
Questions:
Q--What are the supported data types in Python?
Q--How to convert 13.2345245 to 13.234?
Q--What is pass in python?
Q--What is the output of print str * 2 if str = 'Hello World!'?
Q--What is the output of print str[2:] if str = 'Hello World!'?
q--What are the two versions of for loop?
Q--What are negative indexes?
"""

