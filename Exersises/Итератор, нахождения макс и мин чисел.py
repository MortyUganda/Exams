def get_min_max(iterable):
    try:
        if type(iterable) is type(iter(range(0))):
            return (next(iterable), max(iterable))
        lst = list(iterable)
        return (min(lst), max(lst))
    except:
        return None