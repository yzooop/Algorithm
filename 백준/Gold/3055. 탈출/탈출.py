import sys
from collections import deque
input = sys.stdin.readline

def bfs(sy, sx, ey, ex):
    q = deque()
    v = [[0] * C for _ in range(R)]

    # 물 퍼지는거 먼저
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "*":
                q.append(('*', i, j))
    
    # 담에 고슴도치
    q.append(('S', sy, sx))
    v[sy][sx] = 1

    while q:
        type, cy, cx = q.popleft()

        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx

            if 0<=ny<R and 0<=nx<C:
                if type == "*": # 물
                    if arr[ny][nx] == ".":
                        arr[ny][nx] = "*"
                        q.append(('*', ny, nx))
                
                elif type == "S": # 고슴도치
                    # 종료조건
                    if arr[ny][nx] == "D":
                        print(v[cy][cx])
                        return

                    if arr[ny][nx] == "." and v[ny][nx] == 0:
                        v[ny][nx] = v[cy][cx] + 1
                        q.append(('S', ny, nx))
    
    print("KAKTUS")


R, C = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == "D":
            ey, ex = i, j
        elif arr[i][j] == "S":
            sy, sx = i, j
        
bfs(sy, sx, ey, ex)