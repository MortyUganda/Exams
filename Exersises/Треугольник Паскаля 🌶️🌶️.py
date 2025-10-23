from math import factorial
def pascal(n):
    c = []
    for i in range(n+1):
        c.append(int(factorial(n)/(factorial(i)*factorial(n-i))))
    return c
num = int(input())
for i in range(num):
    print(*pascal(i))