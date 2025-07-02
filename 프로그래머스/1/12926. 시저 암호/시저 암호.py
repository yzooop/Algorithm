def solution(s, n):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    result = ''

    for char in s:
        if char == ' ':
            result += ' '
        elif char in upper:
            index = upper.index(char)
            result += upper[(index + n) % 26]
        elif char in lower:
            index = lower.index(char)
            result += lower[(index + n) % 26]

    return result
