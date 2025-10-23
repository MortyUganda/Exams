import functools

def takes(*args_1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args_2, **kwargs):
            st = {type(el) for el in (*args_2, *kwargs.values())}
            if st.issubset(set(args_1)):
                return func(*args_2, **kwargs)
            raise TypeError
        return wrapper
    return decorator

@takes(str, int, list)
def add(a, b):
    '''add docs'''
    return a + b

print(add.__name__)
print(add.__doc__)

try:
    print(add('a', 'b'))
except TypeError as e:
    print(type(e))