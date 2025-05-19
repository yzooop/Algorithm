import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1
    cnt = 0

    while q:
        c = q.popleft()

        for n in arr[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = 1
                cnt += 1
                
    return cnt

# 입력 및 초기화
N, M = map(int, input().strip().split()) 
arr = [[] for _ in range(N+1)]
v = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().strip().split()) 
    arr[b].append(a)

X = int(input().strip())

# 탐색
print(bfs(X))

