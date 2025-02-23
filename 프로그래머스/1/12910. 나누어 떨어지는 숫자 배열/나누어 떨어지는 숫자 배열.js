function solution(arr, divisor) {
    const ans = arr.filter((item) => item % divisor === 0).sort((a, b) => a - b)
    return ans.length > 0 ? ans : [-1]
}