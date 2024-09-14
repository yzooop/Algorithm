import sys
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(5)]

for x in range(15):
    for y in range(5):
        if x < len(arr[y]):
            print(arr[y][x], end="")