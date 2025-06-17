def solution(spell, dic):
    origin = sorted(spell)
    
    for d in dic:
        d = sorted(d)
        
        if d == origin:
            return 1
    
    return 2