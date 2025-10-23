# Write a program that determines:

# the number of lines in which bee occurs as a substring at least two times
# the number of lines in which geek occurs as a word at least once

import re
import sys

cnt1 = 0
cnt2 = 0

for el in map(str.rstrip, sys.stdin):

    if re.search(r'(\w+bee\w+){2,}', el):
        cnt1+=1

    if re.search(r'\bgeek\b', el):
        cnt2+=1
        
print(cnt1)
print(cnt2)

# Sample Input 1:

# beebee bee
# beegeek
# bee geek bee
# Sample Output 1:

# 2
# 1
# Sample Input 2:

# abigail alex
# clint dwarf
# emily
# gil
# Sample Output 2:

# 0