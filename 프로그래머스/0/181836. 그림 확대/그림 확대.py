def solution(picture, k):
    ans = []
    for item in picture:
        row = ""
        for i in item:
            row += i*k
        for i in range(k):
            ans.append(row)
    
    return ans