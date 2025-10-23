n = input()
def rec(n):
    if not n:
        return 0
    else:
        return int(n[0]) + int(rec(n[1:]))

print(rec(n))


