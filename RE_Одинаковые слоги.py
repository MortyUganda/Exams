# Write a program that prints words consisting of two identical parts.

#  Input format
# The program is given an arbitrary number of words, each on a separate line.

#  Output format
# The program should print only those words from the input that consist of two identical syllables. 
# The words should be arranged in their original order, each on a separate line.

import re
import sys

pattern = r'(\w+)\1'

for el in map(str.rstrip, sys.stdin):
    if re.match(pattern, el):
        print(el)

# Sample Input 1:

# Python
# beebee
# PyPy
# portal
# Sample Output 1:

# beebee
# PyPy