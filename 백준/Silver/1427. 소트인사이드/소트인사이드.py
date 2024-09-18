import sys
input = sys.stdin.readline

N = list(input().strip())
ans = []
for i in N:
    i = int(i)
    ans.append(i)
    ans.sort(reverse=True)

for x in ans:
    x = str(x)
    print(x, end='')