def solution(n):
    ans = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                ans[i][j] = 1
    
    return ans