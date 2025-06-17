def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if not isprime(i):
            answer += 1
    return answer - 1

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
