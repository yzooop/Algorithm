def solution(board):
    n = len(board)
    v = [[0] * n for _ in range(n)]
    
    for cy in range(n):
        for cx in range(n):
            if board[cy][cx] == 1:
                for dy, dx in ((-1, -1), (0, -1), (1, -1), 
                               (-1, 0), (0, 0), (1, 0), 
                               (-1, 1), (0, 1), (1, 1)):
                    ny, nx = dy + cy, dx + cx

                    if 0<=ny<n and 0<=nx<n:
                        v[ny][nx] = 1

    ans = 0
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                ans += 1
    
    return ans