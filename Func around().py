# Implement a generator function that takes a single argument:

# iterable — an iterable object
# The function should return a generator that generates a sequence of tuples, each of which contains another element of the iterable object being iterated, as well as the previous and following elements:

# (<previous element>, <next element>, <next element>)
# For the first element, the previous value is None, for the last element, the next value is also None.

def around(iterable, prev=None):
    try:
        iterable = iter(iterable)
        first_position = next(iterable)
        for el in iterable:
            yield prev, first_position, el
            prev = first_position
            first_position = el
        yield prev, first_position, next(iterable, None)
    except:
        return