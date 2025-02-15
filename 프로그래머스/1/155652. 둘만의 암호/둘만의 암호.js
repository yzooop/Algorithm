function solution(s, skip, index) {
    const alp = "abcdefghijklmnopqrstuvwxyz"
    const new_str = alp.split("").filter((item) => !skip.includes(item)).join("")
    
    return [...s].map((item) => {
        return new_str[(new_str.indexOf(item) + index) % new_str.length]
    }).join("")
}