# Разворот матрицы
def print_matrix(height, wight):
    index = 0
    for i in range(1, height + 1):
        c = []
        for _ in range(wight):
            c.append(lst[index])
            index += 1
        c = " ".join(c)
        if i != height:
            print(c)
    return c

y, x = int(input()), int(input())
lst = [input() for _ in range(y * x)]

print(print_matrix(y, x))
print()
print(print_matrix(x, y))
