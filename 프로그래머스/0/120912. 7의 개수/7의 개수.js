function solution(array) {
    let cnt = 0
    const string = array.map(i => i.toString()).join("")
    
    for (const s of string) {
        if (s === "7") {
            cnt += 1
        }
    }
    return cnt
}