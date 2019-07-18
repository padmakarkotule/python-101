

# different ways to itarate over dictionary
d = {True: "Hello", 10: 2.0145, 3.14: [10, 20, 30], (1, 2): {10, 20}}
print("keys:--------------------------------")
for x in d:
    print(x)
print("Print Keys and their values :-------")
for x in d.keys():
    print(x, " ", d[x])
print("values:------------------------- ")
for x in d.values():
    print(x)
print('-----------------------------')
for i in d.items():
    print(i[0], i[1])
print("-----------------------------")
# update
d[True] = "Yes"
print(d)
del (d[(1, 2)])
print(d)

print("-----------------------------")
d1 = {10: 1, 20: 2, 30: 3, 40: 4}
d2 = {50: 500, 60: 600, 30: 300, 40: 400}
d1.update(d2)
print(d1)
d1 = {10: 1, 20: 2, 30: 3, 40: 4}
d2.update(d1)
print(d2)

x = d2.update(d1)
type(x)         # it is none because update function does not return any thing

print("=-----------------------------")
# can do


def f(**kwargs):
    print(kwargs, type(kwargs))


f(a=10, b=30, c=40)
print("--------------------")

l1 = [1,2,3,4]
l2 = ["a", "b", "c"]
rs = zip(l1,l2)
for x in rs:
    print(x)


"""
We can use File handling to read and write data to and from the file.
open the file:
f = open(filename, mode)
close the file:
f.close()  # where f is a file pointer

Opening a file tells Python which file are we going to work with (file path and name) 
and how (read/write and are we using it as a text or as a binary file). If a file 
doesn't exist, it can be created or an exception may be raised, depending on how are 
we opening it.
Reading from or writing to a file can be done only on an open, existing file.
Closing a file tells Python that we are done with it, so it can "tidy up". Among 
other things, this includes flushing the buffer, which makes closing an important 
part of the process


Modes of file
'r'	This is the default mode. It Opens file for reading.
'w'	This Mode Opens file for writing.
    If file does not exist, it creates a new file.
    If file exists it truncates the file.
'x'	Creates a new file. If file already exists, the operation fails.
'a'	Open file in append mode.
If file does not exist, it creates a new file.
't'	This is the default mode. It opens in text mode.
'b'	This opens in binary mode.
'+'	This will open a file for reading and writing (updating)

"""
p = r"C:\Users\gsc-30251\Desktop\PythonPractice\Module2\foo.txt"

# read entire content of file at once
with open(p, 'r') as f:
    print(f.read())

# read word by word
with open(p, 'r') as f:
    for word in f:
        print(word, end=" ")

# read entire content of file at once
with open(p, 'r') as f:
    f.readlines()

# Write
with open(p, 'w+') as f:
    f.write("hello this is me ,..ahhah")

with open(p, 'a') as f:
    f.write("Ths is append mode")

""""
Method	Description
close()	Close an open file. It has no effect if the file is already closed.
detach()	Separate the underlying binary buffer from the TextIOBase and return it.
fileno()	Return an integer number (file descriptor) of the file.
flush()	Flush the write buffer of the file stream.
isatty()	Return True if the file stream is interactive.
read(n)	Read atmost n characters form the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()	Returns the current file location.
truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Write string s to the file and return the number of characters written.
writelines(lines)	Write a list of lines to the file.
"""


file1 = open(r"C:\Users\gsc-30251\Desktop\PythonPractice\Module2\file1.txt", "r+")
with open(p, "a") as f:
    f.write(file1.read())
file1.close()


"""
Q--what is benefit of with open()?
Q--write program to count no of line in file.
Q--What are the diff techniques to iterate over dictionaries?
Q--What are the diff modes for open the file?
"""