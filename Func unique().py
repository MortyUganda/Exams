# Implement a generator function that takes a single argument:

# iterable - iterable object
# The function must return a generator that generates a sequence of elements of the iterable object without duplicates.


def unique(iterable: iter):
    c = set()
    for el in iterable:
        if el not in c:
            yield el
            c.add(el)