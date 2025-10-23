# объявление функции
def digit_sum(n):
    sum = 0
    while n:
        num = n % 10
        sum += num
        n //= 10
    print(sum)

# считываем данные
n = int(input())

# вызываем функцию
digit_sum(n)