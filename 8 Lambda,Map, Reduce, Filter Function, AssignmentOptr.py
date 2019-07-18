# List Comprehension

# filter on output:
import operator

list1 = [x ** 2 - y ** 3 for x in range(10) if x % 2 == 0
         for y in range(10) if y % 2 == 1
         if (x ** 2 - y ** 3) % 3 == 0]
print(list1)

list2 = [x ** 2 - y ** 3 for x in range(10) if x % 2 == 0
         for y in range(10) if y % 2 == 1]
print(list2)
print("--------------------------------------------")

# Lambda Function
"""
In Python, anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword, in Python anonymous
functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions.

Syntax of Lambda Function in python
lambda arguments: expression
"""
# ex1:
double = lambda x: x * 2
print(double(5))

print((lambda x, y: x ** 2 + y ** 3)(10, 13))

a = 12
b = 5
print((lambda x, y: x * a + y * b - 10)(10, 20))

# Higher order function using lambda

print((lambda n: lambda x: x ** n)(10)(2))

print("------------------------------------------")

"""
Map, Filter and Reduce
These are three functions which facilitate a functional approach to programming. 
We will discuss them one by one and understand their use cases.

4.1. Map
Map applies a function to all the items in an input_list.

map(function_to_apply, list_of_inputs)
Most of the times we want to pass all the list elements to a function one-by-one and 
then collect the output. For instance:
Most of the times we use lambdas with map so I did the same. Instead of a list of 
inputs we can even have a list of functions!
"""
# EX1
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)
# Map allows us to implement this in a much simpler and nicer way.

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))


# EX2
def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

"""
4.2. Filter
As the name suggests, filter creates a list of elements for which a function returns 
true. Here is a short and concise example:
"""
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Note: If map & filter do not appear beautiful to you then you can read about list
# /dict/tuple comprehensions.
"""
4.3. Reduce
Reduce is a really useful function for performing some computation on a list and 
returning the result. It applies a rolling computation to sequential pairs of values 
in a list. For example, if you wanted to compute the product of a list of integers.

So the normal way you might go about doing this task in python is using a basic for 
loop:
"""
product = 1
list1 = [1, 2, 3, 4]
for num in list1:
    product = product * num

# Now let’s try it with reduce:

from functools import reduce

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Practice
print(list(map((lambda n: n ** 2), (filter(lambda x: x % 2 == 0, [i for i in range(1, 101)])))))

print(reduce(operator.add, list(map((lambda n: n ** 2), (filter(lambda x: x % 2 == 0, [i for i in range(1, 101)]))))))

# Assignment Operator
(a, b, c) = (10, 20, 30)
print(a, b, c)

[a, b, c] = [10, 20, 30]
print(a, b, c)

list3 = [(10, (20, 30)), (100, (200, 300)), (1000, (2000, 3000))]
for x, (y, z) in list3:
    print(x, y, z)

# star expression
a, *b, c, d = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a)
print(b)
print(c, d)


"""
Questions:
Q--how map() function works?
Q--What is filter()?
Q--how reduce() function works?
Q--What is mean by * expression.(a, *b, c = 1, 2, 3, 4, 5) what is the value of b?
Q--Explain how can you generate random numbers in Python?
"""