function solution(sides) {
    let arr = []
    const sorted = sides.sort((a, b) => b - a)
    for (let i = (sorted[0] - sorted[1] + 1); i < (sorted[0] + sorted[1]); i++) {
        arr.push(i)
    }
    return arr.length
}