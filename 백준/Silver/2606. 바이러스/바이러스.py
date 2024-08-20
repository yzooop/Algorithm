# ------------------------------------
def dfs(c):
    visited[c] = 1
    ans.append(c)
    
    for n in adj[c]:
        if visited[n] == 0:
            dfs(n)

# ------------------------------------
N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(1, N+1):
    adj[i].sort()

visited = [0] * (N+1)
ans = []
dfs(1)
print(len(ans)-1)