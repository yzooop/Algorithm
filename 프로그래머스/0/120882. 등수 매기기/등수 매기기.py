def solution(score):
    avg = list(map(lambda x: (x[0] + x[1]) / 2, score))
    ranks = [sorted(avg, reverse=True).index(s) + 1 for s in avg]
    return ranks
