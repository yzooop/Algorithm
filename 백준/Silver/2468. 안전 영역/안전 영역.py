import sys
from collections import deque
input = sys.stdin.readline

def bfs(sy, sx, h):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
            ny, nx = cy+dy, cx+dx

            if 0<=ny<N and 0<=nx<N and v[ny][nx] == 0 and adj[ny][nx] > h:
                q.append((ny, nx))
                v[ny][nx] = 1

# 입력
N = int(input().strip())
adj = [list(map(int, input().strip().split())) for _ in range(N)]
max_h = max(max(row) for row in adj)
safe_area = 1

for h in range(1, max_h+1):
    v = [[0] * N for _ in range(N)]
    cnt = 0

    for y in range(N):
        for x in range(N):
            if adj[y][x] > h and v[y][x] == 0:
                bfs(y, x, h)
                cnt += 1
    
    safe_area = max(safe_area, cnt)
print(safe_area)