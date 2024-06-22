import sys 

N = int(sys.stdin.readline().strip())
mid = N // 2

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

arr = [[0] * N for _ in range(N)]

i, j, cnt, dr = mid, mid, 1, 0
arr[i][j] = cnt
cnt += 1


length = 1
while cnt <= N * N:
    for _ in range(2):  # 같은 길이로 두 번 회전
        for _ in range(length):
            ni, nj = i + di[dr], j + dj[dr]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                i, j = ni, nj
                arr[i][j] = cnt
                cnt += 1
        dr = (dr + 1) % 4  # 방향 전환
    length += 1  # 한 단계 더 나아감




for row in arr:
    print(row)