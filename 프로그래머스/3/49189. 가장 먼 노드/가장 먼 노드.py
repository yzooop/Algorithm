from collections import deque

def solution(n, edge):
    # 1. 배열 만들기
    arr = [[] for _ in range(n+1)]
    for i in edge:
        arr[i[0]].append(i[1])
        arr[i[1]].append(i[0])
    
    result = bfs(1, n, arr)
    max_result = max(result)
    
    ans = result.count(max_result)
    return ans
    
def bfs(start, n, arr):
    q = deque()
    v = [0] * (n+1)
    
    q.append(start)
    v[start] = 1
    
    while q:
        c = q.popleft()
        
        for n in arr[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
    return v
    