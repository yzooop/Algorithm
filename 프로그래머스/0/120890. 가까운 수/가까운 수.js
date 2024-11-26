function solution(array, n) {
    array.sort((a, b) => a - b)
    const diff = array.map((item) => Math.abs(item - n))
    return array[diff.indexOf(Math.min(...diff))]
}