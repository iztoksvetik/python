def format(n: list[int]) -> str:
    return f'({"".join(map(str, n[:3]))}) {"".join(map(str, n[3:6]))}-{"".join(map(str, n[6:]))}'
