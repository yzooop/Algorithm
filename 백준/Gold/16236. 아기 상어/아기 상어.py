from collections import deque
import sys
input = sys.stdin.readline

# bfs
def bfs(sy, sx, size):
    q = deque()
    q.append((sy, sx, 0)) #상어는 아직 이동안했으니까 거리 0에서 시작
    v = [[0] * N for _ in range(N)]
    fishes = []
    v[sy][sx] = 1

    while q:
        cy, cx, dist = q.popleft()

        # 물고기 찾으면 리스트에 추가
        if 0 < adj[cy][cx] < size:
            fishes.append((dist, cy, cx))

        # 네방향으로 이동
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ny, nx = cy + dy, cx + dx

            # 범위 내 + 방문 안했으면
            if 0<=ny<N and 0<=nx<N and v[ny][nx] == 0:
                # 상어가 지나갈 수 있으면
                if adj[ny][nx] <= size:
                    v[ny][nx] = 1
                    q.append((ny, nx, dist+1))
    
    # 먹을 수 있는 물고기가 여러마리면 거리순, 위쪽, 왼쪽 우선
    if fishes:
        fishes.sort()
        return  fishes[0]
    else:
        return None

# 초기 세팅
N = int(input().strip())
adj = [list(map(int, input().strip().split())) for _ in range(N)]
size = 2
fish_cnt = 0
time = 0

# 상어 위치
for y in range(N):
    for x in range(N):
        if adj[y][x] == 9:
            sy, sx = y, x
            adj[y][x] = 0

# 물고기 먹자
while True:
    result = bfs(sy, sx, size)

    # 먹을거 없으면 종료
    if result is None:
        break

    dist, cy, cx = result
    time += dist # 이동한 거리만큼 시간이 흐름
    sy, sx = cy, cx # 상어를 물고기가 있던 자리로 이동
    adj[cy][cx] = 0
    fish_cnt += 1

    if fish_cnt == size:
        size += 1
        fish_cnt = 0

print(time)