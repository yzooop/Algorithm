from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    q = deque()
    q.append(node)
    v[node] = 1

    while q:
        current = q.popleft()

        for next in adj[current]:
            if v[next] == 0:
                q.append(next)
                v[next] = 1

N, M = map(int, input().strip().split())

# 기본 배열 입력받아서 구성하기
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().strip().split())
    adj[x].append(y)
    adj[y].append(x)

# 정렬
for i in range(1, N+1):
    adj[i].sort()

# 초기화
v = [0] * (N+1)
cnt = 0

# 인접행렬 순회하면서
for i in range(1, N+1):
    # 방문하지 않았으면 bfs 한 사이클 시작
    if v[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)