function solution(a, b) {
    const arr = a <= b 
    ? Array.from({length : b - a + 1}, (_, i) => a + i) 
    : Array.from({length : a - b + 1}, (_, i) => b + i)
    return arr.reduce((a, b) => a+b)
}