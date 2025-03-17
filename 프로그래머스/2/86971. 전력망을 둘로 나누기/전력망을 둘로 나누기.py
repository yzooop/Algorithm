from collections import deque

def solution(n, wires):
    # 배열 구성
    adj = [[] for _ in range(n+1)]
    v = [0] * (n+1)

    for wire in wires:
        adj[wire[0]].append(wire[1])
        adj[wire[1]].append(wire[0])

    # bfs
    def bfs(node):
        q = deque()
        q.append(node)
        v[node] = 1
        ans = 1
        
        while q:
            c = q.popleft()
            
            for next_node in adj[c]:
                if v[next_node] == 0:
                    q.append(next_node)
                    v[next_node] = 1
                    ans += 1
        return ans

    min_diff = float('inf')

    # 전선 제거
    for v1, v2 in wires:
        adj[v1].remove(v2)
        adj[v2].remove(v1)
        
        # BFS 실행
        v = [0] * (n+1)
        cnt1 = bfs(v1) 
        cnt2 = n - cnt1

        # 최소 차이 갱신
        min_diff = min(min_diff, abs(cnt1 - cnt2))

        # 전선 다시 복구
        adj[v1].append(v2)
        adj[v2].append(v1)

    return min_diff
