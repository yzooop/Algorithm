from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    # 초기 : 출발공항, 경로, 쓴 티켓
    q.append(("ICN",["ICN"], []))
    
    while q:
        # 현재 공항, 지금까지 간 경로, 쓴 티켓 인덱스
        airport, path, used = q.popleft()

        # 종료조건 : 쓴 티켓길이 = 티켓 원래길이
        if len(used) == len(tickets):
            answer.append(path)
        
        # 모든 티켓 순회하면서 현재 airport 에서 출발하는 티켓 찾는다.
        for idx, ticket in enumerate(tickets):
            # ticket[0]은 출발지. 현재공항에서 출발하는 티켓만 & 새 티켓만
            if ticket[0] == airport and not idx in used:
                # 큐에 목적지 공항추가, 원래 경로에 목적지 추가, 티켓 추가
                q.append((ticket[1], path+[ticket[1]], used+[idx]))
                
    answer.sort()

    return answer[0]