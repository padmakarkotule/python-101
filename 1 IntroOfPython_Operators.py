""""IDLE is Python’s Integrated Development and Learning Environment.
Module -> Class -> Function -> Statements
type() -> to check type of an object.
Pythons keep the type info with object. It is not associated with object name.

Python is   strongly type-
            dynamic typing-type checking is performed as program run
            Inferred typing- ex:num=10
"""


print("Ready, set, GO! Ready")
# Identiry different types of data types e.g. boolean, Int, float etc.
print("Type of True:-", type(True))
print("Type of False:-", type(False))
# Assign boolean
b1 = True
b2 = False

#Operations can perform on boolens are,
# 1. Negation, 2. conjection and 3. distation

# E.g. negation
if not b1:
    print("Type of b1 is :-", type(b1))
else:
    print("Type of b1 is bool and it's True")


# Hello World
print("Hello World")

# store the value 2 in x
x = 13
print(x)
print(type(x)) # -> to check type of an object.

# use the variable x like:
print(x == x)
print(x*x)
print(x > 6)

# Float division
print("Float division - ", x / 6)
# Integer division
print("Integer division - ", x // 6)
# Reminder
print("Reminder - ", x % 6)

# Identify type of operations
print("Type of x/6 -", type(x/6))
print("Type of x//6 -", type(x//6))
# variable can also be text

book = "The Lord of the Flies"
print(book)
print ("Type of book - ", type(book))

# No requirement of power function, we can use ** e.g.
a = 2
b = 10
print("Exponential operation -, no need of power function", a**b)
print("Using power function - ",pow(a, b))

# find square root of 9
print("Get square root of 9 -", 9 ** 0.5)

# Multiplication example
print ("multipication example - 2 * 10 =", a*b)

# Update
number_of_books = 100
number_of_books += number_of_books+1
print(number_of_books)

""""
not -> unary prefix operator
or -> binary infix operator
and -> binary infix operator"""

b = True
c = False
print(not b)
print(b and c)
print(b or c)

""""
v1 == v2 -> It checks the actual value of Objects
v1 is v2 -> It checks the reference/address -> id(v1)==id(v2)"""
v1 = 3
v2 = v1
print(id(v1), id(v2))

v2 = 4
# get id
print("Get id's - ", id(v1), id(v2))
print(v1, v2)

a = print("Hello")
print("Return type of a - None = ", type(a)) # because print doesn't return any value.

s = "Hello"
print(s.upper())
print(s)    # s does not change because String is Immutable

# Deep copy and Shallow Copy Concept in terms of List
colours1 = ["red", "blue"]
colours2 = colours1
print(id(colours1), id(colours2))      # Address is same
colours2[1] = "green"
print(id(colours1), id(colours2))    # Again Address is same because List is Mutable
colours3= colours2.copy()

""""
Example of deep copy"""
print(colours2 == colours3)
print(colours2 is colours3)
print(colours1)

print(colours2)

# If statement
"""
1: if statement
2: if - else
3: if - elif - elif - else


if <bool-expr>:
    st1...
    st2...
     .
else:
    st1..
        """

"""
Questions:
Q--What is Python?
Q--What is the diff between is and ==
Q--What is the diff between 9//2 and 9/2
Q--What is the difference between deep and shallow copy?
Q--What is the purpose of ** operator?
"""



