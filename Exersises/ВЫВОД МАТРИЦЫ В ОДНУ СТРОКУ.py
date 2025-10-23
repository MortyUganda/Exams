n = int(input())
lst = [[j for i in range(n)] for j in range(n)]

[print(*x) for x in lst]
