# Implement a generator function that takes two arguments in the following order:

# iterable - iterable object

# obj - an arbitrary object
# The function should return a generator that generates a sequence of 
# elements of the iterable object iterable until an element equal to obj is 
# reached. If the iterable object iterable does not contain any element 
# equal to obj, the generator must generate all elements of iterable.

def stop_on(itebale, obj):
    for el in itebale:
        if el != obj:
            yield el
        else: return