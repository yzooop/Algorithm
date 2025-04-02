import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx, v, color):
  q = deque()
  q.append((sy, sx))
  v[sy][sx] = 1
  cnt = 1

  while q:
    cy, cx = q.popleft()

    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      ny, nx = cy + dy, cx + dx

      if 0<=ny<M and 0<=nx<N and arr[ny][nx] == color and v[ny][nx] == 0:
        q.append((ny, nx))
        v[ny][nx] = 1
        cnt += 1
  return cnt



# 입력 및 초기화
N, M = map(int, input().strip().split()) # 가로 N, 세로 M
arr = [list(input().strip()) for _ in range(M)]
W_v = [[0] * N for _ in range(M)]
B_v = [[0] * N for _ in range(M)]
W_ans = []
B_ans = []

# 탐색
for i in range(M):
  for j in range(N):
    if arr[i][j] == 'W' and W_v[i][j] == 0:
      W_ans.append(bfs(i, j, W_v, 'W'))
    if arr[i][j] == 'B' and B_v[i][j] == 0:
      B_ans.append(bfs(i, j, B_v, 'B'))

# 정답
print(sum([x**2 for x in W_ans]), sum([x**2 for x in B_ans]))