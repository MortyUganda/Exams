from collections import Counter
def unique(iterable: iter):
    lst = Counter(iterable)
    yield from lst

iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))