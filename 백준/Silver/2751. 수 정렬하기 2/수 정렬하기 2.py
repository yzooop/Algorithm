import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(int(input().strip()) for _ in range(N))
arr.sort()

for i in arr:
    print(i)