import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
arr = []

for i in range(1, N//2 + 1):
    if N % i == 0:
        arr.append(i)
arr.append(N)

if K > len(arr):
    print(0)
else:
    print(arr[K-1])