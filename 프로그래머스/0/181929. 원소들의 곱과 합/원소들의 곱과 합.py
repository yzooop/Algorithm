def solution(num_list):
    sum_val = 0
    mul_val = 1
    
    for i in num_list:
        sum_val += i
        mul_val *= i
    
    if mul_val < (sum_val)**2:
        return 1
    else:
        return 0