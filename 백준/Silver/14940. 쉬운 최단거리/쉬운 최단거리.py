import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0  # 시작 지점 거리 0

    while q:
        y, x = q.popleft()

        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < m:
                # 갈 수 있는 땅이고 아직 방문 안 했으면
                if arr[ny][nx] == 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
                    
# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 거리 배열 초기화
dist = [[-1] * m for _ in range(n)]

# 목표지점 찾기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            sy, sx = i, j

# BFS 실행
bfs(sy, sx)

# 결과 출력
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()