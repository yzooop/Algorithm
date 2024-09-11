import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1

    p_cnt = 0

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx

            # 범위 안 벗어나게
            if 0<=ny<N and 0<=nx<M and v[ny][nx] == 0:

                # 빈 공간이거나 사람이면 이동
                if adj[ny][nx] == "O" or adj[ny][nx] == "P":
                    q.append((ny, nx))
                    v[ny][nx] = 1

                    if adj[ny][nx] == "P":
                        p_cnt += 1
    return p_cnt

# 입력
N, M = map(int, input().strip().split())
adj = [[i for i in map(str, input().strip())] for _ in range(N)]
v = [[0]* M for _ in range(N)]

# 도연 위치 확보
for y in range(N):
    for x in range(M):
        if adj[y][x] == 'I':
            i_y, i_x = y, x

ans = bfs(i_y, i_x)

if ans == 0:
    print("TT")
else:
    print(ans)
