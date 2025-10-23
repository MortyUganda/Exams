# Черновик333
n = int(input())
matrix = [[int(el) for el in input().split()] for j in range(n)]
k = int(input()) - 1

def rotate_matrix(n, matrix):
    matrix_const = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            matrix_const[r][c] = matrix[c][r]
    return matrix_const

def multiplication_matrix(n, k, matrix):
    matrix_const = rotate_matrix(n, matrix)
    for _ in range(k):
        temp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                cnt = 0
                for x in range(n):
                    cnt += matrix[j][x] * matrix_const[i][x]
                temp[j][i] = cnt
        matrix = temp
    for row in matrix:
        print(*row)
        
multiplication_matrix(n, k, matrix)

