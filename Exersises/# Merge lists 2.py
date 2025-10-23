# считываем данные
n = int(input())
res_list = []
for i in range(n):
    numbers = [int(c) for c in input().split()]
    res_list += numbers
    
res_list.sort()

print(*res_list)
