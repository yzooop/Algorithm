import sys
from collections import deque
input = sys.stdin.readline


# bfs
def bfs(sy, sx):
  q = deque()
  q.append((sy, sx))
  v[sy][sx] = 1
  cnt = 1

  while q:
    cy, cx = q.popleft()

    for dy, dx in ((1, 0), (-1, 0), (0, -1), (0, 1)):
      ny, nx = cy + dy, cx + dx

      if (0<=ny<N and 0<=nx<M and arr[ny][nx] == 1 and v[ny][nx] == 0):
        q.append((ny, nx))
        v[ny][nx] = 1
        cnt += 1

  return cnt
    


# 입력 및 초기화
N, M, K = map(int, input().strip().split())
arr = [[0] * M for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = []


for _ in range(K):
  a, b = map(int, input().strip().split())
  arr[a-1][b-1] = 1

# 탐색
for i in range(N):
  for j in range(M):
    if arr[i][j] == 1 and v[i][j] == 0:
      ans.append(bfs(i, j))

# 정답
print(max(ans))