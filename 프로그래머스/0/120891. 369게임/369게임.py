def solution(order):
    ans = 0
    for i in str(order):
        if i == "3":
            ans += 1
        elif i == "6":
            ans += 1
        elif i == "9":
            ans += 1
    return ans