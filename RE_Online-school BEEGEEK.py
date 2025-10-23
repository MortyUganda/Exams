# BEEGEEK Online School
# In the BEEGEEK online school, the account login is defined as follows:

# the first character is a lower underscore character _
# followed by one or more digits
# followed by zero or more Latin letters in any case
# the login may end with an optional lower underscore character _

import re
import sys

pattern = r'_\d+[A-Za-z]*_?'

for el in sys.stdin:
    if re.match(pattern, el):
        print(True)
    else: 
        print(False)


# Sample Input 1:

# _123abc_
# _1abc_
# 123abc
# _abc123
# _123abc__
# Sample Output 1:

# True
# True
# False
# False
# False