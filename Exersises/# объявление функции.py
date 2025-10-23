# объявление функции
def merge(list1, list2):
    a1 = a3 + a2
    for i in range(1, len(a1)): 
        elem = a1[i]
        j = i
    
        while j >= 1 and a1[j - 1] > elem:
            a1[j] = a1[j - 1]
            j -= 1

        a1[j] = elem
    return a1

# считываем данные
a3 = [int(c) for c in input().split()]
a2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(a3, a2))
