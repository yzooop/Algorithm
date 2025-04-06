import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
  q = deque()
  q.append((sy, sx))
  v[sy][sx] = 1

  while q:
    cy, cx = q.popleft()

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      ny, nx = cy + dy, cx + dx

      if (0<=ny<5 and 0<=nx<5 and v[ny][nx] == 0 and arr[ny][nx] != -1):
        q.append((ny, nx))
        v[ny][nx] = v[cy][cx] + 1
        

# 입력
arr = [list(map(int, input().strip().split())) for _ in range(5)]
v = [[0] * 5 for _ in range(5)]
r, c = map(int, input().strip().split())

for i in range(5):
  for j in range(5):
    if arr[i][j] == 1:
      ey, ex = i, j

# 탐색
bfs(r, c)

# 정답
if v[ey][ex] == 0:
  print(-1)
else:
  print(v[ey][ex] - 1)