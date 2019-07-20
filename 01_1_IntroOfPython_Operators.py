""""IDLE is Python’s Integrated Development and Learning Environment.
Module -> Class -> Function -> Statements
type() -> to check type of an object.
Pythons keep the type info with object. It is not associated with object name.

Python is   strongly type-
            dynamic typing-type checking is performed as program run
            Inferred typing- ex:num=10
"""
import sys

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
print ("multiplications example - 2 * 10 =", a*b)

# Update
number_of_books = 100
number_of_books += number_of_books+1
print(number_of_books)

# Example of print single instances
x = print("Hollo")
y = print ("Howdy?")

print("Single instance, print return type of x pointing to same object", type(x), "id = ", id(x))
print("Single instance, print return type of y pointing to same object", type(y), "id = ", id(y))

print('-' * 80)
# use of .is operator. is operator points to same id where == operator points to separate objects.
s1 = "Hello"
s2 = "Howdy?"
print("Using == operator=", s1==s2, ", and id's are = ", hex(id(s1)), hex(id(s2)))
print ("using is operator =", s1 is s2, ", and id's are = ", hex(id(s1)), hex(id(s2)))

L1 = [10,20,30]
L2 = [10,20,30]
L1 == L2
print("Using == operator=", L1==L2, ", and id's are = ", hex(id(L1)), hex(id(L2)), "True Because values are same")
L1 is L2
print ("using is operator =", L1 is L2, ", and id's are = ", hex(id(L1)), hex(id(L2)), "False because id's are diff.")
print('-' * 80)


# Verify Immutable object (Using string)
s1 = "Hello"
print("Verify String object is Immutable - Before using upper method = ",s1, "id=", id(s1.upper()) )
s1.upper()
print("Verify String object is Immutable - using upper method = ",s1.upper(), "id=", id(s1.upper()))
print("Verify String object is Immutable - After using upper method = ",s1, "id=", id(s1.upper()) )
print('-' * 80)

# Shallow copy example, using list mutable
print("\n", "-----------This example is for shallow copy", "-------------------")
L1 = [10, 20, 30]
L2 = L1
print("Shallow copy example, print L1 & L2, it will be same = ", L2, L1, hex (id(L2)), hex(id(L1)))
L1 is L2
print("Shallow copy example, L1 is L2 = ", L1 is L2, "It's without using is operator", hex(id(L2)), hex(id(L1)))

#After updating list e.g. L1.update then L1 list will update but output of L2 also change and
# it will be similar to L1
print("Before L1 append value of L2 is = ", L2)
L1.append(40)
print("Appended L1 and checking value of L2, L2 also change e.g. =", L2)

# use clone (copy) method if you want to pass by values instead of reference. E.g.
print("\n", "-----------This example is for deep copy", "-------------------")
L1 = [10,20,30,40]
def f (L):
    L.append (1000)
f(L1)
print("Value of L1 after pass by ref. is =", L1)

#Using clone / copy method
L5 = [10,20,30]
print ("Values before clone/copy, this e.g. is for pass by value method=", L5)
f(L5.copy())
print ("Values after clone/copy, this e.g. is for pass by value method=", L5)

f(L5)
print ("This e.g. is for pass by reference method=", L5)
print('-' * 80)

# get Object details, memory address using id, type of obj, value in obj and how many
# variables pointing to that variable (reference count pointed to obj e.g.
# using sys.getrefcount method (import sys) require.
a = 10
#print(sys.getrefcount(a))
print("Object information of obj 10 (variable a) are, \n", "Memory address (id)=", id(a), "\n value in obj=", a)
print("type of obj=", type(a),"and","\n Number of variables pointing to obj 10, i.e. variable a=",sys.getrefcount(a))
# add one more variable and point to a e.g. b = a and again check ref. count
c = 10
#print(sys.getrefcount(a))
print("Rechecking ref. count after assiging one more variable to same obj, =", sys.getrefcount(a))
d = 10
#print(sys.getrefcount(a))
print("Rechecking ref. count after assiging one more variable to same obj, =", sys.getrefcount(a))
del a
print("Rechecking ref. count after deleting var a for obj b, =", sys.getrefcount(b))
# More example using List
print("\n")
L1 = [10,20,30]
print("Values of L1=", L1, "and" " Type of L1 is = ", type(L1))
print(" --- Id of L1= ", hex(id(L1)))
print(" --- Id of L1[0]= ", hex(id(L1[0])))
print(" --- Id of L1[1]= ", hex(id(L1[1])))
print(" --- Id of L1[2]= ", hex(id(L1[2])))
print ("Copy L1 values to L2")
L2 = L1.copy()
print ("Check L1 == L2", L1 == L2)
print ("Check L1 is L2", L1 is L2)
print ("\n Get all address of L2 as it's copied from L1")
print(" --- Id of L2= ", hex(id(L2)))
print(" --- Id of L2[0]= ", hex(id(L2[0])))
print(" --- Id of L2[1]= ", hex(id(L2[1])))
print(" --- Id of L2[2]= ", hex(id(L2[2])))

print('-' * 80)



""""
not -> unary prefix operator
or -> binary infix operator
and -> binary infix operator
"""

b = True
c = False
print(not b)
print(b and c)
print(b or c)

""""
v1 == v2 -> It checks the actual value of Objects
v1 is v2 -> It checks the reference/address -> id(v1)==id(v2)
"""
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



