import sys
sys.setrecursionlimit(10**6)

N, M, K = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

v = [[0] * M for _ in range(N)]

def dfs(y, x):
    v[y][x] = 1
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and v[ny][nx] == 0:
            if abs(arr[ny][nx] - arr[y][x]) <= K:
                dfs(ny, nx)

count = 0
for i in range(N):
    for j in range(M):
        if v[i][j] == 0:
            dfs(i, j)
            count += 1

print(count)
