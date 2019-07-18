"""
function decorator intercept a call to a function
Class decorator intercept a class creation itself
"""
# Practice
from time import sleep


def sleep_decorator(function):
    def wrapper(*args, **kwargs):
        sleep(1)
        return function(*args, **kwargs)

    return wrapper


@sleep_decorator
def print_number(num):
    return num


print(print_number(22))

for num in range(1, 6):
    print(print_number(num))

print("--------------------------------------------")


class decorator_without_arguments(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        """
        The __call__ method is not called until the
        decorated function is called.
        """
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")


@decorator_without_arguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("After first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("After second sayHello() call")

print("-------------------------------------------")


class decorator_with_arguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")

        return wrapped_f


@decorator_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")

""""
Now the process of decoration calls the constructor and then immediately invokes 
__call__(), which can only take a single argument (the function object) and must 
return the decorated function object that replaces the original. Notice that
 __call__() is now only invoked once, during decoration, and after that the decorated 
 function that you return from __call__() is used for the actual calls.
"""
print("------Decorator Functions with Decorator Arguments------")


def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")

        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")

        return wrapped_f

    return wrap


@decorator_function_with_arguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")

print("--------------Chaining--------------")
""""
Chaining decorators:
You can stack more than one decorator on any given function.
"""

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print(hello())

print("---------------------Exception Hadling--------------------------")
"""
An exception is an error that happens during execution of a program.

Exceptions are convenient in many ways for handling errors and special conditions
in a program. When you think that you have a code which can produce an error then
you can use exception handling.

***********************
try:
    <body>
except <ExceptionType 1>:
    <handler1>
except (<ExceptionType N>):
    <handlerN>
except:
    <handlerExcept>
else:
    <process_else>
finally:
    <process_finally>
************************

    BaseException
        |
    Exception
        |
    StandardError
        |
        1- ArithmeticError----> i)ZeroDivisionError
        2- EnvironmentError---> i)IOError   ii)OSError
        3- RuntimeError 
        4- LookupError--------> i)IndexError   ii)KeyError
        5- syntaxError--------> i)IndentationError


IOError
If the file cannot be opened.

ImportError
If python cannot find the module

ValueError
Raised when a built-in operation or function receives an argument that has the
right type but an inappropriate value

KeyboardInterrupt
Raised when the user hits the interrupt key (normally Control-C or Delete)

EOFError
Raised when one of the built-in functions (input() or raw_input()) hits an
end-of-file condition (EOF) without reading any data 
"""


def f(n):
    if n == 1:
        10()
    elif n == 2:
        [10,20,30][30]
    else:
        raise ValueError("HEHE")

try:
    #f(1)
    #f(2)
    f(4)
except(TypeError, IndexError):
    print("Okay")
except ValueError as v:
    print("Wrong Parameter")
    print("Type(v): ", type(v))

print("---------------------------")

try:
    #[10, 20, 30][30]
    [10, 20, 30][0]
except IndexError:
    print("Index Error occur")
else :
    print("Index Error does not occur")
finally:
    print("This will always Executed")


"""
Questions:
Q--Can you pass the argument in decorator?
Q--Where we ca use decorator with arguments?
Q--What is chaining in decorators?
Q--In chaining which decorator will apply first?
Q--What is Exceptions?
Q--What is finally? What is the use of finally?
Q--Can you though multiple exception in one except block? How?
Q--What are the diff Erros?
Q--Syntax for exception?

"""
