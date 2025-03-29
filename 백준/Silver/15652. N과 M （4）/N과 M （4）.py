import sys
input = sys.stdin.readline

def dfs(n, lst, start):
    if n == M:
        ans.append(lst)
        return
    
    for j in range(start, N+1):
        dfs(n+1, lst + [j], j)

N, M = map(int, input().strip().split())
ans = []

dfs(0, [], 1)

for row in ans:
    print(*row)
