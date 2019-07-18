# Assignment
# Write nested function and print its locals
from typing import Any, Callable, Union


def fn():
    n1 = 10
    n2 = [10, 20, 30]
    n3 = 3.14
    n4 = True
    n5 = (1, 2, 3)

    def g1():
        print(n1, n3)
        print("g1: Locals - ", locals())

    def g2():
        print(n2, n4)
        print("g2: Locals - ", locals())

    def g3():
        print(n1, n3, n5)
        print("g3: Locals - ", locals())

    def g4():
        print(n1, n2, n3, n4, n5)
        print("g4: Locals - ", locals())

    print("fn: Locals - ", locals())
    return g1, g2, g3, g4


def main():
    L_F = fn()
    for element in L_F:
        print("Type: ", type(element))
        element()
    # for i in range(len(L_F)):    # anather aproch
    #     L_F[i]()


main()

print("--------------------1---------------")

""""
Dynamically creating variable/method/function names:
Built the the function at runtime.
This is called Higher order function.

def make_func(value_to_print):
     def _function():
         print value_to_print
     return _function

f1 = make_func(1)
f1()
"""


def f(n):
    def g(x):
        return x ** n

    return g


my_sqrt = f(2)
my_cube = f(3)

k = 5
kth_power_function = f(k)

print("my_sqrt : ", my_sqrt(10))  # equal to  -> f(2)(10)
print("my_cube : ", my_cube(10))  # equal to  -> f(3)(10)
print("kth_power_function : ", kth_power_function(10))

print("f(6)(2):", f(6)(2))
print("-----------------------2------------------")

""""
lambda functions: 
In Python, anonymous function is a function that is defined without a name.
While normal functions are defined using the def keyword, in Python anonymous functions 
are defined using the lambda keyword.
Hence, anonymous functions are also called lambda functions.
"""
# ex1
double = lambda x: x * 2
print(double(5))
# ex2
s = lambda x, y: x + y
print(s(2, 3))

# ex : Higher order function using lambda function
print((lambda n: (lambda x: x ** n))(2)(3))

"""
List comprehension provides a concise way to create list. It consists of square brackets
containing expression followed by for clause then zero or more for or if clauses.
"""
# You can do with list comprehension
print("-------List comprehension=----------")
list1 = [x for x in range(10)]
print("list1 :", list1)

list2 = [x + 1 for x in range(10)]
print("list2 :", list2)

set1 = set([x for x in "Hello World"])
print("Set :", set1)

list3 = [x for x in range(10) if x % 2 == 0]
print("list3 :", list3)

list4 = [x * 2 for x in range(10) if x % 2 == 0]
print("list4 :", list4)

list5 = [(x, y) for x in range(3) for y in range(5, 8)]
print("list5 :", list5)

list51 = [x + y for x in range(3) for y in range(5, 8)]
print(list51)

list6 = [(x, y, z) for x in range(5) if x % 2 == 0 for y in range(5, 7) for z in range(6, 9) if z % 2 == 0]
print("list6 :")
for i in list6:
    print(i)

list7 = [(x, y, z) for x in range(100) if x % 2 == 0 for y in range(150) if y % 4 == 0 for z in range(200)]
print(len(list7))

list8 = [x ** 2 + y ** 2 for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 == 1]
print(list8)



"""
Q--What is anonymous/lambda function?
Q--What mean bt higher order function?
Q--What is list comprehension?
Q--What is the difference between Xrange and range?
Q--Create list of possible combination when dies through 3 times.
Q--Write a higher order function to calculate power?
Q--
"""