def solution(dots):
    x = []
    y = []
    
    for dot in dots:
        x.append(dot[0])
        y.append(dot[1])
    
    x = set(x)
    y = set(y)
    
    return (max(x) - min(x)) * (max(y) - min(y))