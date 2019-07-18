""""
Inheritance :
Inheritance is a feature used in object-oriented programming; it refers to defining a new class with less or no
modification to an existing class. The new class is called derived class and from one which it inherits is called
the base. Python supports inheritance; it also supports multiple inheritances. A class can inherit attributes and
behavior methods from another class called subclass or heir class.


Python Inheritance Syntax

class DerivedClass(BaseClass):
    body_of_derived_class
"""


# Example file for working with classes
class myClass():
    def method1(self):
        print("Myclass")

    def method2(self, someString):
        print("Software Testing:" + someString)


class childClass(myClass):
    # def method1(self):
    # myClass.method1(self);
    # print "Child Class Method1"

    def method2(self):
        print("childClass method2")


def main():
    # exercise the class methods
    c2 = childClass()
    c2.method1()
    c2.method2()


if __name__ == "__main__":
    main()

print("------------------------------------")
"""
"Class" is a logical grouping of functions and data. Python class provides all the standard features of 
Object Oriented Programming.


-A derived class that override any method of its base class
-A method can call the method of a base class with the same name
-Python Classes are defined by keyword "class" itself
-Inside classes, you can define functions or methods that are part of the class
-Everything in a class is indented, just like the code in the function, loop, if statement, etc.
-The self argument in Python refers to the object itself. Self is the name preferred by convention by 
 Pythons to indicate the first parameter of instance methods in Python
-Python runtime will pass "self" value automatically when you call an instance method on in instance, 
whether you provide it deliberately or not
-In Python, a class can inherit attributes and behavior methods from another class called subclass or
heir class.
"""


class BaseClass:
    def f(self, msg):
        print("BaseClass type(self) : ", type(self))
        print("msg: ", msg)


print("Global baseClass.__dict__: ", BaseClass.__dict__)
if isinstance(BaseClass, object):
    print("Baseclass derived form class object")
print("--------------------------------")


class DerivedClass(BaseClass):
    pass


ind1 = DerivedClass()
print("Type(ind1):", type(ind1))
print("ind1.__dict__: ", ind1.__dict__)
ind1.f("This is ind1")
print("--------------------------------")

# Replace f from BaseClass
class DerivedClassTwo(BaseClass):
    def f(self, msg):
        print("Insight Derived class 2")
        print("msg*2: ", msg * 2)


ind2 = DerivedClassTwo()
ind2.f("Into Three")
print("Type(ind2):", type(ind2))
print("ind2.__dict__: ", ind2.__dict__)
print("----------------------------------")
# Extend Base Class f
class DerivedClassThree(BaseClass):
    def f(self, msg):
        print("Insight Derived class 3")
        BaseClass.f(self, msg)
        print("msg*3: ", msg * 3)


ind3 = DerivedClassThree()
ind3.f("Into Three")
print("Type(ind3):", type(ind3))
print("ind3.__dict__: ", ind3.__dict__)


"""
Questions:
Q--What is inheritance?
Q--What is class?
Q--What is the use od __dict__?

"""