from collections import deque
import sys
input = sys.stdin.readline

def bfs(sy, sx, adj, v):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1
    color = adj[sy][sx] # 시작시점의 색깔

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy+dy, cx+dx

            if 0<=ny<N and 0<=nx<N and adj[ny][nx] == color and v[ny][nx] == 0:
                q.append((ny, nx))
                v[ny][nx] = 1



N = int(input().strip())
# 일반인 배열
adj = list(list(map(str, input().strip())) for _ in range(N))

# 적록색맹 배열
new_adj = []
for row in adj:
    new_row = []
    for i in range(len(row)):
        if row[i] == "R":
            new_row.append("G")
        else:
            new_row.append(row[i])
    new_adj.append(new_row)

normal_v = [[0] * N for _ in range(N)]
blind_v = [[0] * N for _ in range(N)]

normal_cnt = 0
blind_cnt = 0

for y in range(N):
    for x in range(N):

        # 일반인
        if normal_v[y][x] == 0:
            bfs(y, x, adj, normal_v)
            normal_cnt += 1
        
        # 색맹
        if blind_v[y][x] == 0:
            bfs(y, x, new_adj, blind_v)
            blind_cnt += 1

print(normal_cnt, blind_cnt)