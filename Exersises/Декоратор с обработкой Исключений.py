import functools

def takes_positive(func):
    @functools.wraps(func)
    def f(*args, **kwargs):
        for el in [*args, *kwargs.values()]:
            if type(el) != int:
                raise TypeError()
            if type(el) == int and el <= 0:
                raise ValueError()
        return func(*args, **kwargs)
    return f

@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, par1=1, sep=4))