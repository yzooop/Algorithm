import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
  q = deque()
  q.append(node)
  v[node] = 1
  ans = 0

  while q:
    c = q.popleft()

    for n in arr[c]:
      if v[n] == 0:
        q.append(n)
        v[n] = 1
        parent[n] = c
  
  return ans


# 입력 및 초기화
N = int(input().strip())
arr = [[] for _ in range(N+1)]
v = [0] * (N+1)
parent = [0] * (N+1)

for _ in range(N-1):
  a, b = map(int, input().strip().split())
  arr[a].append(b)
  arr[b].append(a)

# 탐색
bfs(1)

# 정답
for i in range(2, N+1):
  print(parent[i])