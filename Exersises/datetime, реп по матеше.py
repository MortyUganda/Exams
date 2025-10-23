from datetime import datetime, timedelta
p = '%H:%M'
start, end = datetime.strptime(input(), p) , datetime.strptime(input(), p)

while start < end:
    if (end - start).minutes < 45:
        break
    start += timedelta(minutes=55)
    print(f'{(start - timedelta(minutes=55)).strftime(p)} - {(start - timedelta(minutes=10)).strftime(p)}')