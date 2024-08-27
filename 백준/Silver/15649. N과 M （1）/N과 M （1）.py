import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().strip().split())

N_list = list(range(1, N+1))

for perm in permutations(N_list, M):
    print(" ".join(map(str, perm)))
