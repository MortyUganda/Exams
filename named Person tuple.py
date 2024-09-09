# A named Person tuple is available to you, which contains data about the person. The first element
# of the named tuple is the name of the person, the second is  — age, the third is height. A list is also available 
# persons containing these tuples.

# Complete the code below so that it
# groups people from this list according to their height and displays the resulting groups. For each group
# , the height should be indicated first, and then the names of people with
# the corresponding height should be separated by commas. The groups should be arranged in order of increasing height, each by 
# in a separate line, the names in groups are in alphabetical order, in the following format:

# <height>: <name>, <name>, ...

from collections import namedtuple
from itertools import groupby

key_func = lambda person: person.height

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

for k, person in groupby(sorted(persons, key=key_func), key=key_func):
    print(f'{k}:', ', '.join([el.name for el in sorted(person)]))