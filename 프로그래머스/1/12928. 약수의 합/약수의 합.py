def solution(n):
    sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            sum += i
    
    sum += n
    return sum