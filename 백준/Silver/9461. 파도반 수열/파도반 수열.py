import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
  N = int(input().strip())

  dp = [0, 1, 1]

  for i in range(3, N+1):
    ans = dp[i-3] + dp[i-2]
    dp.append(ans)

  print(dp[N])
