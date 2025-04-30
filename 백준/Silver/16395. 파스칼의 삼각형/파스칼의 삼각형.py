import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    dp[1][j] = 1
  dp[i][1] = 1


for i in range(2, n+1):
  for j in range(2, n+1):
    if i + j <= n+1: 
      dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[n+1-k][k])