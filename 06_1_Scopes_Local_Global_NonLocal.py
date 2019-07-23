"""
Global:a variable declared outside of the function or in global scope is known as
global variable. This means, global variable can be accessed inside or outside of
the function.

"""
print('-' * 80)
# Example
print("\t[01] - Examples of LEGB - Scope  L(local) E(eligible), G(global), and B(built-in) ")
x = 100
def f1():
    print("f1:x", x)
    def f2():
        print("f2:x",x)
        def f3():
            print("f3:x",x)
        f3()
    f2()
f1()
print('-' * 80)

# Example
print("\t[02] - Examples of LEGB - Scope  L(local) E(eligible), G(global), and B(built-in) ")
x = 100
print("g:x:",x, "hex id(x):", hex(id(x)))
def f1():
    print("f1:x", x, "hex id(x):", hex(id(x)))
    def f2():
        print("f2:x",x, "hex id(x):", hex(id(x)))
        def f3():
            print("f3:x",x, "hex id(x):", hex(id(x)))
        f3()
    f2()
f1()
print('-' * 80)

# Example
print("\t[03] - Examples of LEGB - Scope  L(local) E(eligible), G(global), and B(built-in) ")
x = 100
print("g:x:",x, "hex id(x):", hex(id(x)))
print("g:globals():",globals() )
def f1():
    print("f1:x", x, "hex id(x):", hex(id(x)))
    print("f1:locals():", locals())
    def f2():
        print("f2:x",x, "hex id(x):", hex(id(x)))
        print("f2:locals():", locals())
        def f3():
            print("f3:x",x, "hex id(x):", hex(id(x)))
            print("f3:locals():", locals())
        f3()
    f2()
f1()
print('-' * 80)

# Example
print("\t[04] - Examples of LEGB - Scope  L(local) E(eligible), G(global), and B(built-in) ")
x = 100
print("g:x:",x, "hex id(x):", hex(id(x)))
print("g:globals():",globals() )
def f1():
    x = 1000 # defining x local scope
    print("f1:x", x, "hex id(x):", hex(id(x)))
    print("f1:locals():", locals())
    def f2():
        print("f2:x",x, "hex id(x):", hex(id(x)))
        print("f2:locals():", locals())
        def f3():
            print("f3:x",x, "hex id(x):", hex(id(x)))
            print("f3:locals():", locals())
        f3()
    f2()
f1()
print('-' * 80)

# Example
print("\t[05] - Examples of LEGB - Scope  L(local) E(eligible), G(global), and B(built-in) ")
x = 100
print("g:x:",x, "hex id(x):", hex(id(x)))
print("g:globals():",globals() )
def f1():
    x = 1000 # defining x local scope
    print("f1:x", x, "hex id(x):", hex(id(x)))
    print("f1:locals():", locals())
    def f2():
        x = 10000
        print("f2:x",x, "hex id(x):", hex(id(x)))
        print("f2:locals():", locals())
        def f3():
            print("f3:x",x, "hex id(x):", hex(id(x)))
            print("f3:locals():", locals())
        f3()
    f2()
f1()
print('-' * 80)

# Example
print("\t[06] - Examples of LEGB - Scope  L(local) E(eligible), G(global), and B(built-in) ")
x = 100
print("g:x:",x, "hex id(x):", hex(id(x)))
print("g:globals():",globals() )
def f1():
    x = 1000 # defining x local scope
    print("f1:x", x, "hex id(x):", hex(id(x)))
    print("f1:locals():", locals())
    def f2():
        x = 10000
        print("f2:x",x, "hex id(x):", hex(id(x)))
        print("f2:locals():", locals())
        def f3():
            x = 100000
            print("f3:x",x, "hex id(x):", hex(id(x)))
            print("f3:locals():", locals())
        f3()
    f2()
f1()
print('-' * 80)

# Example
print("\t[07] - Examples of LEGB - Scope  L(local) E(eligible), G(global), and B(built-in) ")
print("""
Note that this program will fail with error UnboundLocalError: local variable 'x' referenced before assignment
def f1():
    print("f1:x", x, "hex id(x):", hex(id(x)))
    x = 200
    print("f1:x:", x)
It will fail at next line of def f1 and error will be
    UnboundLocalError: local variable 'x' referenced before assignment
To resolve this you have define x before use it, after immediate def f1 line.

""")
x = 100
def f1():
    #print("f1:x", x, "hex id(x):", hex(id(x)))
    x = 200
    print("f1:x:", x)
f1()
print('-' * 80)





# Code by Piush
x = 100  # global
print("x: ", hex(id(x)))
print("x is in global, it's value is -", x, "and it's id, types are -", id(x), type(x))
def f1():
    x = 1000  # Local
    print("x in def f1 (local), it's value is -", x, "and id is", hex(id(x)))

    def f2():
        print(x, " x: ", hex(id(x)))

        def f3():
            print(x, " x: ", hex(id(x)))

        f3()

    f2()


f1()

print("-----------5-----=---")

x = 100


def f1():
    #   print(x, " x: ", hex(id(x)))  # it search the variable x and it found it in
    # local but after var using
    x = 1000  # Local
    print(x, " x: ", hex(id(x)))


f1()

print("------------6---------")
# Use of global
"""
If you want to refer to a global variable in a function, you can use the global keyword 
to declare which variables are global.
if the name referenced in an expression cannot be found in local scope or scopes in the 
functions in which this function is defined, it is looked up among global variables.

However, if you assign to a new variable not declared as global in the function, it is 
implicitly declared as local, and it can overshadow any existing global variable with 
the same name.
"""

x = "Hello"
print(x, " x: ", hex(id(x)))


def fn():
    x = 100

    def fm():
        global x
        print(x, " x: ", hex(id(x)))
        x = 1000
        print(x, " x: ", hex(id(x)))

    fm()


fn()

print("------7-----------")
# Use of non local :
"""
what is nonlocal:
Nonlocal variable are used in nested function whose local scope is not defined. 
This means, the variable can be neither in the local nor the global scope.

The nonlocal statement causes the listed identifiers to refer to previously bound 
variables in the nearest enclosing scope. This is important because the default 
behavior for binding is to search the local namespace first. The statement allows 
encapsulated code to rebind variables outside of the local scope besides the global 
(module) scope."""
x = "Hello"
print(x, " x: ", hex(id(x)))


def fn():
    x = 100

    def fm():
        x = 200

        def fo():
            nonlocal x
            print(x, " x1: ", hex(id(x)))
            x = 500

        print(x, " x2: ", hex(id(x)))
        fo()
        print(x, " x3: ", hex(id(x)))

    fm()
    print(x, " x4: ", hex(id(x)))


fn()
print("------8-----------")

"""
Questions:
Q--What is global scope?
Q--What is local scope?
Q--What is nonlocal?
"""