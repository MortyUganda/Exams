def palindromes():
    n = 1
    yield 1
    while True:
        strn = str(n)
        if len(strn) % 2:
            st = strn[:len(strn) // 2 + 1]
            new = str(int(st) + 1)
            if len(st) < len(new):
                newn = new[:-1] + new[-2::-1]
            else:
                newn = new + new[-2::-1]
            n = int(newn)
        else:
            st = strn[:len(strn) // 2]
            new = str(int(st) + 1)
            if len(st) < len(new):
                newn = new + new[-2::-1]
            else:
                newn = new + new[::-1]
            n = int(newn)
        yield n