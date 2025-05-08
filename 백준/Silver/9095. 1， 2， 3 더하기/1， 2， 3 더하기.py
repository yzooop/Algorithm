import sys
input = sys.stdin.readline

T = int(input().strip())
dp = [0, 1, 2, 4] + [0] * 8

for i in range(4, 12):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
  n = int(input().strip())
  print(dp[n])
