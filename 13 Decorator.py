
# decorator
# calculate the time for execution of code

import time

def code_time(code):
    def wrapper(n):
        t1 = time.time()
        code(n)
        t2 = time.time()
        return "Time it took to run:" + str((t2 -t1) ) +"\n"
    return wrapper

@code_time
def add_till(n):
    sum = 0
    for i in range(n):
        sum = sum +i
    print("sum : ", sum)

print(add_till(1000000))

"""
Question:
Q--Write decorator to calculate execution time for function?
"""