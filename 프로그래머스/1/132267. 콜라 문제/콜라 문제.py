def solution(a, b, n):
    ans = 0
    while n >= a:
        coke = (n // a) * b
        ans += coke
        n = (n % a) + coke
    return ans
