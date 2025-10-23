def dict_travel(dct:dict, key):
    if key in dct.keys():
        return dct[key]
    else:
        for el in sorted(dct.values()):
            if type(el) == dict:
                v = dict_travel(el, key)
                if v is not None:
                    return v
                

data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

print(sorted(data['b']))