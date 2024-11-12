from collections import deque

def solution(numbers, target):
    q = deque()
    q.append((0, 0))
    ans = 0
    
    while q:
        current_sum, idx = q.popleft()
        
        # 종료조건
        if idx == len(numbers):
            if current_sum == target:
                ans += 1
        else:
            q.append((current_sum + numbers[idx], idx + 1))
            q.append((current_sum - numbers[idx], idx + 1))
    return ans