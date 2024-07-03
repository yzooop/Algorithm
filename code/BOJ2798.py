import sys

def c(arr, r):
    if r == 0:
        return [[]]
    
    result = []
    for i in range(len(arr)):
        for next in c(arr[i+1:], r-1):
            result.append([arr[i]] + next)
    return result

def format_c(arr):
    return [[row, []] for row in arr]

def get_sum(arr):
    for i in range(len(arr)):
        arr[i][1].append(sum(arr[i][0]))
    return arr

def get_answer(arr, num):
    max_sum = 0
    for i in range(len(arr)):
        if arr[i][1][0] <= num:
            max_sum = max(max_sum, arr[i][1][0])
    return max_sum


N, M = map(int, sys.stdin.readline().strip().split())

arr = list(map(int, sys.stdin.readline().strip().split()))

ans = c(arr, 3)
f_ans = format_c(ans)

s = get_sum(f_ans)
result = get_answer(s, M)

print(result)