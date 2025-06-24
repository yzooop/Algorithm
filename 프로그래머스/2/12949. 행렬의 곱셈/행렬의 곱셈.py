
def solution(arr1, arr2):
    rows = len(arr1)
    cols = len(arr2[0])

    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result