
def zip_longest(*data, fill=None):
    n = len(max(data, key=len))
    lst = [el + [fill]*n-len(el) for el in data]
    return list(zip(*lst))
    
print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

