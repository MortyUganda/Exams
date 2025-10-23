from fractions import Fraction as F
from math import gcd

n = int(input())

lst = [ F(i, j) for i in range(1, n) for j in range(1, n + 1) if i // j < 1 and gcd(i, j) != 1]
print(lst)

k = n // 2
a = n - k
while gcd(k, a) != 1:
    k -= 1
    a += 1
print(F(k, a))
