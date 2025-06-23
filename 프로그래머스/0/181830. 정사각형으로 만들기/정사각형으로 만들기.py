def solution(arr):
    row = len(arr)
    col = len(arr[0])
    ans = []
    
    if row == col:
        return arr
    
    elif row > col:
        for i in arr:
            i = i + [0] * (row - col)
            ans.append(i)
        return ans
    
    elif row < col:
        for i in range(col - row):
            arr.append([0] * col)
        return arr
        