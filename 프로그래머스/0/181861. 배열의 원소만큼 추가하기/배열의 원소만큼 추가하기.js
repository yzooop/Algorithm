function solution(arr) {
    const added_arr = arr.map((item) => Array(item).fill(item))
    return [].concat(...added_arr)
}