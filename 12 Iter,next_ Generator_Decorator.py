"""
Iterator in Python is simply an object that can be iterated upon. An object
which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods
, __iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in
 containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an
iterator from them.
"""

l = [10, 20, 30, 40, 50]

for i in l:
    print(i)

y = iter(l)
print(type(y))
for i in y:  # print element
    print(i)

for i in y:  # can not print ..eter object can be only once
    print(i)
print("--------------------------------")
# Ex 2 Next()
# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)
# iterate through it using next()
# prints 4
print(next(my_iter))
# prints 7
print(next(my_iter))
# next(obj) is same as obj.__next__()
# prints 0
print(my_iter.__next__())
# prints 3
# print(my_iter.__next__())

# This will raise error, no items left
next(my_iter)
print("---------------------------")

# using while loop
l_iter = l.__iter__()
while True:
    try:
        print(l_iter.__next__())
    except StopIteration:
        break
print("-------------------------------")

d = {"a": 1, "b": 2, "c": 3, "d": 4}

di = d.__iter__()

for i in di:
    print(i, d.__getitem__(i))

print("---using while loop-----")
dii = dict.__iter__(d)
while True:
    try:
        element = dii.__next__()
    except StopIteration:
        break
    print(element, dict.__getitem__(d, element))

print("-------Tuple Iter-------")

tup = (1, 2, 3, 4)
t = tup.__iter__()
for i in t:
    print(i)

print("---------String----------")

s = "hello"
st = s.__iter__()
while True:
    try:
        i = st.__next__()
    except StopIteration:
        break
    print(i)

print("--------Generator-----------")
"""
There is a lot of overhead in building an iterator in Python; we have to 
implement a class with __iter__() and __next__() method, keep track of 
internal states, raise StopIteration when there was no values to be returned etc.

This is both lengthy and counter intuitive. Generator comes into rescue 
in such situations.

Python generators are a simple way of creating iterators. All the overhead 
we mentioned above are automatically handled by generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) 
which we can iterate over (one value at a time).

"""


def gensequence(n):
    for i in range(n):
        yield i ** 2


rs = gensequence(10)
type(rs)
gen_iter = rs.__iter__()
while True:
    try:
        i = gen_iter.__next__()
    except StopIteration:
        break
    print(i)

"""
Differences between Generator function and a Normal function :
-Generator function contains one or more yield statement.

-When called, it returns an object (iterator) but does not start execution 
immediately.

-Methods like __iter__() and __next__() are implemented automatically.
 So we can iterate through the items using next().
 
-Once the function yields, the function is paused and the control is transferred 
 to the caller.
 
-Local variables and their states are remembered between successive calls.

-Finally, when the function terminates, StopIteration is raised automatically on 
 further calls.
"""
print("------------------------------------")


# Understanding with .. as .. : working L


class TraceBlock:
    def massage(self, msg):
        print("Running " + msg)

    def __enter__(self):
        print("Starting with block")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("exit Normally")
        else:
            print("raise an exception " + str(exc_type))
            return False  # Propogate


print("--test1--")
with TraceBlock() as action:
    action.massage("test1")
    print("Reached")

print("--test2---")
with TraceBlock() as action:
    action.massage("test2")
    # raise TypeError
    print("Not Reached")

print("---------Decorator-----------")
"""
Decorator
Functions and methods are called callable as they can be called.

In fact, any object which implements the special method __call__() is termed callable. So, in the most basic sense, a decorator is a callable that returns a callable.

Basically, a decorator takes in a function, adds some functionality and returns it
"""


def F(x):
    print("type(x)", type(x))
    print("hex(id(x))", hex(id(x)))

    def wrapper_function(n1, n2):
        ret = x(n1, n2)
        return ret

    return wrapper_function


@F
def f(n1, n2):
    rs = n1 + n2
    print(rs)


print("hex(id(f)): ", hex(id(f)))
f(10, 20)


"""
Questions:
Q--What is iterator in python?
Q--What are the Iterable objects?
Q--What are generators?
Q--What is the Differences between Generator function and a Normal function ?
Q--What is decorator?
"""