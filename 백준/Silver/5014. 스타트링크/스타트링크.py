import sys
from collections import deque
input = sys.stdin.readline

# bfs
def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()

        # 종료조건
        if c == G:
            return v[c] - 1

        for n in (c + U, c - D):
            if 1<=n<=F and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1

    return -1


# 입력
F, S, G, U, D = map(int, input().strip().split())
v = [0] * (F + 1)

ans = bfs(S)

if ans == -1:
    print("use the stairs")
else:
    print(ans) 
