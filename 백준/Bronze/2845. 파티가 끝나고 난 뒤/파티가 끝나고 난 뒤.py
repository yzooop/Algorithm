import  sys
input = sys.stdin.readline

L, P = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

for i in range(len(arr)):
    arr[i] = arr[i] - (L * P)

print(*arr)