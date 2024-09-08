import sys
from collections import deque
input = sys.stdin.readline

# 숫자세는 bfs
def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1
    count = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx

            if 0<=ny<M and 0<=nx<N and adj[ny][nx] == 1 and v[ny][nx] == 0:
                q.append((ny, nx))
                v[ny][nx] = 1
                count += 1
        
    return count

        

# 입력받고 배열 만들기
M, N, K = map(int, input().strip().split())
adj = [[1] * N for _ in range(M)]
v = [[0] * N for _ in range(M)]
cnt = 0
ans = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for y in range(M - y2, M - y1):
        for x in range(x1, x2):
            adj[y][x] = 0

# 배열 돌면서 bfs 하기
for y in range(M):
    for x in range(N):
        if v[y][x] == 0 and adj[y][x] == 1:
            ans.append(bfs(y, x))
            cnt += 1

print(cnt)
print(*sorted(ans))
