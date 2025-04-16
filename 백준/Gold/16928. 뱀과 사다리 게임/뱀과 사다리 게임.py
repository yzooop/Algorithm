import sys
from collections import deque
input = sys.stdin.readline

# bfs ----------------------------------------
def bfs():
    q = deque()
    q.append((1, 0))  # (현재 위치, 이동 횟수)
    v[1] = 1

    while q:
        c, cnt = q.popleft()

        for dice in range(1, 7):
            n = c + dice

            if n > 100:
                continue

            dest = arr[n]
            if v[dest] == 0:
                v[dest] = 1
                if dest == 100:
                    print(cnt + 1)
                    return
                q.append((dest, cnt + 1))

# 입력 ----------------------------------------
N, M = map(int, input().strip().split())
arr = [i for i in range(101)] 
v = [0] * 101
ladders = []
snakes = []

# 사다리
for _ in range(N):
    a, b = map(int, input().strip().split())
    ladders.append((a, b))

for x, y in ladders:
    arr[x] = y

# 뱀
for _ in range(M):
    a, b = map(int, input().strip().split())
    snakes.append((a, b))

for x, y in snakes:
    arr[x] = y

# 실행 ----------------------------------------
bfs()
