function solution(s) {
    let map = new Map()
    let ans = []
    
    s.split("").forEach((item, idx) => {
        if (map.has(item)) {
            ans.push(idx - map.get(item))
        } else {
            ans.push(-1)
        }
        map.set(item, idx)
    })
    return ans
}