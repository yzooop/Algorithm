from collections import deque
import sys
input = sys.stdin.readline

T = int(input().strip())

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
            ny, nx = cy + dy, cx + dx

            if 0<=ny<N and 0<=nx<M and v[ny][nx] == 0 and arr[ny][nx] == 1:
                q.append((ny, nx))
                v[ny][nx] = 1

for _ in range(T):
    M, N, K = map(int, input().strip().split())

    # 배열 만들기
    arr = [[0] * M for _ in range(N)]
    v = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().strip().split())
        arr[y][x] = 1
    
    cnt = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1 and v[y][x] == 0:
                bfs(y, x)
                cnt += 1
    print(cnt)