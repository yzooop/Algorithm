import sys
input = sys.stdin.readline

T = int(input().strip())

def factorial(n):
    if n == 0:
        return 1
    else:
        dp = [1, 1]
        for i in range(2, n+1):
            v = dp[i-1] * i
            dp.append(v)
        return dp[n]

for _ in range(T):
    n, m = map(int, input().strip().split())
    ans = factorial(m) // (factorial(m-n) * factorial(n))
    print(ans)
    