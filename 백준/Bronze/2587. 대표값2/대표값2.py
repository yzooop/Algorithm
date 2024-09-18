import sys
input = sys.stdin.readline

arr = list(int(input().strip()) for _ in range(5))
arr.sort()

avg = sum(arr) / len(arr)
mid = arr[2]

print(int(avg))
print(mid)
