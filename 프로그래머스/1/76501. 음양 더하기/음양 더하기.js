function solution(absolutes, signs) {
    let real = []
    
    for (let i = 0; i < absolutes.length; i++) {
        let value = signs[i] ? absolutes[i] : -absolutes[i]
        real.push(value)
    }
    return real.reduce((a, b) => a + b, 0)
}