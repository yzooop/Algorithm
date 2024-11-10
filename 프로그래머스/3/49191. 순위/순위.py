from collections import deque

def bfs(start, graph, n):
    q = deque()
    q.append(start)
    v = [0] * (n + 1)
    v[start] = 1
    cnt = 0

    while q:
        current = q.popleft()

        for next in graph[current]:
            if v[next] == 0:
                q.append(next)
                v[next] = 1
                cnt += 1

    return cnt

def solution(n, results):
    # 이긴 선수, 진 선수 정보를 담을 그래프 생성
    arr = [[] for _ in range(n + 1)]
    reverse_arr = [[] for _ in range(n + 1)]
    
    # 그래프 구성
    for win, lose in results:
        arr[win].append(lose)      # 이긴 선수
        reverse_arr[lose].append(win)  # 진 선수

    # 정확한 순위를 매길 수 있는 선수의 수
    answer = 0

    # 각 선수에 대해 탐색
    for i in range(1, n + 1):
        win_count = bfs(i, arr, n)       # i 선수가 이긴 선수의 수
        lose_count = bfs(i, reverse_arr, n)  # i 선수를 이긴 선수의 수

        # 이긴 선수 + 진 선수 == n-1 인 경우 순위를 정확히 매길 수 있음
        if win_count + lose_count == n - 1:
            answer += 1

    return answer