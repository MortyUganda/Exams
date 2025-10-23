from datetime import datetime

lst_dates = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), input().split()))
lst = [abs((lst_dates[i+1] - lst_dates[i])).days for i in range(len(lst_dates)-1)]
print(lst)