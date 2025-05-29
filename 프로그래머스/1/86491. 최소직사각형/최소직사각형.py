def solution(sizes):
    arr = [(max(w, h), min(w, h)) for w, h in sizes]
    max_w = max([w for w, h in arr])
    max_h = max([h for w, h in arr])
    
    return max_w * max_h
