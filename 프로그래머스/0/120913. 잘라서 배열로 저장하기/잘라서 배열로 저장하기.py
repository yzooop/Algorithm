import math

def solution(my_str, n):
    ans = []
    times = math.ceil(len(my_str) / n)
    
    for i in range(1, times + 1):
        ans.append(my_str[(i-1) * n : i * n])
    
    return ans