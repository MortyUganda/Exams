import calendar

year = int(input())
for m in range(1, 12+1):
    m_calendar = calendar.monthcalendar(year, m)
    if m_calendar[0][3]:
        print(f'{m_calendar[2][3]}.{str(m).rjust(2, '0')}.{year}')
    else: print(f'{m_calendar[3][3]}.{str(m).rjust(2, '0')}.{year}')