from datetime import date, timedelta

def num_of_sundays(n):
    cnt = 0
    start_date  = date(year=n, month=1, day=1)
    delta = timedelta(days=1)

    while start_date < date(year=n+1, month=1, day=1):
        if start_date.weekday() == 6:
            cnt += 1
        start_date += delta
    return cnt

year = 2000
print(num_of_sundays(year))

print(num_of_sundays(2022))