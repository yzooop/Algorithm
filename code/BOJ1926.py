import sys

def bfs(si, sj):
    q = []
    q.append((si, sj))

    v[si][sj] = 1
    cnt = 1

    while q:
       ci, cj = q.pop(0)

       for  di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
           ni, nj = ci + di, cj + dj

           if 0<=ni<n and 0<=nj<m and arr[ni][nj] == 1 and v[ni][nj] == 0:
               q.append((ni, nj))
               v[ni][nj] = 1
               cnt += 1
    return  cnt

n, m = map(int, sys.stdin.readline().strip().split())

arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]


ans = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
print(ans[-1])
