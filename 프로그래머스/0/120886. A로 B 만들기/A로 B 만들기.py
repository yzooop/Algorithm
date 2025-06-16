def solution(before, after):
    obj_b = {}
    obj_a = {}
    
    for i in before:
        if i in obj_b:
            obj_b[i] += 1
        else:
            obj_b[i] = 1
    
    for i in after:
        if i in obj_a:
            obj_a[i] += 1
        else:
            obj_a[i] = 1
            
    return 1 if obj_b == obj_a else 0