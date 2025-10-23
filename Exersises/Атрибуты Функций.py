def remove_marks(text:str, marks:str) -> str:
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    return ''.join([el for el in text if el not in marks])

marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))
    
print(remove_marks.count)