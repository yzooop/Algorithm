function solution(s1, s2) {
    let cnt = 0
    s1.forEach((item) => {
        if (s2.includes(item)){
            cnt += 1
        }
    })
    
    return cnt
}