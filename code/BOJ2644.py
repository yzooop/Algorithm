def bfs(start, end):
    q = []
    visited = [0] * (N+1)

    q.append(start)
    visited[start] = 1

    while q:
        current = q.pop(0)
        
        if current == end:
            return visited[end] - 1

        for next in adj[current]:
            if visited[next] == 0:
                q.append(next)
                visited[next] += visited[current] + 1

    return -1

# 입력
N = int(input())
S, E = map(int, input().split())
M = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

ans = bfs(S, E)
print(ans)