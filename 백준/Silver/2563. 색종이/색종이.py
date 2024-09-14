import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().strip().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] = 1

cnt = 0
for row in arr:
    cnt += row.count(1)
print(cnt)