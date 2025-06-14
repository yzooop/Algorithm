def solution(arr, idx):
    for i in range(idx):
        arr[i] = 0
    
    if 1 in arr:
        return arr.index(1)
    else:
        return -1