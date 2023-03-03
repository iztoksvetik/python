def get(n: int) -> int:
    total = sum([int(a) for a in str(n)])
    return total if total < 10 else get(total)
