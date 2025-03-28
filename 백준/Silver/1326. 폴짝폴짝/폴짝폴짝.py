from collections import deque

def min_jumps(N, stones, a, b):
    a, b = a - 1, b - 1
    queue = deque([(a, 0)])
    visited = [False] * N
    visited[a] = True

    while queue:
        current, jumps = queue.popleft()

        if current == b:
            return jumps

        step = stones[current]

        # 앞으로 점프
        next_pos = current + step
        while next_pos < N:
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jumps + 1))
            next_pos += step

        # 뒤로
        next_pos = current - step
        while next_pos >= 0:
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jumps + 1))
            next_pos -= step

    return -1


N = int(input())
stones = list(map(int, input().split())) 
a, b = map(int, input().split()) 


print(min_jumps(N, stones, a, b))
