def solution(park, routes):
    arr = [list(p) for p in park]
    n = len(arr)
    m = len(arr[0])

    # 출발 위치
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "S":
                sy, sx = i, j
                
    move = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
    
    for route in routes:
        d, num = route.split()
        num = int(num)
        dy, dx = move[d]
        
        ny, nx = sy, sx
        
        for _ in range(num):
            ny += dy
            nx += dx
            
            if (0<=ny<n and 0<=nx<m):
                if arr[ny][nx] == "X":
                    break
            else:
                break
        else:
            sy, sx = ny, nx
    return [sy, sx]
                    