# Implement the ncycles() function, which takes two arguments in the following order:
# iterable - iterable object
# times - a natural number
# The function should return an iterator that generates 
# a sequence of elements of the iterable object iterated times times.

from itertools import tee, chain

def ncycles(it, times):
    yield from chain(*tee(it, times))

iterator = iter('bee')

print(*ncycles(iterator, 4))