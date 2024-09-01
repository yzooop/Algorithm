import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

A = [list(map(int, input().strip().split())) for _ in range(N)]
B = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        result = A[i][j] + B[i][j]
        print(result, end=" ")
    print("")