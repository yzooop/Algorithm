def solution(nums):
    answer = len(set(nums))
    n = len(nums) // 2
    
    if answer > n:
        return n
    return answer