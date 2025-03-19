function solution(s) {
    const s_split = s.split("")
    
    if (s_split[0] === "-") {
        return Number(s_split.slice(1,).join("")) * -1
    } 
    return Number(s)
}