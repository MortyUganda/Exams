k = []
for i in range(int(input())):
    pupils = []
    for j in range(int(input())):
        pupils.append(input())
    res = list(map(lambda x: x.endswith('5'), pupils))
    k.append(any(res))
print('YES' if all(k) == True else 'NO')

def evaluate(coefficients, x):
    return coefficients

coefficients = [int(i) for i in input().split()]
x = int(input())

print(evaluate(coefficients, x))


