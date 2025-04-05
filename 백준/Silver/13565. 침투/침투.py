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

    # 종료조건
    if cy == M - 1:
      return True

    for dy, dx in ((1, 0), (-1, 0), (0, -1), (0, 1)):
      ny, nx = cy + dy, cx + dx

      if 0<=ny<M and 0<=nx<N and v[ny][nx] == 0 and arr[ny][nx] == 0:
        q.append((ny, nx))
        v[ny][nx] = 1
        
  return False

# 입력 (세로, 가로)
M, N = map(int, input().strip().split())
arr = [list(map(int, input().strip())) for _ in range(M)]
v = [[0] * N for _ in range(M)]

# 탐색
for j in range(N):
  if arr[0][j] == 0 and v[0][j] == 0:
    if bfs(0, j):
      print("YES")
      break

else:
  print("NO")