import sys
input = sys.stdin.readline

N = int(input().strip())
card = set(map(int, input().strip().split()))

M = int(input().strip())
SG = list(map(int, input().strip().split()))

ans = []

for i in SG:
    if i in card:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)
