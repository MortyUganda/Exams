n, k, a = int(input()), int(input()), 0
while not 2**a <= n <= 2 ** (a + 1) - 1:
    a += 1

wn = k * (n - (2**a)) + 1
print(wn)
