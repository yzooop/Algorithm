def solution(priorities, location):
    p = priorities[:]
    ans = []
    idx = [i for i in range(len(priorities))]

    while p:
        current = p.pop(0)
        current_idx = idx.pop(0)

        if any(current < q for q in p):
            p.append(current)
            idx.append(current_idx)
        else:
            ans.append(current_idx)
            
            if current_idx == location:
                return len(ans)