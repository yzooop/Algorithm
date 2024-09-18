import sys
input = sys.stdin.readline

arr = []
N = int(input().strip())
for _ in range(N):
    x, y = map(int, input().strip().split())
    arr.append([x, y])

arr.sort()

for row in arr:
    for col in row:
        print(col, end=" ")
    print()