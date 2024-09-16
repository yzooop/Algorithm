import sys
input = sys.stdin.readline

left = []
right = []

for _ in range(3):
    x, y = map(int, input().strip().split())
    left.append(x)
    right.append(y)

for i in left:
    if left.count(i) == 1:
        print(i, end=" ")

for i in right:
    if right.count(i) == 1:
        print(i)