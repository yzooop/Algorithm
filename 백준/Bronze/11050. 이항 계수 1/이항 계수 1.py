from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())

list_N = [i for i in range(N, N-K, -1)]
list_K = [i for i in range(1, K+1)]

mul_N = 1
mul_K = 1

for n in list_N:
    mul_N *= n

for k in list_K:
    mul_K *= k

print(int(mul_N / mul_K))