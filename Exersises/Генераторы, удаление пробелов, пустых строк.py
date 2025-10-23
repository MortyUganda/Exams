def nonempty_lines(file):
    with open(file, encoding='utf8', newline='') as file:
        temp = (i.strip() for i in file.readlines())
        k = (el if len(el) > 25 else '...' for el in temp)
        yield from k
