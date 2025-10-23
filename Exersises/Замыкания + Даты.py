from datetime import date

def date_formatter(cnt_code):
    dct = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y', 'ca': '%Y-%m-%d', 'br': '%d/%m/%Y', 'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
    def f(date):
        return date.strftime(dct[cnt_code])
    return f

date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))