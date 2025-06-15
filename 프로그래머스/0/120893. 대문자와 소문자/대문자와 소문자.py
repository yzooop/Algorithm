def solution(my_string):
    ans = ""
    
    for i in range(len(my_string)):
        if my_string[i].islower() == True:
            ans += my_string[i].upper()
        else:
            ans += my_string[i].lower()
    return ans