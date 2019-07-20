"""
String data type examples

"""
print('=' * 30, "Examples of String Data Type ", '=' * 30)
print("\tExample of built-in functions/classes")
s = "Hello"
print("Printing string Hello - ", s)
print("Length of string = ", len(s))
print("Type of string Hello - ", type(s))
print("id of string Hello - ", id(s))
print('-' * 80)

print("\tExample of string concatenation")
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print("concatenation of s1 (hello) + s2 (world) - ", s3)
s = s1 + "," + s2 + "!"
print("concatenation one more e.g. - ", s)
print('-' * 80)

print("\tExample of string multiplication")
s1 = "Hello"
print("Example of string multiplication - ", s1 * 10)
print("Example of string multiplication - ", "*" * 65)
print('-' * 80)

print("\tExample of string index operator")
s1 = "Hello"
print("Index[0] = ", s1[0])
print("Index[1] = ", s1[1])
print("Index[2] = ", s1[2])
print("Index[3] = ", s1[3])
print("Index[4] = ", s1[4])

print("\tExample of string index operator using for loop")
for i in range(len(s1)):
    print("Using for loop - ", s1[i])
print('-' * 80)

# Slicing of String
print("\tExample of string slicing")
print(""" 
Python supports three types for slicing of string,
\ts[i]
\ts[i:j]
\ts[i:j:k]
+ve indexing start from 0
-ve indexing start from -1
"""
      )
print("\tExample of postive index")
s = "Hello,World"
print("Example output of positive string such as s[0:3] of string hello - ", s[0:3])
print(" -- Note -- we have to skip j e.g. 0:3 then we have to take 0,1,2")
print("Example output of entire string s[0:len(s)] of string hello - ", s[0:len(s)])
print("Example - short cut of string slice e.g. [:3], shows start from 0,  - ", s[:3])
print("Example - short cut of string slice e.g. [2:], shows start from 2 and then take till end,  - ", s[2:])
print("Example - short cut of getting entire string e.g. [:] - ", s[:])
print("Multiple e.g., s[-10:-3], s[-1], s[1:8]", s[-10:-3], s[-1], s[1:8])
#


s = "This is Salman khan"
#print("This is example of -", s[8:15])
#print("This is example of -", s[-11:-4])
#print("This is example of -", s[1:15:3])
