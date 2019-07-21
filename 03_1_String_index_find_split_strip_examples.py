"""
String data type examples
Index, Find, in operator, count, Strip, Split, dir (str), help(str.split) examples
"""
#Example of in operator
print("\tExample of in operator in string")
s = "Hello,World"
if "ll" in s:
    print("checking, if ll in Hello,World")
    print("Yes")
print('-' * 80)

# Example of count method (This is class method)
print("\tExample of in count method (This is class based method and executed by . operator")
s = "abcdeaaaedaaedadaadaa"
print("Counting number of character \"aa\" in given string \"abcdeaaaedaaedadaadaa\" - ", s.count("aa"))
s = "aabbccddaa"
search_string = "aa"
print("Finding number of countes of ", search_string, "in", s, "and result is - ", s.count(search_string) )
print('-' * 80)

# Example of index method
print("\tExample of index method")
given_string = "aabbccddaa"
search_string = "aa"
print("printing index of given search string - ", given_string.index(search_string))
print(" example of second parameter - used to start index to find next index - ", given_string.index(search_string, 7))
print('-' * 80)

# Exmpale of find method
print("\tExample of find index method")
given_string = "aabbccddaa"
search_string = "aa"
#print("printing index of given search string - ", given_string.index(search_string,10))
#above will show error as it goes out of range then use find method
print("Using find method-with out of index range for given_search string-", given_string.find(search_string,1))
print("Using find method-with out of index range for given_search string-", given_string.find(search_string,10))
print('-' * 80)

# Exampale to find all index in given string for search string
print("\tExample to find all index in given string for search string")
given_string = "aabbccddaabbaa"
search_string = "aa"
start_index = 0
L = []
while search_string in given_string[start_index :]:
    i = given_string.index(search_string, start_index)
    print("Found given string", search_string, "at index", i)
    start_index = i + 1

print("\tUsing list - Example to find all index in given string for search string")
given_string = "aabbccddaabbaa"
search_string = "aa"
start_index = 0
L = []
while search_string in given_string[start_index :]:
    i = given_string.index(search_string, start_index)
    L.append(i)
    #print("Found given string", search_string, "at index", i)
    start_index = i + 1
print("Printing values from list [] - ", L)
print('-' * 80)

# Example of string upper and lower method
print("\tExample string upper and lower method")
print("\tExample string upper lower method")
given_string = "aabbccddaabbaa"
print("Printing upper letters of  given string", given_string, "-", given_string.upper())

print("\tExample string lower method")
given_string = "AABBCCDDEE"
print("Printing lower letters of  given string", given_string, "-", given_string.lower())

print("Example of upper.lower - ", given_string.upper().lower())
print('-' * 80)

# Example of split method
print("\tExample string strip method")
s = "Hello,World\n"
s1 = s.strip()
print("After using strip, id (address) of org. string and new string are different e.g. -", hex(id(s)), "-", hex(id(s1)))
print("also lens will be different after strip, e.g.")
print("Length of string s - ", len(s), "and")
print("Length of string s1 - ", len(s1), "and")
print('-' * 80)

# Example of split method
print("\tExample split method")
s = "padmakar:x:10:ds_xdk:300:/home/padmakar"
L = s.strip().split(":")
print("Before strip and split", s, "after strip and split", L)
for x in L:
    print(x)
print("After split all values are in string e.g. L[2] - ", type(L[2]))
L[2] = int(L[2])
print("Converting type of second index i.e. L[2] - ", type(L[2]))
print('-' * 80)

# Example of split method
print("\tExample dir (str) and help (str.split) method")
print(" Example of dir(class) e.g. dir(str)", dir(str), "\n")
print("Example of help method, help(class.method), e.g. help(str.split)")

print('-' * 80)
