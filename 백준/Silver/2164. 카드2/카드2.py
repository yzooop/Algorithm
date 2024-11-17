from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
q = deque([i+1 for i in range(N)])

for _ in range(N-1):
    q.popleft()
    q.append(q.popleft())
print(*q)
