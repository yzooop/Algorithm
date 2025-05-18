import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(sy, sx):
  q = deque()
  q.append((sy, sx))
  v[sy][sx] = 1
  wolf, sheep = 0, 0

  while q:
    cy, cx = q.popleft()

    if arr[cy][cx] == "v":
      wolf += 1

    if arr[cy][cx] == "k":
      sheep += 1
    
    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
      ny, nx = cy + dy, cx + dx

      if 0<=ny<R and 0<=nx<C and arr[ny][nx] != '#' and v[ny][nx] == 0:
        q.append((ny, nx))
        v[ny][nx] = 1
  return [wolf, sheep]

# 입력 및 초기화
R, C = map(int, input().strip().split()) # 세로 가로
arr = [list(input().strip()) for _ in range(R)]
v = [[0] * C for _ in range(R)]
answers = []
wolf, sheep = 0, 0

# 탐색
for i in range(R):
  for j in range(C):
    if arr[i][j] != '#' and v[i][j] == 0:
      answers.append(bfs(i, j))

# 정답
for ans in answers:
  if ans[0] >= ans[1]:
    ans[1] = 0
  else :
    ans[0] = 0

  wolf += ans[0]
  sheep += ans[1]
  
print(sheep, wolf)