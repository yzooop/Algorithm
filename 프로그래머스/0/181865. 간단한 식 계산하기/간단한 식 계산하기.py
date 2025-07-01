def solution(binomial):
    lst = binomial.split(" ")
    [a, op, b] = lst
    
    if op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)
    elif op == "*":
        return int(a) * int(b)