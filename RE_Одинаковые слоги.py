# Write a program that prints words consisting of two identical parts.

#  Input format
# The program is given an arbitrary number of words, each on a separate line.

#  Output format
# The program should print only those words from the input that consist of two identical syllables. 
# The words should be arranged in their original order, each on a separate line.

import re
import sys

pattern = r'\b(\w+)\1\b'

for el in sys.stdin:
    res = re.match(pattern, el)
    if res:
        print(res.group())

# Sample Input 1:

# Python
# beebee
# PyPy
# portal
# Sample Output 1:

# beebee
# PyPy