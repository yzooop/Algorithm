import sys
input = sys.stdin.readline

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    
    for j in range(1, N+1):
        dfs(n+1, lst + [j])

N, M = map(int, input().strip().split())
ans = []

dfs(0, [])

for row in ans:
    print(*row)
