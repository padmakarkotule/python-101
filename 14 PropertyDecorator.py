# property
"""
Python @property is one of the built-in decorator. The main purpose
of any decorator is to change you class methods or attributes in such
a way so that the user of your class no need to make any change in their code
"""
p = property()
print(type(p))


def f1(self):
    pass


def f2(self, value):
    pass


def f3(self, value):
    pass


def f3(self):
    pass


print(type(f1), type(f2), type(f3))
print(property.__dict__)
print("-" * 30)

"""
property() is a built-in function that creates and returns a property object. 
The signature of this function is

property(fget=None, fset=None, fdel=None, doc=None)
where, fget is function to get value of the attribute, fset is function to 
set value of the attribute, fdel is function to delete the attribute and doc
is a string (like a comment). As seen from the implementation, these function 
arguments are optional. So, a property object can simply be created as follows.

property()

A property object has three methods, getter(), setter(), and delete() to specify
fget, fset and fdel at a later point. This means, the line

temperature = property(get_temperature,set_temperature)
above can be written as
- make empty property
temperature = property()
- assign fget
temperature = temperature.getter(get_temperature)
- assign fset
temperature = temperature.setter(set_temperature)
"""


class Persons:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("fetching ....")
        return self._name

    def set_name(self, new_name):
        self._name = new_name
        print("setting....")

    def del_name(self):
        print("Removing.....")
        del self._name

    name = property(get_name, set_name, del_name, "Name Property doc")


def main():
    bob = Persons("Eshan kalay")
    print(bob.get_name())
    bob.set_name("Ishan Kalay")
    print(bob.get_name())
    bob.del_name()
    print("-" * 30)
    sue = Persons("Gaurav ")
    print(sue.get_name())
    print(Persons.name.__doc__)


main()

# Temp example:
"""\
We can see above that set_temperature() was called even when we created an object.
because:-
when an object is created, __init__() method gets called. 
This method has the line self.temperature = temperature. This assignment 
automatically called set_temperature().
"""


class Celsius:
    def __init__(self, temp=0):
        self.set_temp(temp)

    def to_fahrenheit(self):
        return (self.get_temp() * 1.8) + 32

    def get_temp(self):
        return self._temp

    def set_temp(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temp = value

    temp = property(to_fahrenheit, set_temp, get_temp, "This is Temp class")


def main():
    c1 = Celsius(32)
    print(c1.get_temp())
    print(c1.to_fahrenheit())


main()

print("---------------Person-----------------------")
""""
Using Getters and Setters
"""


class Person:
    def __init__(self, name, roll):
        self._name = name
        self._roll = roll

    def getName(self):
        print("Getting name")
        return self._name

    def setName(self, new_name):
        self._name = new_name
        print("name updated")

    def delName(self):
        del self._name

    def getRoll(self):
        print("Getting Roll")
        return self._roll

    def setRoll(self, new_roll):
        self._roll = new_roll
        print("roll updated")

    def delRoll(self):
        del self._roll

    managedX = property(getName, setName, delName)
    managedRoll = property()
    managedRoll = managedRoll.setter(setRoll)
    managedRoll = managedRoll.getter(getRoll)
    managedRoll = managedRoll.deleter(delRoll)


def main():
    p = Person("XYZ", 10)
    print("Person.__dict__: ", Person.__dict__)
    print(p.getName())
    print("p.managedX", p.managedX)
    p.managedX = [10, 20, 30]
    print("p.managedX", p.managedX)
    del p.managedX
    p.managedX = (-1, -2, -3)
    print("p.managedX", p.managedX)
    Person.managedRoll.getter(Person.getRoll)
    print(p.managedRoll)


main()

print("--------------------Emp----------------------")


class Emp:
    pass


def __init__(self, name):
    self._name = name


def get_name(self):
    print("fetching ....")
    return self._name


def set_name(self, new_name):
    self._name = new_name
    print("setting....")


def del_name(self):
    print("Removing.....")
    del self._name


def main():
    (Emp.__init__, Emp.get_name, Emp.set_name, Emp.del_name, Emp.name) = (
    __init__, get_name, set_name, del_name, property())
    Emp.name = Emp.name.getter(Emp.get_name)
    Emp.name = Emp.name.setter(Emp.set_name)
    Emp.name = Emp.name.deleter(Emp.del_name)
    e = Emp("Eshan kalay")
    print(e.name)
    e.name = "Ishan kaley"
    print(e.name)
    del e.name


main()

print("-----------------ex--Temperature---------------")


class Celsiua:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


def main():
    temperature = property()
    print("type(temperature)", type(temperature))
    print(temperature)
    temperature = temperature.getter(Celsiua.get_temperature)
    print("type(temperature)", type(temperature))
    print(temperature)
    temperature = temperature.setter(Celsiua.set_temperature)
    print("type(temperature)", type(temperature))
    print(temperature)
    Celsiua.temperature = temperature
    ct = Celsiua()
    ct.temperature = 35
    print("ct.temperature:", ct.temperature)
    fint = ct.to_fahrenheit()
    print("fint: ", fint)


main()

print("------------------------ex Natuaral no------------")


class Natural:
    def __init__(self, N):
        if type(N) != int:
            raise TypeError("Bad type")
        if N <= 0:
            raise ValueError("Bad Value")
        self._N = N

    @property
    def N(self):
        return self.N

    @N.setter
    def N(self, value):
        if type(value) != int:
            raise TypeError("Bad type")
        if value <= 0:
            raise ValueError("Bad Value")
        self.N = value

    @N.deleter
    def N(self):
        del self._N


def main():
    try:
        n = Natural(0)
    except ValueError:
        print("0 is not a natural no")

    n = Natural(10)
    try:
        n.N = -100
    except ValueError:
        print("negatives are not a natural no")


main()


"""
Questions:
Q--What is property()
Q--What are property methods?
Q--Write a property class for temperature?
"""