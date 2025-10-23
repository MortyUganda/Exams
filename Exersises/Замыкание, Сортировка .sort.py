def sort_priority(numbers: list, group: list|set|tuple) -> list[int]:
    numbers.sort(key=lambda x: (x not in group, x))


