rows_1, cols_1 = [int(i) for i in input().split()]
matrix_1 = [[int(el) for el in input().split()] for j in range(rows_1)]

nothing = input()

rows_2, cols_2 = [int(i) for i in input().split()]
matrix_2 = [[int(el) for el in input().split()] for j in range(rows_2)]

matrix = [[0]*cols_1 for _ in range(rows_1)]

for r in range(rows_1):
        for c in range(cols_1):
            matrix[r][c] = matrix_2[c][r]
            print(matrix[r][c], end=' ')
        print()
        
res = [[0]*cols_2 for _ in range(rows_1)]      
for i in range(rows_1):
    for j in range(cols_2):
        cnt = 0
        for x in range(cols_1):
            cnt += matrix_1[i][x]*matrix[j][x]
        res[i][j] = cnt
        print(res[i][j], end=' ')
    print()
