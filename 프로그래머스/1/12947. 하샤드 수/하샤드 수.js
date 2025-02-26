function solution(x) {
    const digit_sum = String(x).split("").reduce((a, b) => Number(a) + Number(b), 0)
    
    return x % digit_sum === 0
}