# Implement the is_rising() function, which takes one argument:

# iterable is an iterable object whose elements are numbers
# The function should return True if the elements of the 
# iterated object are arranged strictly in ascending order, or False otherwise.

from itertools import pairwise

def is_rising(it):
    return all(map(lambda x: int(x[0]) < int(x[1]), pairwise(it)))

iterator = iter([1, 1, 1, 2, 3, 4])
print(is_rising(iterator))

iterator = iter(list(range(100, 200)))
print(is_rising(iterator))

print(is_rising([1, 2, 3, 4, 5]))