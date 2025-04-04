import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
  q = deque()
  q.append((sy, sx))
  v[sy][sx] = 1
  cnt = 0

  while q:
    cy, cx = q.popleft()

    for dy, dx in ((1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
      ny, nx = cy + dy, cx + dx

      if 0<=ny<M and 0<=nx<N and v[ny][nx] == 0 and arr[ny][nx] == 1:
        q.append((ny, nx))
        v[ny][nx] = 1
        cnt += 1
  return cnt

# 입력 (세로, 가로)
M, N = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(M)]
v = [[0] * N for _ in range(M)]
ans = []

# 탐색
for i in range(M):
  for j in range(N):
    if arr[i][j] == 1 and v[i][j] == 0:
      ans.append(bfs(i, j))

# 정답
print(len(ans))