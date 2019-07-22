"""
Examples of data type Set.
"""
print('-' * 80)
# Example of data type Set
print("\tExample - Data type Set")
print("""
In Python Set is collection of, 
    - Immutable objects,
    - Set can be grow or shrink, but in set values can't be replaced.
    - Collection is un-ordered
    - No indexing (as it's send data in un-ordered fashion)
    - and repeation is not allowed, it's used for union data.
    - and special syntax used is pair of curly braces e.g. S = {} 
    - or you can use keyword - set (constructur method)
Set is mainly used to do operations such as, 
    - union (JOINING) data
    - intersection operation
    - minus from one set to another e.g. s2-s1
    - Get Symmatic difference
Mainly used to element common elements between two different sets.
It uses - 
    - For each operations Sets are used to versions/method
    - One is In-place operation and other is 
    - Non-In-place version 

Note: Individual element from "Set" can't be access except that it will accesed using for loop.
e.g. for x in S:
       print(x)

""")
print('-' * 80)

#
print("\tExample - Data type Set")
S1 = {10,20,30,40}
S2 = {30,40,50,60}
print("Get id, type, len of Set data type -", hex(id(S1)), type(S1), len(S1))
print('-' * 80)

# Unable to get data using index e.g.
#print("Set data can't be access using index, e.g. S1[0], it will show error", S1[0])
#It will show error as - 'set' object is not subscriptable

#
print("\tExample - get union data using Set")
S1 = {10,20,30,40}
S2 = {10,20,30}
#S2 = {30,40,50,60}
print("Before union operations values in S1's are - ", S1, "and values in S2 are -", S2)
print("Get union of S1 and S2", S1.union(S2))
print('-' * 80)

#
print("\tExample - of for loop to print data of Set")
S1 = {10,20,30,40}
for x in S1:
    print(x)
print('-' * 80)

#
print("\tExample - of intersection of Sets")
S1 = {10,20,30,40}
S2 = {30,40,50,60}
print("Intersection of S1", S1, "and S2", S2)
print(S1.intersection(S2))
print("and intersection of S2 to S1")
print(S2.intersection(S1))
print('-' * 80)

#
print("\tExample - of difference between Sets")
S1 = {10,20,30,40}
S2 = {30,40,50,60}
print("difference between S1", S1, "and S2", S2)
print(S1.difference(S2))
print(S2.difference(S1))
print('-' * 80)

#
print("\tExample - of Symmetric difference between Sets")
S1 = {10,20,30,40}
S2 = {30,40,50,60}
print("Symmetric difference between S1", S1, "and", S2 )
print(S1.symmetric_difference(S2))
print('-' * 80)

# There are 4 mutable methods used for Set
print("\tExample - of mutable methods of Sets")
S1 = {10,20,30,40}
S2 = {30,40,50,60}
print("Example of Mutable method of Set- update")
S1.update(S2)
print("After S1.update(S2) output- ", S1)
print("S1 is updated but S2 is same e.g. -", S2)
print("""
Other methods of updates are,
    - S1.intersection.update(S2)
    - S1.difference.update(S2)
    - S1.symmetric.difference.update(S2)
""")
S1.intersection_update
print(S1)
S1.difference_update(S2)
print(S1)
S1.symmetric_difference_update(S2)
print(S1)
print('-' * 80)

#
print("\tExample - of issubset Sets")
S1 = {10,20,30,40}
S2 = {10,20,30,40,50,60}
print("S1", S1, "issubset S2 ", S2)
print(S1.issubset(S2))
print("and")
print("S2", S2, "issubset S1 ", S1)
print(S2.issubset(S1))
print("E.g. of superset")
print(S1.issuperset(S2))
print('-' * 80)

#
print("\tExample - add data in Sets")
S1 = {10,20,30}
S1.add(40)
print("Afeter adding S1.add(40) - ", S1)
S1.add(50)
print("Afeter adding S1.add(50) - ", S1)
S1.add(10)
print("Afeter adding S1.add(10) - ", S1)
print("It will not change anything as value (10) is already present in set - ", S1)
print('-' * 80)

#
print("\tExample - remove data from Sets")
S1 = {10,20,30, 40}
S1.remove(10)
print("After removing value data (10) from set - ", S1)

#
print("\tExample - clear, pop and discard methods")
S1 = {10,20,30, 40}
print("Before pop - ", S1)
S1.pop()
print("After discard S1 values are -", S1)
S1.discard(20)
print("After discard (20) - S1 values are -", S1)
S1 = {10,20,30,40,50,60}
print("Before clear method of S1", S1)
S1.clear()
print("After clear method values in S1 are - ", S1)

