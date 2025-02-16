function solution(number, limit, power) {
    let ans = []
    for (let i=1; i<=number; i++) {
        ans.push(divisor_num(i))
    }
    return ans.map((item) => item <= limit ? item : power).reduce((a,b) => a+b, 0)
}

function divisor_num(n) {
    let ans = new Set()
    for (let i=1; i*i<=n; i++) {
        if (n % i ===0) {
            ans.add(i)
            ans.add(n / i)
        }
    }
    return [...ans].sort((a, b) => a - b).length
}