import sys


def dfs(node):
    ans_dfs.append(node)
    v_dfs[node] = 1

    for next in adj[node]:
        if v_dfs[next] == 0:
            dfs(next)


def bfs(start):
    q = []
    q.append(start)
    ans_bfs.append(start)
    v_bfs[start] = 1

    while q:
        current = q.pop(0)
        for next in adj[current]:
            if v_bfs[next] == 0:
                q.append(next)
                ans_bfs.append(next)
                v_bfs[next] = 1
    return


N, M, V = map(int, sys.stdin.readline().strip().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(N+1):
    adj[i].sort()


v_dfs = [0] * (N+1)
v_bfs = [0] * (N+1)

ans_dfs = []
ans_bfs = []

bfs(V)
dfs(V)

print(ans_dfs)
print(ans_bfs)
