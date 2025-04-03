import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    v[start] = 1

    ans = 0

    while q:
        current = q.popleft()

        for neighbor in adj[current]:
            if v[neighbor] == 0:
                v[neighbor] = v[current] + 1
                if v[neighbor] <= 3:
                    ans += 1
                q.append(neighbor)
    return ans

N = int(input().strip())
M = int(input().strip())
adj = [[] for _ in range(N + 1)]
v = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().strip().split())
    adj[a].append(b)
    adj[b].append(a)

print(bfs(1))
