def solution(clothes):
    dic = {}
    
    for item, category in clothes:
        # 있으면 추가하고
        if category in dic:
            dic[category] += 1
        # 없으면 생성
        else:
            dic[category] = 1
    
    ans = 1
    for key, value in dic.items():
        ans *= (value + 1)
    
    return ans-1
    