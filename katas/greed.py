def score(dice: list[str]) -> int:
    counts = dict(zip(range(1,7),[0]*6))
    for item in dice:
        counts[item]+=1 
    threes = [count // 3 * (number * 100 if number > 1 else number * 1000) for number, count in counts.items()]
    return counts[1] % 3 * 100 + counts[5] % 3 * 50 + sum(threes)
