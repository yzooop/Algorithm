def solution(n):
    ans = []
    ans.append(n)
    k = n
    
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        ans.append(k)
    return ans
        
        