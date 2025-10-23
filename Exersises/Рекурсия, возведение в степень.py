def get_fast_pow(a, n):
    if not n:
        return 1
    if n % 2 == 0:
        return get_fast_pow(a*a, n//2)
    return a * get_fast_pow(a, n-1)

print(get_fast_pow(2, 10))