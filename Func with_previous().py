# <!-- Implement a generator function that takes a single argument:

# iterable - iterable object
# The function should return a generator that produces a sequence of tuples, each containing the next element of the iterable object iterable as well as the element preceding it:

# (<next element>, <previous element>).
# For the first element, the value None is considered to be the previous element. -->

def with_previous(iterable):
    start = None
    for el in iterable:
        yield (el, start)
        start = el

gen = with_previous(['bee', 'geek', 'stepik', 'python'])

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))