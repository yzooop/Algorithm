def solution(s):
    stack = []

    for letter in s:
        if letter == "(":
            stack.append(letter)
        else:
            if not stack:  # stack이 비어있으면 짝이 맞지 않음
                return False
            stack.pop()

    return len(stack) == 0  # 모든 괄호가 짝을 이루었는지 확인
