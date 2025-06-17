def solution(my_string):
    total = 0
    num_str = ''
    
    for ch in my_string:
        if ch.isdigit():
            num_str += ch
        else:
            if num_str:
                total += int(num_str)
                num_str = ''

    if num_str:
        total += int(num_str)
    
    return total
