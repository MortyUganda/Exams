# Implement a generator function that takes a single argument:

# iterable — an iterable object
# The function should return a generator that generates a sequence of tuples, each of which contains another element of the iterable object being iterated, as well as the next element following it:

# (<next element>, <next element>)
# For the last element, the next value is None.
from typing import Iterable, Generator

def pairwise(iterable: Iterable, pair=None) -> Generator:
    try:
        iterable = iter(iterable)
        first_position = next(iterable)
        for el in iter(iterable):
            yield (first_position, el)
            first_position = el
        yield first_position, next(iterable, None)
    except StopIteration:
        pass
    
iterator = iter('stepik')

print(*pairwise(iterator))
