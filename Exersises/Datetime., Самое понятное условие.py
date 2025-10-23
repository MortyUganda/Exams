from datetime import date, timedelta, datetime

start, end = [datetime.strptime(input(), '%d.%m.%Y') for _ in range(int(input()))]
td_1, td_3 = timedelta(days=1), timedelta(days=3)

sum_day_month = start.month + start.day
if sum_day_month % 2 == 0:
    start += td_1
    
while start != end:
    if start.weekday not in [0, 3]:
        print(start.strftime('%d.%m.%Y'))
        start += td_3