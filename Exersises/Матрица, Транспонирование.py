def transpose(matrix: list[list]) -> list[list]:
    return [[*el] for el in zip(*matrix)]
