
"""
Decorators allow you to inject or modify code in functions or classes.
it’s both much simpler and (as a result) much more powerful.
 
For example, suppose you’d like to do something at the entry and exit points
of a function (such as perform some kind of security, tracing, locking, etc.
– all the standard arguments for AOP)

"""


# Two dynamically computed attributes with property


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def get_square(self):
        return self._square ** 2

    def set_square(self, value):
        self._square = value

    square = property(get_square, set_square)

    def get_cube(self):
        return self._cube ** 3

    cube = property(get_cube)


def main():
    x = Powers(3, 4)
    print(x.cube)
    print(x.square)
    x.square = 5
    print(x.square)


main()

print("--------------------------------------------")
"""
Introducing __call__
Implementing the __call__ magic method in a class causes its instances to become 
callables -- in other words, those instances now behave like functions. You can 
use the built-in function callable to test if a particular object is a callable 
(callable returns True for functions, methods, and objects that have __call__).
"""


class Test(object):
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print('-' * 10)


def main():
    t = Test()
    t(1, 2, 3)
    t(a=1, b=2, c=3)
    t(4, 5, 6, d=4, e=5, f=6)


main()

"""
You can implement the __call__ magic method like any method or function. The only 
difference is that invoking it doesn't require a name, just the parentheses.

Generally, __call__ is used whenever you want to provide a simple interface that 
resembles a single function, even though the actual implementation requires some 
storing or modification of state. For example, a method that needs to record its
arguments every time it is invoked. Callable objects are also a good way to implement 
partial functions, though they're not as useful for that since Python 2.5 now 
officially supports partial function application.

"""
import time


class testClass:
    def __init__(self, fun):
        self.function = fun

    def __call__(self, *args, **kwargs):
        self.function()


def PrintFun():
    print((" I am in Printfun"))


def main():
    m = testClass(PrintFun)
    m()  # invoke the __call__ passing m as self


main()

print("------------Class Decorate function-------------")


class Logger:
    def __init__(self, ref_fun):
        self.decorated_function = ref_fun
        self.file_name = r"C:\Users\gsc-30251\Desktop\PythonPractice\Module2\test123.txt"
        log_handle = open(self.file_name, "w")
        log_handle.close()

    def __call__(self, *args, **kwargs):
        log_handle = open(self.file_name, "a")
        print("*" * 5, time.ctime(time.time()), file=log_handle)
        for i in range(len(args)):
            print("arg[", i, "]:", args[i], file=log_handle)
        for k in kwargs:
            print(k, ":", kwargs[k], file=log_handle)
        log_handle.close()
        return self.decorated_function(*args, **kwargs)


@Logger
def f1(a, b, c):
    print("I am in f1")


@Logger
def f2(a, b, c, d=10):
    print("I am in f2")


@Logger
def f3(a, b, c, d=10, e=20, f=-1):
    print("I am in f3")


def main():
    f1(1, 2, 3)
    f2(1, 54, 65, 3)
    f3(10, 20, 30, d=20, e=60, f=3)


main()

print("------------Class Decorate class function-------------")


class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("I am in call.....")
        for i in range(len(args)):
            print("arg[", i, "]:", args[i], " Type(i):", type(i))
        self.func(*args)


class inc:
    def __init__(self, n):
        self._n = n

    @Decorator
    def getn(self):
        print("Take n: ", self._n)


def main():
    c = inc(10)
    print("type(c)", type(c))
    c.getn(c)


main()

print("------------Function Decorate class function-------------")


def decorator(arg):
    print("type of ", arg, " := ", type(arg))


@decorator
class d:
    def __init__(self, n):
        self.n = n

    def getn(self):
        return self.n

    def setn(self, new_n):
        self.n = new_n


def main():
    print("type of  d: ", type(d))


main()

# Q Why d is NoneType

"""
Questions:
Q--What is function decorator
Q--What is class decorator
Q--Write a code such Two dynamically computed attributes with property\
Q--write Class Decorate to class function
Q--What are diff combination for using class and function decorator?
"""