function solution(food) {
    let ans = ""
    let str = ""
    const times = food.slice(1, food.length).map(item => Math.floor(item / 2))
    
    times.forEach((t, i) => {
        str += ((i + 1).toString().repeat(t))
    })
    
    ans += str
    ans += "0"
    ans += str.split('').reverse().join("")
    
    return ans
}