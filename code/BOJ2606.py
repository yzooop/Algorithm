import sys

def bfs(node):
    q = []
    q.append(node)

    v[node] = 1

    cnt = 0

    while q:
        current = q.pop(0)
        cnt += 1

        for next in adj[current]:
            if v[next] == 0:
                q.append(next)
                v[next] = 1
    return cnt


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    adj[start].append(end)
    adj[end].append(start)

v = [0] * (N+1)
result = bfs(1)
print(result-1)