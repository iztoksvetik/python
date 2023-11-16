import re

def is_valid_IP(input: str) -> bool:
    match = re.match(r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$', input)
    return bool(match) and all([int(i) < 256 and int(i) >= 0 and not (len(i) > 1 and i.startswith('0')) for i in match.groups()])
