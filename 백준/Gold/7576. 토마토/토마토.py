import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
  q = deque()
  for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))
            v[i][j] = 1  # 방문 + 익은 토마토로 시작

  while q:
    cy, cx = q.popleft()

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      ny, nx = cy + dy, cx + dx

      if (0<=ny<N and 0<=nx<M and v[ny][nx] == 0 and arr[ny][nx] != -1):
        q.append((ny, nx))
        v[ny][nx] = v[cy][cx] + 1
        

# 입력
M, N = map(int, input().strip().split()) # 가로, 세로
arr = [list(map(int, input().strip().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]

# 탐색
for i in range(N):
  for j in range(M):
    if arr[i][j] == 1 and v[i][j] == 0:
      bfs(i, j)

    if arr[i][j] == -1:
      v[i][j] = -1

# 정답
max_v = 0
is_tomato = 0

for i in range(N):
  for j in range(M):
    if v[i][j] == 0:
      is_tomato = 1
    else:
      max_v = max(max_v, v[i][j])

if is_tomato == 1:
  print(-1)
else:
  print(max_v - 1)