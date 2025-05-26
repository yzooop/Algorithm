def solution(board, moves):
    basket = []
    cnt = 0

    N = len(board)
    
    for m in moves:
        col = m - 1
        
        for row in range(N):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0
                
                if basket and basket[-1] == doll:
                    basket.pop()
                    cnt += 2
                else:
                    basket.append(doll)
                break
                
    return cnt
