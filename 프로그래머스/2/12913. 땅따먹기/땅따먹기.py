def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            max_prev = 0
            for k in range(4):
                if k == j:
                    continue
                if land[i - 1][k] > max_prev:
                    max_prev = land[i - 1][k]
            land[i][j] += max_prev
    return max(land[-1])
