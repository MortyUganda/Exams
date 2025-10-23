def do_twice(func):
    def two(*args, **kwargs):
        temp = func(*args, **kwargs)
        func(*args, **kwargs)
        return temp
    return two
 
@do_twice
def beegeek(*args, **kwargs):
    print('beegeek' * sum(args + tuple(kwargs.values())))
    
beegeek(1, 1, 1, sep=1, end=2, step=3)