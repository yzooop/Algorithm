from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    return dfs(0, 0, n-1, m-1, n, m, maps)

def dfs(sy, sx, ey, ex, n, m, maps):
    q = deque()
    v = [[0] * m for _ in range(n)]
    
    q.append((sy, sx))
    v[sy][sx] = 1
    
    while q:
        cy, cx = q.popleft()
        
        # 종료조건
        if (cy, cx) == (ey, ex):
            return v[ey][ex]
            
        
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy+dy, cx+dx
            
            if 0<=ny<n and 0<=nx<m and v[ny][nx] == 0 and maps[ny][nx] == 1:
                q.append((ny, nx))
                v[ny][nx] = v[cy][cx] + 1
    return -1
        