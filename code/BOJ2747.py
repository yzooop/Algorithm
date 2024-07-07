import sys

n = int(sys.stdin.readline().strip())

dp = [0] * (n + 1)

# dp[i] : i번째 피보나치 수
dp[0], dp[1] = 0, 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])