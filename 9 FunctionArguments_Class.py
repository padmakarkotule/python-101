# Passing arguments to function
def fn(a, b, c):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))


fn(10, 20, 30)

# passing multiple values to function:

def fna(*arg):
    print("arg : ", arg, " Type : ", type(arg))
    for i in arg:
        print(i, type(i))


fna(10, 20)
fna(10, 20, 30, 40)
fna(*(10, 24, 354, 565))
print("========================")


# Positional arguments should not follow keyword arguments
def fn(a, b, *arg, c):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print("arg : ", arg, " Type : ", type(arg))
    for i in arg:
        print(i, type(i))


fn(10, 20, 30, 40, 50, c=10)
print("--------------------------")
fn(10, 20, *(30, 40, 50), c=60)
print("===========================")


# Extra keyword argument type

def g(**kwargs):
    print("kwargs:", kwargs, "type: ", type(kwargs))


g(a=19, b=20, c=30)


def master(a, b, *c, d=100, e=200, f, g, **h):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))
    print(f, type(f))
    print(g, type(g))
    print(h, type(h))


master(10, 20, *(30, 40, 50), e=-10, f=200, g=70, i=(10, 20, 30), j=[110, 200, 300], k={"hello", "python", "world"})
print("-=================class==============")
# Class
"""
Instance variables are for data which is unique to every object
Class variables are for data shared between different instances of a class
A class is a blueprint for the object.
The example for class of parrot can be :

class Parrot:
    pass
    
we use class keyword to define an empty class Parrot. From class, we construct 
instances. An instance is a specific object created from a particular class.


Object
An object (instance) is an instantiation of a class. When class is defined, only 
the description for the object is defined. Therefore, no memory or storage is 
allocated.

obj = Parrot()

Here, obj is object of class Parrot.

A constructor is a class function that instantiates an object to predefined values.

It begins with a double underscore (_). It __init__() method
"""

class TestClass:
    def __init__(self, i, f, s):
        if type(i) != int:
            raise TypeError("Bad Argument")
        if type(f) != float:
            raise TypeError("Bad Argument")
        if type(s) != str:
            raise TypeError("Bad Argument")
        self.i = i
        self.f = f
        self.s = s

    def get_int(self):
        return self.i

    def set_int(self, new_int):
        self.i = new_int


def main():
    i = int(input("Enter the Integer:"))        # User input
    f = float(input("Enter the float Value:"))
    s = input("Enter Any String:")
    t = TestClass(i, f, s)          # instance
    print("type: ", type(t))
    print("hex(id(t.i)):", hex(id(t.i)), "id(i):", hex(id(i)))      #checking the id of int
    print("Before set", t.get_int())        # GETTER AND SETTER
    t.set_int(290)
    print("After set:", t.get_int())
    print("hex(id(t.i)):", hex(id(t.i)), "id(i):", hex(id(i)))      # Id after change

main()


"""
Question:
Q--What is instance variable?
Q--What is **kwargs
Q--What is *arg
Q--What is __init__?
Q--What is docstring in Python?
"""


