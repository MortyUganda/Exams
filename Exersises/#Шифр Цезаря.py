# Шифр Цезаря
print("Добро пожаловать в программу Цезаря")
l = input('Давай выберем язык: Если русский введи - "rus", если англиский - "eng"\n')
shifr = input("Нужно зашифровать? Введи '+' если да,'-' если нужно дешифровать\n")
txt = input('Введи текст: ')
k = int(input('Введи ключ сдвига: '))
symbols = '!', '?', ' ', '.', ','
text_pool = input('Нужно ли все возможные варианты')

def decryption(k, txt, l):
    c = ''
    if l == 'rus':
        n = 32
        x = 1102
    else:
        n = 26
        x = 122
    for el in txt:
        if el not in symbols:
            if ord(el.lower()) + k <= x:
                c += chr(ord(el)+k)
            else:
                c += chr(ord(el)+k-n)
        else:
            c += el
    return c
def encryption(k, txt, l):
    c = ''
    if l == 'rus':
        n = 32
        x = 1072
    else:
        n = 26
        x = 97    
    for el in txt:
        if el not in symbols:
            if ord(el.lower()) - k >= x:
                c += chr(ord(el) - k)
            else:
                c += chr(ord(el) - k + n)
        else:
            c += el
    return c
if shifr == '+':
    print(decryption(k, txt, l))
else:
    print(encryption(k, txt, l))