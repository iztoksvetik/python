def next(sq: int) -> int:
    is_perfect = lambda x: (x ** (1/2)).is_integer()
    if not is_perfect(sq):
        return -1
    while not is_perfect(sq + 1):
        sq += 1
    return sq + 1
