# Implement the function grouper(), which takes two arguments in the following order:

# iterable - iterable object
# n - a natural number
# The function must return an iterator that generates a sequence whose elements are 
# neighboring elements of the iterable object combined into tuples of n elements each 
# of the iterable object. If an element does not have enough 
# neighbors, they become the value None.
from itertools import zip_longest, repeat, islice, tee

def grouper(it, n):
    return zip_longest(*[iter(it)]*n)

numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))

iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))