def sandwich(func):
    def w(*args,**kwargs):
        print(f'---- Верхний ломтик хлеба ----')
        f = func(*args,**kwargs)
        print(f'---- Нижний ломтик хлеба ----')
        return f
    return w
 
@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))

add_ingredients(['томат', 'салат', 'сыр', 'бекон'])
print()
@sandwich
def beegeek():
    return 'beegeek'
    
print(beegeek())