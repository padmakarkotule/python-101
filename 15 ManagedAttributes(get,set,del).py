# def __getattr__(self,name):         # on undefined attribute fetch [obj.name]
# def __getattribute__(self, name):   # on all attribute fetch [obj.name]
# def __setattr__(self, name):        # on all attribute assignment [obj.name=value]
# def __delattr__(self, name):        # on all attribute deletion[del obj.name]


"""
__getattr__:
This method will allow you to “catch” references to attributes that 
don’t exist in your object. Let’s see a simple example to understand how it works:
"""


class Dummy(object):
    pass


d = Dummy()
# d.does_not_exist  # Fails with AttributeError
"""
In this example, the attribute access fails (with an AttributeError) because the 
attribute does_not_exist doesn’t exist.

But using the __getattr__ magic method, we can intercept that inexistent attribute 
lookup and do something so it doesnt fail:
"""


class Dummy(object):
    def __getattr__(self, attr):
        return attr.upper()


d = Dummy()
print(d.does_not_exist)  # 'DOES_NOT_EXIST'
print(d.what_about_this_one)  # 'WHAT_ABOUT_THIS_ONE'


# But if the attribute does exist, __getattr__ won’t be invoked:

class Dummy(object):
    def __getattr__(self, attr):
        return attr.upper()


d = Dummy()
d.value = "Python"
print(d.value)
print("----------------------------------------------")
"""
__getattribute__
__getattribute__ is similar to __getattr__, with the important difference that 
__getattribute__ will intercept EVERY attribute lookup, doesn’t matter if the 
attribute exists or not. Let me show you a simple example:
"""


class Dummy(object):
    def __getattribute__(self, attr):
        return 'YOU SEE ME?'


d = Dummy()
d.value = "Python"
print(d.value)  # "YOU SEE ME?"

"""
In that example, the d object already has an attribute value. But when we try to
access it, we don’t get the original expected value (“Python”); we’re just getting 
whatever __getattribute__ returned. It means that we’ve virtually lost the value 
attribute; it has become “unreachable”.

"""


class Dummy(object):
    def __getattribute__(self, attr):
        __dict__ = super(Dummy, self).__getattribute__('__dict__')
        if attr in __dict__:
            return super(Dummy, self).__getattribute__(attr)
        return attr.upper()


d = Dummy()
d.value = "Python"
print(d.value)  # "Python"
print(d.does_not_exist)  # "DOES_NOT_EXIST"
print("----------------------------------------------")
"""
Not recommended
__setattr__ :
 
 __setattr__ allows you to override Python's default mechanism for member assignment.
"""


class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print('set %s to %s' % (name, repr(value)))

        if name in ('a', 'b'):
            object.__setattr__(self, name, value)


t = Test()
t.c = 'z'
setattr(t, 'd', '888')

print("----------------------Person------------------------")


class Person:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, attr):
        print("Get: %s" % attr)
        if attr == 'name':
            return self._name
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        print("Set: %s" % attr)
        if attr == 'name':
            attr = '_name'
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print("Del: %s" % attr)
        if attr == 'name':
            attr = '_name'
        del self.__dict__[attr]


def main():
    p1 = Person("maifie")
    print(p1.name)

    p1.name = "Maifooz"
    print(p1.name)
    del (p1.name)


main()

"""
Questios:
Q--What is the diff between __getattribute__ and __getattr__?
Q--what are managed attributes
Q--What is __call__
"""