import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(s, e):
  q = deque()
  q.append((s, 0))
  v = [0] * (N+1)
  v[s] = 1
  
  while q:
    c, dist = q.popleft()

    # 종료조건
    if c == e:
      return dist
    
    for n, d in arr[c]:
      if v[n] == 0:
        q.append((n, dist + d))
        v[n] = 1
  
  

# 입력 및 초기화
N, M = map(int, input().strip().split())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
  a, b, c = map(int, input().strip().split())
  arr[a].append((b, c))
  arr[b].append((a, c))

# 정답
for _ in range(M):
  s, e = map(int, input().strip().split())
  print(bfs(s, e))