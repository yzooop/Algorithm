import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_iterative(start):
    stack = [start]
    order = 1
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = order
            order += 1
            for next_node in sorted(adj[node], reverse=True):
                if visited[next_node] == 0:
                    stack.append(next_node)

N, M, R = map(int, input().strip().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().strip().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [0] * (N + 1)
dfs_iterative(R)

for i in range(1, N + 1):
    print(visited[i])
