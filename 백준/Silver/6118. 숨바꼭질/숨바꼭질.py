import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(node):
  q = deque()
  q.append(node)
  v[node] = 1

  while q:
    c = q.popleft()

    for n in arr[c]:
      if v[n] == 0:
        q.append(n)
        v[n] = v[c] + 1

# 입력
N, M = map(int, input().strip().split())
arr = [[] for _ in range(N+1)]
v = [0] * (N+1)

for _ in range(M):
  a, b = map(int, input().strip().split())
  arr[a].append(b)
  arr[b].append(a)

for i in arr:
  i.sort()

# 탐색
bfs(1)

# 정답
ans = max(v)
print(v.index(ans), ans - 1, v.count(ans))