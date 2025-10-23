import calendar
from datetime import date

def get_all_mondays(year: int) -> list:
    lst = []
    for m in range(1, 12+1):
        m_calendar = calendar.monthcalendar(year, m)
        for line in m_calendar:
            if line[0]:
                lst.append(date(year, month=m, day=line[0]))
    return lst
    
print(get_all_mondays(2021))