function solution(s) {
    const len = s.length
    
    if (len % 2 === 0) {
        return s.slice(len/2 - 1, len/2 + 1)
    } else {
        return s[Math.floor(len / 2)]
    }
}