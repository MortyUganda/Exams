# A list of tasks is available to you, in which all
# Timur's cases are recorded. Each element of the list is a tuple of three elements: the first is the name
# of the case, the second is the action, and the third is the order.

# Complete the code below so that it displays all Timur's cases in alphabetical order, 
# specifying for each set of appropriate actions in
# the correct order, in the following format:

# <case>:
#     1. <action>
#     2. <action>
# ...

from itertools import groupby

tasks = [('Отдых', 'поспать днем', 3),
        ('Ответы на вопросы', 'ответить на вопросы в дискорде', 1),
        ('ЕГЭ Математика', 'доделать курс по параметрам', 1),
        ('Ответы на вопросы', 'ответить на вопросы в курсах', 2),
        ('Отдых', 'погулять вечером', 4),
        ('Курс по ооп', 'обсудить темы', 1),
        ('Урок по groupby', 'добавить задачи на программирование', 3),
        ('Урок по groupby', 'написать конспект', 1),
        ('Отдых', 'погулять днем', 2),
        ('Урок по groupby', 'добавить тестовые задачи', 2),
        ('Уборка', 'убраться в ванной', 2),
        ('Уборка', 'убраться в комнате', 1),
        ('Уборка', 'убраться на кухне', 3),
        ('Отдых', 'погулять утром', 1),
        ('Курс по ооп', 'обсудить задачи', 2)]

for k, v in groupby(sorted(tasks), key=lambda x: x[0]):
    print(f'{k}:')
    for el in sorted(v, key=lambda x: x[2]):
        print(f'    {el[2]}. {el[1]}')
    print()