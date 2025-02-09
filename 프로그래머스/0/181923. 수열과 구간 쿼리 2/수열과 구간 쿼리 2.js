function solution(arr, queries) {
    let answer = []
    
    queries.forEach((q) => {
        const slice = arr.slice(q[0], q[1] + 1)
        const ans = slice.filter((item) => item > q[2])
        const min_value = Math.min(...ans) === Infinity ? -1 : Math.min(...ans)
        answer.push(min_value)    
    })
    return answer
}