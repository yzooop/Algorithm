import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    a = list(input().strip())
    stack = []

    for i in a:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(" :
                stack.pop(-1)
            else:
                stack.append(i)

    if stack:
        print("NO")
    else:
        print("YES")