def solution(myStr):
    str = myStr.replace("a", " ").replace("b", " ").replace("c", " ")
    
    str_arr = str.split(" ")
    filtered = list(filter(None, str_arr))
    return filtered if filtered else ["EMPTY"]