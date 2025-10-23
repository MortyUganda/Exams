from datetime import datetime, timedelta

dat_in = datetime.strptime(input(), '%d.%m.%Y')
dct = {}
lt = dat_in + timedelta(days=7)

for _ in range(int(input())):
    *name, dt = input().split()
    dt = datetime.strptime(dt, '%d.%m.%Y')
    name = ' '.join(name)
    if dat_in < dt.replace(year=dat_in.year) <= lt or dat_in < dt.replace(year=dat_in.year + 1) <= lt:
        dct.setdefault(dt, []).append(name)
        
print(dct)        
if dct:
    print(*min(dct.items())[1])
else: print('Дни рождения не планируются')