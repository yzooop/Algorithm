def solution(n):
    result = ""
    while n > 0:
        r = n % 3
        if r == 0:
            result = "4" + result
            n = (n // 3) - 1
        else:
            result = str(r) + result
            n = n // 3
    return result
