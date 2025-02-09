function solution(arr) {
    const two = arr.map((item, idx) => item === 2 ? idx : -1).filter((idx) => idx !== -1)
    const min = Math.min(...two)
    const max = Math.max(...two)
    console.log(min, max)
    if (min !== Infinity && max !== Infinity) {
        return arr.slice(min, max + 1)
    } else {
        return [-1]
    }
}