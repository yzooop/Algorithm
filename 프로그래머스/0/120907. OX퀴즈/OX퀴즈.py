def solution(quiz):
    result = []
    for q in quiz:
        parts = q.split()
        x = int(parts[0])
        op = parts[1]
        y = int(parts[2])
        z = int(parts[4])

        if op == '+':
            calc = x + y
        else:
            calc = x - y
            
        if calc == z:
            result.append("O")
        else:
            result.append("X")
    return result
