def solution(n, computers):
    global arr, v
    arr = []
    v = [0] * (n+1)
    for i in range(len(computers)):
        result = []
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                if i != j:
                    result.append(j+1)
        arr.append(result)
    arr = [[]] + arr
    
    ans = 0
    for x in range(1, n+1):
        if v[x] == 0:
            bfs(x)
            ans += 1
    return ans

def bfs(s):
    q = []
    q.append(s)
    v[s] = 1
    
    while q:
        c = q.pop(0)
        
        for n in arr[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = 1