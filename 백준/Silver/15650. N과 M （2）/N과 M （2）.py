from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [i for i in range(1, N+1)]

ans = list(combinations(arr, M))

for i in ans:
    print(*i)
