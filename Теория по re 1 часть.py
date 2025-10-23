# Функция search()
# Функция search() сканирует строку в поисках первого совпадения
import re
print('----------------search---------------')
pattern = r'\w{4}'
text = 'Text1234TEXT'
example = re.search(pattern, text)
print(example.group())
print(example)

# Функция match()     
# Функция match() возвращает специальный объект соответствия (тип Match), если начало строки соответствуют регулярному выражению, 
# или значение None в противном случае.
print('----------------match---------------')
from re import match

match1 = match('super', 'superstition')
match2 = match('super', 'insuperable')

print(match1)
print(match2)

# Функция fullmatch() возвращает специальный объект соответствия (тип Match),
# если вся строка соответствует регулярному выражению, или значение None в противном случае.

from re import fullmatch

print('----------------fullmatch---------------')
match1 = fullmatch(r'\d+', '123foo')
match2 = fullmatch(r'\d+', 'foo123')
match3 = fullmatch(r'\d+', 'foo123bar')
match4 = fullmatch(r'\d+', '123')

print(match1)
print(match2)
print(match3)
print(match4)


# Если мы пользуемся именованными группами, используя синтаксис (?P<name><regex>), тогда мы можем 
# использовать название группы в качестве аргумента метода group().

# Приведенный ниже код:

from re import search
print('----------------group---------------')
# (?P<name><regex>)

match = search(r'(?P<w1>\w+),(?P<w2>\w+)', 'foo,bar,baz')

print(match.group())
print(match.group('w1'))
print(match.group('w2'))
print(match.group('w1', 'w2', 'w2', 'w2', 'w2'))

