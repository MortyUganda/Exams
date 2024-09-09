# Implement the sum_of_digits() function, which takes one argument:

# iterable is an iterable object whose elements are natural numbers

# The function must return a single number — the sum of the digits of all the numbers present in
# the iterable object being iterated.

from itertools import chain

def sum_of_digits(it):
    return sum(map(int, chain.from_iterable(map(str, it))))

print(sum_of_digits([13, 20, 41, 2, 2, 5]))