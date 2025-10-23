dct = {1: 1, 2: 1, 3: 1}

def tribonacci(n):
    res = dct.get(n)
    if res is None:
        res = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
        dct[n] = res
    return res

print(tribonacci(126))