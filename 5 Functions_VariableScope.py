""""
What is a function in Python?
In Python, function is a group of related statements that perform a specific task.

Functions help break our program into smaller and modular chunks. As our program grows
larger and larger, functions make it more organized and manageable.

Furthermore, it avoids repetition and makes code reusable.

Syntax of Function
def function_name(parameters):
	statement(s)
Above shown is a function definition which consists of following components.

Keyword def marks the start of function header.
A function name to uniquely identify it. Function naming follows the same rules of
writing identifiers in Python.
Parameters (arguments) through which we pass values to a function. They are optional.
A colon (:) to mark the end of function header.
Optional documentation string (docstring) to describe what the function does.
One or more valid python statements that make up the function body. Statements must
have same indentation level (usually 4 spaces).
An optional return statement to return a value from the function.
"""


# Assignment: Write a program to intersect of two list, String , set


def intersect(l1, l2):  # Using for loop version 1
    rs = []
    for i in range(len(l1)):
        if l1[i] in l2:
            if not l1[i] in rs:
                rs.append(l1[i])
    return rs


def intersect1(l1, l2):  # Using for loop version 2
    rs = []
    for i in l1:
        if i in l2:
            if not i in rs:
                rs.append(i)
    return rs


def intersect2(l1, l2):
    if type(l1) != list:
        raise TypeError("Problem")
    if type(l2) != list:
        raise TypeError("Problem")


l1 = [1, 2, 3, 4, 4, 5, 5, 67, 7]
l2 = [4, 5, 6, 7, 8, 9, 0]
rs = intersect(l1, l2)
print("List rs: ", rs)

print("-----------1---------")
rs = intersect("Hello", "World")
print("String rs:", rs)
print("------------2--------")
s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {4, 5, 6, 7, 8, 9}
try:
    rs = intersect(s1, s2)  # indexing is not possible in set
    # for loop version uses indexing
except TypeError:
    print("Set can not intersect")

rs = intersect1(s1, s2)
print("Set rs:", rs)
print("------------3--------")

# how Python run code
rs = compile("num = 1000", filename="fakename", mode="single")
print(type(rs))
exec(rs)
print(num)  # not error :

print("-------4 scope-------")
""""
Scopes:
L: Local
E: Enclosing
G: Global
B: Builtin  ex print() function
(Builtin{Global( Local and Enclosing[Need to specify respect to])Global}Builtin)

st a        -> Global
def a:      
    st1
    def b:              -> Local in respect to a
        st1
        def c:          -> Enclosing in respect to a, b
            st1
            
L : local, in def spam (in code3, code 4, code5).

E : Enclosed function, any enclosing functions (if the whole example were in another def)

G : Global. Were there any x declared globally in the module (code1)?

B : Any builtin x in Python.

x will never be found in code
"""

"""
Questions:
Q--What are the diff scopes?
Q--What is function?
Q--Can you write a function without class?
Q--Write program to intersect two list
Q--What is zip()
"""