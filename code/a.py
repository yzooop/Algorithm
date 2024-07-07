import sys

def bfs(sy, sx):
    q = []
    q.append((sy, sx))
    v[sy][sx] = 1
    cnt = 1

    while q:
        cy, cx = q.pop(0)

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx

            if 0<=ny<N and 0<=nx<N and arr[ny][nx] == 1 and v[ny][nx] == 0:
                q.append((ny, nx))
                v[ny][nx] = 1
                cnt += 1
    return cnt

N = int(sys.stdin.readline().strip())

arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and v[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans), *ans, sep="\n")
