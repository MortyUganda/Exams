def print_operation_table(func, rows, cols) -> list:
    mtrx = [[func(i+1, j+1) for j in range(cols)] for i in range(rows)]
    [print(*el) for el in mtrx]

print_operation_table(lambda a, b: a * b, 5, 5)
print_operation_table(pow, 5, 4)