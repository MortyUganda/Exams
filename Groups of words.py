# Input data format
# The program is given a sequence of words as input, separated by a space. 
# Each word is written in lowercase Latin letters.

# Output data format
# The program should group the entered words by their length and output the resulting groups. 
# The length should be specified for each group, and then the words with the appropriate length are listed separated by commas. 
# The groups should be arranged in increasing order of length, each on
# a separate line, the words in the groups should be in alphabetical order, in the following format:

# <length> -> <word>, <word>, ...

from itertools import groupby

res = groupby(sorted(input().split(), key=lambda x: (len(x), x)), key=len)
for key, value in res:
    print(f"{key} -> {', '.join(list(value))}")
    
# Sample Input :

# hi never here my blue

# Sample Output:

# 2 -> hi, my
# 4 -> blue, here
# 5 -> never