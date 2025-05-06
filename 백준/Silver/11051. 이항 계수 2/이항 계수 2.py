import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0:
        return 1
    else:
        dp = [1, 1]
        for i in range(2, n+1):
            v = dp[i-1] * i
            dp.append(v)
        return dp[n]

N, K = map(int, input().strip().split())
ans = factorial(N) // (factorial(N-K) * factorial(K))
print(ans % 10007)