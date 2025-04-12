import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx, ey, ex):
  q = deque()

  q.append((sy, sx))
  v[sy][sx] = 1

  while q:
    cy, cx = q.popleft()

    # 종료조건
    if (cy, cx) == (ey, ex):
      return v[cy][cx]

    for dy, dx in ((2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
      ny, nx = dy + cy, dx + cx

      if 0<=ny<I and 0<=nx<I and v[ny][nx] == 0:
        q.append((ny, nx))
        v[ny][nx] = v[cy][cx] + 1
  
  return v

# 입력
T = int(input().strip())

for _ in range(T):
  I = int(input().strip())
  v = [[0] * I for _ in range(I)]
  sy, sx = map(int, input().strip().split())
  ey, ex = map(int, input().strip().split())
  
  # 탐색
  print(bfs(sy, sx, ey, ex) - 1)
