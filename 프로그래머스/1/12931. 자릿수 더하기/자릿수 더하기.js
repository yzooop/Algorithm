function solution(n) {
    return n.toString().split("").map(item => Number(item)).reduce((a, b) => a+b, 0)
}