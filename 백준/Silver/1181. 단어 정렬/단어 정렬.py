import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [input().strip() for _ in range(N)]
ans = []
arr.sort(key = lambda x : (len(x), x))

for i in arr:
    if i not in ans:
        ans.append(i)

for x in ans:
    print(x)