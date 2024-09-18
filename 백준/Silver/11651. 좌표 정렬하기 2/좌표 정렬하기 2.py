import sys
input = sys.stdin.readline

arr = []
N = int(input().strip())
for _ in range(N):
    x, y = map(int, input().strip().split())
    arr.append([x, y])

arr.sort(key=lambda x: (x[1], x[0]))

for row in arr:
    print(row[0], row[1])