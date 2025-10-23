def evaluate(dts, x):
    lst = [x**i for i in range(len(dts)-1, -1 , -1)] # Создаем список из x ** i...0
    r = sum(map(lambda a, b : a*b, dts, lst))
    return r

dts = list(map(int, input().split())) # Создаем список из оснований
x = int(input())

print(evaluate(dts, x))
