def solution(lines):
    obj = {}
    
    for line in lines:
        for i in range(line[0], line[1]):
            if i in obj:
                obj[i] += 1
            else:
                obj[i] = 1
    
    count = sum(1 for v in obj.values() if v >= 2)
    return count