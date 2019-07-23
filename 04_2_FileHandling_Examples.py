"""
Examples -  data type.

========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    The default mode is 'rt' (open for reading text). For binary random
"""
print('-' * 80)
# Example
print("\tExamples of file handle ")
file_path = r"C:\Users\gs-1062\PycharmProjects\Python101\Mytext.txt"
print(" Printing file path - ", file_path)
print('-' * 80)

print("Examples of file write")
f = open(file_path, "w")
print("id, type and len of file f is -",id(f), type(f))
print("Writting to file, e.g. write Hello into file, the use file=f after semicolon,")
print("Hello", file=f)
f.close()
print('-' * 80)

print("file= is default arg. to print, if we don't provide it, then it takes stdio default arg.")
print("File write when mode is r, it should show error")
f = open(file_path, "r")
#print("Str", file=f)
f.close()
print('-' * 80)

print("Read file line by line useing for loop e.g.")
f = open(file_path, "r")
for line in f:
    print("Reading lines from file:\n")
    print(line)
f.close()

print("SOpen file for append")
f = open(file_path, "a")
print(10,20,30, sep=":")
print(10,20,30, end="None")
num = 10
print(num, file=f)
print('-' * 80)


