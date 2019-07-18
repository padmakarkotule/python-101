"""
What are metaclasses (finally)
Metaclasses are the 'stuff' that creates classes.

You define classes in order to create objects, right?

But we learned that Python classes are objects.

Well, metaclasses are what create these objects. They are the classes' classes,
you can picture them this way:

MyClass = MetaClass()
my_object = MyClass()

You've seen that type lets you do something like this:

MyClass = type('MyClass', (), {})

It's because the function type is in fact a metaclass. type is the metaclass
Python uses to create all classes behind the scenes.

Now you wonder why the heck is it written in lowercase, and not Type?

Well, I guess it's a matter of consistency with str, the class that creates
strings objects, and int the class that creates integer objects. type is just
the class that creates class objects.

You see that by checking the __class__ attribute.

Everything, and I mean everything, is an object in Python. That includes ints,
strings, functions and classes. All of them are objects. And all of them have
been created from a class:
"""

age = 35
print(age.__class__)
name = 'bob'
print(name.__class__)


def foo(): pass


print("foo.__class__", foo.__class__)


class Bar(object): pass


b = Bar()
print(b.__class__)
# Now, what is the __class__ of any __class__ ?

print(age.__class__.__class__)
print(name.__class__.__class__)
print(foo.__class__.__class__)
print(b.__class__.__class__)

"""
So, a metaclass is just the stuff that creates class objects.

You can call it a 'class factory' if you wish.

type is the built-in metaclass Python uses, but of course, you can create your
own metaclass.

The __metaclass__ attribute
You can add a __metaclass__ attribute when you write a class:

class Foo(object):
    __metaclass__ = something...
    [...]
If you do so, Python will use the metaclass to create the class Foo.

Careful, it's tricky.

You write class Foo(object) first, but the class object Foo is not created in
memory yet.

Python will look for __metaclass__ in the class definition. If it finds it, it
will use it to create the object class Foo. If it doesn't, it will use type to
create the class.

Read that several times.

When you do:

class Foo(Bar):
    pass
Python does the following:

Is there a __metaclass__ attribute in Foo?

If yes, create in memory a class object (I said a class object, stay with me here),
with the name Foo by using what is in __metaclass__.

If Python can't find __metaclass__, it will look for a __metaclass__ at the MODULE
level, and try to do the same (but only for classes that don't inherit anything,
basically old-style classes).

Then if it can't find any __metaclass__ at all, it will use the Bar's (the first
parent) own metaclass (which might be the default type) to create the class object.

Be careful here that the __metaclass__ attribute will not be inherited, the metaclass
 of the parent (Bar.__class__) will be. If Bar used a __metaclass__ attribute that
 created Bar with type() (and not type.__new__()), the subclasses will not inherit
 that behavior.

Now the big question is, what can you put in __metaclass__ ?

The answer is: something that can create a class.

And what can create a class? type, or anything that subclasses or uses it.
"""

"""
The __new__ method
One of the most common point of confusion with both classes and metaclasses is 
the __new__ method. It has some very special conventions.

The __new__ method is the constructor (it returns the new instance) while __init__ 
is just a initializer (the instance is already created when __init__ is called).
"""


class Foobar:
    def __new__(cls):
        return super().__new__(cls)


print("------------------------------------------------------------")


class MetaOne(type):
    def __new__(meta, class_name, class_parents, class_attr):
        print("__new__:type(meta))", type(meta))
        print("__new__:type(class_name)", type(class_name))
        print("__new__:type(class_parents)", type(class_parents))
        print("__new__:type(class_attr)", type(class_attr))
        print("__new__:class_name", class_name)
        print("__new__:class_parents")
        for base_class in class_parents:
            print(base_class)
        print("__new__:class_attr")
        for attr in class_attr:
            print(attr)

        return type.__new__(meta, class_name, class_parents, class_attr)

    def __init__(Class, class_name, class_parents, class_attr):
        print("__init__:type(Class))", type(Class))
        print("__init__:type(class_name)", type(class_name))
        print("__init__:type(class_parents)", type(class_parents))
        print("__init__:type(class_attr)", type(class_attr))
        print("__init__:Class ", Class)
        print("__init__:class_name", class_name)
        print("__init__:class_parents", class_parents)
        print("__init__:class_attr", class_attr)


class T(metaclass=MetaOne):
    def __init__(self, n):
        self.n = n

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n


print(type(T))

"""
Foobar.__new__ is used to create instances of Foobar
type.__new__ is used to create the Foobar class (an instance of type in the example)

Subclasses inherit the metaclass
One advantage compared to class decorators is the fact that subclasses inherit the metaclass.

This is a consequence of the fact that Metaclass(...) returns an object which usually has 
Metaclass as the __class__.
"""


class Meta1(type):
    def __init__(Class, class_name, class_parents, class_attrs):
        Class.extra = 100


class Meta2(type):
    def __new__(meta, class_name, class_parents, class_attrs):
        class_attrs['extra'] = 1000
        return type.__new__(meta, class_name, class_parents, class_attrs)


class T1(metaclass=Meta1):
    def __init__(self, n):
        self.n = n

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n


print("------------meta 1----------------------")

print("main:T.__dict__:", T1.__dict__)
print("main:T1.Extra:", T1.extra)
print("main:T1(-1).extra:", T1(-1).extra)


class T2(metaclass=Meta2):
    def __init__(self, n):
        self.n = n

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n


print("-------------meta2-------------------")
print("main:T2.__dict__:", T2.__dict__)
print("main:T2.Extra:", T2.extra)
print("main:T2(-1).extra:", T2(-1).extra)


"""
Questions:
Q--What is Meta Classes?
Q--what is the purpose of meta classes?
Q--What is __new__ method
Q--What is the diff between __init__ And __new__ method?

"""