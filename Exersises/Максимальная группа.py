#Максимальная группа
dict = {}
for el in range(1,int(input())+1):
    dict[el] = sum(map(int, str(el)))

dict2 = {}
for k, v in dict.items():
    dict2[v] = dict2.setdefault(v, []) + [k]

print(len(max(dict2.values(), key = len)))
