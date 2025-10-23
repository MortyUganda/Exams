def bee(n):
    k = dct[n]*f'{n}'
    if n < 4:
        print(k.center(16))
        bee(n + 1)
    print(k.center(16))
    
dct = {1: 16, 2: 12, 3: 8, 4: 4}
bee(1)