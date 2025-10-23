n, xy = 8, input()
matrix = [['.']*n for i in range(n)]
x = '87654321'.index(xy[1])
y = 'abcdefgh'.index(xy[0])
matrix[x][y] = 'N'

for i in range(n):
    for j in range(n):
        k = (x - i) * (y - j)
        if k == 2 or k == -2:
            matrix[i][j] = '*'
        print(matrix[i][j], end=' ')
    print()
        
