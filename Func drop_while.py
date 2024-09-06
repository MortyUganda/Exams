# Implement the drop_while_negative() function, which takes one argument:

# iterable is an iterable object whose elements are integers
# The function should return an iterator that generates all the numbers of the iterable object being iterated, 
# starting with the first non-negative number.


from itertools import dropwhile

def drop_while_negative(iterable):
    return dropwhile(lambda x: x < 0, iterable)

#Test

iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])

print(*drop_while_negative(iterator))