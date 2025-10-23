n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
numbers = [int(i) for i in range(1, (n * n) + 1)]
lst = [int(matrix[i][j]) for i in range(n) for j in range(n)]
diag = sum([int(matrix[i][i]) for i in range(n)])    

flag = False
for i in range(n):
    sm_0 = 0
    sm_1 = 0
    for j in range(n):
        sm_0 += matrix[i][j]
        sm_1 += matrix[j][i]
        if matrix[i][j] in numbers and lst.count(matrix[i][j]) == 1:
            continue
        else:
            break
    if sm_0 == sm_1==diag and matrix[0][0] != matrix[1][1]:
        flag = True
    else:
        flag = False
        break

print('YES' if flag == True else 'NO')   
