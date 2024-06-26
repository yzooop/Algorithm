import sys

M, N = map(int, sys.stdin.readline().strip().split())

arr = [[0] * N for _ in range(M)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

i, j, cnt, dr = 0, 0, 1, 0
arr[i][j] = cnt
cnt += 1
ans = 0

while cnt <= M*N:
    ni, nj = i + di[dr], j + dj[dr]

    if 0<=ni<M and 0<=nj<N and arr[ni][nj] == 0:
        i, j = ni, nj
        arr[i][j] = cnt
        cnt += 1
    else:
        dr = (dr + 1) % 4
        ans += 1

print(ans)

target = M * N

for row in range(M):
    for col in range(N):
        if arr[row][col] == target:
            print(row+1, col+1)
            break