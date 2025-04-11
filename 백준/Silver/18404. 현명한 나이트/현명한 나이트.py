import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
  q = deque()
  v = [[0] * N for _ in range(N)]

  q.append((sy, sx))
  v[sy][sx] = 1

  while q:
    cy, cx = q.popleft()

    for dy, dx in ((2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
      ny, nx = dy + cy, dx + cx

      if 0<=ny<N and 0<=nx<N and v[ny][nx] == 0:
        q.append((ny, nx))
        v[ny][nx] = v[cy][cx] + 1
  
  return v

# 입력
N, M = map(int, input().strip().split())
ky, kx = map(int, input().strip().split()) # 나이트 위치
targets = [tuple(map(int, input().strip().split())) for _ in range(M)]

# 탐색
dist = bfs(ky-1, kx-1)

# 정답
ans = []
for ey, ex in targets:
  ans.append(dist[ey-1][ex-1] - 1)

print(*ans)