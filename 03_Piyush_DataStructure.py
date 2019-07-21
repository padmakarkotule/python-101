""""
List:The list is a most versatile datatype available in Python which can be written
as a list of comma-separated values (items) between square brackets. Important thing
about a list is that items in a list need not be of the same type.

append(x:object)    :None	 Adds an element x to the end of the list and returns None.
count(x:object)     :int	 Returns the number of times element x appears in the list.
extend(l:list)      :None	Appends all the elements in l  to the list and returns None.
index(x: object)    :int 	Returns the index of the first occurrence of element x in the list
insert(index: int, x: object):None 	Inserts an element x at a given index.
            Note that the first element in the list has index 0 and returns None..
remove(x:object)    :None 	Removes the first occurrence of element x from the list
                    and returns None
reverse()           :None 	 Reverse the list and returns None
sort()              : None 	Sorts the elements in the list in ascending order and returns None.
pop(i)              : object 	Removes the element at the given position and returns it.
The parameter i is optional. If it is not specified, pop() removes and returns the
last element in the list.


"""


s = "Hello World"
print("Reverse the string :",s[::-1])
print("\n")

# can do:
if 'll' in s:
    print("YES")
print("\n")

print("No of occurrences : ", s.count('o'))
print("No of occurrences : ", s.count('ll'))
print("\n")

print("Index of substring in String :", s.index("ll"))
print("Index of substring in String form index no 5:", s.index("l", 5))
print("\n")

# All indexes of the substring in String
s = "asssaasasakknnsnaascscabcbsvbbxj vajavscjasbcbablcksnlancscnkcnascassvvas"
ss = "as"
print("All indexes of the substring in String:")
start_index = 0
l = []
while ss in s[start_index:]:
    i = s.index(ss, start_index)
    print(i)
    l.append(i)
    start_index = i+1
print(l)
print("\n")

# upper and lower case
s = "Hello World"
print(s.lower())
print(s.upper())
print(s.upper().lower())
print("\n")

# Split method
print("Split method")
s = "asssaasasakknnsnaascscabcbsvbbxj vajavscjasbcbablcksnlancscnkcnascassvvas"
l = s.split("s")
print(l)
print("\n")
# list Handling

l1 = [11, 22, 33, 44, 55]
l2 = l1*3
l3 = l1+l2

ls = ["Hello"," This is", "List"]
ls.append(l1)
print(len(ls))
print(ls)
print("\n")

l2[l2.index(33):5] = ["a", "b", "c"]
print(l2)
print("\n")

# delete
del(l2[8])
print(l2)
del (l2[l2.index("a"):l2.index("c")+1])
print(l2)
print("\n")

# insert
print("l1: ", l1)
l1.insert(2, "hello")
print(l1)
print("\n")

# sort
l = [1225, 56, 4, 8, 4, 84, 4, 48, 2837, 63]
x = sorted(l)       # return sorted list
print("x:", x)
print("l:", l)
l.sort()    # sort the existing list
print("l:", l)

l.pop()
l.pop()



"""" Tupple :
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
 The differences between tuples and lists are, the tuples cannot be changed unlike lists
 and tuples use parentheses, whereas lists use square brackets."""

# Creating a tuple is as simple as putting different comma-separated values
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
# The empty tuple is written as two parentheses containing nothing
t = ()
# Accessing Values in Tuples
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

print("Append tuple :", tup1 + tup2)

del(tup2)

#Updating Tuples

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print(tup3)


""""
Set: A set is an unordered collection with no duplicate elements
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket)                # fast membership testing

print('crabgrass' in basket)


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a)                                    # unique letters in a
print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                             # letters in a or b but not both


# Day 3 And Day 4
""""
Dictionary :set of key: value pairs, with the requirement that the keys are unique
key : immutable (tuple can be use as key) because key searches the value using hash method. if we
 changes the key then hash value will be change and it could not find the value """

tel = {'jack': 4098, 'sape': 4139}
# Add
tel['guido'] = 4127

print(tel)
# print value by key
print(tel['jack'])
# delete specific item
del tel['sape']

tel['irv'] = 4127
print(tel)

# can do
print(list(tel))
print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)

# create dict
dict = {x: x ** 2 for x in (2, 4, 6)}


"""
Questions:
Q--What are Python's dictionaries?
Q--Reverse the string using indexing
Q--Write character count program
Q--Write a program to get the first distinct char from string.
Q--Write a program to flatten list l = [ [1, 2, [3, 4] ], [5, 6], 7]
Q-- What is the difference between list and tuples?
"""







