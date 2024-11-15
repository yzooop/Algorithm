import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []

for _ in range(N):
    a = list(map(int, input().strip().split()))
    
    # 1번 : 정수를 스택에 넣는다
    if len(a) == 2:
        stack.append(a[1])

    elif len(a) == 1:
        # 2번 : 마지막 수 스택에서 빼고 출력. 없으면 -1
        if a[0] == 2:
            if len(stack) >= 1:
                print(stack[-1])
                stack.pop(-1)
            else:
                print(-1)

        # 3번 : 스택 len    
        elif a[0] == 3:
            print(len(stack))

        # 4번 : 스택이 빈지 아닌지
        elif a[0] == 4:
            if len(stack) == 0:
                print(1)
            else:
                print(0)

        # 5번 : 스택이 비지 않았다면 맨 위의 정수 출력. 없으면 -1
        elif a[0] == 5:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
