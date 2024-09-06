# Implement the alnum_sequence() function, which does not accept any arguments.

# The function should return an iterator that cyclically generates 
# an infinite sequence of natural numbers and uppercase Latin letters:

# 1,A,2,B,3,C,..,X,25,Y,26,Z

import string
import itertools

def alnum_sequence():
    letters = string.ascii_uppercase
    numbers = range(1,27)
    lst = (el for k in zip(numbers, letters) for el in k)
    return itertools.cycle(lst)

alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))