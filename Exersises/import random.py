import random

n = int(input())
number = random.randrange(1, n + 1)
print('задуманное число:', number)

left = 1
right = n + 1
middle = (left + right) // 2
print('Число мидл равно:', middle)
cnt = 0

while middle != number:
    if middle < number:
        left = middle + 1
        middle = (left + right) // 2
        cnt += 1
        print('Число мидл равно: (если мидл меньше)',middle)
    if middle > number:
        right = middle - 1
        middle = (left + right) // 2
        cnt += 1
        print('Число мидл равно: (если мидл больше)',middle)
print(cnt, number,middle)        
