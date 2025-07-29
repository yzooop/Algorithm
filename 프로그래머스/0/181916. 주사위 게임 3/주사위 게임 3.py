from collections import Counter

def solution(a, b, c, d):
    nums = [a, b, c, d]
    counter = Counter(nums)
    values = list(counter.values())
    keys = list(counter.keys())

    if len(counter) == 1:
        return 1111 * keys[0]
    
    if 3 in values:
        p = keys[values.index(3)]
        q = keys[values.index(1)]
        return (10 * p + q) ** 2

    if values.count(2) == 2:
        p, q = keys
        return (p + q) * abs(p - q)

    if 2 in values and values.count(1) == 2:
        p = keys[values.index(2)]
        q, r = [k for k in keys if k != p]
        return q * r

    return min(nums)
