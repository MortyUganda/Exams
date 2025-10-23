from random import choice as ch, shuffle

def generate_pass(count, length):
    dgt = '23456789'
    low = 'abcdefghjkmnpqrstuvwxyz'
    up = 'ABCDEFGHJLKMNPQRSTUVWXYZ'
    symbols = list(dgt + low + up)
    pasw = [[ch(symbols) for _ in range(length - 3) ]for _ in range(count) ]
    
    for el in pasw:
        shuffle(el)
        for i in list(el) + [ch(low) + ch(up) + ch(dgt)]:
            print(i, end = '')
        print()
    
count = int(input())
length = int(input())
generate_pass(count, length)