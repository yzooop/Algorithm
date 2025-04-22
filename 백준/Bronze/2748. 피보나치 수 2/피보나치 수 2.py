import sys
input = sys.stdin.readline

n = int(input().strip())

# 초기값
dp = [0, 1]

# 점화식
for i in range(2, n+1):
    ans = dp[i-2] + dp[i-1]
    dp.append(ans)

print(dp[n])