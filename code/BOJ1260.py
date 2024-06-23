# dfs -------------------------------------
def dfs(current):
    ans_dfs.append(current)
    v_dfs[current] = 1

    for next in adj[current]:
        if not v_dfs[next]:
            dfs(next)


# bfs -------------------------------------
def bfs(start):
    q = [] # 큐 생성

    q.append(start)
    ans_bfs.append(start)
    v_bfs[start] = 1

    while q:
        current = q.pop(0) # 하나씩 빼서
        for next in adj[current]:
            if not v_bfs[next]:
                q.append(next)
                ans_bfs.append(next)
                v_bfs[next] = 1



# 입력 -------------------------------------

N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

for i in range(N+1):
    adj[i].sort()

# 답 -------------------------------------
v_dfs = [0] * (N+1)
ans_dfs = []
dfs(V)
print(ans_dfs)

v_bfs = [0] * (N+1)
ans_bfs = []
bfs(V)
print(ans_bfs)