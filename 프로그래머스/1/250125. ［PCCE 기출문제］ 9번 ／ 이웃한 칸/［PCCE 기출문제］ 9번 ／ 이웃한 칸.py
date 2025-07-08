def solution(board, h, w):
    n = len(board)
    cnt = 0
    current_color = board[h][w]
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    
    for i in range(4):
        ny = dy[i] + h
        nx = dx[i] + w
        
        if 0<=ny<n and 0<=nx<n:
            if board[ny][nx] == current_color:
                cnt += 1
    
    return cnt
        