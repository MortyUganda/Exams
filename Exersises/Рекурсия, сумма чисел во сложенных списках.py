def recursive_sum(data:list):
    k = 0
    if type(data) == int:
        return data
    for el in data:
        k += recursive_sum(el)
    return k

my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))