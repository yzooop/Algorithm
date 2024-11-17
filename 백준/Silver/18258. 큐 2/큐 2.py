from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
q = deque()

for _ in range(N):
    s = list(input().strip().split())

    # 1. push : 큐에 넣기
    if s[0] == "push":
        q.append(s[1])

    # 2. pop : 큐 맨앞에 정수 빼고 그 수 출력. 없으면 -1
    if s[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.popleft()
    
    # 3. size
    if s[0] == "size":
        print(len(q))

    # 4. empty
    if s[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)

    # 5. front
    if s[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    # 5. back
    if s[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])