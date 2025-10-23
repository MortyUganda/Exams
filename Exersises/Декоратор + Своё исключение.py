class MaxRetriesException(Exception):
    pass

import functools

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    pass
            raise MaxRetriesException()
        return wrapper
    return decorator

@retry(100)
def add(a, b):
    add.calls = add.__dict__.get('calls', 0) + 1
    if add.calls < 10:
        raise ValueError
    return a + b
    
try:
    print(add(40, 10))
except Exception as e:
    print(type(e))

    