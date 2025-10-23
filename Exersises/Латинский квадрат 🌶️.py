n = int(input())
matrix = [[int(el) for el in input().split()] for j in range(n)]
numbers = [el for el in range(1, n+1)]
flag = 'YES'

def rotate_matrix(n, matrix):
    matrix_const = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            matrix_const[r][c] = matrix[c][r]
    return matrix_const

for i in range(n):
    for j in range(n):
        if numbers[j] not in matrix[i] or numbers[j] not in rotate_matrix(n, matrix)[i]:
            flag = 'NO'
            break
        else:
            continue
print(flag)
