import sys
from collections import deque
input = sys.stdin.readline

def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)):
            ny, nx = cy+dy, cx+dx

            if 0<=ny<N and 0<=nx<M and v[ny][nx] == 0 and adj[ny][nx] == 1:
                q.append((ny, nx))
                v[ny][nx] = 1


while True:
    # 가, 세
    M, N = map(int, input().strip().split())
    if M == 0 and N == 0:
        break
    
    # 인접행렬 입력
    adj = [list(map(int, input().strip().split())) for _ in range(N)]

    v = [[0] * M for _ in range(N)]
    cnt = 0

    for y in range(N):
        for x in range(M):
            if adj[y][x] == 1 and v[y][x] == 0:
                bfs(y, x)
                cnt += 1

    print(cnt)
