function solution(s) {
    const arr = s.split(" ")
    const ans = []
    
    arr.forEach((item) => {
        if (item === "Z") {
            ans.pop()
        } else {
            ans.push(Number(item))
        }
    })
    return ans.reduce((acc, cur) => acc + cur, 0)
}