abscissas, ordinates, applicates = [[float(i) for i in input().split()]for _ in range(3)]
lst = zip(abscissas,ordinates,applicates)

res = all(map(lambda el: el[0]**2 + el[1]**2 + el[2] ** 2 <= 4, lst))
print(res)
