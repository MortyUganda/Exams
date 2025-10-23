def get_all_values(dct, key):
    st = set()

    for el in dct.values():
        if key in dct.keys():
            st.add(dct[key])

        if type(el) == dict:
            v = get_all_values(el, key)
            st.update(v)
    return st


my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))





