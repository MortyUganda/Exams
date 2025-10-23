from datetime import date, timedelta

dct = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0}

start = date(year=1, month=1, day=1)
end = date(year=9999, month=12, day=31)
dl = timedelta(days=1)

while start != end:
    if start.day == 13:
        dct[start.isoweekday()] += 1
    start += dl

print(*dct.values(),sep='\n')