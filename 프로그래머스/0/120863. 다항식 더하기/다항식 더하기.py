def solution(polynomial):
    lst = polynomial.split(" ")
    x_lst = []
    n_lst = []
    
    for i in lst:
        if "x" in i:
            x_lst.append(i)
        elif i != "+":
            n_lst.append(int(i))
            
    x_n = 0
    for x in x_lst:
        if x == "x":
            x_n += 1
        else:
            x_n += int(x[:-1])

    if x_n != 0 and sum(n_lst) != 0: # nx + n
        if x_n == 1: # 1일때 생략
            x_part = "x"
        else: # 일반
            x_part = f"{x_n}x"

        c_part = sum(n_lst)
        return f"{x_part} + {c_part}"

    elif x_n != 0: # nx
        if x_n == 1:
            return "x"
        else:
            return f"{x_n}x"

    else: # n
        return str(sum(n_lst))
