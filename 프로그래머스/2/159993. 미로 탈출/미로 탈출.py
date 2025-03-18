from collections import deque

def solution(maps):
    sy, sx, ey, ex, ly, lx = -1, -1, -1, -1, -1, -1
    adj = [list(m) for m in maps]
    
    # 좌표 저장
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "S":
                sy, sx = y, x
            if maps[y][x] == "E":
                ey, ex = y, x
            if maps[y][x] == "L":
                ly, lx = y, x
    
    # start -> lever
    s_to_l = bfs(sy, sx, ly, lx, maps, adj)
    if s_to_l == -1:
        return -1
    
    l_to_e = bfs(ly, lx, ey, ex, maps, adj)
    if l_to_e == -1:
        return -1
    
    return s_to_l + l_to_e
    
            
    
    
    
    
def bfs(sy, sx, ey, ex, maps, adj):
    q = deque([(sy, sx)])
    v = [[-1] * len(maps[0]) for _ in range(len(maps))]
    v[sy][sx] = 0
    
    
    while q:
        cy, cx = q.popleft()
        
        if (cy, cx) == (ey, ex):
            return v[cy][cx]
        
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = dy + cy, dx + cx
            
            if (0<=ny<len(maps) and 0<=nx<len(maps[0]) and adj[ny][nx] != "X" and v[ny][nx] == -1):
                q.append((ny, nx))
                v[ny][nx] = v[cy][cx] + 1
    return -1