"""
Examples of Tuple data type.
"""
print('-' * 80)
# Example
print("\tExample - Tuple data types")
T1 = (100,200,300,400)
T2 = (500,600,700,800)
print("T1 - Checking T1, id, type - ", T1, id(T1), type(T1))
print('-' * 80)

# Example
print("\tExample - Tuple count")
T1 = (100,200,300,400,100)
T2 = (500,600,700,800)
search_string = 100
print("Count of tuple e.g. - ", T1.count(search_string))
print('-' * 80)

#
print("\tExample - of sinle value in Tuple data types")
print("In () bracket tuple, must have comma after adding value, "
      "if not then it will consider different data type e.g.")
T1 = (10)
T2 = (10,)
print("Data type of T1 = (10) is -", type(T1), "and data type of T2=(10,) is -", type(T2))
print('-' * 80)

# Other examples of tuple  Similar to list e.g. +, *
print("\tExample - Tuple data combination (+)")
T1 = (10,20,30,40,50)
T2 = (10,20,30,40,50)
print("Print T1 + T2 - ", T1 + T2)
print('-' * 80)

# Other examples of tuple  Similar to list e.g. +, *
print("\tExample - Tuple data multiplication (*)")
T1 = (10,20,30,40,50)
T2 = (10,20,30,40,50)
print("Print T1 *5  - ", T1 *5)
print('-' * 80)

# Other examples of tuple  Similar to list e.g. +, *
print("\tExample - Tuple for loop and getting value using indexe.g.)")
T1 = (10,20,30,40,50)
T2 = (10,20,30,40,50)
print("for loop version1 - for tuple")
for x in T1:
    print("x in tuple -", x, "and type of x - ", type(x))
print("for loop version 2")
for i in range(len(T1)):
    print("T1[i] - ", T1[i], "and", "type - ", type(T1[i]))
print('-' * 80)

#
print("No left hand data side operation e.g. = ")
#T1[0] = 700
#print("Value of T1",T1) #It will show error as 'tuple' object does not support item assignment

# examples fetch value using index
print("\tExample - Tuple index")
T1 = (10,20,30,40,50)
print("Print T1[2]   - ", T1[2])
print('-' * 80)