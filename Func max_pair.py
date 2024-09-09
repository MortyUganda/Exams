# Implement the max_payne() function, which takes one argument:

# iterable is an iterable object whose elements are numbers
# The function must return a single number — the maximum 
# sum of two adjacent numbers of the iterable object being iterated.

from itertools import pairwise

def max_pair(it):
    return max(a+b for a, b in pairwise(it))

print(max_pair([1, 8, 2, 4, 3]))

iterator = iter([1, 2, 3, 4, 5])

print(max_pair(iterator))