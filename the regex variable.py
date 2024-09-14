# Complete the code below so that the regex variable contains a regular expression 
# that corresponds to the dates of the following formats:

# DD.MM.YYYY
# DD/MM/YYYY
# YYYY.MM.DD
# YYYY/MM/DD
# Note 1. Additional date verification is not required.

regex = (
    r'[0-1]\d:[0-5]\d|'
    r'[2][0-3]:[0-5]\d'
)


# Sample Input 1:
# So why does my watch say 91:44? It doesn't matter, I'll be there at 17:30

# Sample Output 1:
# 17:30