from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    v = [[0] * m for _ in range(n)]
    
    ans = bfs(0, 0, n-1, m-1, n, m, maps, v)
    
    if ans == 0: 
        return -1
    else: 
        return ans

def bfs(sy, sx, ey, ex, n, m, arr, v):
    q = deque()
    q.append((sy, sx))
    v[sy][sx] = 1
    
    while q:
        cy, cx = q.popleft()
        
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx
            
            if 0<=ny<n and 0<=nx<m and arr[ny][nx] == 1 and v[ny][nx] == 0:
                q.append((ny, nx))
                v[ny][nx] = v[cy][cx] + 1
                
    return v[n-1][m-1]
    