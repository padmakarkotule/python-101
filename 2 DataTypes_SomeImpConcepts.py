'''
In python everything is object even basic data types like int, float, string

Variables are named locations which are used to store references to the object stored
in memory. The names we choose for variables and functions are commonly known as
Identifiers. In python Identifiers must obey the following rules.

-All identifiers must start with letter or underscore ( _ ) , you can’t use digits.
-For e.g my_var  is valid identifier while 1digit  is not.
-Identifiers can contain letters, digits and underscores ( _  ).
-They can be of any length.
-Identifier can’t be a keyword (keywords are reserved words that Python uses for special
purpose).Following are Keywords in python 3.



Data types: classification On different parameters
[1]
Atomic      :Boolean, Integer ,Float, String
container   : Tuple, List, Dictionary, Set
[2]
sequential                      : String, Tuple, List
associative                     : Dictionary
not sequential, not associative : Set
[3]
Immutable   : Boolean, Integer ,Float, String, Tuple
Mutable     : List, Dictionary, Set

'''

S1 = "Hello"
s2 = "World"
s3 = "Hello'World"
# for giving path
s4 = "C:\new folder)"
print(s4)
s5 = r"C:\new folder"  # \n  not act as a new line
print(s5)

# convert  to string
list1 = [1, 2, 3, 4]
s6 = str(list1)  # list to String
s7 = str(100)  # num to string
type(s6)
type(s7)

"""
Datatype conversion

Data type conversion is also known as Type casting.
"""
# Converting int to float
# To convert int  to float  you need to use float() function.
print("------------------")
i = 10
print(float(i))

print("------------------")
# Converting float to int
# To convert float  to int  you need to use int() function.

f = 14.66
print(int(f))

print("------------------")
# Converting string to int
# You can also use int()  to convert string  to int

s = "123"
print(int(s))
# Note: If string contains non numeric character then int()  will throw ValueError.
print("------------------")
# Converting number to string
# To convert number  to string  you need to use str()  function.

i = 100
str(i)

f = 1.3
print(str(f))
print("------------------")
# Rounding numbers
# To round numbers you need to use round()  function.

#Syntax: round(number[, ndigits])

i = 23.97312
print(round(i))

i = 23.97312
print(round(i, 2))

print("------------------")


for c in s6:  # String is an iterable
    print(c)

# Range Function

l1 = [1, 2, 3]
# for loop version 1
for i in l1:
    print(i)

# for loop version 2
for i in range(len(l1)):
    print(l1[1])

# Diff Between for loop v1 and v2

# for loop version 1
for i in l1:
    i = i + 3
print(l1)  # does not change

# for loop version 2
for i in range(len(l1)):
    l1[i] = l1[i] + 3
print(l1)  # Change

# Break statement : to exit out of a loop when an external
# condition is triggered.
number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        break  # break here
    print('Number is ' + str(number))

# continue: to skip over the part of a loop where an external
# condition is triggered.

number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        continue  # continue here
    print('Number is ' + str(number))

# Pass : When an external condition is triggered, the pass
# statement allows you to handle the condition without the
# loop being impacted in any way.

number = 0
for number in range(10):
    number = number + 1
    if number == 5:
        pass  # pass here
    print('Number is ' + str(number))

# The pass statement tells the program to disregard that
# condition and continue to run the program as usual.

# Slicing of String
s = "This is Salman khan"
""""
+ve indexing start from 0
-ve indexing start from -1"""

print(s[8:15])
print(s[-11:-4])
print(s[1:15:3])


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

