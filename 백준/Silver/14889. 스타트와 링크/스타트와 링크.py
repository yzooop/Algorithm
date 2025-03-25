import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

N_arr = [i for i in range(N)]
c = list(combinations(N_arr, N // 2))
min_diff = float('inf')

for team in c:
    left_team = list(set(N_arr) - set(team))

    team_sum = sum(arr[i][j] + arr[j][i] for i, j in combinations(team, 2))
    left_team_sum = sum(arr[i][j] + arr[j][i] for i, j in combinations(left_team, 2))

    min_diff = min(min_diff, abs(team_sum - left_team_sum))

print(min_diff)