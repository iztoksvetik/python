def case(string: str) -> str:
    return ' '.join(map(lambda s: s.capitalize(), string.split(" ")))
