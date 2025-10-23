def filter_names(names: list, ignore_char: str, max_names: int):
    dig = (name for name in names if all(i not in '0123456789' for i in name))
    char = (name for name in dig if not name.lower().startswith(ignore_char.lower()))
    yield from (name for i, name in enumerate(char) if i < max_names)

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))