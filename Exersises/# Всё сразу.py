n = int(input())
matrix = [[int(el) for el in input().split()]for _ in range(n)]
numbers = [int(i)for i in range(1, (n*n)+1)]
print(numbers)
flag = 'YES'
all_numbers = matrix[0]
for i in range(n):
    if all_numbers == matrix[n]:
        for j in range(n):
            if numbers[n] in matrix:
                flag = True
    else:
        flag = False
        break















for i in range(n):
    for j in range(n):
        if matrix[i][j] in numbers and flag == 'YES':
            flag = 'YES'
        else:
            flag = 'NO'
            break
v = sum(matrix[2])        
a = sum(matrix[1])
b = sum([int(matrix[i][1]) for i in range(n)])
l = sum([int(matrix[i][2]) for i in range(n)])
c = sum([int(matrix[i][i]) for i in range(n)])
d = sum([int(matrix[i][n - 1- i])for i in range(n)])

if a == b == c == d== l == v and matrix[0][0] != matrix[1][1] and flag == 'YES':
    flag = 'YES'
else:
    flag = 'NO'

print(flag)