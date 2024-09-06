# Implement the tabulate() function, which takes one argument:

# func is an arbitrary function
# The tabulate() function should return an iterator that 
# generates an infinite sequence of return values of the func 
# function, first with argument 1, then 2, then 3, and so on.

from itertools import starmap, count

def tabulate(func):
    for el in count(1):
        yield func(el)

func = lambda x: x
values = tabulate(func)

print(next(values))
print(next(values))