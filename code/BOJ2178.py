import sys

def bfs(sy, sx, ey, ex):
    q = []
    q.append((sy, sx))

    v = [[0] * M for _ in range(N)]
    v[sy][sx] = 1

    while q:
        cy, cx = q.pop(0)

        if (cy, cx) == (ey, ex):
            return v[ey][ex]
    
        for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
            ny, nx = cy+dy, cx+dx
            if(0<=ny<N and 0<=nx<M and arr[ny][nx]==1 and v[ny][nx]==0):
                q.append((ny, nx))
                v[ny][nx] = v[cy][cx] + 1


N, M = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

ans = bfs(0, 0, N-1, M-1)
print(ans)