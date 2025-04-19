import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1

    while q:
        cy, cx = q.popleft()

        # 종료조건

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx

            if (0<=ny<N and 0<=nx<M and v[ny][nx] == 0 and lab[ny][nx] == 0):
                q.append((ny, nx))
                v[ny][nx] = 1

# 입력
N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
empty = []
virus = []
ans = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 0:
            empty.append((i, j))

# 벽 3개
for walls in combinations(empty, 3):
    lab = [row[:] for row in arr]

    for y, x in walls:
        lab[y][x] = 1

    v = [[0] * M for _ in range(N)]

    # 바이러스 퍼뜨리기
    for sy, sx in virus:
        bfs(sy, sx)

    # 안전영역 계산
    safe = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0 and v[i][j] == 0:
                safe += 1
    
    ans = max(ans, safe)

print(ans)