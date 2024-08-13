import  sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

arr = [0] * N

for _ in range(M):
    i, j, k = map(int, input().strip().split())
    
    for x in range(i-1, j):
        arr[x] = k

print(" ".join(map(str, arr)))
