res = [el for el in (input() + ' запретил букву')]
abc = [el for el in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']

for i in abc:    
    
    if i in res:
        s = ''.join(res)
        s = " ".join(s).split()
        print(s, i)
        
        for _ in res:
            for _ in range(res.count(i)):
                res.remove(i)
                