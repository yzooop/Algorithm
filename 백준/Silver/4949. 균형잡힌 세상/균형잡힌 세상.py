import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == ".":
        break

    stack = []
    balanced = True

    for char in line:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balanced = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balanced = False
                break

    # 스택이 비어있고, balanced가 True면 균형이 맞는 문자열
    if balanced and not stack:
        print("yes")
    else:
        print("no")
