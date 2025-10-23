def flatten(nested_list):
    for el in nested_list:
        if type(el) == list:
            yield from flatten(el)
        else:
            yield el

generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)