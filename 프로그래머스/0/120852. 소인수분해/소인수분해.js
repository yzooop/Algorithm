function solution(n) {
    let ans = []
    for (let i = 2; i <= n; i++) {
        while (n % i === 0) {
            if (!ans.includes(i)) {
                ans.push(i)
            }
            n = n / i
        }
    }
    return ans
}