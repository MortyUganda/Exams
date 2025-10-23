def find_key(dct:dict, key):
    if key in dct.keys():
        return dct[key]
    else:
        for el in dct.values():
            if type(el) == dict:
                v = find_key(el, key)
                if v is not None:
                    return v

info = {'name': 'Alyson', 
        'surname': 'Hannigan', 
        'birthday': {'day': 24, 'month': 'March', 'year': 1974},
        'family': {'parents': {'mother': 'Emilie Posner', 'father': 'Alan Hannigan'}}}

print(find_key(info, 'year'))
print(find_key(info, 'father'))