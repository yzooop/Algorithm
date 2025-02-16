function solution(left, right) {
    const arr = Array.from({length : right - left + 1}, (_, i) => left + i)
    
    return arr.map((item) => isPerfectSquare(item) ? item * -1 : item).reduce((a, b) => a + b , 0)
}

function isPerfectSquare(n) {
    return Number.isInteger(Math.sqrt(n));
}