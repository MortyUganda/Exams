def nop(*rest, **kwargs):
    lst = map(lambda x: x.upper() if type(x)==str else x, rest)
    if kwargs:
        old_print(*lst, sep=kwargs['sep'].upper(), end=kwargs['end'].upper())                           # заглушка, функция ничего не делает
    return old_print(*lst)

old_print = print

print = nop
print('Привет', 'мир')
print('Stepik', 'Beegeek', 'Python', sep='*', end='sdf')
print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')