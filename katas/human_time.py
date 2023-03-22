def make_readable(seconds: int) -> str:
    return f'{int(seconds/3600):02}:{int(seconds/60)%60:02}:{seconds%60:02}'
