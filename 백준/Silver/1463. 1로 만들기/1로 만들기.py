import sys
input = sys.stdin.readline

N = int(input().strip())
dp = [0] * (N+1)
INF = 10 ** 6 + 1

for i in range(2, N+1):
  dp[i] = min(
    dp[i - 1],
    dp[i // 2] if i % 2 == 0 else INF,
    dp[i // 3] if i % 3 == 0 else INF
  ) + 1

print(dp[N])