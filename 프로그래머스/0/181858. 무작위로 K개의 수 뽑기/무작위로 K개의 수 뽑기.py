def solution(arr, k):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
            if len(result) == k:
                break
    while len(result) < k:
        result.append(-1)
    return result
