dct = {}

with open(r"c:\Users\Sergei\Downloads\dataset_3380_5 (1).txt", "r+") as file:

    for line in file.readlines():
        cls, name, res = [el.strip() for el in line.split()]
        dct.setdefault(int(cls), {})
        dct[int(cls)].setdefault(name, int(res))

for i in range(1,12):
    key, value = i, dct.get(i, '-')
    try:
        print(key, round(sum(value.values())/len(value), 5))
    except:
        print(key, value)