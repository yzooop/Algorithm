import sys
input = sys.stdin.readline

levels = [60, 100, 140, 200, 250]
level = []

N = int(input().strip())

for _ in range(N):
    level.append(int(input().strip()))

level.sort(reverse=True)
level = level[:42]

exp_cnt = 0

for i in level:
    for exp in levels:
        if i >= exp:
            exp_cnt += 1



print(sum(level), exp_cnt)