from collections import deque

def solution(x, y, n):
    v = set()
    q = deque()
    q.append((x, 0))

    while q:
        c, cnt = q.popleft()

        if c == y:
            return cnt

        for nx in (c + n, c * 2, c * 3):
            if nx <= y and nx not in v:
                v.add(nx)
                q.append((nx, cnt + 1))

    return -1
