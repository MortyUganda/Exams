from datetime import datetime

with open('diary.txt', encoding='utf8') as file:
    dct = {}
    for el in file.readlines():
        try:
            k = datetime.strptime(el.strip(), '%d.%m.%Y; %H:%M')
        except ValueError:
            if el.strip():
                dct.setdefault(k, []).append(el.strip())
    
    for k, v in sorted(dct.items()):
        print(k.strftime('%d.%m.%Y; %H:%M'))
        print(*v,sep='\n')
        print()
        
    print(dct)