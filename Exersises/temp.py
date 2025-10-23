from datetime import datetime, timedelta

h, m, s = [int(i) for i in input().split(':')]
S = timedelta(seconds=int(input()))
res = timedelta(hours=h, minutes=m, seconds=s) + S
print(res.days)
while res.days >= 1:
    res = res - timedelta(days=1)
    print(res)
print((datetime.strptime(str(res), '%H:%M:%S')).time())