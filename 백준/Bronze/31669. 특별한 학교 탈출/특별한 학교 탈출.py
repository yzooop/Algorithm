import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [input().strip() for _ in range(N)]
X_count = [[] for _ in range(M)]

for i in range(M):
    for s in arr:
        X_count[i].append(s[i])

ans = []

for row in X_count:
    ans.append(row.count('X'))

if N in ans:
    print(ans.index(N) + 1)
else:
    print("ESCAPE FAILED")