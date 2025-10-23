def rec(txt):
    txt = int(input())
    if txt != 0:
        rec()
    print(txt)

rec()