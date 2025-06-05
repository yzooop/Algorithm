def solution(data, ext, val_ext, sort_by):
    col = ["code", "date", "maximum", "remain"]
    ext_idx = col.index(ext)
    sort_idx = col.index(sort_by)
    
    ans = []
    
    for d in data:
        if d[ext_idx] < val_ext:
            ans.append(d)
    
    sorted_ans = sorted(ans, key=lambda x:x[sort_idx])
    return sorted_ans