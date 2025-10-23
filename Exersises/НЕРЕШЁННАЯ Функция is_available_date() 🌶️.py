from datetime import datetime

def convert_date_str(dat:str):
    pat = '%d.%m.%Y'
    if '-' in dat:
        range_date = dat.split('-')
        first_time = datetime.strptime(range_date[0], pat).timestamp()
        second_time = datetime.strptime(range_date[1], pat).timestamp()
        return list(range(int(first_time), int(second_time)+1))
    return int(datetime.strptime(dat, pat).timestamp())

def is_available_date(dates:list, some_date:str)->bool:
    lst_dates = [convert_date_str(el) for el in dates]
    dates = convert_date_str(some_date)
    for date in lst_dates:
        print(date)
        if type(date) == list:
            return True
    return False

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))




