def solution(x, n):
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = x
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + x
    
    return dp[1:]