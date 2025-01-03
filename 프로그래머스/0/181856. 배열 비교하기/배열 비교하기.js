function solution(arr1, arr2) {
    if (arr1.length < arr2.length) return -1
    else if (arr1.length > arr2.length) return 1
    else if (arr1.length === arr2.length) {
        const arr1_sum = arr1.reduce((acc, cur) => acc + cur)
        const arr2_sum = arr2.reduce((acc, cur) => acc + cur)
        
        if (arr1_sum > arr2_sum) return 1
        else if (arr1_sum < arr2_sum) return -1
        else if (arr1_sum === arr2_sum) return 0
    }
}