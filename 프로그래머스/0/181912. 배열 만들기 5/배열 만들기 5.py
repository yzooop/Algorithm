def solution(intStrs, k, s, l):

    parsed = []
    ans = []

    for i in intStrs:
        parsed.append(i[s:s+l])

    for j in parsed:
        j = int(j)
        if j > k:
            ans.append(j)
            
    return ans